"""Ingest a source into memory: a YouTube video (captions with timestamps), a web page, or a local file.

  wiki ingest https://www.youtube.com/watch?v=VIDEO
  wiki ingest https://example.com/article
  wiki ingest ~/Downloads/paper.pdf        # copied into wiki/files/ so the site can link to it
"""

import re
import shutil
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from llmwiki import db
from llmwiki.config import FILES_DIR

CHUNK_SECONDS = 45
CHUNK_CHARS = 1200
USER_AGENT = "Mozilla/5.0 (compatible; llm-wiki/0.1; personal research)"


def youtube_id(url: str) -> str | None:
    u = urlparse(url)
    host = u.netloc.removeprefix("www.").removeprefix("m.")
    if host == "youtu.be":
        return u.path.strip("/").split("/")[0] or None
    if host.endswith("youtube.com"):
        if u.path == "/watch":
            return parse_qs(u.query).get("v", [None])[0]
        m = re.match(r"/(?:embed|shorts|live|v)/([\w-]{11})", u.path)
        return m.group(1) if m else None
    return None


def _split_text(text: str, size: int = CHUNK_CHARS) -> list[str]:
    """Split on paragraph boundaries into ~size-character chunks."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if cur and len(cur) + len(p) > size:
            chunks.append(cur)
            cur = ""
        cur = f"{cur}\n\n{p}" if cur else p
        while len(cur) > size * 2:  # one huge paragraph
            chunks.append(cur[:size])
            cur = cur[size:]
    if cur:
        chunks.append(cur)
    return chunks


def ingest_video(url: str, force: bool = False) -> dict:
    vid = youtube_id(url)
    if not vid:
        return {"error": f"not a YouTube URL: {url}"}
    if db.has_source(vid) and not force:
        return {"id": vid, "status": "already_ingested"}
    from youtube_transcript_api import YouTubeTranscriptApi
    try:
        fetched = YouTubeTranscriptApi().fetch(vid, languages=["en", "en-US", "en-GB"])
    except Exception as e:  # disabled captions, network, rate limit
        return {"id": vid, "error": f"{type(e).__name__}: {e}"[:300]}

    chunks, text, start = [], "", 0.0
    for snip in fetched:
        if not text:
            start = snip.start
        text += " " + snip.text.replace("\n", " ")
        if snip.start + snip.duration - start >= CHUNK_SECONDS:
            chunks.append((int(start), text.strip()))
            text = ""
    if text:
        chunks.append((int(start), text.strip()))

    title, author = _youtube_meta(vid)
    db.add_source(vid, "video", f"https://www.youtube.com/watch?v={vid}", title, author, "", chunks)
    return {"id": vid, "status": "ingested", "kind": "video", "title": title, "author": author,
            "chunks": len(chunks)}


def _youtube_meta(vid: str) -> tuple[str, str]:
    """Title and channel via YouTube's public oEmbed endpoint (no API key)."""
    import requests
    try:
        r = requests.get("https://www.youtube.com/oembed",
                         params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"}, timeout=10)
        r.raise_for_status()
        j = r.json()
        return j.get("title", ""), j.get("author_name", "")
    except Exception:
        return "", ""


def _html_to_text(html: str) -> tuple[str, str, str, str]:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    meta = lambda *names: next((m.get("content", "") for n in names
                                for m in soup.find_all("meta", attrs={"name": n}) + soup.find_all("meta", attrs={"property": n})
                                if m.get("content")), "")
    title = meta("og:title") or (soup.title.string.strip() if soup.title and soup.title.string else "")
    author = meta("author", "article:author", "og:site_name")
    published = meta("article:published_time", "date", "citation_publication_date")[:10]
    for tag in soup(["script", "style", "noscript", "nav", "footer", "header", "aside", "form", "svg"]):
        tag.decompose()
    root = soup.find("article") or soup.find("main") or soup.body or soup
    blocks = []
    for el in root.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "blockquote", "td"]):
        t = " ".join(el.get_text(" ", strip=True).split())
        if len(t) > 1 and (el.name != "li" or len(t) > 20):
            blocks.append(t)
    text = "\n\n".join(dict.fromkeys(blocks))  # drop exact duplicates, keep order
    return title, author, published, text


def ingest_web(url: str, force: bool = False) -> dict:
    url = url.split("#")[0]
    if db.has_source(url) and not force:
        return {"id": url, "status": "already_ingested"}
    import requests
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=20)
        r.raise_for_status()
    except Exception as e:
        return {"id": url, "error": f"{type(e).__name__}: {e}"[:300]}
    ctype = r.headers.get("content-type", "")
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        title, pages = _pdf_pages(r.content)
        chunks = [(n, t) for n, t in pages if t.strip()]
        title = title or Path(urlparse(url).path).name
        author, published = "", ""
    elif "html" in ctype or not ctype:
        title, author, published, text = _html_to_text(r.text)
        chunks = list(enumerate(_split_text(text), 1))
    else:  # plain text, markdown, JSON
        title, author, published = Path(urlparse(url).path).name, "", ""
        chunks = list(enumerate(_split_text(r.text), 1))
    if not chunks:
        return {"id": url, "error": "no readable text (page may need JavaScript)"}
    db.add_source(url, "web", url, title, author, published, chunks)
    return {"id": url, "status": "ingested", "kind": "web", "title": title, "chunks": len(chunks)}


def _pdf_pages(data: bytes) -> tuple[str, list[tuple[int, str]]]:
    import io
    from pypdf import PdfReader
    reader = PdfReader(io.BytesIO(data))
    title = (reader.metadata.title if reader.metadata and reader.metadata.title else "") or ""
    return title, [(i, (p.extract_text() or "")) for i, p in enumerate(reader.pages, 1)]


def ingest_file(path: str, force: bool = False) -> dict:
    src = Path(path).expanduser().resolve()
    if not src.is_file():
        return {"error": f"no such file: {path}"}
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    dest = FILES_DIR / src.name
    sid = f"files/{src.name}"
    if db.has_source(sid) and not force:
        return {"id": sid, "status": "already_ingested"}
    if src != dest:
        shutil.copy2(src, dest)
    suffix = src.suffix.lower()
    if suffix == ".pdf":
        title, pages = _pdf_pages(dest.read_bytes())
        chunks = [(n, t) for n, t in pages if t.strip()]
    elif suffix in (".html", ".htm"):
        title, _, _, text = _html_to_text(dest.read_text(encoding="utf-8", errors="replace"))
        chunks = list(enumerate(_split_text(text), 1))
    else:
        title, text = "", dest.read_text(encoding="utf-8", errors="replace")
        chunks = list(enumerate(_split_text(text), 1))
    if not chunks:
        return {"id": sid, "error": "no readable text"}
    published = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
    db.add_source(sid, "file", f"../files/{src.name}", title or src.stem, "", published, chunks)
    return {"id": sid, "status": "ingested", "kind": "file", "title": title or src.stem, "chunks": len(chunks)}


def ingest(target: str, force: bool = False) -> dict:
    if target.startswith(("http://", "https://")):
        return ingest_video(target, force) if youtube_id(target) else ingest_web(target, force)
    return ingest_file(target, force)

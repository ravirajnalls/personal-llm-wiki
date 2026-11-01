"""Regenerate the "## References" section at the end of every page from the page's own citations.

Run it after every edit; never write the section by hand.
"""

import re
from pathlib import Path
from urllib.parse import unquote, urlparse

from llmwiki import db
from llmwiki.pages import content_pages

HEADING = "## References"
OLD_SECTION = re.compile(r"\n## (?:References|Sources)\s*\n.*?(?=\n## |\Z)", re.S)
VIDEO = re.compile(r"\[▶ ([\d:]+)\]\((https?://[^)\s]*?[?&]v=([\w-]{11})[^)\s]*)\)")
LINK = re.compile(r"\[([^\]]+)\]\(((?:https?://|\.\./files/)[^)\s]+)\)")


def _seconds(label: str) -> int:
    total = 0
    for part in label.split(":"):
        total = total * 60 + int(part)
    return total


def _title(source_id: str, fallback: str) -> str:
    try:
        row = db.get_source(source_id)
    except Exception:
        row = None
    return (row["title"] if row and row["title"] else "") or fallback


def _old_titles(text: str) -> dict[str, str]:
    """Titles from the page's current References section, kept when memory.db doesn't know a source."""
    m = OLD_SECTION.search(text)
    if not m:
        return {}
    found = {}
    for name, url in re.findall(r"^\d+\. \[([^\]]+)\]\(([^)\s]+)\)", m.group(0), re.M):
        vid = re.search(r"[?&]v=([\w-]{11})", url)
        found[vid.group(1) if vid else url.rstrip("/")] = name
    return found


def build(text: str) -> str:
    body = OLD_SECTION.sub("", text)
    old = _old_titles(text)
    videos: dict[str, list[str]] = {}
    for label, _, vid in VIDEO.findall(body):
        if label not in videos.setdefault(vid, []):
            videos[vid].append(label)
    web: dict[str, str] = {}
    files: dict[str, set] = {}
    for label, url in LINK.findall(body):
        if label.startswith("▶") or "youtube.com/watch" in url or "youtu.be/" in url:
            continue
        if url.startswith("../files/"):
            path, _, frag = url.partition("#")
            pages = files.setdefault(path, set())
            if frag.startswith("page="):
                pages.add(int(frag[5:]))
        else:
            web.setdefault(url.split("#")[0].rstrip("/"), label)

    if not (videos or web or files):
        return ""
    out = [HEADING, ""]
    if videos:
        out += ["**Videos**", ""]
        for n, (vid, labels) in enumerate(videos.items(), 1):
            row = db.get_source(vid) if _safe() else None
            if row and row["title"]:
                name = row["title"] + (f" ({row['author']})" if row["author"] else "")
            else:
                name = old.get(vid, f"YouTube video {vid}")
            moments = ", ".join(f"[{lab}](https://www.youtube.com/watch?v={vid}&t={_seconds(lab)}s)"
                                for lab in sorted(labels, key=_seconds))
            out.append(f"{n}. [{name}](https://www.youtube.com/watch?v={vid}), cited at {moments}")
        out.append("")
    if web:
        out += ["**Web**", ""]
        for n, url in enumerate(web, 1):
            u = urlparse(url)
            fallback = f"{u.netloc.removeprefix('www.')}{u.path.rstrip('/')}"
            title = (_title(url, "") if _safe() else "") or (old.get(url, "") if old.get(url, "") != fallback else "")
            out.append(f"{n}. [{title or fallback}]({url})" + (f" — {u.netloc.removeprefix('www.')}" if title else ""))
        out.append("")
    if files:
        out += ["**Files**", ""]
        for n, (path, pages) in enumerate(files.items(), 1):
            name = unquote(path.removeprefix("../files/"))
            cited = f", cited at p. {', '.join(map(str, sorted(pages)))}" if pages else ""
            out.append(f"{n}. [{name}]({path}){cited}")
        out.append("")
    return "\n".join(out)


def _safe() -> bool:
    from llmwiki.config import DB_PATH
    return DB_PATH.exists()


def update_page(path: Path, write: bool = True) -> bool:
    text = path.read_text(encoding="utf-8")
    refs = build(text)
    if not refs:
        return False
    new = OLD_SECTION.sub("", text).rstrip() + "\n\n" + refs
    if new == text:
        return False
    if write:
        path.write_text(new, encoding="utf-8")
    return True


def update_all(write: bool = True) -> list[str]:
    from llmwiki.config import WIKI_DIR
    return [p.relative_to(WIKI_DIR).as_posix() for p in content_pages() if update_page(p, write)]

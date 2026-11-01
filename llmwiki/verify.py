"""Check every citation in the wiki against what was actually ingested.

Errors (exit 1):
  - a video label (MM:SS) that doesn't match the link's t= seconds
  - a quoted sentence next to a video citation that is in the transcript, but far from the cited time
  - a web text-fragment (#:~:text=) whose words aren't in the ingested page
  - a link to ../files/ that doesn't exist
Warnings:
  - a cited source that was never ingested (the claim can't be checked)
  - a page missing one of its collection's sections, or citing fewer than 2 sources
"""

import re
from pathlib import Path
from urllib.parse import unquote

from llmwiki import cite, config, db
from llmwiki.config import WIKI_DIR
from llmwiki.pages import content_pages, split_frontmatter

VIDEO = re.compile(r"\[▶ ([\d:]+)\]\((https?://[^)]*?[?&]v=([\w-]{11})[^)]*?[?&]t=(\d+)s?[^)]*)\)")
FRAGMENT = re.compile(r"\]\((https?://[^)\s#]+)#:~:text=([^)\s]+)\)")
FILE_LINK = re.compile(r"\]\((\.\./files/[^)\s#]+)(?:#[^)\s]*)?\)")
ANY_LINK = re.compile(r"\]\((https?://[^)\s]+|\.\./files/[^)\s]+)\)")
QUOTE = re.compile(r"[\"“]([^\"”]{20,})[\"”]")
NEAR_SECONDS = 90


def _norm(s: str) -> str:
    return " ".join(re.sub(r"[^\w\s]", " ", s.lower()).split())


def _seconds(label: str) -> int:
    total = 0
    for part in label.split(":"):
        total = total * 60 + int(part)
    return total


def _quote_time(vid: str, quote: str) -> int | None:
    words = _norm(quote).split()[:6]
    if len(words) < 3:
        return None
    needle = " ".join(words)
    for row in db.source_chunks(vid):
        if needle in _norm(row["text"]):
            return int(row["loc"])
    return None


def check_page(path: Path, fix: bool = False) -> tuple[list[str], list[str]]:
    name = path.relative_to(WIKI_DIR).as_posix()
    text = path.read_text(encoding="utf-8")
    errors, warnings, fixes = [], [], []
    have_db = config.DB_PATH.exists()
    body = re.split(r"\n## References\s*\n", text)[0]

    for line in body.splitlines():
        quotes = QUOTE.findall(line)
        for m in VIDEO.finditer(line):
            lab, url, vid, t = m.group(1), m.group(2), m.group(3), int(m.group(4))
            if _seconds(lab) != t:
                errors.append(f"{name}: label {lab} but link jumps to {cite.mmss(t)} ({vid})")
            if not have_db:
                continue
            if not db.has_source(vid):
                warnings.append(f"{name}: video {vid} cited but never ingested")
                continue
            for q in quotes:
                found = _quote_time(vid, q)
                if found is not None and abs(found - t) > NEAR_SECONDS:
                    errors.append(f"{name}: quote \"{q[:50]}…\" is at {cite.mmss(found)}, cited at {cite.mmss(t)}")
                    fixes.append((m.group(0), cite.video(vid, found)))

    if have_db:
        for url, frag in FRAGMENT.findall(body):
            src = db.find_source_by_url(url)
            if not src:
                warnings.append(f"{name}: {url} cited but never ingested")
                continue
            words = _norm(unquote(frag.split("&")[0]).split(",")[0])
            full = _norm(" ".join(r["text"] for r in db.source_chunks(src["id"])))
            if words and words not in full:
                errors.append(f"{name}: quote \"{words[:50]}\" not found in {url}")

    for rel in set(FILE_LINK.findall(body)):
        if not (path.parent / unquote(rel)).resolve().exists():
            errors.append(f"{name}: missing file {rel}")

    meta, _ = split_frontmatter(text)
    coll = path.relative_to(WIKI_DIR).parts[0]
    sections = ((config.load()["collections"].get(coll) or {}).get("sections")) or []
    headings = {h.strip().lower() for h in re.findall(r"^## (.+)$", body, re.M)}
    optional = {"disagreements", "open questions", "gotchas"}
    for s in sections:
        if s.lower() not in headings and s.lower() not in optional:
            warnings.append(f"{name}: no '## {s}' section")
    distinct = {re.sub(r"[?&]t=\d+s?", "", u).split("#")[0] for u in ANY_LINK.findall(body)}
    if len(distinct) < 2:
        warnings.append(f"{name}: cites {len(distinct)} source(s)")

    if fix and fixes:
        for old, new in fixes:
            text = text.replace(old, new, 1)
        path.write_text(text, encoding="utf-8")
    return errors, warnings


def check_all(fix: bool = False) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    for p in content_pages():
        e, w = check_page(p, fix)
        errors += e
        warnings += w
    return errors, warnings

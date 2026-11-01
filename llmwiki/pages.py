"""Read wiki pages and rebuild the index pages from their frontmatter."""

from pathlib import Path

import yaml

from llmwiki import config
from llmwiki.config import WIKI_DIR

SKIP_DIRS = {"files", "sources", "assets", "stylesheets"}


def split_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            try:
                meta = yaml.safe_load(text[3:end]) or {}
            except yaml.YAMLError:
                meta = {}
            return (meta if isinstance(meta, dict) else {}), text[end + 4:].lstrip("\n")
    return {}, text


def content_pages() -> list[Path]:
    """Every researched page: wiki/<collection>/<page>.md, not index pages."""
    out = []
    for p in sorted(WIKI_DIR.rglob("*.md")):
        rel = p.relative_to(WIKI_DIR)
        if p.name == "index.md" or rel.parts[0] in SKIP_DIRS or len(rel.parts) < 2:
            continue
        out.append(p)
    return out


def page_info(path: Path) -> dict:
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    title = meta.get("title") or next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), path.stem)
    rel = path.relative_to(WIKI_DIR)
    return {"title": str(title), "summary": str(meta.get("summary", "")).strip(), "updated": str(meta.get("updated", "")),
            "collection": rel.parts[0], "path": rel.as_posix(), "slug": path.stem, "tags": meta.get("tags") or []}


def rebuild_index() -> list[str]:
    """Write wiki/index.md and one index.md per collection. Returns the files written."""
    cfg = config.load()
    by_coll: dict[str, list[dict]] = {}
    for p in content_pages():
        info = page_info(p)
        by_coll.setdefault(info["collection"], []).append(info)

    written = []
    lines = [f"# {cfg['title']}", "", cfg.get("description", ""), ""]
    lead = ["categories", "topics"]  # generated cross-playlist views first
    names = lead + [n for n in cfg["collections"] if n not in lead] + \
        sorted(set(by_coll) - set(cfg["collections"]) - set(lead))
    for name in names:
        pages = sorted(by_coll.get(name, []), key=lambda i: i["title"].lower())
        desc = (cfg["collections"].get(name) or {}).get("description", "")
        if not pages:
            continue
        lines += [f"## [{name.title()}]({name}/index.md)", ""]
        lines += [f"- [{i['title']}]({i['path']}) — {i['summary']}" for i in pages]
        lines.append("")
        coll_lines = [f"# {name.title()}", "", desc, ""]
        coll_lines += [f"- [{i['title']}]({i['slug']}.md) — {i['summary']}"
                       + (f" *(updated {i['updated']})*" if i["updated"] else "") for i in pages]
        coll_file = WIKI_DIR / name / "index.md"
        coll_file.write_text("\n".join(coll_lines).rstrip() + "\n", encoding="utf-8")
        written.append(coll_file.relative_to(WIKI_DIR).as_posix())
    if (WIKI_DIR / "sources" / "index.md").exists():
        lines += ["## [Sources](sources/index.md)", "", "Every synced playlist and video transcript.", ""]
    if not by_coll:
        lines += ["Nothing here yet. Run `wiki research \"a topic\"` to add the first page.", ""]
    (WIKI_DIR / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    written.append("index.md")
    return written

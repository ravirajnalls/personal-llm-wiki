"""Catalog pages under wiki/sources/, rebuilt after every sync and classify.

  sources/index.md            the channel's timeline: every playlist by year, with counts
  sources/case-studies.md     every case study, by event, with its organizations
  sources/<playlist id>.md    one playlist: its videos, their kind and organizations
  sources/videos/<id>.md      one video: labels, playlists and the full timestamped transcript
"""

import json

from llmwiki import cite, config, db
from llmwiki.config import WIKI_DIR

SOURCES_DIR = WIKI_DIR / "sources"
KIND_LABEL = {"case_study": "case study", "concept": "concept", "tutorial": "tutorial", "panel": "panel",
              "keynote": "keynote", "other": "other", None: ""}


def _when(p) -> str:
    if not p["year"]:
        return "undated"
    return f"{p['year']}-{p['month']:02d}" if p["month"] else str(p["year"])


def _cell(s) -> str:
    return str(s or "").replace("|", "/").replace("\n", " ")


def _write(path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def build() -> None:
    if not config.DB_PATH.exists():
        return
    cfg = config.load()
    transcripts = cfg.get("research", {}).get("transcript_pages", True)
    ch = cfg.get("channel") or {}
    pls = db.playlists()

    top = ["# Sources", "", f"Every playlist synced from [{ch.get('url', 'the channel')}]({ch.get('url', '')}), "
           "oldest first. Each playlist is one point on the timeline.", "",
           "See also: [all case studies](case-studies.md).", ""]
    year = object()
    for p in pls:
        if p["year"] != year:
            year = p["year"]
            top += ["", f"## {year or 'Undated'}", "", "| Playlist | Videos | Transcripts | Case studies |",
                    "| --- | --- | --- | --- |"]
        top.append(f"| [{_cell(p['title'])}]({p['id']}.md) | {p['n_videos']} | {p['n_ok'] or 0} | "
                   f"{p['n_case_studies'] or 0} |")
        _playlist_page(p, transcripts)
    _write(SOURCES_DIR / "index.md", "\n".join(top) + "\n")
    _case_studies_page(pls)
    if transcripts:
        for v in db.videos("status = 'ok'"):
            _video_page(v)


def _playlist_page(p, transcripts: bool):
    lines = [f"# {p['title']}", "", f"{_when(p)} · {p['n_videos']} videos · {p['n_ok'] or 0} transcripts · "
             f"{p['n_case_studies'] or 0} case studies · "
             f"[on YouTube](https://www.youtube.com/playlist?list={p['id']})", "",
             "| # | Talk | Kind | Organizations | Length |", "| --- | --- | --- | --- | --- |"]
    for v in db.playlist_items(p["id"]):
        t = _cell(v["title"] or v["id"])
        link = f"[{t}](videos/{v['id']}.md)" if transcripts and v["status"] == "ok" else \
            f"[{t}](https://www.youtube.com/watch?v={v['id']})"
        if v["status"] in ("no_transcript", "error"):
            link += " *(no transcript)*"
        orgs = ", ".join(json.loads(v["orgs"] or "[]"))
        dur = cite.mmss(v["duration"]) if v["duration"] else ""
        lines.append(f"| {v['position']} | {link} | {KIND_LABEL.get(v['kind'], v['kind'])} | {_cell(orgs)} | {dur} |")
    _write(SOURCES_DIR / f"{p['id']}.md", "\n".join(lines) + "\n")


def _case_studies_page(pls):
    lines = ["# Case studies", "", "Every talk where an organization reports its own experience, by event, oldest "
             "first. Use `wiki find \"topic\"` to narrow this down to one topic.", ""]
    seen = set()
    for p in pls:
        rows = [v for v in db.playlist_items(p["id"]) if v["kind"] == "case_study" and v["id"] not in seen]
        if not rows:
            continue
        seen.update(v["id"] for v in rows)
        lines += [f"## {_when(p)} · [{p['title']}]({p['id']}.md)", ""]
        for v in rows:
            orgs = ", ".join(json.loads(v["orgs"] or "[]"))
            target = f"videos/{v['id']}.md" if v["status"] == "ok" else f"https://www.youtube.com/watch?v={v['id']}"
            lines.append(f"- [{v['title']}]({target})" + (f" — **{orgs}**" if orgs else "")
                         + (f". {v['summary']}" if v["summary"] else ""))
        lines.append("")
    _write(SOURCES_DIR / "case-studies.md", "\n".join(lines).rstrip() + "\n")


def _video_page(v):
    chunks = db.source_chunks(v["id"])
    if not chunks:
        return
    orgs = json.loads(v["orgs"] or "[]")
    topics = json.loads(v["topics"] or "[]")
    pls = db.video_playlists(v["id"])
    title = (v["title"] or v["id"]).replace('"', "'")
    out = ["---", f'title: "{title}"', f"video: {v['id']}", f"kind: {v['kind'] or ''}",
           f"orgs: {json.dumps(orgs, ensure_ascii=False)}", f"topics: {json.dumps(topics, ensure_ascii=False)}",
           "---", "", f"# {v['title'] or v['id']}", "",
           " · ".join(x for x in [KIND_LABEL.get(v["kind"], ""), ", ".join(orgs),
                                  cite.mmss(v["duration"]) if v["duration"] else "",
                                  f"[Watch on YouTube](https://www.youtube.com/watch?v={v['id']})"] if x), ""]
    if pls:
        out += ["Playlists: " + ", ".join(f"[{p['title']}](../{p['id']}.md)" for p in pls), ""]
    if v["summary"]:
        out += [f"> {v['summary']}", ""]
    if topics:
        out += ["Topics: " + ", ".join(f"`{t}`" for t in topics), ""]
    out += ["## Transcript", ""]
    out += [f"{cite.video(v['id'], int(c['loc']))} {c['text']}\n" for c in chunks]
    _write(SOURCES_DIR / "videos" / f"{v['id']}.md", "\n".join(out))

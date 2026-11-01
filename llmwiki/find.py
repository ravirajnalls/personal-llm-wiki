"""Find every talk on a topic across all playlists, laid out on the timeline.

  wiki find "autoscaling"                    # case studies (default)
  wiki find "cilium" --kind all              # every kind of talk
  wiki find "gpu scheduling" --kind concept
  wiki find "multi-tenancy" --page           # also write wiki/topics/multi-tenancy.md

A video matches when the topic is in its title, labels (topics, orgs, summary) or is mentioned in its
transcript at least --min-mentions times. Each match shows the moments where it's discussed.
"""

import json
import re
from datetime import date

from llmwiki import cite, config, db
from llmwiki.config import WIKI_DIR

KINDS = ("case_study", "concept", "tutorial", "panel", "keynote", "other")


def _words(text: str) -> list[str]:
    return [w for w in re.findall(r"\w+", text.lower()) if len(w) > 1]


def _contains_all(hay: str, words: list[str]) -> bool:
    hay = hay.lower()
    return all(re.search(rf"\b{re.escape(w)}", hay) for w in words)


def find(topic: str, kinds: list[str] | None = ("case_study",), min_mentions: int = 2,
         playlist: str | None = None, moments: int = 3) -> list[dict]:
    """Matches grouped by playlist, in timeline order: [{playlist, year, month, videos: [...]}]."""
    words = _words(topic)
    if not words:
        return []
    # Transcript mentions, best first
    hits: dict[str, list] = {}
    with db.get_db() as conn:
        for r in conn.execute("SELECT source_id, loc, snippet(chunks, 2, '**', '**', ' … ', 24) AS snip "
                              "FROM chunks WHERE chunks MATCH ? ORDER BY rank LIMIT 50000",
                              (db.fts_query(topic),)):
            hits.setdefault(r["source_id"], []).append(r)

    groups: dict[str, dict] = {}
    for p in db.playlists():
        if playlist and p["id"] != playlist:
            continue
        for v in db.playlist_items(p["id"]):
            if kinds and v["kind"] not in kinds:
                continue
            labels = " ".join([v["summary"] or "", " ".join(json.loads(v["topics"] or "[]")),
                               " ".join(json.loads(v["orgs"] or "[]"))])
            in_title = _contains_all(v["title"] or "", words)
            in_labels = _contains_all(labels, words)
            vh = hits.get(v["id"], [])
            if not (in_title or in_labels or len(vh) >= min_mentions):
                continue
            score = 10 * in_title + 8 * in_labels + min(len(vh), 15)
            g = groups.setdefault(p["id"], {"playlist": p["title"], "playlist_id": p["id"], "year": p["year"],
                                            "month": p["month"], "videos": []})
            g["videos"].append({
                "id": v["id"], "title": v["title"], "kind": v["kind"], "score": score,
                "orgs": json.loads(v["orgs"] or "[]"), "summary": v["summary"] or "",
                "mentions": len(vh), "transcript": v["status"] == "ok",
                "moments": [{"t": int(h["loc"]), "cite": cite.video(v["id"], int(h["loc"])),
                             "text": " ".join(h["snip"].split())}
                            for h in sorted(vh[:moments], key=lambda h: int(h["loc"]))],
            })
    out = []
    seen: set[str] = set()
    for p in db.playlists():  # timeline order; a video in several playlists is listed under the first
        g = groups.get(p["id"])
        if not g:
            continue
        g["videos"] = [v for v in sorted(g["videos"], key=lambda v: -v["score"]) if v["id"] not in seen]
        seen.update(v["id"] for v in g["videos"])
        if g["videos"]:
            out.append(g)
    return out


def _plural(kind: str) -> str:
    return {"case_study": "case studies", "other": "other talks"}.get(kind, kind + "s")


def when(g: dict) -> str:
    if not g["year"]:
        return "undated"
    return f"{g['year']}-{g['month']:02d}" if g["month"] else str(g["year"])


def print_results(topic: str, groups: list[dict], kinds) -> None:
    n = sum(len(g["videos"]) for g in groups)
    label = "talks" if not kinds else " / ".join(_plural(k) for k in kinds)
    print(f"{n} {label} on '{topic}' across {len(groups)} playlist(s)\n")
    for g in groups:
        print(f"== {when(g)}  {g['playlist']}")
        for v in g["videos"]:
            orgs = f"  [{', '.join(v['orgs'])}]" if v["orgs"] else ""
            print(f"  - {v['title']}{orgs}")
            print(f"    https://www.youtube.com/watch?v={v['id']}  ({v['kind']}, {v['mentions']} mentions)")
            if v["summary"]:
                print(f"    {v['summary']}")
            for m in v["moments"]:
                print(f"    {m['cite']}  {m['text'][:150]}")
        print()


def write_page(topic: str, groups: list[dict], kinds) -> str:
    slug = config.slugify(topic)
    path = WIKI_DIR / "topics" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    n = sum(len(g["videos"]) for g in groups)
    label = "talks" if not kinds else ", ".join(_plural(k) for k in kinds)
    orgs = sorted({o for g in groups for v in g["videos"] for o in v["orgs"]})
    lines = ["---", f"title: \"{topic.title()}: {label} over time\"",
             f"summary: {n} {label} on {topic} across {len(groups)} events"
             + (f", from {', '.join(orgs[:8])}{' and more' if len(orgs) > 8 else ''}" if orgs else "") + ".",
             f"tags: [timeline, {slug}]", f"updated: {date.today():%Y-%m-%d}", "generated: wiki find", "---", "",
             f"# {topic.title()}: {label} over time", "",
             f"> {n} {label} across {len(groups)} events, oldest first. Generated by `wiki find \"{topic}\"`; "
             f"each moment links to where the talk discusses it.", ""]
    if orgs:
        lines += ["**Organizations:** " + ", ".join(orgs), ""]
    for g in groups:
        lines += [f"## {when(g)} · {g['playlist']}", ""]
        for v in g["videos"]:
            who = f" — {', '.join(v['orgs'])}" if v["orgs"] else ""
            lines.append(f"### [{v['title']}](https://www.youtube.com/watch?v={v['id']}){who}")
            lines.append("")
            if v["summary"]:
                lines += [v["summary"], ""]
            for m in v["moments"]:
                lines.append(f"- {m['cite']} {m['text'][:220]}")
            if v["transcript"]:
                lines.append(f"- [Full transcript](../sources/videos/{v['id']}.md)")
            lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path.relative_to(WIKI_DIR).as_posix()

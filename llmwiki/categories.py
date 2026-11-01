"""Broad categories (Observability, Security, ...) that cut across every playlist.

Defined under `categories:` in wiki.yaml as name -> keywords. A video is in a category when a keyword is in
its title, its Claude topics or summary, or its transcript keeps coming back to it (at least
category_settings.min_mentions chunks and min_share of all its chunks). Nothing is stored: membership is
recomputed from the labels and transcripts, so editing the keywords takes effect on the next run.
"""

import json
import re
from collections import Counter
from functools import lru_cache

from llmwiki import config, db
from llmwiki.config import WIKI_DIR

KIND_ORDER = {"case_study": 0, "concept": 1, "tutorial": 2, "panel": 3, "keynote": 4, "other": 5, None: 6}
KIND_LABEL = {"case_study": "case study", "concept": "concept", "tutorial": "tutorial", "panel": "panel",
              "keynote": "keynote", "other": "other", None: "unlabeled"}


def defined() -> dict[str, list[str]]:
    cats = config.load().get("categories") or {}
    return {str(name): [str(k).lower() for k in (kws or [])] for name, kws in cats.items()}


def find_category(text: str) -> str | None:
    t = text.strip().lower()
    for name in defined():
        if name.lower() == t or config.slugify(name) == config.slugify(t):
            return name
    return None


def _pattern(keywords: list[str]):
    alts = sorted({re.escape(k) for k in keywords if k}, key=len, reverse=True)
    return re.compile(r"(?<![\w-])(?:" + "|".join(alts) + r")(?![\w-])", re.I) if alts else None


@lru_cache
def membership() -> dict[str, list[str]]:
    """{category: [video ids]} for every defined category."""
    settings = config.load().get("category_settings") or {}
    min_mentions = int(settings.get("min_mentions", 6))
    min_share = float(settings.get("min_share", 0.2))
    vids = db.videos()
    with db.get_db() as conn:
        totals = dict(conn.execute("SELECT source_id, count(*) FROM chunks GROUP BY source_id").fetchall())
    out = {}
    for name, kws in defined().items():
        pat = _pattern(kws)
        if not pat:
            out[name] = []
            continue
        mentions: Counter = Counter()
        fts = " OR ".join('"' + " ".join(re.findall(r"\w+", k)) + '"' for k in kws if re.findall(r"\w+", k))
        if fts:
            with db.get_db() as conn:
                for (sid,) in conn.execute("SELECT source_id FROM chunks WHERE chunks MATCH ?", (fts,)):
                    mentions[sid] += 1
        members = []
        for v in vids:
            labels = " ".join([v["title"] or "", v["summary"] or "", " ".join(json.loads(v["topics"] or "[]"))])
            m = mentions.get(v["id"], 0)
            if pat.search(labels) or (m >= min_mentions and m >= min_share * totals.get(v["id"], 1)):
                members.append(v["id"])
        out[name] = members
    return out


@lru_cache
def _by_video() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for name, members in membership().items():
        for vid in members:
            out.setdefault(vid, []).append(name)
    return out


def of_video(vid: str) -> list[str]:
    return _by_video().get(vid, [])


def _when(p) -> str:
    if not p["year"]:
        return "undated"
    return f"{p['year']}-{p['month']:02d}" if p["month"] else str(p["year"])


def build_pages() -> list[str]:
    """wiki/categories/<name>.md for every category, plus wiki/categories/index.md."""
    if not config.DB_PATH.exists() or not defined():
        return []
    membership.cache_clear()
    _by_video.cache_clear()
    folder = WIKI_DIR / "categories"
    folder.mkdir(parents=True, exist_ok=True)
    pls = db.playlists()
    transcripts = config.load().get("research", {}).get("transcript_pages", True)
    written = []
    plural = lambda n, word, many=None: f"{n} {word if n == 1 else (many or word + 's')}"
    for old in folder.glob("*.md"):  # categories removed from wiki.yaml, or now empty
        if old.name != "index.md":
            old.unlink()
    for name, members in membership().items():
        if not members:
            continue
        members_set = set(members)
        seen: set[str] = set()
        events = []
        for p in pls:  # timeline order; a video in several playlists goes under the first
            rows = [v for v in db.playlist_items(p["id"]) if v["id"] in members_set and v["id"] not in seen]
            if rows:
                seen.update(v["id"] for v in rows)
                events.append((p, sorted(rows, key=lambda v: (KIND_ORDER.get(v["kind"], 9), v["position"]))))
        n_case = sum(1 for _, rows in events for v in rows if v["kind"] == "case_study")
        orgs = Counter(o for _, rows in events for v in rows if v["kind"] == "case_study"
                       for o in json.loads(v["orgs"] or "[]"))
        slug = config.slugify(name)
        lines = ["---", f'title: "{name}"',
                 f"summary: {plural(len(seen), 'talk')} ({plural(n_case, 'case study', 'case studies')}) across "
                 f"{plural(len(events), 'event')}"
                 + (f"; organizations include {', '.join(o for o, _ in orgs.most_common(6))}" if orgs else "") + ".",
                 f"tags: [category, {slug}]", "generated: categories", "---", "", f"# {name}", "",
                 f"> {plural(len(seen), 'talk')} across {plural(len(events), 'event')}, oldest first: "
                 f"{plural(n_case, 'case study', 'case studies')} where an organization reports its own experience, "
                 "plus concept talks and tutorials.", "",
                 f"Keywords: {', '.join(defined()[name])} (edit under `categories:` in wiki.yaml).", ""]
        by_year = Counter()
        case_by_year = Counter()
        for p, rows in events:
            by_year[p["year"] or 0] += len(rows)
            case_by_year[p["year"] or 0] += sum(v["kind"] == "case_study" for v in rows)
        if by_year:
            lines += ["## Over time", "", "| Year | Talks | Case studies |", "| --- | --- | --- |"]
            lines += [f"| {y or 'undated'} | {by_year[y]} | {case_by_year[y]} |" for y in sorted(by_year)]
            lines.append("")
        if orgs:
            lines += ["## Organizations with case studies", "",
                      ", ".join(f"{o} ({c})" if c > 1 else o for o, c in orgs.most_common()), ""]
        lines += ["## Talks by event", ""]
        for p, rows in events:
            lines += [f"### {_when(p)} · [{p['title']}](../sources/{p['id']}.md)", ""]
            for v in rows:
                link = f"../sources/videos/{v['id']}.md" if transcripts and v["status"] == "ok" else \
                    f"https://www.youtube.com/watch?v={v['id']}"
                org = ", ".join(json.loads(v["orgs"] or "[]"))
                lines.append(f"- **{KIND_LABEL.get(v['kind'], v['kind'])}** · [{v['title']}]({link})"
                             + (f" — {org}" if org else "") + (f". {v['summary']}" if v["summary"] else ""))
            lines.append("")
        (folder / f"{slug}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        written.append(f"categories/{slug}.md")
    return written

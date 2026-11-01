"""Label every video: what kind of talk it is, whose experience it reports, and what it covers.

  kind:   case_study (an organization reports its own use: adoption, migration, scaling, incident, lessons)
          concept    (how a technology works, design, deep dive, project update)
          tutorial   (hands-on, workshop, getting started)
          panel | keynote | other
  orgs:   for case studies, the organizations whose own experience it is (not the vendor of the tool)
  topics: technologies and concepts it covers

  wiki classify                  # Claude labels unlabeled videos (and replaces heuristic labels), 30 per call
  wiki classify --heuristic      # free and instant: rules on the title only
  wiki classify --all            # relabel everything
"""

import json
import re

from llmwiki import claude, db

BATCH = 30

CASE = re.compile(
    r"\b(how|why|what) (we|our|i)\b|\bour (journey|story|experience|path|migration)\b|\bjourney\b|lessons? learned|"
    r"\bin production\b|\bcase study\b|\bmigrat\w*|\bwar stor|\bpost-?mortem|\bat scale\b|\badopt\w*|\bend[- ]user\b|"
    r"\bfrom .{2,40} to\b|\breal[- ]world\b|\bsuccess stor", re.I)
# Case-sensitive: an organization name right after "at" or "How": "... at Spotify", "How Zalando Runs ..."
ORG_CASE = re.compile(
    r"\b[Aa]t (?!Scale\b|KubeCon\b|CNCF\b|The\b|A\b|An\b)[A-Z][\w&.]+|"
    r"\b[Hh]ow (?!To\b|We\b|I\b|You\b|The\b|A\b|An\b|Not\b)[A-Z][\w&.]+(?: [A-Z][\w&.]+)? (?:\w+ )?"
    r"(?:[Uu]ses?|[Uu]sed|[Ss]caled?|[Rr]uns?|[Bb]uilt|[Bb]uilds|[Mm]oved|[Mm]igrated|[Aa]dopted|[Mm]anages?|"
    r"[Oo]perates?|[Ss]ecured?|[Ss]aved?|[Rr]educed?|[Cc]ut|[Ss]hips?|[Tt]amed)\b")
ORG_AFTER = re.compile(r"\b(?:[Aa]t|[Hh]ow) ([A-Z][\w&.]+(?: [A-Z][\w&.]+)?)")
KEYNOTE = re.compile(r"\bkeynote\b|opening remarks|closing remarks|welcome", re.I)
PANEL = re.compile(r"\bpanel\b|\bfireside\b|\bask me anything\b|\bama\b", re.I)
TUTORIAL = re.compile(r"\btutorial\b|\bworkshop\b|hands-on|getting started|\b101\b|\bintro(duction)? to\b|\blab\b|"
                      r"\bbeginner", re.I)


def split_title(title: str) -> tuple[str, list[str]]:
    """'Talk - Ana Li, Spotify & Bo Chen, Google' -> ('Talk', ['Spotify', 'Google'])."""
    parts = re.split(r"\s[-–|]\s", title)
    if len(parts) < 2:
        return title, []
    talk, people = " - ".join(parts[:-1]), parts[-1]
    orgs = []
    for person in re.split(r"\s*(?:&|;|\band\b)\s*", people):
        if "," in person:
            org = person.split(",", 1)[1].strip()
            if org and org not in orgs:
                orgs.append(org)
    return talk, orgs


def heuristic(title: str) -> dict:
    talk, speaker_orgs = split_title(title)
    if KEYNOTE.search(talk):
        kind = "keynote"
    elif PANEL.search(talk):
        kind = "panel"
    elif TUTORIAL.search(talk):
        kind = "tutorial"
    elif CASE.search(talk) or ORG_CASE.search(talk):
        kind = "case_study"
    else:
        kind = "concept"
    orgs = []
    if kind == "case_study":
        m = ORG_CASE.search(talk) and ORG_AFTER.search(ORG_CASE.search(talk).group(0))
        if m:
            name = re.sub(r" (?:[A-Z]\w*ed|Uses?|Runs?|Builds?|Manages?|Operates?|Ships?)$", "", m.group(1))
            orgs.append(name)
        orgs += [o for o in speaker_orgs if o not in orgs]
    return {"kind": kind, "orgs": orgs, "topics": [], "summary": ""}


def classify_heuristic(only_unclassified: bool = True) -> int:
    rows = db.videos("kind IS NULL" if only_unclassified else "classified_by IS NOT 'claude' OR kind IS NULL")
    for v in rows:
        h = heuristic(v["title"] or "")
        db.set_video_class(v["id"], h["kind"], h["orgs"], h["topics"], h["summary"], "heuristic")
    return len(rows)


PROMPT = """Label each conference talk below. Use the title, its playlist (event) and the start of its transcript.

kind, exactly one of:
  case_study  an organization reports ITS OWN real use: adoption, migration, scaling, operating in production,
              an incident or outage, cost results, lessons learned. Vendor product pitches are NOT case studies.
  concept     how a technology or pattern works: design, architecture, deep dive, project update, roadmap
  tutorial    hands-on, workshop, getting started
  panel       panel or group discussion
  keynote     keynote, opening or closing remarks, sponsor stage talk
  other       anything else
orgs: for case_study, the organizations whose own experience it is (e.g. ["Spotify"]). Otherwise [].
topics: 3 to 8 specific technologies or concepts covered, as short lowercase names (e.g. "cilium", "multi-tenancy",
  "gpu scheduling", "cost optimization"). Prefer project names over generic words.
summary: one sentence on what the talk shows. For a case study, name the organization and the outcome.

TALKS (JSON):
{talks}

Reply with ONLY this JSON object: {{"videos": [{{"id": "...", "kind": "...", "orgs": [], "topics": [], "summary": "..."}}]}}"""


def _opening(vid: str, chars: int = 1500) -> str:
    text = ""
    for c in db.source_chunks(vid):
        text += " " + c["text"]
        if len(text) > chars:
            break
    return text.strip()[:chars]


def classify_claude(relabel_all: bool = False, limit: int = 0, log=print, model: str | None = None) -> dict:
    where = "1" if relabel_all else "kind IS NULL OR classified_by IS NOT 'claude'"
    rows = db.videos(where)
    if limit:
        rows = rows[:limit]
    done, failed = 0, 0
    for start in range(0, len(rows), BATCH):
        batch = rows[start:start + BATCH]
        talks = []
        for v in batch:
            pls = db.video_playlists(v["id"])
            talks.append({"id": v["id"], "title": v["title"], "playlist": pls[0]["title"] if pls else "",
                          "transcript_start": _opening(v["id"])})
        result = claude.run(PROMPT.format(talks=json.dumps(talks, ensure_ascii=False)), [], timeout_min=10,
                            model=model)
        labels = {x.get("id"): x for x in result.get("videos") or [] if isinstance(x, dict)}
        for v in batch:
            x = labels.get(v["id"])
            if not x or x.get("kind") not in ("case_study", "concept", "tutorial", "panel", "keynote", "other"):
                failed += 1
                continue
            db.set_video_class(v["id"], x["kind"], [str(o) for o in x.get("orgs") or []],
                               [str(t).lower() for t in x.get("topics") or []], str(x.get("summary") or ""), "claude")
            done += 1
        log(f"  labeled {done}/{len(rows)}" + (f" ({failed} not labeled: {result.get('reason', '')[:120]})"
                                               if failed else ""))
    return {"labeled": done, "failed": failed, "total": len(rows)}

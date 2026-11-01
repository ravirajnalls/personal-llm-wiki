"""Build the research prompt and run it. The agent finds sources, ingests them, writes or updates one
page, and the checks run before anything is committed."""

import json
import subprocess
from datetime import date

from llmwiki import claude, config, db, pages, references, verify
from llmwiki.config import ROOT, WIKI_DIR


def _style() -> str:
    path = ROOT / "style.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _existing_page(coll: str, slug: str):
    path = WIKI_DIR / coll / f"{slug}.md"
    return path if path.exists() else None


def build_prompt(topic: str, coll_name: str, coll: dict, slug: str, urls: list[str], files: list[str],
                 web_search: bool, notes: str = "") -> str:
    cfg = config.load()
    rc = cfg.get("research", {})
    max_sources = rc.get("max_sources", 8)
    years = rc.get("prefer_recent_years", 3)
    page = f"wiki/{coll_name}/{slug}.md"
    exists = _existing_page(coll_name, slug)
    prefer = ", ".join(coll.get("prefer_domains") or []) or "any reputable site"
    avoid = ", ".join(coll.get("avoid_domains") or []) or "none"
    channels = ", ".join(coll.get("youtube_channels") or [])
    sections = "\n".join(f"     ## {s}" for s in coll.get("sections") or ["Summary", "Key ideas"])
    given = "\n".join(f"     - {u}" for u in urls + files) or "     (none)"

    discover = (f"""2. DISCOVER. Use WebSearch to find up to {max_sources} strong sources on the topic, mixing kinds:
   primary docs or papers, in-depth articles, and recorded talks or interviews on YouTube.
   - Prefer these domains: {prefer}. Never cite: {avoid}.
   {f"- Good YouTube channels for this collection: {channels}." if channels else ""}
   - Prefer material from the last {years} years unless the topic is historical or the original source is older.
   - Skip SEO listicles, content farms and pages that only rehash other pages.
   - The user's own sources below come first and must be used."""
                if web_search else
                f"""2. DISCOVER. Web search is OFF: build the page ONLY from the synced sources in memory and the user's sources below.
   Start with the timeline of every talk on the topic, across all playlists (events), oldest first:
     wiki find "TOPIC" --kind all
     wiki find "TOPIC"                      (case studies only: organizations reporting their own use)
   Run it for synonyms and related project names too. Then find exact passages:
     wiki search "KEYWORDS" --limit 20      (add --playlist ID to stay inside one event)
   Read wiki/sources/videos/<video id>.md for the full transcript around a hit.
   Add a "## Timeline" section (after the first section) showing how the topic evolved across events: what
   changed from year to year, and which organizations reported what. Cover every relevant case study `wiki find` lists, not just the first few.
   Use up to {max_sources * 2} videos if they add something; drop ones that only repeat others.""")

    return f"""You are the research agent for a personal wiki ("{cfg['title']}"). Working directory: {ROOT}
Today is {date.today():%Y-%m-%d}.

TOPIC: {topic}
COLLECTION: {coll_name} ({coll.get('description', '')})
PAGE: {page} ({'EXISTS: update it, keep what is still right, add what is new' if exists else 'new page'})
USER'S SOURCES:
{given}
{f"USER'S NOTES: {notes}" if notes else ""}

1. READ FIRST. Read wiki/index.md{f' and {page}' if exists else ''}. Check memory for what you already have:
     wiki search "KEYWORDS"
   Reuse pages that exist (link to them) instead of repeating them.

{discover}

3. INGEST every source you will cite. This stores its text so citations can be checked:
     wiki ingest URL_OR_PATH
   YouTube links get timestamped captions; web pages and PDFs get their text. If a source fails to ingest
   (no captions, blocked, needs JavaScript), you may read it with WebFetch, but say so in the run report
   and prefer sources that ingest.

4. FIND EXACT SPOTS. For each claim, search memory and copy the citation it prints:
     wiki search "KEYWORDS" --source SOURCE_ID
   Citation formats (the search output prints them ready to paste):
     video: [▶ 12:34](https://www.youtube.com/watch?v=VIDEO&t=754s)   MM:SS must equal the t= seconds
     web:   [example.com](https://example.com/page#:~:text=first%20words%20of%20the%20passage)
     pdf:   [paper.pdf p.3](../files/paper.pdf#page=3)
   The words in a #:~:text= fragment must appear verbatim in the source. Never invent a timestamp, page, quote or number.

5. WRITE {page}:
   - YAML frontmatter:
       title: (human title)
       summary: (one line)
       tags: [a, few, tags]
       updated: {date.today():%Y-%m-%d}
   - Then "# Title", a one-sentence blockquote answer, then these sections in order (drop "Disagreements" or
     "Open questions" if there is nothing to say):
{sections}
   - Every factual sentence ends with a citation. Link other wiki pages with relative links (same folder: other.md,
     other collection: ../tech/other.md).
   - Do NOT write a References or Sources section; step 6 generates it.
   Writing style:
{_style()}

6. CHECK. Run:
     wiki check
   Fix every ERROR it reports for {page} and rerun until it is clean. Warnings about sections are worth fixing too.
   Don't edit other pages except to add a link to {page} where it clearly belongs. Don't run git.

End with ONLY this JSON object on the last line:
{{"status": "done" | "failed", "page": "{page}", "sources_ingested": N, "citations": N, "notes": "anything the user should know, e.g. sources you couldn't ingest"}}"""


def git_commit(message: str, push: bool) -> str:
    def git(*args):
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if git("rev-parse", "--is-inside-work-tree").returncode != 0:
        return "not a git repo, skipped commit"
    git("add", "wiki")
    c = git("commit", "-m", message)
    if c.returncode != 0:
        return "nothing to commit"
    if push:
        p = git("push")
        return "committed and pushed" if p.returncode == 0 else f"committed; push failed: {p.stderr.strip()[:200]}"
    return "committed"


def research(topic: str, collection: str | None = None, urls: list[str] | None = None,
             files: list[str] | None = None, web_search: bool | None = None, slug: str | None = None,
             notes: str = "", commit: bool = True, push: bool = False, model: str | None = None) -> dict:
    coll_name, coll = config.collection(collection)
    if web_search is None:
        rc = config.load().get("research", {})
        web_search = rc.get("web_search", not config.load().get("channel"))
    slug = slug or config.slugify(topic)
    (WIKI_DIR / coll_name).mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(topic, coll_name, coll, slug, urls or [], files or [], web_search, notes)
    timeout = config.load().get("research", {}).get("timeout_minutes", 20)
    tools = claude.RESEARCH_TOOLS if web_search else [t for t in claude.RESEARCH_TOOLS if t != "WebSearch"]
    result = claude.run(prompt, tools, timeout_min=timeout, model=model)

    page = f"{coll_name}/{slug}.md"
    if (WIKI_DIR / page).exists():
        references.update_all()
        pages.rebuild_index()
        errors, warnings = verify.check_page(WIKI_DIR / page)
        result["errors"], result["warnings"] = errors, warnings
        if result.get("status") == "done" and commit and not errors:
            result["git"] = git_commit(f"wiki: {topic}", push)
    elif result.get("status") == "done":
        result["status"] = "failed"
        result["reason"] = f"agent reported done but {page} doesn't exist"
    db.log_run(topic, coll_name, result.get("status", "failed"), page,
               json.dumps({k: v for k, v in result.items() if k != "_text"})[:2000])
    return result


def ask(question: str, model: str | None = None) -> str:
    prompt = f"""Answer the question using ONLY this personal wiki (folder wiki/) and its source memory.
Working directory: {ROOT}
Start from wiki/index.md, read the relevant pages, and use `wiki search "KEYWORDS"` for passages from ingested sources.
Answer in a few short paragraphs. Keep the citations the pages use (copy their links) so every claim is traceable,
and name the wiki pages you used. If the wiki doesn't cover it, say so plainly and suggest a `wiki research` topic.

QUESTION: {question}

End with ONLY this JSON object on the last line: {{"answer": "markdown answer", "pages": ["collection/page.md"]}}"""
    result = claude.run(prompt, claude.READ_TOOLS, timeout_min=10, model=model)
    return result.get("answer") or result.get("reason") or result.get("_text", "")

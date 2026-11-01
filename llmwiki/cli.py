"""wiki: research topics into a cited personal wiki.

  wiki sync [--list-only] [--max N]    list every playlist on the channel, fetch new transcripts
  wiki classify [--heuristic]          label videos: case study, concept, ...; orgs and topics
  wiki find "topic" [--kind K] [--page] every case study (or talk) on a topic, across playlists, by date
  wiki sources                         the playlists on the timeline, with counts
  wiki auto                            sync + classify + rebuild + commit + push, unattended
  wiki schedule [--time HH:MM]         run `wiki auto` daily (Task Scheduler / cron); --remove to stop
  wiki research "topic" [-c collection] [--url URL ...] [--file PATH ...] [--web | --no-search] [--push]
  wiki ask "question"                  answer from your wiki, with citations
  wiki ingest URL_OR_PATH ...          add a source to memory without writing a page
  wiki search "keywords" [--source ID] find passages in ingested sources, with ready-to-paste citations
  wiki check [--fix]                   rebuild References + index, verify every citation
  wiki list                            pages, sources and recent runs
  wiki serve                           preview the site (mkdocs serve)
  wiki init [FOLDER]                   start a new wiki folder
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from llmwiki import config


def cmd_research(a):
    from llmwiki.research import research
    for topic in a.topics:
        print(f"Researching: {topic}", flush=True)
        web = True if a.web else (False if a.no_search else None)
        r = research(topic, a.collection, a.url, a.file, web_search=web, slug=a.slug,
                     notes=a.notes or "", commit=not a.no_commit, push=a.push, model=a.model)
        print(f"  {r.get('status')}: {r.get('page', '')}")
        for k in ("sources_ingested", "citations", "git", "notes", "reason"):
            if r.get(k):
                print(f"  {k}: {r[k]}")
        for e in r.get("errors", []):
            print(f"  ERROR {e}")
        for w in r.get("warnings", []):
            print(f"  warn  {w}")


def cmd_ask(a):
    from llmwiki.research import ask
    print(ask(" ".join(a.question), model=a.model))


def cmd_ingest(a):
    from llmwiki.ingest import ingest
    for t in a.targets:
        print(json.dumps(ingest(t, force=a.force), ensure_ascii=False))


def cmd_search(a):
    from llmwiki import cite, db
    rows = db.search(" ".join(a.query), a.limit, a.source, a.playlist)
    if not rows:
        print("No matches. Try fewer or different words, or ingest more sources.")
    for r in rows:
        loc = cite.mmss(int(r["loc"])) if r["kind"] == "video" else f"#{r['loc']}"
        print(f"--- {r['title'] or r['source_id']}  [{r['source_id']} {loc}]")
        print("  " + " ".join(r["snippet"].split()))
        print(f"  cite: {cite.for_chunk(r)}")


def cmd_sync(a):
    from llmwiki import pages, sync
    st = sync.sync(a.playlist, list_only=a.list_only, retry=a.retry, max_fetch=a.max, delay=a.delay)
    pages.rebuild_index()
    print(f"\n{st['playlists']} playlists, {st['videos']} videos listed; {st['fetched']} new transcripts, "
          f"{st['no_transcript']} without captions, {st['errors']} errors")
    for f in st["failed_playlists"]:
        print(f"  failed playlist {f}")
    print("Next: `wiki classify` labels case studies with Claude (titles-only labels are already in place).")


def cmd_classify(a):
    from llmwiki import catalog, classify, pages
    if a.heuristic:
        n = classify.classify_heuristic(only_unclassified=not a.all)
        print(f"Labeled {n} videos from their titles.")
    else:
        r = classify.classify_claude(relabel_all=a.all, limit=a.limit, model=a.model)
        print(f"Labeled {r['labeled']} of {r['total']} videos with Claude ({r['failed']} not labeled).")
    catalog.build()
    pages.rebuild_index()


def cmd_find(a):
    from llmwiki import find, pages
    kinds = None if a.kind == "all" else a.kind.split(",")
    groups = find.find(" ".join(a.topic), kinds, a.min_mentions, a.playlist)
    find.print_results(" ".join(a.topic), groups, kinds)
    if a.page and groups:
        path = find.write_page(" ".join(a.topic), groups, kinds)
        pages.rebuild_index()
        print(f"Wrote wiki/{path}")


def cmd_sources(a):
    from llmwiki import db, find
    if not config.DB_PATH.exists() or not db.playlists():
        print("Nothing synced yet. Set `channel:` in wiki.yaml, then run `wiki sync`.")
        return
    for p in db.playlists():
        print(f"{find.when(p):<8} {p['n_videos']:>4} videos {p['n_ok'] or 0:>4} transcripts "
              f"{p['n_case_studies'] or 0:>3} case studies  {p['title'][:70]}")
    counts = {r["status"]: r["n"] for r in db.get_db().execute("SELECT status, count(*) n FROM videos GROUP BY status")}
    print(f"\nVideos: {sum(counts.values())} total, " + ", ".join(f"{v} {k}" for k, v in counts.items()))


def cmd_auto(a):
    from llmwiki import auto
    sys.exit(auto.run())


def cmd_schedule(a):
    from llmwiki import auto
    print(auto.remove() if a.remove else auto.install(a.time))


def cmd_check(a):
    from llmwiki import pages, references, verify
    changed = references.update_all()
    pages.rebuild_index()
    errors, warnings = verify.check_all(fix=a.fix)
    for c in changed:
        print(f"refs  {c}")
    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors and not a.fix else 0)


def cmd_list(a):
    from llmwiki import db, pages
    ps = [pages.page_info(p) for p in pages.content_pages()]
    print(f"Pages ({len(ps)})")
    for i in ps:
        print(f"  {i['path']:<50} {i['summary'][:70]}")
    if config.DB_PATH.exists():
        srcs = db.all_sources()
        print(f"\nSources ({len(srcs)})")
        for s in srcs[: a.limit]:
            print(f"  {s['kind']:<5} {(s['title'] or s['id'])[:60]:<60} {s['n_chunks']} chunks")
        runs = db.recent_runs(a.limit)
        if runs:
            print("\nRecent runs")
            for r in runs:
                print(f"  {r['time']}  {r['status']:<7} {r['topic']}")


def cmd_serve(a):
    if not shutil.which("mkdocs"):
        sys.exit("mkdocs not installed: pip install -e .")
    subprocess.run(["mkdocs", "serve", "-a", a.addr], cwd=config.ROOT)


def cmd_init(a):
    dest = Path(a.folder).expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent.parent
    for name in ("wiki.yaml", "style.md", "mkdocs.yml", ".gitignore"):
        if (src / name).exists() and not (dest / name).exists():
            shutil.copy2(src / name, dest / name)
    (dest / "wiki").mkdir(exist_ok=True)
    print(f"New wiki at {dest}. cd there, edit wiki.yaml, then: wiki research \"your first topic\"")


def main(argv=None):
    p = argparse.ArgumentParser(prog="wiki", description=__doc__.splitlines()[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("research", help="research topics and write cited pages")
    r.add_argument("topics", nargs="+")
    r.add_argument("-c", "--collection")
    r.add_argument("--url", action="append", default=[], help="a source you want used (repeatable)")
    r.add_argument("--file", action="append", default=[], help="a local file to use as a source (repeatable)")
    r.add_argument("--web", action="store_true", help="also search the web (default when wiki.yaml has no sources)")
    r.add_argument("--no-search", action="store_true", help="only use synced sources, --url/--file and memory")
    r.add_argument("--slug", help="page file name (default: from the topic)")
    r.add_argument("--notes", help="extra guidance, e.g. 'focus on cost'")
    r.add_argument("--no-commit", action="store_true")
    r.add_argument("--push", action="store_true", help="git push after committing")
    r.add_argument("--model")
    r.set_defaults(fn=cmd_research)

    y = sub.add_parser("sync", help="sync the channel's playlists, videos and transcripts")
    y.add_argument("--playlist", help="one playlist id or URL only")
    y.add_argument("--list-only", action="store_true", help="refresh playlists and videos, skip transcripts")
    y.add_argument("--max", type=int, default=0, help="fetch at most N transcripts this run")
    y.add_argument("--retry", action="store_true", help="retry videos that failed or had no transcript")
    y.add_argument("--delay", type=float, default=1.0, help="seconds between transcripts (default 1)")
    y.set_defaults(fn=cmd_sync)

    k = sub.add_parser("classify", help="label videos as case study / concept / ..., with orgs and topics")
    k.add_argument("--heuristic", action="store_true", help="free, title-only rules instead of Claude")
    k.add_argument("--all", action="store_true", help="relabel every video")
    k.add_argument("--limit", type=int, default=0, help="label at most N videos")
    k.add_argument("--model")
    k.set_defaults(fn=cmd_classify)

    f = sub.add_parser("find", help="every case study on a topic across playlists, on the timeline")
    f.add_argument("topic", nargs="+")
    f.add_argument("--kind", default="case_study",
                   help="case_study (default), concept, tutorial, panel, keynote, other, a comma list, or all")
    f.add_argument("--min-mentions", type=int, default=2, help="transcript mentions needed (default 2)")
    f.add_argument("--playlist", help="limit to one playlist id")
    f.add_argument("--page", action="store_true", help="write the result to wiki/topics/<topic>.md")
    f.set_defaults(fn=cmd_find)

    u = sub.add_parser("auto", help="one unattended update: sync, classify, rebuild, commit, push")
    u.set_defaults(fn=cmd_auto)

    h = sub.add_parser("schedule", help="run `wiki auto` every day")
    h.add_argument("--time", help="HH:MM, 24h (default: schedule.time in wiki.yaml, else 02:00)")
    h.add_argument("--remove", action="store_true", help="remove the scheduled task")
    h.set_defaults(fn=cmd_schedule)

    o = sub.add_parser("sources", help="playlists on the timeline, with counts")
    o.set_defaults(fn=cmd_sources)

    q = sub.add_parser("ask", help="answer a question from the wiki")
    q.add_argument("question", nargs="+")
    q.add_argument("--model")
    q.set_defaults(fn=cmd_ask)

    i = sub.add_parser("ingest", help="add sources to memory")
    i.add_argument("targets", nargs="+")
    i.add_argument("--force", action="store_true", help="re-ingest even if already in memory")
    i.set_defaults(fn=cmd_ingest)

    s = sub.add_parser("search", help="full-text search ingested sources")
    s.add_argument("query", nargs="+")
    s.add_argument("--source", help="limit to one source id (video id, URL or files/name)")
    s.add_argument("--playlist", help="limit to the videos of one playlist (its id)")
    s.add_argument("--limit", type=int, default=8)
    s.set_defaults(fn=cmd_search)

    c = sub.add_parser("check", help="rebuild References and index, verify citations")
    c.add_argument("--fix", action="store_true", help="move video citations to where the quote was found")
    c.set_defaults(fn=cmd_check)

    l = sub.add_parser("list", help="pages, sources and recent runs")
    l.add_argument("--limit", type=int, default=15)
    l.set_defaults(fn=cmd_list)

    v = sub.add_parser("serve", help="preview the site")
    v.add_argument("--addr", default="127.0.0.1:8000")
    v.set_defaults(fn=cmd_serve)

    n = sub.add_parser("init", help="start a new wiki folder")
    n.add_argument("folder", nargs="?", default=".")
    n.set_defaults(fn=cmd_init)

    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()

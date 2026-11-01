"""Sync the YouTube sources listed under `sources:` in wiki.yaml.

For each playlist or channel: list every video, fetch the full transcript of each one that isn't in memory
yet, store it chunked for full-text search, then write the source catalog pages under wiki/sources/.
Re-running only fetches what's new (and, with --retry, what failed before).

  wiki sync                     # every source
  wiki sync kubecon-eu-2025     # one source by name
  wiki sync --retry             # also retry videos that had no transcript or errored
"""

import re
import time

from llmwiki import cite, config, db
from llmwiki.config import WIKI_DIR
from llmwiki.ingest import ingest_video, youtube_id

TYPES = ("youtube_playlist", "youtube_channel", "youtube_video")
SOURCES_DIR = WIKI_DIR / "sources"


def configured_sources() -> list[dict]:
    """The `sources:` list from wiki.yaml, validated, with defaults filled in."""
    cfg = config.load()
    out = []
    for i, s in enumerate(cfg.get("sources") or [], 1):
        if not isinstance(s, dict) or not s.get("url"):
            raise SystemExit(f"wiki.yaml sources #{i}: needs at least a url")
        s = dict(s)
        s.setdefault("type", _guess_type(s["url"]))
        if s["type"] not in TYPES:
            raise SystemExit(f"wiki.yaml sources #{i}: type must be one of {', '.join(TYPES)}")
        s.setdefault("name", config.slugify(s.get("title") or s["url"]))
        s.setdefault("collection", cfg["default_collection"])
        s.setdefault("languages", ["en", "en-US", "en-GB"])
        s.setdefault("include", [])
        s.setdefault("exclude", [])
        s.setdefault("limit", 0)
        out.append(s)
    names = [s["name"] for s in out]
    if len(names) != len(set(names)):
        raise SystemExit("wiki.yaml sources: every source needs a unique name")
    return out


def _guess_type(url: str) -> str:
    if "list=" in url:
        return "youtube_playlist"
    if youtube_id(url):
        return "youtube_video"
    return "youtube_channel"


def list_videos(url: str) -> tuple[str, list[dict]]:
    """Title and videos of a playlist or channel, without downloading anything (uses yt-dlp)."""
    import yt_dlp
    class _Quiet:  # errors are raised and reported by sync; don't also print yt-dlp's own
        def debug(self, msg): pass
        def info(self, msg): pass
        def warning(self, msg): pass
        def error(self, msg): pass
    opts = {"extract_flat": "in_playlist", "quiet": True, "no_warnings": True, "skip_download": True,
            "logger": _Quiet()}
    if not "list=" in url and re.search(r"youtube\.com/(@|c/|channel/|user/)", url) and not re.search(
            r"/(videos|streams|playlists)/?$", url):
        url = url.rstrip("/") + "/videos"  # a channel's uploads tab
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    entries = []
    for e in info.get("entries") or []:
        if not e or not e.get("id") or len(e["id"]) != 11:
            continue
        title = e.get("title") or ""
        if title in ("[Private video]", "[Deleted video]"):
            continue
        d = e.get("upload_date") or ""
        entries.append({
            "id": e["id"],
            "title": title,
            "channel": e.get("channel") or e.get("uploader") or info.get("channel") or info.get("uploader") or "",
            "duration": int(e["duration"]) if e.get("duration") else None,
            "published": f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else "",
        })
    return info.get("title") or "", entries


def _wanted(title: str, src: dict) -> bool:
    low = title.lower()
    if src["include"] and not any(k.lower() in low for k in src["include"]):
        return False
    return not any(k.lower() in low for k in src["exclude"])


def sync_source(src: dict, retry: bool = False, delay: float = 1.0, log=print) -> dict:
    name = src["name"]
    if "REPLACE_WITH" in src["url"]:
        raise ValueError("placeholder url: put your playlist URL in wiki.yaml")
    if src["type"] == "youtube_video":
        vid = youtube_id(src["url"])
        title, videos = src.get("title", ""), [{"id": vid, "title": src.get("title", ""), "channel": "",
                                                "duration": None, "published": ""}]
    else:
        title, videos = list_videos(src["url"])
    db.upsert_feed(name, src["type"], src["url"], src.get("title") or title, src["collection"])
    kept = [v for v in videos if _wanted(v["title"], src)]
    if src["limit"]:
        kept = kept[: src["limit"]]
    for pos, v in enumerate(kept, 1):
        db.upsert_item(name, v["id"], pos, v["title"], v["channel"], v["duration"], v["published"])
    log(f"{name}: {len(videos)} videos listed, {len(kept)} kept")

    status = {r["video_id"]: r["status"] for r in db.feed_items(name)}
    todo = [v for v in kept if status.get(v["id"]) in ("pending", None)
            or (retry and status.get(v["id"]) in ("error", "no_transcript"))]
    counts = {"ok": 0, "no_transcript": 0, "error": 0, "already": len(kept) - len(todo)}
    for n, v in enumerate(todo, 1):
        if db.has_source(v["id"]):  # already ingested through another source or `wiki ingest`
            db.set_item_status(name, v["id"], "ok")
            counts["already"] += 1
            continue
        r = ingest_video(v["id"], meta={"title": v["title"], "author": v["channel"], "published": v["published"]},
                         languages=src["languages"])
        if r.get("error"):
            kind = "no_transcript" if re.search(r"TranscriptsDisabled|NoTranscriptFound|VideoUnavailable",
                                                r["error"]) else "error"
            db.set_item_status(name, v["id"], kind, r["error"])
            counts[kind] += 1
            log(f"  [{n}/{len(todo)}] {kind:<13} {v['title'][:70]}")
        else:
            db.set_item_status(name, v["id"], "ok")
            counts["ok"] += 1
            log(f"  [{n}/{len(todo)}] ok {r.get('chunks', 0):>4} chunks  {v['title'][:70]}")
        if delay and n < len(todo):
            time.sleep(delay)  # be gentle; YouTube rate-limits caption requests
    return counts


def sync(names: list[str] | None = None, retry: bool = False, delay: float = 1.0, log=print) -> dict:
    sources = configured_sources()
    if names:
        unknown = set(names) - {s["name"] for s in sources}
        if unknown:
            raise SystemExit(f"No source named {', '.join(sorted(unknown))} in wiki.yaml")
        sources = [s for s in sources if s["name"] in names]
    if not sources:
        raise SystemExit("No sources in wiki.yaml. Add a `sources:` list (see README).")
    results = {}
    for s in sources:
        try:
            results[s["name"]] = sync_source(s, retry, delay, log)
        except Exception as e:  # one broken playlist shouldn't stop the rest
            results[s["name"]] = {"failed": f"{type(e).__name__}: {e}".removeprefix("DownloadError: ERROR: ")[:300]}
    build_catalog()
    return results


# ---------- catalog pages: wiki/sources/ ----------

def _dur(seconds) -> str:
    return cite.mmss(seconds) if seconds else ""


def build_catalog(transcript_pages: bool | None = None) -> list[str]:
    """wiki/sources/index.md, one index per source, and (optionally) one transcript page per video."""
    cfg = config.load()
    if transcript_pages is None:
        transcript_pages = cfg.get("research", {}).get("transcript_pages", True)
    if not config.DB_PATH.exists():
        return []
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    top = ["# Sources", "", "Everything the wiki is built from, synced from `sources:` in wiki.yaml.", "",
           "| Source | Collection | Videos | Transcripts | Synced |", "| --- | --- | --- | --- | --- |"]
    for f in db.feeds():
        items = db.feed_items(f["name"])
        top.append(f"| [{f['title'] or f['name']}]({f['name']}/index.md) | {f['collection']} | {f['n_videos']} | "
                   f"{f['n_ok'] or 0} | {(f['synced_at'] or '')[:10]} |")
        folder = SOURCES_DIR / f["name"]
        folder.mkdir(exist_ok=True)
        lines = [f"# {f['title'] or f['name']}", "", f"[{f['url']}]({f['url']}) · collection: {f['collection']} · "
                 f"{f['n_ok'] or 0} of {f['n_videos']} transcripts", "",
                 "| # | Video | Channel | Published | Length | Transcript |", "| --- | --- | --- | --- | --- | --- |"]
        for it in items:
            t = (it["title"] or it["video_id"]).replace("|", "/")
            link = f"[{t}]({it['video_id']}.md)" if transcript_pages and it["status"] == "ok" else \
                f"[{t}](https://www.youtube.com/watch?v={it['video_id']})"
            state = {"ok": "yes", "no_transcript": "none available", "error": "error", "pending": "not yet"}.get(
                it["status"], it["status"])
            lines.append(f"| {it['position']} | {link} | {(it['channel'] or '').replace('|', '/')} | "
                         f"{it['published'] or ''} | {_dur(it['duration'])} | {state} |")
            if transcript_pages and it["status"] == "ok":
                _write_transcript_page(folder, it)
        (folder / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(f"sources/{f['name']}/index.md")
    (SOURCES_DIR / "index.md").write_text("\n".join(top) + "\n", encoding="utf-8")
    written.append("sources/index.md")
    return written


def _write_transcript_page(folder, it):
    path = folder / f"{it['video_id']}.md"
    chunks = db.source_chunks(it["video_id"])
    if not chunks:
        return
    title = (it["title"] or it["video_id"]).replace('"', "'")
    out = ["---", f'title: "{title}"', f"video: {it['video_id']}", f"channel: \"{(it['channel'] or '').replace(chr(34), '')}\"",
           f"published: \"{it['published'] or ''}\"", "---", "", f"# {it['title'] or it['video_id']}", "",
           f"{it['channel'] or ''} · {it['published'] or ''} · {_dur(it['duration'])} · "
           f"[Watch on YouTube](https://www.youtube.com/watch?v={it['video_id']})", "", "## Transcript", ""]
    out += [f"{cite.video(it['video_id'], int(c['loc']))} {c['text']}\n" for c in chunks]
    text = "\n".join(out)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")

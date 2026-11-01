"""Sync one YouTube channel: every playlist (a point on the timeline) and every video in it.

  wiki sync                      # list playlists + videos, fetch new transcripts, rebuild the catalog
  wiki sync --list-only          # just refresh playlists and videos (fast), no transcripts
  wiki sync --max 200            # fetch at most 200 transcripts this run (YouTube rate-limits big bursts)
  wiki sync --playlist PLxxxx    # one playlist only
  wiki sync --retry              # also retry videos that had no transcript or errored

Configured under `channel:` in wiki.yaml. Re-running only fetches what's new.
"""

import re
import time

from llmwiki import config, db
from llmwiki.ingest import ingest_video

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def channel_config() -> dict:
    cfg = config.load()
    ch = cfg.get("channel")
    if not ch or not ch.get("url"):
        raise SystemExit("No channel in wiki.yaml. Add:\n  channel:\n    url: https://www.youtube.com/@handle")
    ch = dict(ch)
    ch.setdefault("collection", cfg["default_collection"])
    ch.setdefault("languages", ["en", "en-US", "en-GB"])
    pl = dict(ch.get("playlists") or {})
    for k in ("include", "exclude", "only"):
        pl[k] = [str(x) for x in pl.get(k) or []]
    pl["timeline"] = {str(k): str(v) for k, v in (pl.get("timeline") or {}).items()}
    ch["playlists"] = pl
    vids = dict(ch.get("videos") or {})
    vids["exclude"] = [str(x) for x in vids.get("exclude") or []]
    ch["videos"] = vids
    return ch


def _ydl():
    import yt_dlp

    class _Quiet:  # sync reports errors itself
        def debug(self, msg): pass
        def info(self, msg): pass
        def warning(self, msg): pass
        def error(self, msg): pass

    return yt_dlp.YoutubeDL({"extract_flat": "in_playlist", "quiet": True, "no_warnings": True,
                             "skip_download": True, "logger": _Quiet()})


def playlist_id(text: str) -> str:
    m = re.search(r"list=([\w-]+)", text)
    return m.group(1) if m else text.strip()


def list_playlists(channel_url: str) -> list[dict]:
    """[{id, title}] for every public playlist on the channel."""
    url = re.sub(r"/(videos|streams|shorts|featured|playlists)/?$", "", channel_url.rstrip("/")) + "/playlists"
    with _ydl() as ydl:
        info = ydl.extract_info(url, download=False)
    out = []
    for e in info.get("entries") or []:
        pid = (e or {}).get("id") or playlist_id((e or {}).get("url", ""))
        if pid and pid.startswith(("PL", "OL", "UU", "FL")):
            out.append({"id": pid, "title": e.get("title") or pid})
    return out


def list_playlist_videos(pid: str) -> tuple[str, list[dict]]:
    with _ydl() as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/playlist?list={pid}", download=False)
    vids = []
    for e in info.get("entries") or []:
        if not e or len(e.get("id") or "") != 11 or e.get("title") in ("[Private video]", "[Deleted video]"):
            continue
        d = e.get("upload_date") or ""
        vids.append({"id": e["id"], "title": e.get("title") or "",
                     "channel": e.get("channel") or e.get("uploader") or info.get("channel") or "",
                     "duration": int(e["duration"]) if e.get("duration") else None,
                     "published": f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else ""})
    return info.get("title") or pid, vids


def timeline_date(title: str, override: str | None = None) -> tuple[int | None, int | None]:
    """(year, month) for a playlist: wiki.yaml override 'YYYY' or 'YYYY-MM', else read from the title."""
    if override:
        m = re.match(r"(\d{4})(?:-(\d{1,2}))?", override)
        if m:
            return int(m.group(1)), int(m.group(2)) if m.group(2) else None
    years = re.findall(r"(?<!\d)(20\d{2}|19\d{2})(?!\d)", title)
    year = int(years[-1]) if years else None
    month = None
    for word in re.findall(r"[A-Za-z]{3,}", title.lower()):
        if word[:3] in MONTHS and (len(word) == 3 or word in (
                "january", "february", "march", "april", "june", "july", "august", "september", "october",
                "november", "december", "sept")):
            month = MONTHS[word[:3]]
            break
    return year, month


def _match(title: str, words: list[str]) -> bool:
    low = title.lower()
    return any(w.lower() in low for w in words)


def wanted_playlists(ch: dict, found: list[dict]) -> list[dict]:
    pl = ch["playlists"]
    if pl["only"]:
        only = {playlist_id(x) for x in pl["only"]}
        known = {p["id"]: p for p in found}
        return [known.get(pid, {"id": pid, "title": pid}) for pid in only]
    keep = [p for p in found if (not pl["include"] or _match(p["title"], pl["include"]))
            and not _match(p["title"], pl["exclude"])]
    return keep


def _needs_relist(pid: str, title: str, ch: dict, known: dict) -> bool:
    """Old event playlists don't change: re-list a playlist only if it's new, from the last two years
    (videos are still being added), or wasn't checked for `relist_days`."""
    from datetime import datetime, timedelta
    row = known.get(pid)
    if not row or not row["synced_at"]:
        return True
    year, _ = timeline_date(title or row["title"] or "", ch["playlists"]["timeline"].get(pid))
    if year is None or year >= datetime.now().year - 1:
        return True
    try:
        last = datetime.strptime(row["synced_at"][:19], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return True
    return datetime.now() - last > timedelta(days=int(ch.get("relist_days", 30)))


def sync(playlist: str | None = None, list_only: bool = False, retry: bool = False, max_fetch: int = 0,
         delay: float = 1.0, log=print, full: bool = False) -> dict:
    ch = channel_config()
    stats = {"playlists": 0, "videos": 0, "fetched": 0, "no_transcript": 0, "errors": 0, "failed_playlists": []}

    if playlist:
        targets = [{"id": playlist_id(playlist), "title": ""}]
    else:
        log(f"Listing playlists on {ch['url']} …")
        found = list_playlists(ch["url"])
        targets = wanted_playlists(ch, found)
        log(f"  {len(found)} playlists, {len(targets)} kept by the wiki.yaml filters")
        if not full:
            known = {r["id"]: r for r in db.playlists()}
            fresh = [p for p in targets if _needs_relist(p["id"], p["title"], ch, known)]
            if len(fresh) < len(targets):
                log(f"  {len(targets) - len(fresh)} older playlists already synced and unchanged; "
                    f"checking {len(fresh)} new or recent ones (use --full to re-check all)")
            targets = fresh

    for n, p in enumerate(targets, 1):
        try:
            title, vids = list_playlist_videos(p["id"])
        except Exception as e:
            stats["failed_playlists"].append(f"{p['id']}: {type(e).__name__}: {e}"[:200])
            log(f"  [{n}/{len(targets)}] FAILED {p['title'] or p['id']}")
            continue
        vids = [v for v in vids if not _match(v["title"], ch["videos"]["exclude"])]
        year, month = timeline_date(title, ch["playlists"]["timeline"].get(p["id"]))
        db.upsert_playlist(p["id"], title, year, month, len(vids))
        for v in vids:
            db.upsert_video(v["id"], v["title"], v["channel"], v["duration"], v["published"])
        db.set_playlist_videos(p["id"], [v["id"] for v in vids])
        stats["playlists"] += 1
        stats["videos"] += len(vids)
        log(f"  [{n}/{len(targets)}] {year or '????'}  {len(vids):>4} videos  {title[:70]}")

    if not list_only:
        fetch_transcripts(ch, playlist_id(playlist) if playlist else None, retry, max_fetch, delay, stats, log)

    from llmwiki import classify
    classify.classify_heuristic(only_unclassified=True)
    from llmwiki import catalog
    catalog.build()
    return stats


def fetch_transcripts(ch: dict, pid: str | None, retry: bool, max_fetch: int, delay: float, stats: dict, log):
    states = "('pending', 'error', 'no_transcript')" if retry else "('pending')"
    where = f"status IN {states}"
    args: tuple = ()
    if pid:
        where += " AND id IN (SELECT video_id FROM playlist_videos WHERE playlist_id = ?)"
        args = (pid,)
    todo = db.videos(where, args)
    if max_fetch:
        todo = todo[:max_fetch]
    log(f"Fetching {len(todo)} transcript(s) …")
    for n, v in enumerate(todo, 1):
        if db.has_source(v["id"]):
            db.set_video_status(v["id"], "ok")
            continue
        r = ingest_video(v["id"], meta={"title": v["title"], "author": v["channel"], "published": v["published"]},
                         languages=ch["languages"])
        if r.get("error"):
            if re.search(r"TranscriptsDisabled|NoTranscriptFound|VideoUnavailable", r["error"]):
                db.set_video_status(v["id"], "no_transcript", r["error"])
                stats["no_transcript"] += 1
                log(f"  [{n}/{len(todo)}] no captions: {v['title'][:70]}")
            else:
                db.set_video_status(v["id"], "error", r["error"])
                stats["errors"] += 1
                if re.search(r"IpBlocked|RequestBlocked|TooManyRequests|429", r["error"]):
                    log("  YouTube is rate-limiting caption requests. Stopping; run `wiki sync` again later "
                        "(or with a larger --delay) to continue where it left off.")
                    break
                log(f"  [{n}/{len(todo)}] error: {v['title'][:70]}")
        else:
            db.set_video_status(v["id"], "ok")
            stats["fetched"] += 1
            log(f"  [{n}/{len(todo)}] ok  {v['title'][:70]}")
        if delay and n < len(todo):
            time.sleep(delay)

"""SQLite memory: every ingested source and its text, chunked for full-text search.

A source is ingested once. Chunks keep a location so a claim can cite the exact spot:
seconds for a video, page number for a PDF, chunk number for a web page or text file.
"""

import sqlite3

from llmwiki.config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY,          -- YouTube video id, URL, or files/<name>
    kind TEXT NOT NULL,           -- video | web | file
    url TEXT,
    title TEXT,
    author TEXT,
    published TEXT,
    ingested_at TEXT DEFAULT (datetime('now'))
);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(
    source_id UNINDEXED,
    loc UNINDEXED,                -- seconds (video), page (pdf), chunk number (web/text)
    text
);
CREATE TABLE IF NOT EXISTS playlists (
    id TEXT PRIMARY KEY,          -- YouTube playlist id
    title TEXT,
    year INTEGER,                 -- timeline position, from the title (or wiki.yaml overrides)
    month INTEGER,
    n_listed INTEGER,
    synced_at TEXT
);
CREATE TABLE IF NOT EXISTS playlist_videos (
    playlist_id TEXT,
    video_id TEXT,
    position INTEGER,
    PRIMARY KEY (playlist_id, video_id)
);
CREATE TABLE IF NOT EXISTS videos (
    id TEXT PRIMARY KEY,
    title TEXT,
    channel TEXT,
    duration INTEGER,
    published TEXT,
    status TEXT DEFAULT 'pending', -- pending | ok | no_transcript | error
    error TEXT,
    kind TEXT,                     -- case_study | concept | tutorial | panel | keynote | other
    orgs TEXT,                     -- JSON list: organizations whose own experience the talk reports
    topics TEXT,                   -- JSON list: technologies and concepts
    summary TEXT,
    classified_by TEXT             -- claude | heuristic
);
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT DEFAULT (datetime('now')),
    topic TEXT,
    collection TEXT,
    status TEXT,
    page TEXT,
    detail TEXT
);
"""


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def has_source(source_id: str) -> bool:
    with get_db() as conn:
        return conn.execute("SELECT 1 FROM sources WHERE id = ?", (source_id,)).fetchone() is not None


def add_source(source_id: str, kind: str, url: str, title: str, author: str, published: str,
               chunks: list[tuple[int, str]]):
    with get_db() as conn:
        conn.execute("DELETE FROM chunks WHERE source_id = ?", (source_id,))
        conn.execute(
            "INSERT OR REPLACE INTO sources (id, kind, url, title, author, published) VALUES (?, ?, ?, ?, ?, ?)",
            (source_id, kind, url, title, author, published),
        )
        conn.executemany("INSERT INTO chunks (source_id, loc, text) VALUES (?, ?, ?)",
                         [(source_id, loc, text) for loc, text in chunks])


def get_source(source_id: str):
    with get_db() as conn:
        return conn.execute("SELECT * FROM sources WHERE id = ?", (source_id,)).fetchone()


def find_source_by_url(url: str):
    url = url.split("#")[0].rstrip("/")
    with get_db() as conn:
        return conn.execute("SELECT * FROM sources WHERE rtrim(url, '/') = ? OR id = ?", (url, url)).fetchone()


def source_chunks(source_id: str):
    with get_db() as conn:
        return conn.execute("SELECT loc, text FROM chunks WHERE source_id = ? ORDER BY CAST(loc AS INTEGER)",
                            (source_id,)).fetchall()


def fts_query(text: str) -> str:
    """Turn free text into an FTS5 query: every word must appear (quoted, so punctuation is safe)."""
    import re
    words = re.findall(r"\w+", text)
    return " ".join(f'"{w}"' for w in words) or '""'


def search(query: str, limit: int = 10, source_id: str | None = None, playlist: str | None = None):
    sql = """SELECT c.source_id, c.loc, snippet(chunks, 2, '[', ']', ' … ', 40) AS snippet, c.text,
                    s.kind, s.url, s.title FROM chunks c JOIN sources s ON s.id = c.source_id
             WHERE chunks MATCH ?"""
    args: list = [fts_query(query)]
    if source_id:
        sql += " AND c.source_id = ?"
        args.append(source_id)
    if playlist:
        sql += " AND c.source_id IN (SELECT video_id FROM playlist_videos WHERE playlist_id = ?)"
        args.append(playlist)
    sql += " ORDER BY rank LIMIT ?"
    args.append(limit)
    with get_db() as conn:
        rows = conn.execute(sql, args).fetchall()
        if not rows and " " in query.strip():
            # Fall back to any-word match
            args[0] = " OR ".join(fts_query(query).split())
            rows = conn.execute(sql, args).fetchall()
    return rows


def all_sources():
    with get_db() as conn:
        return conn.execute(
            "SELECT s.*, (SELECT count(*) FROM chunks c WHERE c.source_id = s.id) AS n_chunks "
            "FROM sources s ORDER BY ingested_at DESC").fetchall()


def log_run(topic: str, collection: str, status: str, page: str = "", detail: str = ""):
    with get_db() as conn:
        conn.execute("INSERT INTO runs (topic, collection, status, page, detail) VALUES (?, ?, ?, ?, ?)",
                     (topic, collection, status, page, detail[:2000]))


def recent_runs(limit: int = 20):
    with get_db() as conn:
        return conn.execute("SELECT * FROM runs ORDER BY id DESC LIMIT ?", (limit,)).fetchall()


def upsert_playlist(pid: str, title: str, year: int | None, month: int | None, n_listed: int):
    with get_db() as conn:
        conn.execute(
            """INSERT INTO playlists (id, title, year, month, n_listed, synced_at)
               VALUES (?, ?, ?, ?, ?, datetime('now'))
               ON CONFLICT(id) DO UPDATE SET title=excluded.title, year=excluded.year, month=excluded.month,
               n_listed=excluded.n_listed, synced_at=excluded.synced_at""",
            (pid, title, year, month, n_listed))


def set_playlist_videos(pid: str, video_ids: list[str]):
    with get_db() as conn:
        conn.execute("DELETE FROM playlist_videos WHERE playlist_id = ?", (pid,))
        conn.executemany("INSERT OR IGNORE INTO playlist_videos (playlist_id, video_id, position) VALUES (?, ?, ?)",
                         [(pid, v, n) for n, v in enumerate(video_ids, 1)])


def upsert_video(vid: str, title: str, channel: str, duration: int | None, published: str):
    with get_db() as conn:
        conn.execute(
            """INSERT INTO videos (id, title, channel, duration, published) VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
               title=coalesce(nullif(excluded.title, ''), videos.title),
               channel=coalesce(nullif(excluded.channel, ''), videos.channel),
               duration=coalesce(excluded.duration, videos.duration),
               published=coalesce(nullif(excluded.published, ''), videos.published)""",
            (vid, title, channel, duration, published))


def set_video_status(vid: str, status: str, error: str = ""):
    with get_db() as conn:
        conn.execute("UPDATE videos SET status = ?, error = ? WHERE id = ?", (status, error[:300], vid))


def set_video_class(vid: str, kind: str, orgs: list[str], topics: list[str], summary: str, by: str):
    import json
    with get_db() as conn:
        conn.execute("UPDATE videos SET kind = ?, orgs = ?, topics = ?, summary = ?, classified_by = ? WHERE id = ?",
                     (kind, json.dumps(orgs), json.dumps(topics), summary, by, vid))


def videos(where: str = "1", args: tuple = ()):
    with get_db() as conn:
        return conn.execute(f"SELECT * FROM videos WHERE {where} ORDER BY id", args).fetchall()


TIMELINE_ORDER = "coalesce(p.year, 9999), coalesce(p.month, 0), p.title"


def playlists():
    """Every playlist in timeline order, with counts."""
    with get_db() as conn:
        return conn.execute(
            f"""SELECT p.*, count(pv.video_id) AS n_videos, sum(v.status = 'ok') AS n_ok,
                       sum(v.kind = 'case_study') AS n_case_studies
                FROM playlists p LEFT JOIN playlist_videos pv ON pv.playlist_id = p.id
                LEFT JOIN videos v ON v.id = pv.video_id
                GROUP BY p.id ORDER BY {TIMELINE_ORDER}""").fetchall()


def playlist_items(pid: str):
    with get_db() as conn:
        return conn.execute(
            """SELECT v.*, pv.position FROM playlist_videos pv JOIN videos v ON v.id = pv.video_id
               WHERE pv.playlist_id = ? ORDER BY pv.position""", (pid,)).fetchall()


def video_playlists(vid: str):
    with get_db() as conn:
        return conn.execute(
            f"""SELECT p.* FROM playlist_videos pv JOIN playlists p ON p.id = pv.playlist_id
                WHERE pv.video_id = ? ORDER BY {TIMELINE_ORDER}""", (vid,)).fetchall()

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


def search(query: str, limit: int = 10, source_id: str | None = None):
    sql = """SELECT c.source_id, c.loc, snippet(chunks, 2, '[', ']', ' … ', 40) AS snippet, c.text,
                    s.kind, s.url, s.title FROM chunks c JOIN sources s ON s.id = c.source_id
             WHERE chunks MATCH ?"""
    args: list = [fts_query(query)]
    if source_id:
        sql += " AND c.source_id = ?"
        args.append(source_id)
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

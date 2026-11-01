"""Citation formats. Pages live at wiki/<collection>/<page>.md, so local files are always ../files/.

  video:  [▶ 12:34](https://www.youtube.com/watch?v=VIDEO&t=754s)
  web:    [example.com](https://example.com/post#:~:text=first%20words%20of%20the%20quote)
  pdf:    [paper.pdf p.3](../files/paper.pdf#page=3)
  text:   [notes.md](../files/notes.md)
"""

import re
from urllib.parse import quote, urlparse


def mmss(seconds: int) -> str:
    h, rest = divmod(int(seconds), 3600)
    m, s = divmod(rest, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def video(video_id: str, seconds: int) -> str:
    return f"[▶ {mmss(seconds)}](https://www.youtube.com/watch?v={video_id}&t={int(seconds)}s)"


def text_fragment(quote_text: str, words: int = 8) -> str:
    """A #:~:text= fragment that makes the browser scroll to and highlight the quote."""
    ws = re.findall(r"\S+", quote_text)[:words]
    return "#:~:text=" + quote(" ".join(ws), safe="") if ws else ""


def web(url: str, quote_text: str = "") -> str:
    host = urlparse(url).netloc.removeprefix("www.")
    return f"[{host}]({url.split('#')[0]}{text_fragment(quote_text) if quote_text else ''})"


def file(name: str, page: int | None = None) -> str:
    if page:
        return f"[{name} p.{page}](../files/{quote(name)}#page={page})"
    return f"[{name}](../files/{quote(name)})"


def for_chunk(row) -> str:
    """A ready-to-paste citation for a search result row (from db.search)."""
    kind, sid, loc = row["kind"], row["source_id"], int(row["loc"])
    if kind == "video":
        return video(sid, loc)
    if kind == "file":
        name = sid.removeprefix("files/")
        return file(name, loc if name.lower().endswith(".pdf") else None)
    return web(row["url"], row["text"][:200])

"""MCP server: use your wiki from inside Claude (Claude Code, Claude Desktop).

  claude mcp add llm-wiki -- wiki-mcp
  (or: claude mcp add llm-wiki -- python -m llmwiki.mcp_server)

Set LLMWIKI_ROOT to your wiki folder if the server doesn't start inside it.
"""

from mcp.server.fastmcp import FastMCP

from llmwiki import cite, db, pages
from llmwiki.config import WIKI_DIR

mcp = FastMCP("llm-wiki")


@mcp.tool()
def list_pages() -> list[dict]:
    """Every page in the personal wiki: title, collection, path and one-line summary."""
    return [pages.page_info(p) for p in pages.content_pages()]


@mcp.tool()
def get_page(path: str) -> str:
    """A page's full markdown with its citations. path is from list_pages, e.g. 'tech/cilium.md'."""
    target = (WIKI_DIR / path).resolve()
    if WIKI_DIR.resolve() not in target.parents or not target.exists():
        return f"No page '{path}'. Use list_pages."
    return target.read_text(encoding="utf-8")


@mcp.tool()
def search_wiki(query: str, limit: int = 8) -> list[dict]:
    """Search the wiki pages' text. Returns matching pages with the lines that matched."""
    terms = [t.lower() for t in query.split() if len(t) > 2]
    hits = []
    for p in pages.content_pages():
        text = p.read_text(encoding="utf-8")
        low = text.lower()
        score = sum(low.count(t) for t in terms)
        if score:
            lines = [l.strip() for l in text.splitlines() if any(t in l.lower() for t in terms)][:4]
            hits.append((score, {**pages.page_info(p), "matches": lines}))
    hits.sort(key=lambda h: -h[0])
    return [h for _, h in hits[:limit]]


@mcp.tool()
def search_sources(query: str, limit: int = 8) -> list[dict]:
    """Search the raw text of every ingested source (video transcripts, web pages, files), with citations."""
    return [{"source": r["title"] or r["source_id"], "snippet": " ".join(r["snippet"].split()),
             "citation": cite.for_chunk(r)} for r in db.search(query, limit)]


def main():
    mcp.run()


if __name__ == "__main__":
    main()

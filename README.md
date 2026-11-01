# LLM Wiki

A personal research wiki on any topic, written by Claude Code, where every claim links back to the exact
spot in its source: the second of a video, the passage of a web page, the page of a PDF.

```bash
wiki research "Cilium network policy" -c tech
wiki research "Sourdough hydration" --url https://www.youtube.com/watch?v=... --notes "I bake at high altitude"
wiki research "Attention is all you need" -c papers --file ~/Downloads/1706.03762.pdf
wiki ask "Which CNI should I use for a small home lab?"
```

It runs on your machine, whenever you want. No search API key and no payment step: discovery uses Claude
Code's built-in web search, and everything else is plain Python and SQLite.

## How a research run works

1. **Read memory.** The agent reads `wiki/index.md`, the existing page if there is one, and searches what it
   has already ingested, so a topic grows instead of being rewritten.
2. **Discover.** Claude Code's WebSearch finds sources, guided by the collection's preferred domains and
   YouTube channels in `wiki.yaml`. Your own `--url`/`--file` sources always come first; `--no-search` uses
   only those.
3. **Ingest.** `wiki ingest` stores each source's text in `memory.db` (SQLite full-text search): YouTube
   captions with timestamps, web page text, PDF text by page. A source is never ingested twice.
4. **Cite exact spots.** `wiki search` prints a ready-to-paste citation for every passage it finds.
5. **Write** `wiki/<collection>/<topic>.md` using the collection's sections and your `style.md`.
6. **Check.** `wiki check` regenerates each page's References list, rebuilds the index pages and verifies
   citations against memory. A run with citation errors is not committed.

## Citations

| Source | Looks like | What `wiki check` verifies |
| --- | --- | --- |
| YouTube | `[▶ 12:34](https://www.youtube.com/watch?v=ID&t=754s)` | label matches `t=`; a quoted sentence next to it is in the transcript near that time (`--fix` moves it) |
| Web page | `[example.com](https://example.com/post#:~:text=first%20words)` | the highlighted words really are on the ingested page; browsers scroll to and highlight them |
| PDF / file | `[paper.pdf p.3](../files/paper.pdf#page=3)` | the file exists in `wiki/files/` |

It also warns about cited sources that were never ingested, missing collection sections, and pages with
fewer than two sources.

## Setup

Needs Python 3.10+ and [Claude Code](https://claude.com/claude-code) (`claude` on your PATH, signed in).

```bash
git clone https://github.com/ravirajnalls/llm-wiki && cd llm-wiki
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[mcp]"
wiki research "your first topic"
wiki serve                                             # http://127.0.0.1:8000
```

## Make it yours: `wiki.yaml`

Collections are folders in `wiki/`, each with its own sources and page shape. Three come as examples
(`general`, `tech`, `papers`); rename, delete or add your own:

```yaml
collections:
  cooking:
    description: Recipes and technique.
    prefer_domains: [seriouseats.com, kingarthurbaking.com]
    youtube_channels: [America's Test Kitchen]
    sections: [Summary, Technique, Ratios, Troubleshooting, Disagreements]
```

`style.md` is injected into every run; edit it to change how pages read. `research.max_sources`,
`prefer_recent_years` and `timeout_minutes` tune each run. Set `LLMWIKI_MODEL` to pick a Claude model.

## Commands

| Command | Does |
| --- | --- |
| `wiki research TOPIC... [-c COLL] [--url U] [--file F] [--no-search] [--notes N] [--push]` | research and write or update pages, then commit |
| `wiki ask QUESTION` | answer from your wiki, keeping its citations |
| `wiki ingest URL_OR_PATH...` | add sources to memory without writing a page |
| `wiki search WORDS [--source ID]` | find passages in ingested sources, with citations |
| `wiki check [--fix]` | rebuild References and indexes, verify citations |
| `wiki list` | pages, sources and recent runs |
| `wiki serve` | preview the site |
| `wiki init FOLDER` | start a separate wiki folder (e.g. a private one) with this config |

## Use it inside Claude (MCP)

```bash
claude mcp add llm-wiki -- wiki-mcp
```

Tools: `list_pages`, `get_page`, `search_wiki` and `search_sources` (raw transcript and page text with
citations). Set `LLMWIKI_ROOT` if the server starts outside your wiki folder.

## Private or public

The wiki is plain markdown in git. Keep the repo private and use `wiki serve` locally, or publish it with
GitHub Pages: enable *Settings → Pages → Source: GitHub Actions* and `.github/workflows/pages.yml` builds
the site on every push. `memory.db` stays out of git (it can hold full copies of pages you read); delete
the workflow file if you never want to publish.

## Origin

Grew out of Cloud Native Brain, a hackathon project that sold cited CNCF wikis. This version drops the
storefront and the CNCF-only scope and keeps the part that made the pages worth reading: every claim
checked against the source it cites.

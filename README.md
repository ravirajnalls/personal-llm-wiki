# LLM Wiki

A personal research wiki on any topic, written by Claude Code, where every claim links back to the exact
spot in its source: the second of a video, the passage of a web page, the page of a PDF.

Built around one YouTube channel. Each playlist on the channel is a point on the timeline (an event, a
season, a year) and each video in it is a talk: a technical concept, a case study, a tutorial. Search a
topic and you get every case study on it across all the playlists, oldest first, with the exact moments.

```bash
wiki sync                         # every playlist + video on the channel, full transcripts, indexes
wiki classify                     # label each video: case study / concept / ..., its orgs and topics
wiki find "autoscaling"           # every autoscaling case study, by event, with timestamped moments
wiki find "autoscaling" --page    # ... and save it as wiki/topics/autoscaling.md
wiki research "Autoscaling on Kubernetes" -c tech    # Claude writes a cited page from those talks
wiki ask "Who moved from HPA to KEDA, and why?"
```

It runs on your machine, whenever you want. Pages are built only from the channel you configure (turn on
Claude Code's built-in web search per run with `--web`). No API keys and no payment step; everything else is
plain Python and SQLite.

## The channel: `wiki.yaml`

```yaml
channel:
  url: https://www.youtube.com/@cncf
  collection: tech
  playlists:
    include: [KubeCon, CloudNativeCon]     # keep playlists whose title has one of these (empty = all)
    exclude: [Shorts, Livestream]
    only: []                               # or list exact playlist ids/URLs
    timeline:                              # dates come from titles ("... Europe 2024"); fix any here
      PLj6h78yzYM2xxxxxxxxxxxxxxxxxxxx: 2024-03
  videos:
    exclude: [Keynote, Opening Remarks]
```

### 1. `wiki sync`: playlists, videos, transcripts

Lists every playlist on the channel and every video in each (with yt-dlp, no API key), dates each playlist
from its title, and fetches each video's **full transcript** into `memory.db`. A video in several playlists is
stored once. Sync is incremental: only new videos are fetched on the next run. YouTube rate-limits caption
requests, so for a big channel use `wiki sync --max 300` and run it again later; it continues where it left
off and stops by itself if YouTube starts refusing. `--list-only` refreshes playlists without transcripts,
`--retry` retries failures, and `wiki sources` shows the timeline with counts.

### 2. `wiki classify`: what each video is

Claude reads each title, its event and the start of its transcript (30 videos per call) and labels it:

- **kind:** `case_study` (an organization reports its own use: adoption, migration, scaling, incidents,
  lessons learned), `concept`, `tutorial`, `panel`, `keynote` or `other`;
- **orgs:** for case studies, whose experience it is (the end user, not the vendor);
- **topics** and a one-sentence **summary**.

Sync already applies free title-only rules (`"How Spotify Scaled…"`, `"…at Zalando"`, `"lessons learned"`,
`"in production"`, `"our journey"`), so `wiki find` works before you classify; `wiki classify` makes it accurate.
`wiki classify --heuristic` reruns just the rules.

### 3. `wiki find "topic"`: case studies across the timeline

Finds every video whose title, labels or transcript covers the topic, keeps the case studies (or
`--kind concept`, `--kind all`, ...), and groups them by playlist in timeline order with the organizations,
summary and the timestamped moments where the topic comes up. `--page` saves it as a wiki page.

### Indexes it builds

- full-text search over every transcript in ~45-second timestamped chunks (`wiki search`, `--playlist ID`);
- `wiki/sources/index.md`: the channel's timeline, every playlist by year with video, transcript and
  case-study counts;
- `wiki/sources/case-studies.md`: every case study by event, with its organizations;
- `wiki/sources/<playlist>.md`: each playlist's talks with their kind and organizations;
- `wiki/sources/videos/<id>.md`: each video's labels and full transcript, every paragraph linked to its moment.

## How a research run works

1. **Read memory.** The agent reads `wiki/index.md`, the existing page if there is one, and searches what it
   has already ingested, so a topic grows instead of being rewritten.
2. **Discover.** By default, from the synced channel only: the agent runs `wiki find` for the topic and its
   synonyms, then `wiki search` for exact passages, and writes a Timeline section showing how the topic
   evolved across events. With `--web` (or `research.web_search: true`), Claude
   Code's WebSearch also finds sources, guided by the collection's preferred domains. Your own `--url`/`--file`
   sources always come first.
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
git clone https://github.com/ravirajnalls/personal-llm-wiki && cd personal-llm-wiki
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
| `wiki sync [--list-only] [--max N] [--playlist ID] [--retry] [--delay S]` | sync the channel's playlists, videos and full transcripts; rebuild the catalog |
| `wiki classify [--heuristic] [--all] [--limit N]` | label videos: kind, organizations, topics, summary |
| `wiki find TOPIC [--kind K] [--min-mentions N] [--page]` | every case study (or other kind) on a topic, by event |
| `wiki sources` | the playlists on the timeline, with counts |
| `wiki research TOPIC... [-c COLL] [--url U] [--file F] [--web \| --no-search] [--notes N] [--push]` | research and write or update pages, then commit |
| `wiki ask QUESTION` | answer from your wiki, keeping its citations |
| `wiki ingest URL_OR_PATH...` | add sources to memory without writing a page |
| `wiki search WORDS [--source ID] [--playlist ID]` | find passages in ingested sources, with citations |
| `wiki check [--fix]` | rebuild References and indexes, verify citations |
| `wiki list` | pages, sources and recent runs |
| `wiki serve` | preview the site |
| `wiki init FOLDER` | start a separate wiki folder (e.g. a private one) with this config |

## Use it inside Claude (MCP)

```bash
claude mcp add llm-wiki -- wiki-mcp
```

Tools: `find_talks` (case studies on a topic across the timeline), `timeline`, `list_pages`, `get_page`,
`search_wiki` and `search_sources` (raw transcript text with citations). Set `LLMWIKI_ROOT` if the server starts outside your wiki folder.

## Private or public

The wiki is plain markdown in git. Keep the repo private and use `wiki serve` locally, or publish it with
GitHub Pages: enable *Settings → Pages → Source: GitHub Actions* and `.github/workflows/pages.yml` builds
the site on every push. `memory.db` stays out of git (it can hold full copies of pages you read); delete
the workflow file if you never want to publish. If the site is public, consider `research.transcript_pages: false`
so full transcripts aren't republished; search still works from `memory.db`.

## Origin

Grew out of Cloud Native Brain, a hackathon project that sold cited CNCF wikis. This version drops the
storefront and the CNCF-only scope and keeps the part that made the pages worth reading: every claim
checked against the source it cites.

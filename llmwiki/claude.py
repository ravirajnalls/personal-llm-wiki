"""Run headless Claude Code (`claude -p`) and parse the JSON object it ends with.

Research uses Claude Code's own WebSearch and WebFetch tools, so no search API key is needed.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from llmwiki.config import ROOT

RESEARCH_TOOLS = [
    "WebSearch", "WebFetch", "Read", "Write", "Edit", "Glob", "Grep",
    "Bash(wiki:*)", "Bash(python -m llmwiki:*)",
]
READ_TOOLS = ["Read", "Glob", "Grep", "Bash(wiki search:*)", "Bash(python -m llmwiki search:*)"]


def parse_last_json(text: str) -> dict | None:
    decoder = json.JSONDecoder()
    last, pos = None, text.find("{")
    while pos != -1:
        try:
            obj, end = decoder.raw_decode(text, pos)
        except json.JSONDecodeError:
            pos = text.find("{", pos + 1)
            continue
        if isinstance(obj, dict):
            last = obj
        pos = text.find("{", end)
    return last


def run(prompt: str, tools: list[str], timeout_min: int = 20, model: str | None = None) -> dict:
    exe = shutil.which("claude")
    if not exe:
        return {"status": "failed", "reason": "Claude Code CLI not found. Install it: https://claude.com/claude-code"}
    allowed = tools if not tools else (os.environ.get("LLMWIKI_ALLOWED_TOOLS", "").split() or tools)
    cmd = [exe, "-p"] + (["--allowedTools", *allowed] if allowed else [])
    if model or os.environ.get("LLMWIKI_MODEL"):
        cmd += ["--model", model or os.environ["LLMWIKI_MODEL"]]
    # Make sure the agent's `wiki` commands use this same install (e.g. an un-activated venv)
    env = {**os.environ, "LLMWIKI_ROOT": str(ROOT),
           "PATH": str(Path(sys.executable).parent) + os.pathsep + os.environ.get("PATH", "")}
    try:
        no_window = {"creationflags": 0x08000000} if os.name == "nt" else {}  # no console flash from a scheduled run
        proc = subprocess.run(cmd, input=prompt, cwd=str(ROOT), env=env, **no_window, capture_output=True, text=True, encoding="utf-8", timeout=timeout_min * 60)
    except subprocess.TimeoutExpired:
        return {"status": "failed", "reason": f"timed out after {timeout_min} minutes"}
    out = (proc.stdout or "").strip()
    parsed = parse_last_json(out)
    if parsed is not None:
        parsed.setdefault("_text", out)
        return parsed
    return {"status": "failed", "reason": (proc.stderr or out or f"exit code {proc.returncode}")[-800:], "_text": out}

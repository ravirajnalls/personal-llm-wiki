"""Find the wiki's root folder and load wiki.yaml."""

import os
from functools import lru_cache
from pathlib import Path

import yaml


def find_root() -> Path:
    """The folder holding wiki.yaml: $LLMWIKI_ROOT, else the nearest parent of the cwd, else the repo."""
    if env := os.environ.get("LLMWIKI_ROOT"):
        return Path(env).resolve()
    here = Path.cwd().resolve()
    for folder in (here, *here.parents):
        if (folder / "wiki.yaml").exists():
            return folder
    return Path(__file__).resolve().parent.parent


ROOT = find_root()
WIKI_DIR = ROOT / "wiki"
FILES_DIR = WIKI_DIR / "files"
DB_PATH = ROOT / "memory.db"


@lru_cache
def load() -> dict:
    path = ROOT / "wiki.yaml"
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    cfg.setdefault("title", "My Wiki")
    cfg.setdefault("collections", {"general": {"sections": ["Summary", "Key ideas", "Open questions"]}})
    cfg.setdefault("default_collection", next(iter(cfg["collections"])))
    cfg.setdefault("research", {})
    return cfg


def collection(name: str | None) -> tuple[str, dict]:
    cfg = load()
    name = name or cfg["default_collection"]
    if name not in cfg["collections"]:
        known = ", ".join(cfg["collections"])
        raise SystemExit(f"Unknown collection '{name}'. Known: {known} (add it to wiki.yaml)")
    return name, cfg["collections"][name] or {}


def slugify(text: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:80] or "page"

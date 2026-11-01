#!/bin/sh
# Run the wiki update now (macOS/Linux). `chmod +x update-wiki.sh` once.
cd "$(dirname "$0")"
PY=python3; [ -x .venv/bin/python ] && PY=.venv/bin/python
exec "$PY" -m llmwiki auto

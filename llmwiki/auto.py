"""One unattended update: sync the channel, classify new videos, rebuild every page, commit and push.

  wiki auto                # what the scheduled task runs
  wiki schedule            # install the daily task (Windows Task Scheduler, or cron on macOS/Linux)
  wiki schedule --remove

Settings live under `schedule:` in wiki.yaml. Every run appends to logs/auto.log.
"""

import os
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime

from llmwiki import config
from llmwiki.config import ROOT

TASK_NAME = "LLM Wiki update"
LOG_DIR = ROOT / "logs"
LOCK = ROOT / ".auto.lock"


def settings() -> dict:
    s = dict(config.load().get("schedule") or {})
    s.setdefault("time", "02:00")
    s.setdefault("max_transcripts", 300)   # per run; YouTube rate-limits big bursts
    s.setdefault("delay_seconds", 2)
    s.setdefault("classify", "claude")     # claude | heuristic | off
    s.setdefault("max_classify", 600)      # videos labeled by Claude per run (30 per call)
    s.setdefault("push", True)
    return s


class _Log:
    def __init__(self):
        LOG_DIR.mkdir(exist_ok=True)
        self.f = open(LOG_DIR / "auto.log", "a", encoding="utf-8")

    def __call__(self, msg: str):
        line = f"{datetime.now():%Y-%m-%d %H:%M:%S}  {msg}"
        print(line, flush=True)
        self.f.write(line + "\n")
        self.f.flush()


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def run() -> int:
    log = _Log()
    if LOCK.exists() and time.time() - LOCK.stat().st_mtime < 6 * 3600:
        log("Another update is still running (or crashed less than 6h ago); skipping. Delete .auto.lock to force.")
        return 0
    LOCK.write_text(str(os.getpid()))
    try:
        return _run(log, settings())
    except SystemExit as e:
        log(f"Stopped: {e}")
        return 1
    except Exception as e:
        log(f"FAILED: {type(e).__name__}: {e}")
        return 1
    finally:
        LOCK.unlink(missing_ok=True)


def _run(log, s: dict) -> int:
    from llmwiki import catalog, classify, pages, references, sync
    log("=== update started ===")
    if s["push"] and _git("rev-parse", "--is-inside-work-tree").returncode == 0:
        p = _git("pull", "--rebase", "--autostash")
        if p.returncode:
            log(f"git pull failed, continuing with local copy: {p.stderr.strip()[:200]}")

    st = sync.sync(max_fetch=s["max_transcripts"], delay=s["delay_seconds"], log=log)
    log(f"sync: {st['playlists']} playlists, {st['videos']} videos, {st['fetched']} new transcripts, "
        f"{st['no_transcript']} without captions, {st['errors']} errors")

    labeled = 0
    if s["classify"] == "claude":
        if shutil.which("claude"):
            r = classify.classify_claude(limit=s["max_classify"], log=log)
            labeled = r["labeled"]
            log(f"classify: Claude labeled {labeled} of {r['total']} waiting")
        else:
            log("classify: Claude Code CLI not found, using title rules only")
    elif s["classify"] == "heuristic":
        labeled = classify.classify_heuristic(only_unclassified=True)

    catalog.build()
    references.update_all()
    pages.rebuild_index()

    if _git("rev-parse", "--is-inside-work-tree").returncode != 0:
        log("not a git repo; pages updated locally only")
        return 0
    _git("add", "wiki")
    msg = f"wiki: auto update {datetime.now():%Y-%m-%d} (+{st['fetched']} transcripts, {labeled} labeled)"
    c = _git("commit", "-m", msg)
    if c.returncode:
        log("nothing changed; no commit")
    else:
        log(f"committed: {msg}")
        if s["push"]:
            p = _git("push")
            log("pushed" if p.returncode == 0 else f"push failed: {p.stderr.strip()[:300]}")
    log("=== update finished ===")
    return 0


# ---------- installing the schedule ----------

def _python() -> str:
    exe = sys.executable
    if platform.system() == "Windows" and exe.lower().endswith("python.exe"):
        pyw = exe[:-10] + "pythonw.exe"  # no console window popping up at night
        if os.path.exists(pyw):
            return pyw
    return exe


def install(at: str | None = None) -> str:
    at = at or settings()["time"]
    if platform.system() == "Windows":
        cmd = f'cmd /c cd /d "{ROOT}" && "{_python()}" -m llmwiki auto'
        r = subprocess.run(["schtasks", "/Create", "/F", "/SC", "DAILY", "/ST", at, "/TN", TASK_NAME, "/TR", cmd],
                           capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f"schtasks failed: {r.stderr.strip() or r.stdout.strip()}")
        return f"Daily task '{TASK_NAME}' runs at {at}. See it in Task Scheduler; log: {LOG_DIR / 'auto.log'}"
    hh, mm = at.split(":")
    line = f'{int(mm)} {int(hh)} * * * cd "{ROOT}" && "{sys.executable}" -m llmwiki auto >/dev/null 2>&1  # {TASK_NAME}'
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    kept = [l for l in current.splitlines() if TASK_NAME not in l]
    subprocess.run(["crontab", "-"], input="\n".join(kept + [line]) + "\n", text=True, check=True)
    return f"cron job runs daily at {at}; log: {LOG_DIR / 'auto.log'}"


def remove() -> str:
    if platform.system() == "Windows":
        r = subprocess.run(["schtasks", "/Delete", "/F", "/TN", TASK_NAME], capture_output=True, text=True)
        return "Removed the scheduled task." if r.returncode == 0 else r.stderr.strip()
    current = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    kept = [l for l in current.splitlines() if TASK_NAME not in l]
    subprocess.run(["crontab", "-"], input="\n".join(kept) + "\n", text=True, check=True)
    return "Removed the cron job."

@echo off
rem Double-click to update the wiki now: sync new videos, classify, rebuild, commit, push.
cd /d "%~dp0"
if exist .venv\Scripts\python.exe (set PY=.venv\Scripts\python.exe) else (set PY=python)
%PY% -m llmwiki auto
pause

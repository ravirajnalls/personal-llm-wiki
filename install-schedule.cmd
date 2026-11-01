@echo off
rem Double-click once to run the wiki update every day (time is schedule.time in wiki.yaml).
cd /d "%~dp0"
if exist .venv\Scripts\python.exe (set PY=.venv\Scripts\python.exe) else (set PY=python)
%PY% -m llmwiki schedule
pause

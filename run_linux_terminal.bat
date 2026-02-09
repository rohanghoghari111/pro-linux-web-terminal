@echo off
title Pro Linux Web Terminal

echo Starting Pro Linux Web Terminal...
echo.

REM Start FastAPI server in background (FULL SCREEN CMD)
start cmd /k "mode con: cols=120 lines=40 && powershell -command \"$Host.UI.RawUI.WindowState='Maximized'\" && python app.py"

REM Small delay to allow server start
timeout /t 2 >nul

REM Open browser automatically
start http://127.0.0.1:8000

exit
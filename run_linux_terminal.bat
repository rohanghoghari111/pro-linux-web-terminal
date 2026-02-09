@echo off
title Pro Linux Web Terminal
cd /d "%~dp0"

REM Kill anything using port 8000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    taskkill /PID %%a /F >nul 2>&1
)

REM Start server
start "Linux Server" cmd /k python app.py

REM Wait until server ready
powershell -Command ^
"$port=8000; while(-not (Test-NetConnection 127.0.0.1 -Port $port -InformationLevel Quiet)) { Start-Sleep -Milliseconds 200 }"

REM Open browser
start "" "http://127.0.0.1:8000"
exit

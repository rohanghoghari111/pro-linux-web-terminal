@echo off
cd /d "%USERPROFILE%\OneDrive\Desktop\linux-terminal"

REM Start server hidden (no cmd window)
powershell -WindowStyle Hidden -Command "Start-Process python -ArgumentList 'app.py' -WindowStyle Hidden"

REM Wait until server is actually ready (port 8000 open)
:wait
powershell -WindowStyle Hidden -Command "try { $c = New-Object Net.Sockets.TcpClient; $c.Connect('127.0.0.1',8000); $c.Close(); exit 0 } catch { exit 1 }"
if errorlevel 1 (
    timeout /t 1 >nul
    goto wait
)

REM Open browser only when ready
start "" "http://127.0.0.1:8000"
exit

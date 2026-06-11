@echo off
REM PaneForge demo launcher — starts the kernel and opens the calendar.
cd /d "%~dp0"
echo Starting PaneForge kernel...
start "PaneForge Kernel" /min python kernel\paneforge_kernel.py 8770
timeout /t 3 /nobreak >nul
echo Opening calendar at http://localhost:8770/
start http://localhost:8770/
echo.
echo PaneForge is running. Close the "PaneForge Kernel" window to stop.
echo Try: the gear button (bottom-right) - Ink mode, layout, add events.
pause

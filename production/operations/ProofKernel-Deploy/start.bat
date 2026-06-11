@echo off
REM ============================================================================
REM CQECMPLX Kernel - One-Line Launch (Windows)
REM ============================================================================
REM 
REM Just run this batch file and your kernel starts with OpenCode CLI ready
REM Everything is auto-configured, just log in and start typing
REM
REM Usage:
REM   start.bat
REM
REM ============================================================================

setlocal enabledelayedexpansion

set COMPOSE_FILE=docker-compose-kernel-with-opencode.yml

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   CQECMPLX Kernel - Launching                                  ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if services are running
docker ps 2>nul | find "cqecmplx-proof-kernel" >nul
if errorlevel 0 (
    echo [INFO] Services already running
    echo.
    echo Access OpenCode terminal:
    echo   docker exec -it cqecmplx-opencode-cli bash
    echo.
    goto :end
)

REM Start services
echo [INFO] Starting services...
docker-compose -f %COMPOSE_FILE% up -d

REM Wait for kernel
echo [INFO] Waiting for kernel to be ready...
setlocal enabledelayedexpansion
for /l %%i in (1,1,30) do (
    docker exec cqecmplx-proof-kernel curl -s http://localhost:8765/health >nul 2>&1
    if errorlevel 0 (
        echo [INFO] ✓ Kernel is ready
        goto :ready
    )
    echo   Attempt %%i/30...
    timeout /t 1 /nobreak >nul
)

:ready
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   OpenCode CLI Terminal is Running                            ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo OpenCode terminal is waiting for you to connect.
echo.
echo Access it with:
echo.
echo   docker exec -it cqecmplx-opencode-cli bash
echo.
echo Then in the terminal, just start typing:
echo   ^> validate("CQE-paper-00")
echo   ^> validate(["CQE-paper-00", "CQE-paper-01"])
echo   ^> status()
echo.
echo All commands are ready to go!
echo.

:end

@echo off
title Task App - Server Locale
echo.
echo ========================================
echo   TASK APP - Avvio in corso...
echo ========================================
echo.

:: Check if Python is available
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRORE: Python non trovato!
    echo Installa Python da https://www.python.org/downloads/
    echo Assicurati di spuntare "Add Python to PATH" durante l'installazione.
    pause
    exit /b 1
)

:: Run the server from the same directory as this bat file
cd /d "%~dp0"
python serve.py
pause

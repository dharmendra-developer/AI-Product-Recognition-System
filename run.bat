@echo off
title AI Product Recognition
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Setup has not been completed yet.
    echo Run setup.bat first.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" src\product_detector.py
if errorlevel 1 (
    echo.
    echo The app stopped because of an error. See the terminal message above.
    pause
)

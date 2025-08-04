@echo off
title Python Code Obfuscator
color 0A

echo ================================
echo     Python Code Obfuscator
echo ================================

echo.
echo [1/3] Checking for Python...
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not added to PATH.
    pause
    exit /b
)
echo Python found.
echo.

echo [2/3] Running obfuscator.py...
python obfuscator.py
if errorlevel 1 (
    echo ERROR: obfuscator.py failed to run.
    pause
    exit /b
)
echo obfuscator.py ran successfully.
echo.

echo [3/3] Output written to obfuscated_code.py (if script succeeded).
echo Done!
pause

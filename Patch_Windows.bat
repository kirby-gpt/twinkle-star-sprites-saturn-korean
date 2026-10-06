@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 apply_patch.py
) else (
  python apply_patch.py
)
echo.
pause

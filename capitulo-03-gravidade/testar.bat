@echo off
chcp 65001 >nul
if exist ..\.venv\Scripts\python.exe (
    ..\.venv\Scripts\python.exe teste.py
) else (
    py -3 teste.py 2>nul || python teste.py
)
pause

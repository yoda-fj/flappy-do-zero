@echo off
chcp 65001 >nul
if exist ..\.venv\Scripts\python.exe (
    ..\.venv\Scripts\python.exe jogo.py
) else (
    py -3 jogo.py 2>nul || python jogo.py
)

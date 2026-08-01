@echo off
chcp 65001 >nul
if exist ..\.venv\Scripts\pgzrun.exe (
    ..\.venv\Scripts\pgzrun.exe jogo.py
) else (
    pgzrun jogo.py
)

@echo off
chcp 65001 >nul
py -3 teste.py 2>nul || python teste.py
pause

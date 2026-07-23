@echo off

cd /d D:\tickflow-stock-panel\backend\ai_selector

python daily_selector.py

python backtest.py

pause
@echo off
py -m nuitka --standalone --follow-imports --disable-console --main=./code/game.py --include-package=pygame 
pause
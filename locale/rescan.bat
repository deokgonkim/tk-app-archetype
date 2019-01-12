@echo off

if "b%1" == "b" (
    echo Please speciy program name
    goto :end
)

pygettext.py -d %1 -o %1.pot ..\src

:end

@echo off

if "b%1" == "b" (
    echo Please specify program name
    goto :end
)

for /d %%i in (*) do (
    echo Compiling %%i\LC_MESSAGES\%1.po
    msgfmt.py %%i\LC_MESSAGES\%1.po
)

:end

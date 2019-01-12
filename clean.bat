@echo off

@rem remove build directory
setup.py clean -a

@rem remove MANIFEST
echo Removing file MANIFEST (for source distribution)
if exist MANIFEST del MANIFEST

@rem del dist
echo Cleaning directory 'dist'
if exist dist del /q dist

@rem rmdir dist
echo Removing directory 'dist'
if exist dist rmdir dist

@rem remove .pyc files
echo Removing '*.pyc' files
for /r %%i in (*.pyc) do del %%i

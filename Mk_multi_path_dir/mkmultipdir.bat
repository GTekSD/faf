:: Script to create multiple paths mentioned in "list.txt" file.

REM @echo off

REM setlocal EnableDelayedExpansion

REM set LIST_FILE=list.txt

REM if not exist %LIST_FILE% (
  REM echo List file %LIST_FILE% not found.
  REM exit /b 1
REM )

REM for /f "delims=" %%a in (%LIST_FILE%) do (
  REM set "path=%%a"
  REM set "parent_dir=!path:*\=!"
  REM mkdir "!parent_dir!" 2>nul
  REM mkdir "%%a" 2>nul
REM )

REM echo Directories created successfully.

REM endlocal

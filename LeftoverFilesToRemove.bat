@echo off
setlocal enabledelayedexpansion

:: Set the target and destination folders
set "target_folder=%~dp0"
set "destination_folder=%~dp0LEFTOVER FILES FOR DELETION"

:: List of files to move. Default set for Enhanced AI mod
set "files_to_move=em\em018\00\data\em018.dtt_epg em\em018\05\data\em018.dtt_epg em\em023\00\data\em023.dtt_epg em\em023\05\data\em023.dtt_epg em\em027\00\data\em027.dtt_epg em\em037\00\data\em037.dtt_epg em\em057\00\data\em057.dtt_epg em\em057\01\data\em057.dtt_epg em\em063\05\data\em063.dtt_epg em\em080\01\data\em080.dtt_epg em\em100\00\data\em100.dtt_epg em\em100\01\data\em100.dtt_epg em\em103\05\data\em103.dtt_epg em\em109\00\data\em109.dtt_epg em\em111\05\data\em111.dtt_epg em\em113\00\data\em113.dtt_epg em\em113\01\data\em113.dtt_epg em\em121\00\data\em121.dtt_epg"

echo Searching for files to move from %target_folder% to %destination_folder%...

:: Loop through each file and move it
for %%i in (%files_to_move%) do (
    set "source_path=%target_folder%\%%i"
    set "destination_path=%destination_folder%\%%i"

    :: Create the destination folder if it doesn't exist
    if not exist "!destination_path!" (
        mkdir "!destination_path!"
    )

    :: Move the file
    move "!source_path!" "!destination_path!" > nul 2>&1

    :: Check for errors
    if errorlevel 1 (
        echo No leftover found for %%i
    ) else (
        echo Moved file: !destination_path!
    )
)

echo Move process completed.
pause

@echo off
:: inkscape
:: -z without gui
:: -D export area drawing
:: -C or --export-area-page

inkscape.exe -D -z --file=%1 --export-png=%~n1.png --export-dpi=300 --export-area-page
echo Converted %%~n1

REM pause

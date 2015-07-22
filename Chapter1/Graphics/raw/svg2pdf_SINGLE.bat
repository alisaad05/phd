@echo off
:: inkscape
:: -z without gui
:: -D export area drawing
:: -C or --export-area-page

inkscape.exe -D -z --file=%1 --export-pdf=%~n1.pdf --export-area-page
echo Converted %%~n1

REM pause

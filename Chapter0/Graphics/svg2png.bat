@echo off
:: inkscape
:: -z without gui
:: -D export area drawing
:: -C or --export-area-page

REM for %%i in (*.svg) do echo %%~ni
for %%i in (*.svg) do  (
							:: inkscape.exe -D -z --file=%%~ni.svg --export-pdf=%%~ni.pdf --export-latex
							inkscape.exe -D -z --file=%%~ni.svg --export-png=%%~ni.png --export-dpi=300 --export-area-page
							echo Converted %%~ni
)

REM pause
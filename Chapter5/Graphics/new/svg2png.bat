@echo off
:: inkscape
:: -z without gui
:: -D export area drawing

REM for %%i in (*.svg) do echo %%~ni
for %%i in (*.svg) do  (
							:: inkscape.exe -D -z --file=%%~ni.svg --export-pdf=%%~ni.pdf --export-latex
							inkscape.exe -D -z --file=%%~ni.svg --export-png=%%~ni.png --export-dpi=300
							echo Converted %%~ni
)

REM pause
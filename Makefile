all: pdf clean

pdf:
	@echo ---------
	@echo COMPILING
	@echo ---------
	
	pdflatex -interaction=nonstopmode main.tex
	bibtex main
	pdflatex -interaction=nonstopmode main.tex
	# pdflatex -interaction=nonstopmode main.tex
	pdflatex -synctex=1 -interaction=nonstopmode main.tex

clean:
	@echo --------
	@echo CLEANING
	@echo --------
	
	rm -f *.aux *.log *.bbl *.blg *.toc *.lof *.lot *.out *.mtc*
	rm -f References/*.aux References/*.log
	rm -f Chapter1/*.aux Chapter1/*.log
	rm -f *.maf #removes the MS Access shortcut
autocommit:
	@echo --------------
	@echo AUTOCOMMITTING
	@echo --------------
	
	git add .
	git commit -m "Auto Commit"
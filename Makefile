all: pdf 

pdf:
	@echo ---------
	@echo COMPILING
	@echo ---------
	
	pdflatex -interaction=nonstopmode main.tex
	bibtex main
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -synctex=1 -interaction=nonstopmode main.tex

clean:
	@echo --------
	@echo CLEANING
	@echo --------
	
	rm -f *.aux *.log *.bbl *.blg *.toc *.lof *.lot *.brf 
	rm -f *.maf *.out *.mtc* *.tdo *.dpth *.md5 *.auxlock
	rm -f *.bib *.xml
	rm -f Chapter0/*.aux Chapter0/*.log
	rm -f Chapter1/*.aux Chapter1/*.log
	rm -f Chapter2/*.aux Chapter2/*.log
	rm -f Chapter3/*.aux Chapter3/*.log
	rm -f Chapter4/*.aux Chapter4/*.log
	rm -f Chapter5/*.aux Chapter5/*.log
	rm -f Chapter6/*.aux Chapter6/*.log
	rm -f Appendices/*.aux Appendices/*.log
	rm -f Preamble/*.aux Preamble/*.log
	rm -f Frontmatter/*.aux Frontmatter/*.log
	rm -f References/*.aux References/*.log

autocommit:
	@echo --------------
	@echo AUTOCOMMITTING
	@echo --------------
	
	git add .
	git commit -m "Auto Commit"	

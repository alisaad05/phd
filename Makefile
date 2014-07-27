all: pdf clean

pdf:
	# pdflatex main
	pdflatex -synctex=1 -interaction=nonstopmode main.tex
	pdflatex -synctex=1 -interaction=nonstopmode main.tex
	pdflatex -synctex=1 -interaction=nonstopmode main.tex
	# bibtex main
	# pdflatex main
	# pdflatex main
	# pdflatex main

clean:
	rm -f *.aux *.log *.bbl *.blg *.toc *.lof *.lot *.out
	rm -f head/*.aux head/*.log
	rm -f main/*.aux main/*.log
	rm -f tail/*.aux tail/*.log
	
autocommit:
	git add .
	git commit -m "Auto Commit"
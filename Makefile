all: pdf clean

pdf:
	# pdflatex main
	pdflatex -interaction=nonstopmode main.tex
	bibtex main
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -synctex=1 -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.bbl *.blg *.toc *.lof *.lot *.out
	rm -f References/*.aux References/*.log
	rm -f Chapter1/*.aux Chapter1/*.log
	
autocommit:
	git add .
	git commit -m "Auto Commit"
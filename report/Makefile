name=main

stopping.pdf: ${name}.tex biblio.bib
	pdflatex ${name}
	bibtex ${name}
	pdflatex ${name}
	pdflatex ${name}

clean:
	rm -f *~ ${name}.pdf ${name}.log ${name}.aux ${name}.bbl ${name}.blg ${name}.toc

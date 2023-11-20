ROOTNAME = main
PDFFILE = $(ROOTNAME).pdf
DVIFILE = $(ROOTNAME).dvi
TEXFILE = $(ROOTNAME).tex
LATEX = pdflatex
L2R = latex2rtf

all: base 

base:
	$(LATEX) $(ROOTNAME)
	bibtex $(ROOTNAME)
	$(LATEX) $(ROOTNAME)
	$(LATEX) $(ROOTNAME)

clean:
	del /f *.dvi *.ps *.aux *.bbl *.blg *.log *.out *.lof *.lot *.toc 

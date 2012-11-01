# LaTeX commands
LCOMPILER = pdflatex
LCFLAGS = --halt-on-error

OBJECTS = simpleMath.sty\
	Mechanik-GreensFkt.pdf

# Pattern rules

# compile LaTeX three times to fix links
%.pdf: %.tex
	$(LCOMPILER) $(LCFLAGS) $<
	bibtex $(basename $<)
	$(LCOMPILER) $(LCFLAGS) $<
	$(LCOMPILER) $(LCFLAGS) $<

# ultimate target:
all: $(OBJECTS)

# other targets:
simpleMath.sty:
	cp ../simpleMath.sty .

clean:
	rm Mechanik-Schwingungen.pdf *.out *.bbl *.aux *.blg *.log simpleMath.sty


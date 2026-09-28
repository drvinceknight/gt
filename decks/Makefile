# Build every write-on deck. Run `make` here, or `pdflatex main.tex` from
# a single deck's directory.

DECKS := $(wildcard */main.tex)
PDFS := $(DECKS:.tex=.pdf)

.PHONY: all clean
all: $(PDFS)

%/main.pdf: %/main.tex preamble.tex
	cd $* && pdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	rm -f */main.aux */main.log */main.out

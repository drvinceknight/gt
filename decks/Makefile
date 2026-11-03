# Build every write-on deck. Run `make` here, or `pdflatex main.tex` from
# a single deck's directory. `make answers` builds the same decks with the
# answers written in and renders each page as an image for the facilitator
# notes; a deck only appears there once it has answers to show.

DECKS := $(wildcard */main.tex)
PDFS := $(DECKS:.tex=.pdf)

# The decks whose answers are written into the source. The rest build blank
# only, so they are added here as their answers go in.
ANSWERED := auctions \
            cooperative-games \
            direct-reciprocity \
            games \
            matching-games \
            moran-process \
            nash-equilibrium \
            rationalisation \
            repeated-games \
            replicator-dynamics \
            routing-games \
            social-choice \
            subgame-perfection
ANSWER_PDFS := $(ANSWERED:%=%/main-answers.pdf)
IMAGE_DIR := ../assets/img/decks

.PHONY: all answers clean
all: $(PDFS)

%/main.pdf: %/main.tex preamble.tex
	cd $* && pdflatex -interaction=nonstopmode -halt-on-error main.tex

# The same source again with \answermode defined, so the key cannot drift away
# from the deck it answers.
%/main-answers.pdf: %/main.tex preamble.tex
	cd $* && pdflatex -interaction=nonstopmode -halt-on-error \
	  -jobname=main-answers "\def\answermode{}\input{main.tex}"

answers: $(ANSWER_PDFS)
	for deck in $(ANSWERED); do \
	  rm -rf $(IMAGE_DIR)/$$deck; \
	  mkdir -p $(IMAGE_DIR)/$$deck; \
	  pdftoppm -r 100 -png $$deck/main-answers.pdf $(IMAGE_DIR)/$$deck/page; \
	done

clean:
	rm -f */main.aux */main.log */main.out
	rm -f */main-answers.aux */main-answers.log */main-answers.out

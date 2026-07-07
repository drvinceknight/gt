# Revision quizzes

Each `*.yml` file here is a short, surface-level multiple-choice quiz, named by
the **topic tag**. For example `nash-equilibrium.yml` attaches to the topic page
whose frontmatter has `tag: nash-equilibrium`. The same files feed two outputs:
`build.py` embeds each quiz in its topic page as an interactive widget, and
`main.py` renders each quiz to a LaTeX document and a PDF.

## Format

A quiz file has a `title`, an optional `pick`, and a list of `questions`. Each
question carries the question text, a list of `options` with exactly one marked
correct, and an optional `explain` string shown as feedback.

```yaml
title: Nash equilibrium     # heading, and localStorage key for best scores
pick: 5                     # optional: show 5 random questions of the pool
questions:
  - q: "Question text (may contain LaTeX with \\( ... \\))."
    options:
      - text: "the correct option"
        correct: true       # exactly one option must be marked correct
      - text: "a distractor"
      - text: "another distractor"
    explain: "Optional feedback shown after answering (LaTeX allowed)."
```

A few rules govern the content:

- Each question must have **exactly one** option with `correct: true`; both the
  web build and the PDF build rely on this.
- Maths uses the MathJax delimiters `\( ... \)` and `\[ ... \]`. These are also
  valid LaTeX, so the same source renders in the browser and in the PDF without
  change.
- `pick` and `explain` are optional. Omit `pick` to show the whole pool.
- The correct option is conventionally listed first. Both outputs reshuffle the
  options, so this ordering is never visible to a reader.

## Rendering on the site

Nothing extra is needed for the web quizzes: `uv run python build.py` picks up
any quiz whose filename matches a topic tag and embeds it automatically, and
`assets/js/quiz.js` reshuffles the questions and options on every attempt.

## Rendering the PDFs

We generate printable quizzes with `main.py`, which reads every `*.yml` file,
renders each to a LaTeX document, writes that `.tex` source, and compiles it to
a PDF with `latexmk`. Both the `.tex` and the `.pdf` are written to
`assets/quizzes/`, so the source sits alongside the output and the topic pages
can link to `assets/quizzes/<topic>.pdf`.

```bash
python main.py              # student .tex + .pdf into assets/quizzes/
python main.py --answers    # also write <topic>-answers.tex/.pdf (answer key)
python main.py --combined   # also write all-quizzes.tex/.pdf
python main.py --no-tex     # keep only the PDFs, delete the .tex sources
```

The default output is the student version: every question with its options, but
no marked answer and no explanation. This is what the topic pages serve.
Passing `--answers` writes a separate answer key to `<topic>-answers.tex` and
`<topic>-answers.pdf`, so the student files are never overwritten. The options
are shuffled with a seed derived from each question's text, so the order is
stable across rebuilds and identical between the student and answer-key
versions.

Rendering the PDFs needs `pyyaml` and a TeX distribution providing `latexmk`;
use `--output-dir` to write the files somewhere other than `assets/quizzes/`.

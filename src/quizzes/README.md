# Revision quizzes

Each `*.yml` file here is a short, surface-level multiple-choice quiz, named by
the **topic tag** (e.g. `nash-equilibrium.yml` attaches to the topic page whose
frontmatter has `tag: nash-equilibrium`). `build.py` reads these files, validates
them, and embeds each as JSON in its topic page; `assets/js/quiz.js` runs the
quiz in the browser, reshuffling questions and options on every attempt.

## Format

```yaml
title: Nash equilibrium     # used as the localStorage key for best scores
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

Rules:

- Each question must have **exactly one** option with `correct: true`; the build
  fails otherwise.
- Maths uses MathJax delimiters `\( ... \)` and `\[ ... \]`, and is re-typeset
  after each question is rendered.
- `pick` and `explain` are optional. Omit `pick` to show the whole pool.

## Building

Nothing extra to run: `uv run python build.py` picks up any quiz whose filename
matches a topic tag and embeds it automatically.

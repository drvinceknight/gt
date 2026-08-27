#!/usr/bin/env python3
"""Generate LaTeX and PDF versions of the revision quizzes.

Reads every ``src/quizzes/*.yml`` file, renders each quiz to a LaTeX
document, writes that ``.tex`` source, and compiles it to a PDF with
``latexmk``. Both the ``.tex`` and the ``.pdf`` are kept side by side in
``assets/quizzes/``, so the source is always available alongside the output.

By default we produce the student version: every question with its options
but no marked answers and no explanations. This is what the topic pages link
to. Passing ``--answers`` additionally writes a marked-up answer key to
``<topic>-answers.tex``/``.pdf`` so the student files are never overwritten.

The quiz maths already uses the MathJax delimiters ``\\( ... \\)`` and
``\\[ ... \\]``, which are valid LaTeX, so the mathematical content passes
straight through; only the surrounding prose is escaped.

Usage:
    python main.py                 # student PDFs (+ .tex) in assets/quizzes/
    python main.py --answers       # also write the answer-key versions
    python main.py --combined      # also write a single all-quizzes document
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import random
import re
import shutil
import subprocess
import sys

import yaml

QUIZ_DIR = pathlib.Path(__file__).resolve().parent
ROOT = QUIZ_DIR.parents[1]
DEFAULT_OUTPUT = ROOT / "assets" / "quizzes"

# Spans delimited by \( ... \) or \[ ... \] are mathematics and are copied
# verbatim; everything outside them is ordinary prose and is escaped.
MATH_SPAN = re.compile(r"\\\(.+?\\\)|\\\[.+?\\\]", re.DOTALL)

TEXT_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "#": r"\#",
    "_": r"\_",
    "$": r"\$",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{enumitem}
\usepackage{parskip}
\setlist[enumerate,2]{label=(\alph*), itemsep=1pt, topsep=2pt}
\setlength{\parindent}{0pt}
\newcommand{\correct}[1]{\textbf{#1}\;$\checkmark$}
\begin{document}
"""


def escape_prose(prose: str) -> str:
    """Escape LaTeX special characters in a non-mathematical string."""
    return "".join(TEXT_ESCAPES.get(character, character) for character in prose)


def render(text: str) -> str:
    """Escape prose while leaving \\( ... \\) and \\[ ... \\] spans intact."""
    pieces = []
    cursor = 0
    for match in MATH_SPAN.finditer(text):
        pieces.append(escape_prose(text[cursor : match.start()]))
        pieces.append(match.group(0))
        cursor = match.end()
    pieces.append(escape_prose(text[cursor:]))
    return "".join(pieces)


def shuffled_options(question: dict) -> list[dict]:
    """Return the options in a deterministic, question-specific order.

    The quiz files always list the correct option first, which would make
    every answer ``(a)`` on the page. We shuffle with a seed derived from the
    question text so the order is stable across rebuilds and identical in the
    student and answer-key versions of a quiz.
    """
    seed = int(hashlib.md5(question["q"].encode()).hexdigest(), 16)
    options = list(question["options"])
    random.Random(seed).shuffle(options)
    return options


def quiz_body(quiz: dict, show_answers: bool) -> str:
    """Render one quiz (title, questions, options, optional answers) to LaTeX."""
    lines = [rf"\section*{{{render(quiz['title'])}}}", r"\begin{enumerate}[itemsep=6pt]"]
    for question in quiz["questions"]:
        lines.append(rf"  \item {render(question['q'])}")
        lines.append(r"  \begin{enumerate}")
        correct_label = None
        for index, option in enumerate(shuffled_options(question)):
            label = chr(ord("a") + index)
            text = render(option["text"])
            if option.get("correct"):
                correct_label = label
                if show_answers:
                    text = rf"\correct{{{text}}}"
            lines.append(rf"    \item {text}")
        lines.append(r"  \end{enumerate}")
        if show_answers:
            answer = rf"  \emph{{Answer:}} ({correct_label})"
            if question.get("explain"):
                answer += rf" \emph{{---}} {render(question['explain'])}"
            lines.append(answer)
    lines.append(r"\end{enumerate}")
    return "\n".join(lines)


def document(bodies: list[str]) -> str:
    """Wrap one or more quiz bodies in a complete LaTeX document."""
    return PREAMBLE + "\n\n\\clearpage\n\n".join(bodies) + "\n\\end{document}\n"


def write_quiz(tex_source: str, stem: str, output_dir: pathlib.Path, keep_tex: bool):
    """Write <stem>.tex, compile it to <stem>.pdf, and clean up aux files."""
    tex_path = output_dir / f"{stem}.tex"
    tex_path.write_text(tex_source)
    result = subprocess.run(
        [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={output_dir}",
            str(tex_path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stdout[-2000:])
        raise SystemExit(f"latexmk failed for {stem}")
    # latexmk -c removes aux/log/fls/etc. but keeps the .tex and .pdf.
    subprocess.run(
        ["latexmk", "-c", f"-output-directory={output_dir}", str(tex_path)],
        capture_output=True,
    )
    if not keep_tex:
        tex_path.unlink(missing_ok=True)


def load_quizzes() -> list[tuple[str, dict]]:
    """Return (stem, quiz) pairs for every quiz file, in filename order."""
    return [(path.stem, yaml.safe_load(path.read_text())) for path in sorted(QUIZ_DIR.glob("*.yml"))]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT,
        help="where to write the .tex and .pdf files (default: assets/quizzes)",
    )
    parser.add_argument(
        "--answers",
        action="store_true",
        help="write <topic>-answers.{tex,pdf} with marked answers and explanations",
    )
    parser.add_argument(
        "--combined",
        action="store_true",
        help="also write a single all-quizzes document containing every quiz",
    )
    parser.add_argument(
        "--no-tex",
        action="store_true",
        help="delete the generated .tex, keeping only the compiled PDF",
    )
    arguments = parser.parse_args()

    if shutil.which("latexmk") is None:
        raise SystemExit("latexmk not found; install a TeX distribution first.")

    show_answers = arguments.answers
    suffix = "-answers" if show_answers else ""
    keep_tex = not arguments.no_tex
    output_dir = arguments.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    quizzes = load_quizzes()
    if not quizzes:
        raise SystemExit(f"No quiz files found in {QUIZ_DIR}.")

    for stem, quiz in quizzes:
        write_quiz(document([quiz_body(quiz, show_answers)]), stem + suffix, output_dir, keep_tex)
        print(f"wrote {output_dir / (stem + suffix + '.pdf')} ({len(quiz['questions'])} questions)")

    if arguments.combined:
        bodies = [quiz_body(quiz, show_answers) for _, quiz in quizzes]
        write_quiz(document(bodies), "all-quizzes" + suffix, output_dir, keep_tex)
        total = sum(len(quiz["questions"]) for _, quiz in quizzes)
        print(f"wrote {output_dir / ('all-quizzes' + suffix + '.pdf')} ({total} questions)")


if __name__ == "__main__":
    main()

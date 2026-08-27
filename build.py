#!/usr/bin/env python3
"""Build script for the Game Theory course site.

Reads content from src/, renders Jinja2 templates, and writes static HTML
to the repo root so that `uv run python -m http.server` serves the site
directly.

Usage:
    uv run python build.py
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
from typing import Any

import frontmatter
import jinja2
import markdown as md_module
import yaml

Post = dict[str, Any]

SITE_TITLE = "Game Theory"
BASEURL = ""

# URL path (and output directory) for the facilitator notes. The source files
# still live in src/class-notes/.
NOTES_URL = "run"

SRC = pathlib.Path("src")
ROOT = pathlib.Path(".")


def slugify(text: str) -> str:
    text = str(text).lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def _strip_liquid(text: str) -> str:
    """Replace Liquid site variables and remove remaining block/variable tags."""
    text = text.replace("{{ site.baseurl}}", BASEURL)
    text = text.replace("{{ site.baseurl }}", BASEURL)
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{.*?\}\}", "", text, flags=re.DOTALL)
    return text


def markdown_to_html(text: str) -> str:
    text = _strip_liquid(text)
    return md_module.markdown(
        text,
        extensions=["extra", "toc", "pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )


def note_label(url: str, page_title: str = "") -> str:
    """Return readable link text for a notes URL instead of the raw URL."""
    if "/gtb/chapters/" in url or "/gtb/appendices/" in url or "gtb/main-" in url:
        return f"{page_title}: course textbook chapter" if page_title else (
            "Course textbook chapter"
        )
    labels = {
        "vknight.org/tex": "Mathematical writing notes",
        "vknight.org/pop": "Principles of presentations",
        "vknight.org/pfm": "Python for mathematics",
        "github.com/drvinceknight/pom": "Project organisation notes",
    }
    for key, label in labels.items():
        if key in url:
            return label
    return url


def read_page(path: pathlib.Path) -> Post:
    post = frontmatter.load(path)
    data: Post = dict(post.metadata)
    data["slug"] = path.stem
    if "date" not in data:
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.stem)
        if match:
            data["date"] = match.group(1)
    data["content_html"] = markdown_to_html(post.content)
    m = re.search(r"<p>(.*?)</p>", data["content_html"], re.DOTALL)
    data["excerpt"] = f"<p>{m.group(1)}</p>" if m else ""
    return data


def read_collection(path: pathlib.Path, pattern: str = "*.md") -> list[Post]:
    pages = []
    for p in sorted(path.glob(pattern)):
        if p.stem == "index":
            continue
        pages.append(read_page(p))
    return pages


def to_json(value: Any) -> str:
    """Serialise to JSON, escaped so it is safe inside an HTML <script> tag."""
    return (
        json.dumps(value, ensure_ascii=False)
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def load_quizzes(path: pathlib.Path) -> dict[str, Post]:
    """Read quiz YAML files, keyed by filename stem (the topic tag)."""
    quizzes: dict[str, Post] = {}
    if not path.exists():
        return quizzes
    for p in sorted(path.glob("*.yml")):
        quiz = yaml.safe_load(p.read_text())
        for question in quiz.get("questions", []):
            n_correct = sum(1 for o in question.get("options", []) if o.get("correct"))
            if n_correct != 1:
                raise ValueError(
                    f"{p.name}: question '{question.get('q', '?')[:50]}' has "
                    f"{n_correct} correct options (exactly one required)"
                )
        quizzes[p.stem] = quiz
    return quizzes


def make_env() -> jinja2.Environment:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"), autoescape=False)
    env.filters["slugify"] = slugify
    env.filters["note_label"] = note_label
    env.filters["quiz_json"] = to_json
    return env


def write_html(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    # Load data
    toc = yaml.safe_load((SRC / "data/toc.yml").read_text())

    # Load collections
    topics = read_collection(SRC / "topics")
    class_notes = read_collection(SRC / "class-notes")
    faqs = read_collection(SRC / "faqs")
    faqs.sort(key=lambda faq: faq.get("order", 99))
    assessment = read_page(SRC / "assessment/index.md")
    solutions = read_collection(SRC / "solutions") if (SRC / "solutions").exists() else []
    quizzes_by_tag = load_quizzes(SRC / "quizzes")

    # Tag indices for cross-referencing
    notes_by_tag: dict[str, Post] = {}
    for notes in class_notes:
        tag = notes.get("tag")
        if not tag:
            tags = notes.get("tags", [])
            tag = tags[0] if tags else None
        if tag:
            notes_by_tag[tag] = notes

    solutions_by_tag: dict[str, Post] = {
        sol["tag"]: sol for sol in solutions if sol.get("tag")
    }

    env = make_env()
    css_path = ROOT / "assets/css/style.css"
    css_version = (
        hashlib.md5(css_path.read_bytes()).hexdigest()[:8]
        if css_path.exists()
        else "0"
    )
    ctx = {
        "site_title": SITE_TITLE,
        "baseurl": BASEURL,
        "css_version": css_version,
        "notes_dir": NOTES_URL,
    }

    # --- Topic pages ---
    for topic in topics:
        tag = topic.get("tag")
        html = env.get_template("topic.html").render(
            **ctx,
            page=topic,
            class_notes=notes_by_tag.get(tag),
            solution=solutions_by_tag.get(tag),
            quiz=quizzes_by_tag.get(tag),
        )
        write_html(ROOT / "topics" / f"{slugify(topic['title'])}.html", html)

    # --- Solution pages ---
    for sol in solutions:
        html = env.get_template("solution.html").render(**ctx, page=sol)
        write_html(ROOT / "solutions" / f"{slugify(sol['title'])}.html", html)

    # --- Class-notes pages ---
    for notes in class_notes:
        html = env.get_template("class-notes.html").render(**ctx, page=notes)
        write_html(ROOT / NOTES_URL / f"{slugify(notes['title'])}.html", html)

    # --- Class-notes index (ordered to follow the schedule) ---
    notes_by_slug = {slugify(n["title"]): n for n in class_notes}
    toc_order = [
        slugify(topic["title"])
        for week in toc
        for topic in week.get("topics", [])
        if not topic.get("example")
    ]
    ordered_notes: list[Post] = []
    seen: set[str] = set()
    for slug in ["about-the-class", *toc_order, *sorted(notes_by_slug)]:
        if slug in notes_by_slug and slug not in seen:
            ordered_notes.append(notes_by_slug[slug])
            seen.add(slug)
    notes_index = read_page(SRC / "class-notes/index.md")
    html = env.get_template("class-notes-index.html").render(
        **ctx, page=notes_index, notes=ordered_notes
    )
    write_html(ROOT / NOTES_URL / "index.html", html)

    # --- Assessment page ---
    html = env.get_template("assessment.html").render(**ctx, page=assessment)
    write_html(ROOT / "assessment" / "index.html", html)

    # --- Start here page ---
    start_here = read_page(SRC / "start-here/index.md")
    html = env.get_template("page.html").render(**ctx, page=start_here)
    write_html(ROOT / "start-here" / "index.html", html)

    # --- Home / schedule page ---
    html = env.get_template("index.html").render(**ctx, toc=toc, faqs=faqs)
    write_html(ROOT / "index.html", html)

    print(
        f"Built {len(topics)} topics, {len(class_notes)} class-notes, "
        f"{len(solutions)} solutions, {len(quizzes_by_tag)} quizzes → repo root"
    )


if __name__ == "__main__":
    main()

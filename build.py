#!/usr/bin/env python3
"""Build script for the Game Theory course site.

Reads content from src/, renders Jinja2 templates, and writes static HTML
to the repo root so that `uv run python -m http.server` serves the site
directly.

Internal links are written relative to each page, so the site works wherever
it is mounted: at the root of a local preview, and under /gt/ on
vknight.org.

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

# GitHub Pages serves 404.html at whatever path was requested, so that page
# sits at an unknown depth and its links cannot be relative. It is the one
# place where the mount point has to be named.
SITE_ROOT = "/gt"

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


def baseurl_for(output_dir: pathlib.Path) -> str:
    """Return the relative path from a page in ``output_dir`` to the site root.

    A page at the root gets ``.`` and one a directory down gets ``..``, so that
    links resolve wherever the site is mounted: at the root of a local preview,
    and under /gt/ on vknight.org.
    """
    depth = len(output_dir.parts)
    return "/".join([".."] * depth) if depth else "."


def _strip_liquid(text: str) -> str:
    """Drop Liquid site variables and remaining block/variable tags.

    A leftover ``{{ site.baseurl }}`` becomes nothing, leaving a root-relative
    link that :func:`_relativise` then rewrites like any other.
    """
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{.*?\}\}", "", text, flags=re.DOTALL)
    return text


def _relativise(html: str, baseurl: str) -> str:
    """Rewrite root-relative links and images to be relative to the page.

    Content is written with links such as ``/assessment/`` so that the source
    reads naturally and stays independent of where the site is mounted.
    Protocol-relative URLs (``//example.com``) are left alone.
    """
    return re.sub(r'((?:href|src)=")/(?!/)', rf"\1{baseurl}/", html)


def markdown_to_html(text: str, baseurl: str) -> str:
    text = _strip_liquid(text)
    html = md_module.markdown(
        text,
        extensions=["extra", "toc", "pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )
    return _relativise(html, baseurl)


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


def read_page(path: pathlib.Path, baseurl: str) -> Post:
    post = frontmatter.load(path)
    data: Post = dict(post.metadata)
    data["slug"] = path.stem
    if "date" not in data:
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.stem)
        if match:
            data["date"] = match.group(1)
    data["content_html"] = markdown_to_html(post.content, baseurl)
    m = re.search(r"<p>(.*?)</p>", data["content_html"], re.DOTALL)
    data["excerpt"] = f"<p>{m.group(1)}</p>" if m else ""
    return data


def read_collection(
    path: pathlib.Path, baseurl: str, pattern: str = "*.md"
) -> list[Post]:
    pages = []
    for p in sorted(path.glob(pattern)):
        if p.stem == "index":
            continue
        pages.append(read_page(p, baseurl))
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

    # Output directories, which fix how deep each page sits and hence the
    # relative prefix its links need.
    topics_dir = ROOT / "topics"
    solutions_dir = ROOT / "solutions"
    notes_dir = ROOT / NOTES_URL
    assessment_dir = ROOT / "assessment"
    start_here_dir = ROOT / "start-here"

    # Load collections
    topics = read_collection(SRC / "topics", baseurl_for(topics_dir))
    class_notes = read_collection(SRC / "class-notes", baseurl_for(notes_dir))
    faqs = read_collection(SRC / "faqs", baseurl_for(ROOT))
    faqs.sort(key=lambda faq: faq.get("order", 99))
    assessment = read_page(SRC / "assessment/index.md", baseurl_for(assessment_dir))
    solutions = (
        read_collection(SRC / "solutions", baseurl_for(solutions_dir))
        if (SRC / "solutions").exists()
        else []
    )
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

    def render(
        template: str,
        output: pathlib.Path,
        baseurl: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Render a template to ``output``, with links relative to it."""
        html = env.get_template(template).render(
            site_title=SITE_TITLE,
            baseurl=baseurl if baseurl is not None else baseurl_for(output.parent),
            css_version=css_version,
            notes_dir=NOTES_URL,
            **kwargs,
        )
        write_html(output, html)

    # --- Topic pages ---
    for topic in topics:
        tag = topic.get("tag")
        render(
            "topic.html",
            topics_dir / f"{slugify(topic['title'])}.html",
            page=topic,
            class_notes=notes_by_tag.get(tag),
            solution=solutions_by_tag.get(tag),
            quiz=quizzes_by_tag.get(tag),
        )

    # --- Solution pages ---
    for sol in solutions:
        render(
            "solution.html", solutions_dir / f"{slugify(sol['title'])}.html", page=sol
        )

    # --- Class-notes pages ---
    for notes in class_notes:
        render(
            "class-notes.html",
            notes_dir / f"{slugify(notes['title'])}.html",
            page=notes,
        )

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
    notes_index = read_page(SRC / "class-notes/index.md", baseurl_for(notes_dir))
    render(
        "class-notes-index.html",
        notes_dir / "index.html",
        page=notes_index,
        notes=ordered_notes,
    )

    # --- Assessment page ---
    render("assessment.html", assessment_dir / "index.html", page=assessment)

    # --- Start here page ---
    start_here = read_page(SRC / "start-here/index.md", baseurl_for(start_here_dir))
    render("page.html", start_here_dir / "index.html", page=start_here)

    # --- Home / schedule page ---
    render("index.html", ROOT / "index.html", toc=toc, faqs=faqs)

    # --- 404 page (absolute links; see SITE_ROOT) ---
    render("404.html", ROOT / "404.html", baseurl=SITE_ROOT)

    print(
        f"Built {len(topics)} topics, {len(class_notes)} class-notes, "
        f"{len(solutions)} solutions, {len(quizzes_by_tag)} quizzes → repo root"
    )


if __name__ == "__main__":
    main()

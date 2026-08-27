# Game Theory

Class site for a third year Game Theory course taught at Cardiff University.

Official attributes:

- Level 6 UG Degree Module
- Autumn Semester
- 10 Credits

# Outline description of course

This module introduces students to the mathematical study of multiple
interactive agent decision making. This is an introduction to Game Theory
through notions such as Nash Equilibria and Evolutionary Game Theory. Students
will learn Game Theory in an active way through role playing and student-led
activities.

# Upon completion of this course a student should be able to

- represent games in both Extensive Form and Normal Form.
- understand concepts linked to mixed strategies.
- compute dominant strategies.
- identify best responses.
- define and compute Nash Equilibria.
- understand and carry out backward induction.
- understand concepts of subgame perfection.
- compute equilibria and best responses in repeated games.
- understand concepts of Evolutionary Game Theory.
- compute evolutionary stable strategies.
- model finite population evolutionary games using the Moran process.
- apply Karush-Kuhn-Tucker conditions to optimisation problems.
- understand routing games and compute Nash flows.
- model and solve matching games using the Gale-Shapley algorithm.
- understand auction mechanisms and compute Bayesian Nash equilibria.
- apply Arrow's Impossibility Theorem in social choice settings.
- understand basic concepts in cooperative game theory.

# Syllabus content

- Games and Rationalisation.
- Zero Sum Games.
- Nash Equilibrium.
- Subgame Perfection.
- Repeated Games and Direct Reciprocity.
- Evolutionary Biology and Replicator Dynamics.
- Absorbing Markov Chains and the Moran Process.
- Karush-Kuhn-Tucker Conditions.
- Routing Games.
- Matching Games.
- Auction Theory.
- Social Choice.
- Cooperative Games.

# Assessment

- A 2 hour exam: 100%

# Building the site

The site is built with a Python script using [uv](https://docs.astral.sh/uv/).

## Prerequisites

Install `uv`:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Build

```
uv run python build.py
```

HTML is written directly to the repo root. Internal links are relative to
each page, so the site works both at the root of a local preview and under
`/gt/` on vknight.org. To preview locally:

```
uv run python -m http.server
```

Then open `http://localhost:8000/` in a browser.

The one exception is `404.html`: GitHub Pages serves it at whatever path was
requested, so its depth is unknown and its links have to be absolute. They are
built from the `SITE_ROOT` constant in `build.py`, which is the only place the
mount point is named.

## Deployment

Commit the generated HTML and push to `main`. The GitHub Actions workflow
(`.github/workflows/deploy.yml`) deploys the repo root to GitHub Pages
automatically — no build step runs in CI.

## Content

| Directory | Purpose |
|---|---|
| `src/topics/` | Student-facing topic pages (one per syllabus topic) |
| `src/class-notes/` | Facilitator notes (activity + discussion plans) |
| `src/posts/` | Class log entries |
| `src/faqs/` | Frequently asked questions (shown on home page) |
| `src/assessment/` | Assessment information page |
| `src/data/toc.yml` | Weekly schedule (drives the home page) |
| `assets/` | PDFs, images, and other static files |
| `templates/` | Jinja2 HTML templates |

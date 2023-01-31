---
layout: default
---

# Individual coursework (40%)

A mock coursework is available:
[here]({{site.baseurl}}/assets/assessment/mock/ind/assignment.ipynb).

# Group project (60%)

## [Marking criteria](#marking-criteria)

### 2 Page Paper

- Summary: Has a clear description of the high-level functionality and
  purpose of the software for a diverse, non-specialist audience been
  provided?  [10%]
- A statement of need: Do the authors clearly state what problems the
  software is designed to solve and who the target audience is?
- State of the field: Do the authors describe how this software compares
  to other commonly-used packages? [10%]
- Quality of writing: Is the paper well written (i.e., it does not
  require editing for structure, language, or writing quality)? [10%]
- References: Is the list of references complete, and is everything
  cited appropriately that should be cited (e.g., papers, datasets,
  software)? Do references in the text use the proper citation syntax? [10%]

### 15 Minute Presentation

- Functionality: Have the functional claims of the software been
  confirmed? [10%]
- Documentation: Does the documentation have a Tutorial, How to section,
  Reference and Explanation section? Is it clear? Is the source code clear?
  [10%]
- Modularity: Is the code written in a modular way? [10%]
- Testing: Is all code tested? [10%]
- Presentation: Was the presentation format used appropriately? Were the
  visual aids appropriate? [10%]


Note that this marking criteria has some overlap with the review criteria for
the [Journal of Open Source
Software](https://joss.readthedocs.io/en/latest/review_checklist.html). Some
examples of papers written for that journal that can be helpful are:

- [Matching: A Python library for solving matching games](https://joss.theoj.org/papers/10.21105/joss.02169)
- [Nashpy: A Python library for the computation of Nash equilibria](https://joss.theoj.org/papers/10.21105/joss.00904)

Examples of presentations are available at: [vknight.org/pop/](https://vknight.org/pop/)

## [Past group project](#past-group-projects)

A list of titles of past projects:

{% for year in site.data.projects %}
### {{ year.year }}
{% for title in year.titles %}
- {{ title }}
{% endfor %}
{% endfor %}

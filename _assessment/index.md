---
layout: default
tag: assessment
---

# Continuous Individual coursework (20%)

On learning central there are 9 online quizzes available to you.

You can submit as many times as you want.

# Teaching Resource (Individual coursework - 20%)

Write a Jupyter notebook demonstrating your understanding of the use of Python
for the study of the game theoretic topics covered in this module.

The target audience: students on this course.

Marking: The grades for this coursework will be marked on a **piecewise linear
curve** to ensure approximately a third of the class have a grade above \\(70%\\) and resulting in a mean of \\(60\pm \frac{25}{\sqrt{n}}\\) (where \\(n\\) is the
number of students in the class). For example, with a
class of size \\(n=80\\) the mean mark will fall within the range \\(60 \pm 2.8\\).

# Group project (60%)

Carry out a group research project using Game Theory. This can either be a
theoretical exploration of a topic of Game Theory or an applied problem:
investigating some interactive process using the tools of the course.

You will evidence your progress with 2 mediums:

1. A 2 page paper
2. A 15 minute recorded presentation

Your final submission should include the following **3** files:

1. A `main.pdf` file: the pdf file for a 2 page paper written in [LaTeX](({{ site.baseurl }}/topics/latex.html)
   ).
2. A `presentation.mp4` (or similar file format): the video recording of [your 15 minute presentation]({{ site.baseurl }}/topics/presenting-mathematics.html)
3. A `contribution.md` file: a file describing the contributions of every member of your group.

## [Marking criteria](#marking-criteria)

### 2 Page Paper

- Summary: Has a clear description of the high-level work undertaken been given. [10%]
- A statement of need: Do the authors clearly state what problems their work is applied to. [10%]
- State of the field: Do the authors describe how any other work relates to theirs? [10%]
- Quality of writing: Is the paper well written (i.e., it does not require editing for structure, language, or writing quality)? [10%]
- References: Is the list of references complete, and is everything cited appropriately that should be cited (e.g., papers, datasets, software)? Do references in the text use the proper citation syntax? [10%]

### 15 Minute Presentation

- Scope: Are the details of the work clear? [10%]
- Theory: Is an understanding of relevant theory demonstrated? [10%]
- Code: Is code well written and appropriate? [10%]
- Accuracy: Is the work correct? [10%]
- Presentation: Was the presentation format used appropriately? Were the visual aids appropriate? [10%]

Examples of presentations are available at: [vknight.org/pop/](https://vknight.org/pop/)

Marking: The grades for this coursework will be marked on a **piecewise linear
curve** to ensure approximately a third of the class have a grade above \\(70%\\) and resulting in a mean of \\(60\pm \frac{25}{\sqrt{n}}\\) (where \\(n\\) is the
number of students in the class). For example, with a
class of size \\(n=80\\) the mean mark will fall within the range \\(60 \pm 2.8\\).

## [Past group projects](#past-group-projects)

A list of titles of past projects:

{% for year in site.data.projects %}

### {{ year.year }}

{% for title in year.titles %}

- {{ title }}
  {% endfor %}
  {% endfor %}

## [Log of past relevant classes](#log-of-past-relevant-classes)

{% for post in site.posts %}
{% if post.tags contains page.tag %}
[{{post.date | date: "%D"}}: {{ post.title }}]({{site.baseurl}}{{post.url}})
{{ post.excerpt }}
{% endif %}
{% endfor %}

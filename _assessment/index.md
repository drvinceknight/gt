---
layout: default
tag: assessment
---

# Individual coursework (40%)

A mock coursework is available:
[here]({{site.baseurl}}/assets/assessment/mock/ind/assignment.ipynb).

The 2022-2023 coursework is available here:
[here]({{site.baseurl}}/assets/assessment/2022-2023/ind/assignment.ipynb).

The topics for the individual coursework for the past few years have been:

- 2022-2023:
    1. [Repeated games]({{ site.baseurl }}/topics/repeated-games.html)
    2. [Replicator Dynamics]({{ site.baseurl }}/topics/replicator-dynamics.html)
    3. [Support enumeration]({{ site.baseurl }}/topics/support-enumeration.html)
    4. [Asymmetric replicator dynamics](https://nashpy.readthedocs.io/en/stable/text-book/asymmetric-replicator-dynamics.html)
- 2021-2022:
    1. [Moran Process]({{ site.baseurl }}/topics/moran-process.html)
    2. [Replicator Dynamics]({{ site.baseurl }}/topics/replicator-dynamics.html)
    3. [Support enumeration]({{ site.baseurl }}/topics/support-enumeration.html)
    4. [Fictitious play](https://nashpy.readthedocs.io/en/stable/text-book/fictitious-play.html)
- Mock:
    1. [Support enumeration]({{ site.baseurl }}/topics/support-enumeration.html)
    2. [Prisoners dilemma]({{ site.baseurl }}/topics/prisoners-dilemma.html)
    3. [Repeated games]({{ site.baseurl }}/topics/repeated-games.html)
    4. [Lemke Howson Algorithm](https://nashpy.readthedocs.io/en/stable/text-book/lemke-howson.html#the-lemke-howson-algorithm)

# Group project (60%)

Carry out a group research project using Game Theory. This can either be a
theoretical exploration of a topic of Game Theory or an applied problem:
investigating some interactive process using the tools of the course.

You will evidence your progress with 3 mediums:

1. Regular logs (to be filled in individually).
2. A 2 page paper
3. A 15 minute presentation

## [Marking criteria](#marking-criteria)

### 2 Page Paper

- Summary: Has a clear description of the high-level work undertaken been given. [10%]
0  A statement of need: Do the authors clearly state what problems their work is applied to.
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

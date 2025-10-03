---
layout: default
tag: assessment
---

There are two piece of assessment in this course:

- A 2 hour exam (75%)
- A group research project (25%)

# Exam (75%)

Work in progress: Example and mock exams to appear here.

# Group research project (25%)

Due date: end of the Autumn Semester.

Carry out a group research project using Game Theory for a chosen topic of your
choice.

The choice of topic is yours, two potential general areas of investigation:

- Prove and illustrate a theorem from the notes (or otherwise);
- Model a real world scenario using game theory.

You are able to use code to tackle the numerical computations to allow
you to delve further in to the investigation you choose.

You will evidence your work with 2 mediums:

1. A 2 page paper
2. A 15 minute recorded presentation

Your final submission should include the following **3** files:

1. A `main.pdf` file: the pdf file for a 2 page paper.
2. A `presentation.mp4` (or similar file format): the video recording of [your 15 minute presentation]({{ site.baseurl }}/topics/presenting-mathematics.html)
3. A `contribution.md` file: a file describing the contributions of every member of your group.

## [Marking criteria](#marking-criteria)

### 40-44%

- The work shows limited effort and lacks clarity and insight.
- Ideas are vague, disorganized, and not well supported.
- Limited understanding of basic game theory concepts, such as Nash equilibrium.
- Arguments, if present, are weak and lack structure or evidence.
- Overall, the submission suggests significant gaps in understanding or preparation.

### 45-54%

- Some understanding of the topic is evident, but analysis is basic and lacks depth.
- Concepts such as payoff matrices or strategies are included but may be inaccurate or superficial.
- Writing is somewhat clear but may lack precision or organization.
- Evidence and examples, such as real-world applications, are limited or not well integrated.
- The work shows effort but is underdeveloped.

### 55-64%%

- Demonstrates a reasonable understanding of game theory with moderately developed ideas.
- Key concepts, such as strategies or best responses, are mostly accurate but lack deeper exploration.
- Writing is clear and organized, with occasional lapses in coherence.
- Supporting evidence is relevant but may not fully support arguments.
- The submission is competent but not particularly original or insightful.

### 65-69%

- Shows strong understanding of game theory with well-developed ideas and analysis.
- Key concepts are applied accurately and effectively.
- Writing is effective, with good organization and clear transitions.
- Evidence and examples, such as real-world scenarios or well chosen examples, are relevant and support the research well.
- The submission is solid but may not achieve a high level of originality or insight.

### 70-74%

- Displays a strong understanding of the topic with insightful analysis.
- Concepts such as evolutionary game theory or repeated games are explored thoughtfully and creatively.
- Writing is polished, with clear organization and precise language.
- Evidence is well-chosen and effectively integrated.
- The submission may need minor refinement.

### 75-79%

- Exceptional understanding of game theory with advanced analysis and arguments.
- Key ideas are connected to broader contexts.
- Writing is consistently polished and clear.
- Evidence is of high quality adding depth to the analysis.
- The work is excellent but may lack the highest level of originality or rigor.

### 80-84%

- Exemplary work with advanced understanding of game theory.
- Analysis is insightful and connects to broader or interdisciplinary topics, such as behavioral economics or biology.
- Writing is excellent, with clarity and coherence throughout.
- Evidence is of high relevance, such as critiques of existing literature.
- The submission is of publishable quality with minor refinements.

### 85-89%

- Outstanding mastery of game theory, pushing boundaries of understanding.
- Arguments are highly original and innovative, such as advanced approaches to repeated or dynamic games.
- Writing is flawless, with professional clarity and tone.
- Evidence is unique and effectively supports arguments, including advanced mathematical models or simulations.
- The work sets a high standard for excellence.

### 90-94%

- An extraordinary piece of work with groundbreaking analysis.
- Unique perspectives and methods are applied to theoretical topics at the boundaries of the taught content.
- Writing is exceptional, with engaging and clear presentation.
- Evidence and examples are original, such as innovative takes on classic problems or stochastic games.
- The submission is of publishable quality and demonstrates critical and creative engagement.

### 95-100%

- Exceptional work demonstrating a profound understanding of game theory.
- Analysis and ideas are highly original, creative, and well-supported.
- Writing is professional and engaging, clearly communicating complex ideas.
- Evidence and examples, whether theoretical or computational, are thoughtfully chosen and seamlessly integrated.
- This level represents outstanding academic achievement, demonstrating both depth and originality,
  for those who fully engage with the subject matter.

## Specific Criteria Descriptions

### 1. Content and Depth

- Demonstrates understanding of relevant topics.
- Includes original and creative ideas.
- Covers key concepts such as Nash equilibrium, Bayesian games, or bargaining solutions accurately and appropriately.
- Effectively incorporates computational tools to support analysis and exploration.

### 2. Writing Style and Organization

- Ideas are presented clearly and logically.
- Writing is organized and uses suitable language.
- Sections flow well and enhance the overall argument.

### 3. Evidence and Supporting Details

- Includes relevant and well-integrated evidence.
- Uses examples or visuals, like payoff matrices or diagrams, to clarify points.
- Demonstrates effective use of computational outputs to support arguments.

### 4. Analysis and Argumentation

- Develops clear and logical arguments.
- Uses evidence effectively to build ideas.
- Incorporates computational tools to replace repetitive calculations and enable deeper analysis.
- Addresses counterarguments where relevant.

## [Past projects](#past-group-projects)

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

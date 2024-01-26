---
layout: class-notes
---

## Class notes

{% for notes in site.class-notes %}

- [{{ notes.title }}]({{notes.title | slugify}}.html)

{% endfor %}

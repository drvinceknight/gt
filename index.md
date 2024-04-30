---
layout: default
---

## [Schedule](#schedule)

{% for week in site.data.toc %}

### {{ week.title }}

{% for topic in week.topics %}

- [{{ topic.title }}](./topics/{{topic.title | slugify}}.html)
  {% endfor %}
  {% endfor %}

## [FAQs](#faqs)

{% for question in site.faqs %}

### [{{ question.title }}](#{{ question.slug }})

```plaintext
{{ question.content | strip_html}}
```

{% endfor %}

## [Assessment]({{ site.baseurl}}/assessment/)

## [Seminar series]({{ site.baseurl}}/seminars/)

## [Log](#blog)

([RRS feed]({{ site.baseurl }}/feed.xml))

{% for post in site.posts %}

- [{{post.date | date: '%Y-%m-%d'}}: {{ post.title }}](./{{ post.url }})
  {{ post.excerpt }}
  {% endfor %}

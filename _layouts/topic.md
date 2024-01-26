---
layout: default
---

<div class="container">

<h1> {{ page.title }} </h1>

{% if page.note_urls %}
<h3> Notes </h3>

        <ul>
            {% for url in page.note_urls %}
                <li><a href="{{ url }}">{{ url }}</a></li>
            {% endfor %}
        </ul>

{% endif %}

{% if page.video_urls %}
<h3> Videos </h3>
<ol>
{% for url in page.video_urls %}
<li>{{ url | markdownify }}</li>
{% endfor %}
</ol>
{% endif %}

{% if page.meeting_urls %}
<h3> Class meeting notes </h3>

        <ul>
            {% for url in page.meeting_urls %}
                <li><a href="{{ url }}">{{ url }}</a></li>
            {% endfor %}
        </ul>

{% endif %}

{{ page.content }}

<h2>Log of past relevant classes</h2>

{% for post in site.posts %}
{% if post.tags contains page.tag %}

<h4>
<a href="{{site.baseurl}}{{post.url}}">{{post.date | date: "%D"}}: {{ post.title }}
</a>
</h4>
  {{ post.excerpt }}
    {% endif %}
{% endfor %}
</div>

{% for notes in site.class-notes %}
{% if notes.tags contains page.tag %}

<small>
<code><a href="{{site.baseurl}}{{notes.url}}">Class notes: {{ notes.title }}
</a></code>
</small>
{% endif %}
{% endfor %}

{% include utterances.html %}

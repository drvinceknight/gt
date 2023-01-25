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

{% if page.public_videos %}
    <h3> YouTube playlist </h3>

        <ol>
            {% for url in page.public_videos %}
                <li>{{ url | markdownify }}</li>
            {% endfor %}
        </ol>
{% endif %}

{% if page.private_videos %}
    <h3> Cardiff University hosted playlist </h3>

        <ol>
            {% for url in page.private_videos %}
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
</div>

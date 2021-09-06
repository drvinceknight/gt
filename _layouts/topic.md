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
    <h3> Video playlist </h3>

        <ul>
            {% for url in page.video_urls %}
                <li><a href="{{ url }}">{{ url }}</a></li>
            {% endfor %}
        </ul>
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
<script src="https://utteranc.es/client.js"
        repo="drvinceknight/gt"
        issue-term="pathname"
        label="💬 comment"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>

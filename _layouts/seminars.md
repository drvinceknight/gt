---
layout: default
---

<div class="container" style="border:blue; border-width:5px; border-style:solid;">

<tt>
<h1 > {{ page.title }} </h1>

<div style="border:blue; border-width:3px; border-style:dashed;">
<b>Note: this is a collection of resources for a seminar. The goal of a seminar
                is to spike your interest and not necessarily for you to learn
                anything. For the learning resources please take a look at the
                corresponding topics listed at the bottom of this page.</b>
</div>

{{ page.content }}

</div>

{% if page.topics %}

<h3> Corresponding Topics</h3>

<ul>
{% for topic in page.topics %}
<li>
    <a href="{{site.baseurl}}/topics/{{topic}}.html">{{topic | replace: "-"," " | capitalize}}
</a>
</li>

{% endfor %}
{% endif %}

</ul>
{% include utterances.html %}
</tt>

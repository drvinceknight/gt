---
layout: default
---

<div class="container" style="border:red; border-width:5px; border-style:solid;">

<tt>
<h1 > {{ page.title }} </h1>

<div style="border:red; border-width:3px; border-style:dashed;">
<b>Note: These are not designed to be
student facing.</b>

<p >I make these notes available with the intent of making it easier to plan and/or take
notes from class.
</p>

<p>
Student facing resources for each topic are all available at <a href={{site.baseurl}}/>vknight.org/gt/</a>.
</p>
</div>

{{ page.content }}

</div>

{% include utterances.html %}
</tt>

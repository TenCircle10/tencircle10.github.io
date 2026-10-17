<ul class="note-list">
{% for page in site.pages %}
{% if page.path contains 'notes/' and page.name != 'index.md' %}
{% unless page.name contains 'sync-test' or page.name contains 'slug-demo' %}
<li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name }}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

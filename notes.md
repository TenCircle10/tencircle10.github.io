<ul class="note-list">
{% for page in site.pages %}
{% if page.path contains 'notes/' and page.name != 'index.md' %}
{% assign page_name = page.name | downcase %}
{% unless page_name contains 'test' or page_name contains 'torture' or page_name contains '测试' or page_name contains 'demo' %}
<li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name }}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

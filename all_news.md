---
layout: default
title: All news
permalink: /all_news/
---

# Categories:

{% for category in site.categories %}
  <details>
    <summary><h2>{{ category[0] | capitalize }}: <a>({{category[1] | size}} items)</a></h2></summary>
    <ul>
      {% for post in category[1] %}
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
        {{ post.excerpt }}
      {% endfor %}
    </ul>
  </details>
{% endfor %}


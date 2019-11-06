---
layout: default
title: All news
---

{% for category in site.categories %}
  <h2> {{ category[0] | capitalize }}</h2>
  <ul>
    {% for post in category[1] %}
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      {{ post.excerpt }}
    {% endfor %}
  </ul>
{% endfor %}


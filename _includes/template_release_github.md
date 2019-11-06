{% capture p_url %}https://github.com/{{ include.p_owner }}/{{ include.p_name }}/{% endcapture %}
{% capture p_tag %}{{ p_url }}releases/tag/v{{ include.p_vers }}{% endcapture %}

Version {{ include.p_vers }} of [{{ include.p_name }}]({{ p_url }}) has been released!

Go check it out at: [{{ p_tag }}]({{ p_tag }})
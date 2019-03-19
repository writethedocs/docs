{% for talk in data %}

{% for speaker in talk.speakers %}
.. _speaker-{{ shortcode }}-{{ year }}-{{ speaker.slug }}:
{% endfor %}

.. Comment to break up reference issues
.. * Ashleigh Rentz – `The Facts About FAQs <https://www.writethedocs.org/conf/portland/2018/speakers/#speaker-portland-2018-ashleigh-rentz>`_

{% for speaker in talk.speakers %}
* {{ speaker.name }} – `{{ talk.title }} <https://www.writethedocs.org/conf/{{ shortcode }}/{{ year }}/speakers/#speaker-{{ shortcode }}-{{ year }}-{{ speaker.slug }}>`__
{% endfor %}
{% endfor %}

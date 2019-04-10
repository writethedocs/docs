{% for talk in data %}
{% set is_keynote = talk.title.startswith("Keynote") %}

{% for speaker in talk.speakers %}
{% if speaker.slug %}
.. _speaker-{{ speaker.slug }}:
{% endif %}
{% endfor %}
.. raw:: html

    {% for speaker in talk.speakers %}
    {% if speaker.slug %}<a name="speaker-{{ speaker.slug }}"></a>{% endif %}
    {% endfor %}
    <div class="row row-speaker {% if is_keynote %}row-speaker-keynote{% endif %}">
      <div class="{% if is_keynote %}col-md-4 col-sm-4{% else %}col-md-2 col-sm-2 col-md-offset-1 col-sm-offset-1{% endif %}">
        {% for speaker in talk.speakers %}
        <img class="speaker-image" src="{{ speaker.image }}" alt="" />
        {% endfor %}
      </div>
      <div class="col-md-8 col-sm-8">
        <h3>{% for speaker in talk.speakers %}{% if loop.index > 1 %} &amp; {% endif %}{{ speaker.name }}{% endfor %}
          <span class="speaker-details">
          {% set website_shown = talk.speakers|map(attribute='website')|join('') %}
          {% set company_shown = talk.speakers|map(attribute='company')|join('') %}
          {% set twitter_shown = talk.speakers|map(attribute='twitter')|join('') %}
          {% for speaker in talk.speakers %}
            {% if speaker.company and loop.first %}
                {{ speaker.company }}
            {% endif %}
          {% endfor %}
          {% if company_shown and website_shown %} &mdash; {% endif %}
          {% for speaker in talk.speakers %}
            {% if speaker.website %}
                <a href="{{ speaker.website }}">{{ speaker.websiteLabel }}</a>
            {% endif %}
          {% endfor %}
          {% if (company_shown or website_shown) and twitter_shown %} &mdash; {% endif %}
          {% for speaker in talk.speakers %}
            {% if speaker.twitter %}
                <a href="https://twitter.com/{{ speaker.twitter }}">@{{ speaker.twitter }}</a>
            {% endif %}
          {% endfor %}
          </span></h3>
        <h4>{{ talk.title }}</h4>
        {{ talk.abstract }}
      </div>
    </div>

{% endfor %}
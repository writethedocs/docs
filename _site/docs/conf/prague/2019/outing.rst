:template: {{year}}/generic.html

{% if shortcode == 'prague'%}
:banner: _static/2019/assets/headers/group.png

Write the Docs Boat Ride
========================

{% include "conf/prague/boat.rst" %}

{% elif shortcode == 'portland'%}

:banner: _static/2019/assets/headers/hike.png

Write the Docs Hike
===================

{% include "conf/portland/hike.rst" %}

{% else %}

We don't have an outing yet.

{% endif %}

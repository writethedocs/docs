:template: {{year}}/generic.html


Run of show
============


Monday, May 20
--------------

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-1.yaml
   :template: include/ros{{year}}.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Tuesday, May 21
---------------

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-2.yaml
   :template: include/ros{{year}}.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

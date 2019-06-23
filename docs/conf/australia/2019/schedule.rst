:template: {{year}}/generic.html


Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{% if flaglivestreaming %}

We're `live streaming </conf/{{shortcode}}/{{year}}/livestream>`_ the talks!

{% endif %}

Thursday, 14th November 2019
----------------------------

*Tea, coffee and lunch will be provided, as well as snacks and drinks all day.*

Conference talks
~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **9:00-14:30** (including a lunch break)
* **Details**: TBA

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-1.yaml
   :template: include/schedule2018.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel with the workshop.

* **Where**: {{about.unconfroom}}
* **When**: **14:30-16:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Thursday Night Social
~~~~~~~~~~~~~~~~~~~~~~~

The official Write the Docs Australia social!
This event is for **conference attendees only**, so please bring your badge to be let into the venue.
There will be drinks and nibbles available while our tab lasts.

* **Where**: TBA
* **When**: **6.00pm-8.30pm**


Friday, 15th November 2019
----------------------------------------

*Tea, coffee and lunch will be provided, as well as snacks and drinks all day.*

Conference Talks
~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **9:00-14:30** (including a lunch break)
* **Details**: TBA

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-2.yaml
   :template: include/schedule2018.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the mini-workshop.

* **Where**: {{about.unconfroom}}
* **When**: **14:30-16:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

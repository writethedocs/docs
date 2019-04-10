:template: {{year}}/generic.html
:banner: _static/2018/assets/headers/venue.png

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none


Thursday, 15th November 2018
----------------------------

*Tea, coffee and lunch will be provided, as well as snacks and drinks all day.*

Conference talks
~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **9:00-14:30** (including a lunch break)
* **Details**: Full main stage schedule below!

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-1.yaml
   :template: include/schedule2018.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Workshop: Tech Writing 101
~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **14:30-16:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/workshop-tech-writing`

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

* **Where**: Tap831, 831 Bourke St, Docklands VIC 3008
* **When**: **6.00pm-8.00pm**


Friday, 16th November 2018
----------------------------------------

*Tea, coffee and lunch will be provided, as well as snacks and drinks all day.*

Conference Talks
~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **9:00-14:00** (including a lunch break)
* **Details**: Full main stage schedule below!

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-2.yaml
   :template: include/schedule2018.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Workshop 1: Let's Create a Style Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **14:30-15:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/workshop-style-guide`

Workshop 2: Static Site Generators, What, Why and How
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Where**: {{about.mainroom}}
* **When**: **15:40-16:40**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/workshop-ssg`

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the mini-workshop.

* **Where**: {{about.unconfroom}}
* **When**: **14:30-16:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

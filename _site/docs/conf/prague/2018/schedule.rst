:template: {{year}}/generic.html

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{{date.day_one.dotw}}, {{date.day_one.date}}
--------------------------------------------------

{% if flaghashike %}

Hike
~~~~

The only event scheduled on Saturday is the :doc:`annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us on the hike and take the chance to explore Portland in all of its glory.

* **Where**: Lower Macleay Park or Macleay Park Entrance.
* **When**: 13:45
* **Details**: :doc:`Annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`

{% endif %}

{% if flaghasboat %}

Boat Ride
~~~~~~~~~

The only event scheduled on Saturday is the :doc:`Prague Boat Ride </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us and experience Prague from the water.

* **Where**: `Prague Boats, pier no. 5 <https://goo.gl/maps/bqLP3VaytVo>`_
* **When**: 13:45 boarding, boat leaves **promptly** at 14:00
* **Details**: :doc:`Prague Boat Ride </conf/{{shortcode}}/{{year}}/outing>`

{% endif %}


{{date.day_two.dotw}}, {{date.day_two.date}}
----------------------------------------

The Writing Day and Welcome Reception will be held at the **{{about.venue}}**.

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

.. contents::
    :local:
    :backlinks: none

Writing Day
~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **9:00-17:00**
* **Details**: :doc:`Writing Day documentation sprints </conf/{{shortcode}}/{{year}}/writing-day>`

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-0.yaml
   :template: include/schedule2018.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Reception
~~~~~~~~~

We encourage everyone to drop by on Sunday evening for the conference reception.
You'll have a chance to get acquainted with each other over some drinks and snacks.
We'll also help groups organize dinner plans, so you can continue your conversations over more substantial food as well.

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **17:00-20:00**

Monday, September 10
--------------------

.. contents::
   :local:
   :backlinks: none

This is the main event! Hear from lots of interesting folks about all things documentation.
We will have talks all day on the main stage, and a unconference session running in parallel in the afternoon.

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00-18:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`


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

The unconference sessions run in parallel to the main conference talks.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **10:40-18:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Monday Night Social
~~~~~~~~~~~~~~~~~~~

The official Write the Docs social!

This event is for **conference attendees only**. Please bring your badge to be let into the venue.
There will be light snacks and drinks available on the conference while our tab lasts.

* **Where**: `Hoffa Bar, Senovážné Náměstí 22, Prague 1 <https://goo.gl/maps/b1egvQhoDxt>`_
* **When**: **20:00-23:00**
* **Details**: Drinks and snacks are included while our tab lasts. If you want a sit-down dinner we recommend to grab it before, as we will only have light snacks and finger food at the event. The bar is located on the ground floor and is accessible to wheelchairs.

Tuesday, September 11
---------------------

.. contents::
   :local:
   :backlinks: none

And the conference goes on!

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00-16:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-2.yaml
   :template: include/schedule2018.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

.. _{{shortcode}}-{{year}}-job-fair:

Job Fair
~~~~~~~~

New in 2018! We'll be holding a job fair on Tuesday morning!

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **10:30-11:50**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/job-fair`

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **12:10-15:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

:template: {{year}}/generic.html


Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

All conference events (except the hike & social event) will be held at **Crystal Ballroom located at 1332 W Burnside St**.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{% if flaglivestreaming %}

We're `live streaming </conf/{{shortcode}}/{{year}}/livestream>`_ the talks!

{% endif %}

Saturday, May 18
----------------

Hike
~~~~

The only event scheduled on Saturday is the :doc:`annual hike </conf/{{shortcode}}/{{year}}/hike>`.
If you get into town early, join us on the hike and take the chance to explore Portland in all of its glory.

* **Where**: Lower Macleay Park or Macleay Park Entrance.
* **When**: 1:45pm
* **Details**: :doc:`Annual hike </conf/{{shortcode}}/{{year}}/hike>` page

Sunday, May 19
--------------

Writing Day
~~~~~~~~~~~

Get together with other documentarians and work on an open source project and learn some new skills.

* **Where**: Crystal Ballroom
* **When**: **9am-5pm**, Doors & Breakfast at 8am.
* **Details**: :doc:`Writing Day documentation sprints </conf/{{shortcode}}/{{year}}/writing-day>`

Reception
~~~~~~~~~

We encourage everyone to drop by on Sunday evening for the conference reception.
You'll have a chance to get acquainted with each other over some drinks and snacks,
and pick up your badge so you can skip the line in the morning. Note that we are not
able to accomodate additional guests at this event.

* **Where**: Crystal Ballroom
* **When**: **5pm-8pm**

Monday, May 20
--------------

Unconference
~~~~~~~~~~~~

Have in depth discussions about a large number of topics.
This is scheduled on the day of, so feel free to suggest your own session!

* **Where**: Lola's room, Crystal Ballroom
* **When**: **9:40am-5:00pm**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`


Conference Talks
~~~~~~~~~~~~~~~~

The "main event" -- we'll have a variety of speakers on the stage sharing their experience and knowledge.

* **Where**: Main stage, Crystal Ballroom
* **When**: **9am-5pm**
* **Details**: Full main stage schedule below

.. separator to fix list formatting

{% if flaglivestreaming %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-1.yaml
   :template: include/schedule{{year}}.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Monday Night Social
~~~~~~~~~~~~~~~~~~~

The official Write the Docs social!
This event is for **conference attendees only**, so please bring your badge to be let into the venue.
There will be light snacks and drinks available on the conference while our tab lasts.

* **Where**: TBD
* **When**: **7pm-10pm**

Tuesday, May 21
---------------

Job Fair
~~~~~~~~

We'll be holding a job fair on Tuesday morning!

* **Where**: Lola's room (downstairs at the Crystal Ballroom)
* **When**: **9:30am-11:40am**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/job-fair`

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks.

* **Where**: Lola's room (downstairs at the Crystal Ballroom)
* **When**: **1:20-3:30pm**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: Main stage, Crystal Ballroom
* **When**: **9am-4pm**
* **Details**: Full main stage schedule below!

.. separator to fix list formatting

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{templatecode}}-{{year}}-day-2.yaml
   :template: include/schedule{{year}}.rst
   :include_context:

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

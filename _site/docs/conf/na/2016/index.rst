:template: 2016/na.html


Thanks!
=======

Thanks to everyone who made this year another wonderful event.
We're so grateful to our sponsors, speakers, volunteers, and attendees for making the conference possible.

We have posted the `videos <https://www.youtube.com/playlist?list=PLmV2D6sIiX3U03qc-FPXgLFGFkccCEtfv>`_ and `photos <https://www.flickr.com/photos/writethedocs/albums/72157669467964085>`_ from the conference for those who couldn't attend.
Hopefully they allow you to bask in the beauty of the event from the comfort of your own chair.

We hope you'll join us in `Prague <http://www.writethedocs.org/conf/eu/2016/>`_ in September,
or again in Portland next year!

About the conference
====================

We invite you to join 400 other folks for a three-day event to explore the art and science of
documentation. The conference covers any topic related to documentation
in the software industry. Past talks
have also covered such diverse topics as empathy, the history of math symbols,
and using emoji to keep your users' attention.

Write the Docs brings *everyone* who writes the docs together in the
same room: Writers, Developers, Support Folks. We all have things to
learn from each other, and there's no better way than sitting together
and talking.

The main presentation track takes place from **May 23-24 (Monday and
Tuesday) from 9am to 6pm**. We will return to the historic `Crystal
Ballroom <http://www.mcmenamins.com/CrystalBallroom>`_, `centrally
located <http://goo.gl/maps/D2WrJ>`_ in the heart of Portland. During
the main event we also run a :doc:`/conf/na/2016/unconference`,
downstairs in Lola's Room.

You can find out more information about the venue and its accessibility on our :doc:`/conf/na/2016/venue` page.


.. raw:: html

    <div class="row row-images">
      <div class="col-md-6 col-sm-6 col-sm-offset-0 col-xs-8 col-xs-offset-2">
        <a href="https://www.flickr.com/photos/writethedocs/14151785456/in/album-72157644692192083/">
    <img src="/_static/img/2016/na/attendees.jpg" alt="Attendees waving to the camera">
        </a>
      </div>
      <div class="col-md-6 col-sm-6 col-sm-offset-0 col-xs-8 col-xs-offset-2">
        <a href="https://www.flickr.com/photos/writethedocs/13991334230/in/album-72157644692192083/">
    <img src="/_static/img/2016/na/group.jpg" alt="A group of people talking together">
        </a>
      </div>
    </div>


News
^^^^

- :doc:`/conf/na/2016/news/announcing-2016`
- :doc:`/conf/na/2016/news/cfp-tickets`
- :doc:`/conf/na/2016/news/cfp-reminder`
- :doc:`/conf/na/2016/news/announcing-presentations`
- :doc:`/conf/na/2016/news/schedule-welcome-wagon-events`
- :doc:`/conf/na/2016/news/welcome`
- :doc:`/conf/na/2016/news/thanks-for-coming`

Presentations
-------------

{% for talk in na_2016_speakers %}

.. raw:: html

    {% for speaker in talk.speakers %}
    <a name="speaker-{{ speaker.slug }}"></a>
    {% endfor %}
    <div class="row row-speaker">
      <div class="col-md-2 col-md-offset-1 col-sm-2 col-sm-offset-1">
        {% for speaker in talk.speakers %}
        <img class="speaker-image" src="/_static/img/speakers/{{ speaker.img_file }}" />
        {% endfor %}
      </div>
      <div class="col-md-8 col-sm-8">
        <h3>
          {% for speaker in talk.speakers %}
          {{ speaker.name|indent(10) }}
          <span class="speaker-details">
          {% if speaker.twitter %}
          <a href="https://twitter.com/{{ speaker.twitter }}">@{{ speaker.twitter }}</a>
          {% endif %}
          </span>
          {% endfor %}
        </h3>
        <h4>
        <a href="/conf/na/2016/speakers/#speaker-{{ talk.speakers.0.slug}}">
        {{ talk.title }}
        </a>
        </h4>
      </div>
    </div>

{% endfor %}

.. role:: strike
    :class: strike

Tickets
-------

Tickets are sold out.
Thanks to everyone who bought them!

Ticket includes:

* Breakfast, Snacks, and Lunch on both Conference Days
* Reception and Party that will have light snacks, and free drinks.
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue.

Corporate Tickets
-----------------

Purchase this ticket if a company is paying for your attendance.
Companies interested in sponsorship can also receive tickets to the
conference with a sponsorship package.

* :strike:`$300 Corporate Early Bird` - **Sold Out**
* $350 Corporate

Independent Tickets
-------------------

Purchase this ticket if you are paying for yourself, work at a
non-profit, or at a company with less than 10 employees.

* :strike:`$150 Independent Early Bird` - **Sold Out**
* $200 Independent

Student or Unemployed
---------------------

Purchase this ticket if you are currently enrolled as a student, or
don't currently have a source of income.

* $75 Student or Unemployed Tickets

Financial Assistance
--------------------

If you can't afford these prices and still wish to attend, please email
us at portland@writethedocs.org. Being a community event that keeps prices low,
we can only offer discounted ticket prices,
and not travel or hotel assistance.

Lodging and Travel
------------------

We don't have an official conference hotel, but there are many options
for staying in downtown Portland, and the city offers many methods of
getting around.

-  `Hotels near the conference
   venue </conf/na/2016/visiting/#where-to-stay>`__
-  `Transportation options around the
   city </conf/na/2016/visiting/#how-to-get-around>`__

Schedule
--------

Write the Docs is more than a conference. Each year we organize a wide
bunch of events so that people can meet, collaborate, and learn
from each other.

This year, we have events planned all day on Sunday, the day before the
conference, and our annual hike will take
place on Saturday afternoon. Our Sunday events include our Writing
Day documentation sprints during the
day, and our conference reception in the evening.

The main conference event will be held May 23-24th, during the day. We
will be holding unconference sessions
after lunch both days of the events, downstairs from the main stage, in
Lola's Room. Everyone is welcome and encouraged to join in on the unconference.

You can see the full schedule on the :doc:`/conf/na/2016/schedule` page.

.. raw:: html

    <div class="row row-images">
      <div class="col-md-6 col-sm-6 col-sm-offset-0 col-xs-8 col-xs-offset-2">
        <a href="https://www.flickr.com/photos/writethedocs/14151984286/in/album-72157644692192083/">
    <img src="/_static/img/2016/na/tshirt.jpg" alt="Attendees grabbing conference's t-shirts">
        </a>
      </div>
      <div class="col-md-6 col-sm-6 col-sm-offset-0 col-xs-8 col-xs-offset-2">
        <a href="https://www.flickr.com/photos/writethedocs/14174678071/in/album-72157644692192083/">
    <img src="/_static/img/2016/na/laptop.jpg" alt="A group of people talking together">
        </a>
      </div>
    </div>

Sponsors
--------

We are seeking corporate partners to help us create the best conference
possible. Contact us at sponsorship@writethedocs.org for more
information on sponsoring Write the Docs.

This year's conference is graciously brought to you by the following
companies:

.. raw:: html

    <div class="row row-sponsors">
      <!-- Patron -->
      <div class="col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
        <a href="http://google.com/">
        <img src="/_static/img/2016/sponsors/google.png" width=400/></a>
      </div>

      <!-- Editor -->
      <div class="col-md-8 col-sm-4">
        <a href="https://github.com">
        <img src="/_static/img/2016/sponsors/github.png" width=200/></a>
      </div>
      <div class="col-md-8 col-sm-4">
        <a href="https://developer.mozilla.org/">
        <img src="/_static/img/2016/sponsors/mdn.png" width=200/></a>
      </div>
      <div class="col-md-8 col-sm-4">
        <a href="https://twilio.com">
        <img src="/_static/img/2016/sponsors/twilio.png" width=200/></a>
      </div>
      <div class="col-md-8 col-sm-4">
        <a href="https://opennews.org">
        <img src="/_static/img/2016/sponsors/opennews.png" width=200/></a>
      </div>
   </div>
   <br>
   <br>
   <br>

Write the Docs is also helped out by companies that give their employees time to work on the conference.
Write the Docs is produced by:

.. raw:: html

    <div class="row row-sponsors">
      <!-- Patron -->
      <div class="col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
        <a href="https://readthedocs.com">
        <img src="/_static/img/2016/sponsors/read-the-docs.png" width=400/></a>
      </div>
   </div>


Organizers
----------

Write the Docs NA is put on by the following lovely group of folks:

-  `Kelly O'Brien <https://twitter.com/OBrienEditorial>`_
-  `Jennifer Rondeau <https://twitter.com/bradamante>`_
-  `Eric Holscher <https://twitter.com/ericholscher>`_
-  `Adrienne Lowe <https://twitter.com/adriennefriend>`_
-  `Becky Yoose <https://twitter.com/yo_bj>`_


Write-Ups From the Community
----------------------------

-  `6 Favorite Write the Docs 2016 Conference Takeaways <https://kirstengantenbein.com/2016/05/29/6-favorite-write-the-docs-2016-conference-takeaways/>`_ by Kirsten Gantenbein‏
-  `Move fast and document things <https://www.interana.com/blog/move-fast-and-document-things/>`_ by Neal Kaplan
-  `Write the Docs 2016 <https://www.davidbaumgold.com/blog/2016/05/wtd-na-2016/>`_ by David Baumgold
-  `Write the Docs 2016 Recap <https://circleci.com/blog/write-the-docs-2016-recap/>`_ by Ricardo N Feliciano
-  `Write the Docs NA 2016 wrapup <https://ffeathers.wordpress.com/2016/05/25/write-the-docs-na-2016-wrapup/>`_ by Sarah Maddox


Contact Us
----------

If you wish to receive more information as it becomes available,
follow us on Twitter at `@writethedocs <https://twitter.com/writethedocs>`_,
email us at portland@writethedocs.org,
or sign up for our mailing list:

{% include "na-mailchimp.rst" %}

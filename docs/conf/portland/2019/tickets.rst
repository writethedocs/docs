:template: {{year}}/generic.html

Tickets
=======

Ticket Information
------------------

{% if flagticketsonsale %}

**Tickets are on sale now!**

{% elif flaghasschedule %}

Ticket status
~~~~~~~~~~~~~

**Tickets are sold out!**

We have a `waiting list <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`_ where you can register in case of cancellations, but we usually don't have a high rate of cancellations so please do not book travel unless you have a ticket.

{% else %}

**Tickets will be available in {{ date.tickets_live }}.**

{% endif %}

Ticket details
~~~~~~~~~~~~~~

Each ticket includes:

* Entry to all conference events and activities
* Breakfast, snacks, and lunch on all event days (Sunday-Tuesday)
* Welcome Reception and Social Event with light snacks and drinks
* Wi-Fi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

Refund Policy
-------------

Refunds will be offered with a 10% processing fee until 2 weeks before the conference.
We can't do refunds after that date because all of our catering, badge, & swag orders will have been placed.

Ticket Types
------------


{% if flaghasshirts %}

.. class:: ticket

**Official Conference Shirts**
------------------------------------

Inspired by our friends at DjangoCon US, we decided to shake things up and sell shirts separately, so you can buy exactly the fit and size that you want! You can now visit our Write the Docs Portland 2019 Pop-Up Shop and order this year’s branded shirt. The campaign will run until **April 15th** to allow for timely delivery of your shirts ahead of the conference.

* Buy Portland 2019 Shirt

{% endif %}

.. class:: ticket

**Corporate Tickets** *{{tickets.corporate.price}}*
--------------------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

* `Buy Corporate Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets** *{{tickets.independent.price}}*
--------------------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with fewer than 10 employees.

{% if flagticketsonsale %}

* `Buy Independent Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Student or Unemployed Tickets** *{{tickets.student.price}}*
--------------------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

* `Buy Student or Unemployed Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**None of the above**
---------------------

If you can't afford these prices and still wish to attend, please email us at `{{shortcode}}@writethedocs.org <mailto:{{shortcode}}@writethedocs.org>`_. Being a community event that keeps prices low, we can only offer discounted ticket prices, and not travel or hotel assistance.


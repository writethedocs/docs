:template: {{year}}/generic.html
:banner: _static/2018/assets/headers/venue.png

Tickets
=======

{% if flagticketsonsale %}

**Tickets are on sale now!**

{% endif %}

Each ticket includes:

* Entry to all conference events and activities
* Tea, coffee and snacks
* Entry to social event with light snacks and drinks
* Wi-fi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

.. class:: ticket

**Corporate Tickets** *{{tickets.corporate.price}}*
------------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

* `Buy Corporate Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets** *{{tickets.independent.price}}*
------------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with less than 10 employees.

{% if flagticketsonsale %}

* `Buy Independent Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}

.. class:: ticket

**Student or Unemployed Tickets** *{{tickets.student.price}}*
----------------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

* `Buy Student or Unemployed Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

{% endif %}
.. class:: ticket

**None of the above**
---------------------

If you can't afford these prices and still wish to attend, please email us at `{{shortcode}}@writethedocs.org <mailto:{{shortcode}}@writethedocs.org>`_. Being a community event that keeps prices low, we can only offer discounted ticket prices, and not travel or hotel assistance.

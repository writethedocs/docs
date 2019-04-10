:template: {{year}}/generic.html
:banner: _static/2018/assets/headers/venue.png

Tickets
=======

{% if flagticketsonsale %}

**Tickets are on sale now!**

{% else %}

**Tickets are sold out!**

{% endif %}

Each ticket includes:

* Entry to all conference events and activities
* Breakfast, snacks, and lunch on all conference days
* Welcome Reception and Social Event with light snacks and free drinks
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue

{% if flaghasshirts %}

.. class:: ticket

**Official Conference Shirts**
------------------------------------

Inspired by our friends at DjangoCon US, we decided to shake things up and sell shirts separately, so you can buy exactly the fit and size that you want! You can now visit our `Write the Docs Portland 2018 Pop-Up Shop <https://teespring.com/wtd-portland-2018-shirts>`_ and order this year’s branded shirt. The campaign will run until **April 15th** to allow for timely delivery of your shirts ahead of the conference.

* `Buy Portland 2018 Shirt <https://teespring.com/wtd-portland-2018-shirts>`__

{% endif %}

.. class:: ticket

**Community Sponsorship Tickets** *{{tickets.community.price}}*
--------------------------------------------------

Support the growing community! Get a logo on our website, as well as a ticket.
This option is great for startups, open-source projects, and small non-profit organizations.
Limit 1 per organization.
If you are a larger company or organization, please contact us at sponsorship@writethedocs.org to arrange for sponsorship.

{% if flagticketsonsale %}

* `Buy Community Sponsorship Ticket <https://ti.to/writethedocs/write-the-docs-{{shortcode}}-{{year}}>`__

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

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with less than 10 employees.

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

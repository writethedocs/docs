:template: 2017/na-content.html

{% include "conf/events/writing-day.rst" %}


Logistics
^^^^^^^^^

Please bring a computer or some other mechanism with which to create written words.

We'll be creating and editing content,
so make sure that you have the tools you need to contribute.

- Date & Time: **Sunday, May 14th, 9am-6pm**,
  with the conference opening reception in the same space until 9.
- Location: **Crystal Ballroom, 1332 W Burnside St**. We will be in the main ballroom.
- Projects:

  + :ref:`writewrite`
  + :ref:`kubernetes`
  + :ref:`openstack`
  + :ref:`media`
  + anything else you fancy

Writing Day Schedule
^^^^^^^^^^^^^^^^^^^^

.. datatemplate::
   :source: /_data/na-2017-writing-day.yaml
   :template: include/schedule.rst

Documenting a new project?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Check out our `beginners guide <http://www.writethedocs.org/guide/writing/beginners-guide-to-docs/>`_ to writing documentation.
This should help you get started,
and give you some ideas for how you can contribute to a project that you love.

.. _writewrite:

Write Write the Docs on Writing Day
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This year we're also running a session where you can help improve your favorite website. Yup, you can brainstorm improvements, write helpful content and posts, or just magically improve `Write the Docs <http://www.writethedocs.org>`_.

If you're writing text to add to the website, ideally you'll already be familiar with GitHub and writing in plain text (markdown or restructured text), but we'll be there to help out if you're not.

If you'd rather brainstorm a content reorganization in Google Docs, improve our python scripts or our jinja templates we've got plenty to do there as well.

Here are a few things we'll be working on on writing day, reach out to `@plaindocs <https://twitter.com/plaindocs>`_ or `@meker <https://twitter.com/meker>`_ if you have any questions or more suggestions.

Brainstorm user oriented architecture
=======================================

The website is currently organised around meetups, conferences, guides, etc – find ways to introduce user-oriented labels considering audience. Who is coming to the site, why? What are the goals of the site?

- Learn about docs
- Get involved with the community
- Attend conference
- Submit a conference proposal
- Find a video of a talk that I saw

Improve navigation
===================

Let's discuss information architecture -- can we organize the content better? Provide better navigation?

Write articles for the newsletter
====================================

Summarize content from the Slack channel for the `newsletter </blog/newsletter-may-2017/#looking-ahead>`_.

Help develop the Documentation Guide
===========================================

Help reorganize the guide content, or write and edit topics. Check out :doc:`/guide/index/` ahead of time and bring your ideas to the table!"

Fix website issues
===================

We have a list of `issues on GitHub <https://github.com/writethedocs/www/issues?q=is%3Aissue+is%3Aopen+label%3Awritingday>`_ tagged as `writingday` that includes things like

- fix broken links (we have a lot of these)
- improve the meetup pages
- make a better video archive
- add list of conference write ups for past conferences

.. _kubernetes:

Kubernetes
^^^^^^^^^^^^

If you're looking to contribute to open source documentation on Github during
Writing Day, you'll have the opportunity to edit content for Kubernetes.
Kubernetes is an open source system that manages containerized applications
across different infrastructures.

The Kubernetes doc folks are looking for help to edit content, get it into
templates, and verify that it conforms to their new site architecture. No
previous product experience is necessary to help out, and they pay in swag,
gracious thanks, and enthusiastic high-fives. Docs are located at `Kubernetes.io
<https://kubernetes.io/docs/home/>`_ and they're pulled directly from `Github
<https://github.com/kubernetes/kubernetes.github.io>`_.

`Detailed instructions <https://docs.google.com/document/d/18oSE-QV7viiH75N-0Qb6LuHI-PwgiN-DdihHMeo8sts/edit>`_

.. _openstack:

OpenStack
^^^^^^^^^

It's great to learn about open source contribution in a friendly, welcoming
environment like OpenStack. OpenStack offers a collection of projects for
cloud services such as compute, storage, and networks. Yes, it's large, but we
have some maps for contributors who like to work with and build clouds.

OpenStack documentation tools, tests, and processes are the same as the Python code processes for all projects. The source is in `RST`_ and the docs build
with Sphinx using scripts run in a virtual environment with the
`tox command line tool`_. The source control system is git, and the review
system is `gerrit`_. The source files are in the project repos and a docs-only
repo, `openstack-manuals`_. The documentation sites are:

- `docs.openstack.org <https://docs.openstack.org>`_
- `developer.openstack.org <https://developer.openstack.org>`_

You can find all the instructions for contributing to documentation in the
`OpenStack Docs Contributor Guide`_, including a comprehensive `style guide`_
and a quick start guide for `first timers`_. Recently the team members added a
section about contributors who speak `English as a second language`_. There's
also a comprehensive, collaborative set of `translation tools`_.

The bug tracking system is in Launchpad. For example, go to the `bug tracker`_
for the openstack-manuals project, and search for doc bugs that are tagged with
`low-hanging-fruit` and also unassigned.

There are `REST API docs`_ with specific contributor information, administrator
docs, user docs, a variety of developer docs, and tools upon which to work.
With a Facebook login (sorry, yes, we want to improve that gated access), you
can try using an OpenStack cloud at https://trystack.org. Go see what you can
learn about collaborating on a large set of open source cloud projects.

.. _RST: http://www.sphinx-doc.org/en/stable/rest.html
.. _tox command line tool: https://tox.readthedocs.io/en/latest/
.. _gerrit: https://review.openstack.org
.. _openstack-manuals : https://github.com/openstack/openstack-manuals
.. _OpenStack Docs Contributor Guide: https://docs.openstack.org/doc-contrib-guide/
.. _style guide: https://docs.openstack.org/doc-contrib-guide/writing-style.html
.. _First timers: https://docs.openstack.org/doc-contrib-guide/quickstart/first-timers.html#setting-up-for-contribution
.. _English as a second language: https://docs.openstack.org/doc-contrib-guide/non-native-english-speakers.html
.. _translation tools: https://wiki.openstack.org/wiki/I18n/Tools
.. _bug tracker: https://bugs.launchpad.net/openstack-manuals/+bugs
.. _REST API docs: https://docs.openstack.org/doc-contrib-guide/api-guides.html

.. _media:

MediaWiki
^^^^^^^^^^^

Team up with other volunteer tech writers and contribute to the documentation
for `MediaWiki <http://mediawiki.org/>`_, the open source software powering
Wikipedia . We are looking for help with various types of tasks such as
improving the technical documentation of articles, re-organizing content,
verifying documentation, and writing tutorials on how to use or install a
service. If you're interested, you can prepare ahead of the writing day:

- Create a MediaWiki account.
- Read this `list of available tasks <https://www.mediawiki.org/wiki/Write_the_Docs_San_Francisco_Meetup_May_2017>`_ we're planning to showcase at the writing day.
- Watch this presentation from `Write the Docs SF <https://youtu.be/ixU_3Gjkya4?t=3m21s>`_ [3:15 - 34:17]

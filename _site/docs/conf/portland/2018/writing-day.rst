:template: {{year}}/generic.html
:banner: _static/2018/assets/headers/writing-day.png

Writing Day
===========

{% include "conf/events/writing-day.rst" %}

Schedule
--------

- Date & Time: **Sunday, May 6th, 9am-5pm**,
  with the conference opening reception in the same space until 9.
- Location: **Crystal Ballroom, 1332 W Burnside St**. We will be in the main ballroom.

Projects
--------

.. contents::
   :local:
   :depth: 1
   :backlinks: none


Kubernetes Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

If you’re looking to contribute to open source documentation on GitHub, consider helping improve the Kubernetes docs. Issues and projects this year include improving the user journeys that provide the landing page for the docs, helping develop a custom Kubernetes dictionary for common spellcheckers, and more.

Kubernetes is an open source system that manages containerized applications across different infrastructures. No previous product experience is needed to help with the docs. Docs are published at `kubernetes.io <https://kubernetes.io/docs/home/>`_ and they're pulled directly from `Github
<https://github.com/kubernetes/website>`_. So you’ll need a GitHub account, and some familiarity with Markdown. You can also take a look at our contributor guidelines, and if you haven’t contributed before, it’ll save time if you sign the contributor license agreement before you arrive at Writing Day.

`Detailed information, including how to sign the CLA <https://docs.google.com/document/d/1-mlmb9yHgdLsTqR8t52MegAWlUgXsZeko247hUMJaVU/edit?usp=sharing>`_

And if you have questions before Writing Day, feel free to ask in the #kubernetes channel in the Write the Docs Slack.


CockroachDB Docs
~~~~~~~~~~~~~~~~

`CockroachDB <https://www.cockroachlabs.com>`_ is a distributed SQL database built on a transactional and strongly-consistent key-value store. Here’s a quick overview video:

https://www.youtube.com/watch?v=VgXiMcbGwzQ

Following are a few ways you can contribute to the CockroachDB docs:

Improve our current docs
^^^^^^^^^^^^^^^^^^^^^^^^

If you love fiddling around with a new product, you can:

- User-test our `Getting Started docs <https://github.com/cockroachdb/docs/issues/3028>`_ or `Production docs <https://github.com/cockroachdb/docs/issues/3027>`_ and give us feedback about clarity, correctness, and ease-of-use
- Improve existing docs by `adding missing details <https://github.com/cockroachdb/docs/issues?q=is%3Aopen+is%3Aissue+label%3Awtd-writing-day+label%3Aincorrect-info>`_ or `correcting errors <https://github.com/cockroachdb/docs/issues?q=is%3Aopen+is%3Aissue+label%3Awtd-writing-day+label%3Aincorrect-info>`_
- Make our code samples more user-friendly by `adding copy-to-clipboard functionality <https://github.com/cockroachdb/docs/issues?q=is%3Aopen+is%3Aissue+label%3Awtd-writing-day+label%3Aenhancement>`_

Fill gaps in our docs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you’d like to dig in deeper, we’re missing docs on a handful of important features. `You can help us fill these gaps! <https://github.com/cockroachdb/docs/issues?q=is%3Aopen+is%3Aissue+label%3Awtd-writing-day+label%3Aproduct>`__

Help us improve our processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- `Test and provide feedback on our Docs contribution process <https://github.com/cockroachdb/docs/issues/3029>`_
- `Share best practices for using tables in Markdown <https://github.com/cockroachdb/docs/issues/3030>`_

Feel free to go through the full list of GitHub issues labeled `wtd-writing-day <https://github.com/cockroachdb/docs/labels/wtd-writing-day>`_ and claim the ones you want to work on.

And of course, we (`@jseldess` and `@amruta` on the Write the Docs Slack channel) will be available throughout the day to help out. Also feel free to reach out to us if you have questions or suggestions in the interim. See you on Writing Day!


Netlify CMS
~~~~~~~~~~~

`Netlify CMS <https://www.netlifycms.org/>`_ is an open source CMS for static site generators, created by the folks at `Netlify <https://www.netlify.com/>`_. You can add it to your site's Git repository to enable rich-text content editing in a `neat UI <https://cms-demo.netlify.com/>`_ with side-by-side realtime preview. Git functions like pull requests and commits are abstracted away behind UI buttons for publishing and creating drafts.

We're a really friendly and active community, happy to answer questions in `Gitter chat <https://gitter.im/netlify/netlifyCMS>`_ or even Write the Docs Slack. (Try #static-site-generator or ping @verythorough!) We uphold the Contributor Covenant `Code of Conduct <https://github.com/netlify/netlify-cms/blob/master/CODE_OF_CONDUCT.md>`_, and we work hard to make sure all contributors feel welcome, supported, and `recognized <https://github.com/netlify/netlify-cms#contributors>`_.

Documentation plays a key role in Netlify CMS—check out our first major foray into **documentation-driven development** with PR `#1311 <https://github.com/netlify/netlify-cms/pull/1311>`_, and feel free to add your thoughts!

If contributing to Netlify CMS interests you, here are some possible paths to getting started:

* Use a `starter template <https://www.netlifycms.org/docs/start-with-a-template/>`_ to get a site up in minutes, then take what you learn as you try the UI, and consider helping write a `user guide for content editors <https://github.com/netlify/netlify-cms/issues/1340/>`_.
* Try the `tutorial <https://www.netlifycms.org/docs/add-to-your-site/>`_ for adding Netlify CMS to your existing static site, then help improve the experience for others by filing an issue or suggest a change directly by clicking **Edit this page**.
* Check the issues labeled  `Area: docs <https://github.com/netlify/netlify-cms/issues?q=is%3Aissue+is%3Aopen+label%3A%22area%3A+docs%22>`_ to find out where we're looking for docs-related help. Some issues involve coding as well as writing, if that strikes your fancy.

Jessica (@verythorough in Slack) and Irene will be arriving for Writing Day after lunch, and will be happy to answer questions and collaborate. If you want to get started in the morning but find yourself stuck, feel free to ask in `Gitter chat <https://gitter.im/netlify/netlifyCMS>`_. We look forward to meeting you!


Write the Docs
~~~~~~~~~~~~~~

This year we're also running a session where you can help improve your favorite website.
Yup, you can brainstorm on improvements, write helpful content and posts, or just magically improve `Write the Docs <http://www.writethedocs.org>`_.

If you're writing text to add to the website, ideally you'll already be familiar with GitHub and writing in plain text (markdown or restructured text), but we'll be there to help out if you're not.

If you'd rather brainstorm on content reorganization in Google Docs, improve our Python scripts or our jinja templates, we've got plenty to do there as well.

Here are a few things we'll be working on on writing day, reach out to `@plaindocs <https://twitter.com/plaindocs>`_ if you have any questions or more
suggestions.

Brainstorm user-oriented architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The website is currently organised around meetups, conferences, guides, etc – find ways to introduce user-oriented labels considering audience. Who is coming to the site, why? What are the goals of the site?

- Learn about docs
- Get involved with the community
- Attend conference
- Submit a conference proposal
- Find a video of a talk that I saw

Improve navigation
^^^^^^^^^^^^^^^^^^

Let's discuss information architecture -- can we organize the content better? Provide better navigation?

Write articles for the newsletter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Summarize content from the Slack channel for the `newsletter </blog/newsletter-may-2018/#looking-ahead>`_.

Help develop the Documentation Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Help reorganize the guide content, or write and edit topics. Check out :doc:`/guide/index/` ahead of time and bring your ideas to the table!

Fix website issues
^^^^^^^^^^^^^^^^^^

We have a list of `issues on GitHub <https://github.com/writethedocs/www/issues?q=is%3Aissue+is%3Aopen+label%3Awritingday>`_
tagged as `writingday` that includes things like:

- fix broken links (we have a lot of these)
- improve the meetup pages
- make a better video archive
- add list of conference write ups for past conferences

The Lone Writers Guide
~~~~~~~~~~~~~~~~~~~~~~

If you're the new sole writer at a company and you've inherited a mess, what should you do first? What decisions (and trade offs) are the most important to address right away? What are the milestones you would try to hit in the first 30, 60, and 90 days?

We started a guide for people who are thrown into the deep end, to give them a plan for the first 90 days. It already includes pages about things like identifying your stakeholders, choosing the right tools, and getting everyone to write. You can expand on these topics, or create a new one.

Get started at our GitHub repo:
https://github.com/San-Francisco-Write-The-Docs/lone-writers-guide

The Lone Writers Guide was started by Write the Docs San Francisco Bay Area; when complete, it will be available on the web.


Your project here
~~~~~~~~~~~~~~~~~

Send us a pull request or an email talking about what you want to work on!

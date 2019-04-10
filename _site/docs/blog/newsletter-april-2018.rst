.. post:: April 9, 2018
   :tags: newsletter


########################################
Write the Docs Newsletter – April 2018
########################################

Hello hello!
Kelly O. here, with a ton of exciting community stuff to share with you this month!
There's a lot to cover, so I'll cut right to the chase!

First, we're coming up on the Portland conference here in just four weeks (!?), and we're starting to get pretty stoked.
Tickets are fully sold out, but if you're itching for a conference fix, now's a great time to look ahead to Prague in September... especially if you'd like to speak!
The Prague call for proposals is open until **midnight, Tuesday May 15th**, and you can read more and submit your talk idea `here on our CFP page <http://www.writethedocs.org/conf/prague/2018/cfp/>`_.

We also have a new virtual resource to announce – the `Write the Docs Video Archive <http://www.writethedocs.org/videos/>`_!
You can now easily browse all of the videos from every North American and European conference, going back over the last three years.
There are hours of excellent talks in there, on almost any docs-topic you can think of.
Dive in!

In case you missed it, there's a new episode of the Write the Docs Podcast up: `Episode 14 – Humanizing you documentation <http://bit.ly/wtdpodcast_episode_14_humanizing_docs>`_.
Hosts Tom Johnson and Chris Ward talk to Carolyn Stransky, a journalist and JavaScript developer living in Berlin, about how to write with transparency, empathy, sensitivity, clarity, and more, to make your docs as human as possible.

In addition to all that, we had a handful of intriguing discussions crop up across Slack this month.
Read on for those, as well as some featured listings from the `Job Board <http://jobs.writethedocs.org/>`_, news about upcoming community meetups, and a `discount link <https://ti.to/supportdriven/sd-expo-2018/discount/wtd>`_ for anyone interested in attending the `Support Driven Expo <https://www.supportdriven.com/expo/>`_ this June!

Whew!
Big month!

----------------------------------------------------
Evolving your developer docs as your product matures
----------------------------------------------------

A question came up this month about the best approach for hosting the different parts of a public SDK – docs, examples, reference apps, and more.
The heart of the original poster's question had to do with evolving their documentation approach as the product matured.
Developers began to contribute samples and reference apps, and it started to become apparent that the developer resources might need their own home and processes separate from the user and admin content.

The community came up with a handful of points that a good solution would need to address:

* A plan for how developers will be able to update and maintain their samples from release to release.
* Options for auto-generating reference documentation for the APIs, if possible.
* And if auto-generation isn't an option, a way to communicate changes in the APIs to developers so they can document them.

Turns out this is a situation that lots of others had dealt with, and the consensus was strong: testing is key.
If you want to maintain up-to-date samples, it's well worth putting in the time to build some kind of testing that runs the latest version of the product and compares the relevant areas of code to the samples in your documentation.
Granted, these tests can be difficult to implement, especially if you're working with pre-existing, manually generated content, but even small steps are steps in the right direction.

*Want to dig deeper into docs testing? We've got just the channel for you:* `#doc-testing <https://writethedocs.slack.com/messages/doc-testing>`_

--------------------------------
Number formatting in data tables
--------------------------------

This month in #general, there was a quick but engaging discussion on conventions for formatting numbers in tables and specifically, how best to handle blank cells.
The community's answers yielded several helpful guidelines for number and table formatting:

- Avoid leaving cells blank unless the data for the cell is actually missing.
  Blank cells often indicate missing data.
- When you use a placeholder or no-value indicator, use a different alignment than you used for cells with values.
- If, however, you want to specifically draw attention cells that have no value, leaving them blank can be a good way to get them to stand out in larger tables.

The group also had some good examples of formatting options for no-value indicators:

- ``N/A``
- ``$0.00``
- ``null``
- a centered em dash
- or a dash length of your choice ;)

As always, context is key.
Consider your audience and publishing format when determining the formatting fate of your empty cells.

*Got a finicky formatting or mechanics question? The friendly folks in* `#general <https://writethedocs.slack.com/messages/general>`_ *can help you answer it.*

------------------------------------------
New tool to try out: automated screenshots
------------------------------------------

Although we don't often feature conversations about specific tools, there was one that popped up this month that we thought was worth a quick mention.
On what feels like a weekly basis, someone brings up the difficulty of keeping screenshots up to date.
So when someone pointed to `CronShot <https://www.npmjs.com/package/cronshot>`_, a Node module for programmatically scheduling and saving screenshots of web pages, we thought we'd share it around.
In addition, if you're so inclined (and comfortable with JavaScript), you can add the `Nick.js <https://www.npmjs.com/package/nickjs>`_ library in order to automate browser navigation altogether.

*Have another docs tool to share or chat about?* `#doctools <https://writethedocs.slack.com/messages/doctools>`_ *is the place for you.*

-----------------------------
Rebranding 'Technical Writer'
-----------------------------

The topic of job titles is a perennial one on the Write the Docs Slack.
In this month's iteration, there were some interesting reflections about how your title can impact the way your team thinks about your role.
For many of us, our contributions do not start and end with writing documentation.
We often work closely with product teams to contribute to the information architecture, content design, and product copy that shapes our users' experience.

In order to center those contributions, some folks have been shifting their job titles away from the more traditional 'Tech Writer' or 'Technical Author' and towards things like 'Product Content Strategist', 'UX/UI Writer', or 'Content Designer'.
Adopting titles like this can help clarify the way you work, the range of your expertise, and at what point in the cycle you should be involved (hint: from the beginning).
Even if you're not job-hunting at present, it might be worth revisiting your title in your current position to see if it can do more to reflect the realities of your role.

*Itching to jump in on the ever-evolving job titles discussion? Join in at* `#career-advice <https://writethedocs.slack.com/messages/career-advice>`_.

---------------------
Featured job postings
---------------------

`Senior Technical Author <https://jobs.writethedocs.org/job/58/senior-technical-author/>`_ – Full-time – Metaswitch – London, UK

`Technical Writer <https://jobs.writethedocs.org/job/52/technical-writer/>`__ – Full-time – Nexmo – London, UK (part-remote)

`Technical Writer <https://jobs.writethedocs.org/job/56/technical-writer/>`__ – Full-time – Elastic – Remote

*To apply for these jobs or to post a listing, visit the* `Write the Docs Job Board <https://jobs.writethedocs.org/>`_.

-------------------------
Upcoming community events
-------------------------

If you're looking for another docs-adjacent conference adventure this summer, check out `Support Driven Expo <https://www.supportdriven.com/expo/>`_, happening June 21-22 in Portland.
Some highlights include a docs talk by Emily Richardson from MailChimp, an ally skills workshop by Meg Brennan and Trisha Todman from Airbnb, and a workshop on negotiating by Diana Potter from Qwilr.
Use `this link <https://ti.to/supportdriven/sd-expo-2018/discount/wtd>`_ by April 30th to get **$75 off tickets**!

And if you need a community fix in the meantime, we've got a good handful of meetups coming up, as well!

April 11 – Herzliya, Israel – `What's Next? Second event for WTD Herzliya
<https://www.meetup.com/Write-The-Docs-Herzliya/events/248951748/>`_

April 11 – Austin, TX, USA - `ATX Write the Docs monthly meeting
<https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/246590115/>`_

April 12 – Berkeley, CA, USA – `(East Bay) Let's Talk About Best Practices
<https://www.meetup.com/Write-the-Docs-SF/events/249423979/>`_

April 19 – Denver, CO, USA – `UI Text: Simplicity is Difficult (PAID event co-hosted meetup with STCRMC) <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/248316008/>`_

May 2 – Australia – `The great Australian remote WTD meetup
<https://www.meetup.com/Write-the-Docs-Australia/events/248727427/>`_

.. post:: October 08, 2018
   :tags: newsletter


########################################
Write the Docs Newsletter – October 2018
########################################

Hi folks!

Kelly O. here, wishing you a happy October! I hope the change of season, whether it's fall or spring, is starting out well for everybody! Although nearly a month has passed, the good vibes from the Prague conference are still lingering (at least for me!). We were really proud and excited to see such a crowd turn out for our fifth European conference. As usual, we had an awesome batch of speakers, a bustling writing day, a vibrant unconf track, and just generally a great few days of getting to interact with the community in real life. If you missed out on the conference, you can catch up on the talk videos `on our YouTube channel <https://www.youtube.com/playlist?list=PLZAeFn6dfHplRZcYDQjST22bAVeeWML4d>`_.

Also, while every single one of our lightning talks this year was stellar (they're included in the playlist above), I would be remiss if I didn't call out what was one of the best moments of any Write the Docs conference I've been to. On Tuesday afternoon, a particularly intrepid group of attendees got up on stage and delivered a lightning talk in the form of a documentation-themed, a capella cover of Michael Jackson's 'Man in the Mirror'. I cried from laughing (and also, if I'm honest, from community feels). `Don't miss it. <https://youtu.be/3U48bgbccj0>`_

If you're dying to get in on a Write the Docs conference before the end of the year, you have one more chance! Our `Australian conference <http://www.writethedocs.org/conf/australia/2018/>`_ is coming up November 15-16 in Melbourne, and we would love to have you join us! Check out the `conference website <http://www.writethedocs.org/conf/australia/2018/>`_ to peruse the great line up of speakers and to buy your ticket!

Before we jump into stories, I just wanted to say – as this my last issue – thank you all so much for letting me take up space in your inboxes over the last couple of years! It's been a real pleasure. We have an excellent editor lined up to take the reins, but I'll let her introduce herself next issue. Rest assured, you're in great hands. ;)

Now, let's see what folks have been talking about this month!

-------------------------------------------------
To prompt, or not to prompt, that is the question
-------------------------------------------------
We had a great conversation emerge this month that is at once very narrow in scope – the whole thing revolves around just 1 or 2 characters – and broadly relevant to anyone writing docs that include code samples. The question at its heart: What's the best way to handle command prompts in code samples?

There's a surprising number of considerations to account for here. First, depending on your reader's environment, the prompt they're used to staring at might vary. Second, is it safe to assume that everyone will interpret a `$` or a `#` at the beginning of a line as a prompt and not as part of the command? (Probably not, was the feeling.) Third, if you're including code samples in your docs, you should also be optimizing them for copying and pasting. Including the prompt, while it does provide some context, means your reader has to manually remove it if they're copying and pasting into the command line.

The general consensus was to strike a balance by including the prompt character in the code samples, but preventing it from being copied and pasted with a little bit of CSS wizardry. You can see examples of how this looks in `Stripe's documentation <https://stripe.com/docs/building-extensions#use-api>`_. And `this blog post <https://evanhahn.com/how-to-disable-copy-paste-on-your-website/>`_ covers a handful of approaches to making text unselectable.

*If you're ever struggling with code sample styling in your own docs, pop into* `#documenting-apis <https://writethedocs.slack.com/messages/documenting-apis>`_

--------------------------------------------------------
Resources for planning out your information architecture
--------------------------------------------------------

Often, when tackling a new docs project, one of the biggest challenges can be figuring out how to approach your information architecture. This month, a user came to the WTD hivemind for help with this very problem. Many of the good documentarians of Slack jumped in to share an excellent array of IA and user testing resources:

* `Optimal Workshop <https://www.optimalworkshop.com>`_: suite of user research tools and services to help improve UX (folks specifically recommended their OptimalSort card sorting tool)
* `Complete Beginner’s Guide to Information Architecture <http://www.uxbooth.com/articles/complete-beginners-guide-to-information-architecture/>`_: UX Booth article
* `Nielsen Norman IA archive <https://www.nngroup.com/search/?q=information+architecture&searchSubmit=Search>`_: collection of articles from a UX research firm
* `How to Make Sense of Any Mess <http://abbytheia.com/makesense/>`_: book + website by Abby Covert, which includes a fun and thorough seven-step IA process
* `The Information Architecture Institute <https://www.iainstitute.org/what-is-ia>`_: brief overview with suggested books on IA

*If you can't get enough IA, check out the* `#infoarchitecture <https://writethedocs.slack.com/messages/infoarchitecture/>`_ *channel on Slack.*

------------------------------------
Task management tools for docs teams
------------------------------------

While we often discuss the tools we use to create our documentation, we also, from time to time, compare our other tool sets. This month, there was a hearty discussion on to topic of task management tools. In the age of "`Docs Like Code <https://www.docslikecode.com/>`_," many documentarians have also begun to adopt doing "Tasks Like Code". In other words, many docs teams use similar task management tools as developers, such as Jira or GitHub issues. This approach comes with its own benefits and challenges.

Benefits:

* Easier alignment with development & QA teams
* Built-in sprint planning tools

Challenges:

* Viewing all documentation-related tasks at once
* Developer tasks and documentation tasks not being one-to-one

Of course, there are those of us who use non-developer driven task management tools – either instead of or in addition to those tools – such as Trello, Asana, or Flow.

While we may use different tools, what matters in the end is that you utilize a task management tool (or tool set) that works for you!

*Have more thoughts about your toolset? Come share them in* `#doctools <https://writethedocs.slack.com/messages/doctools>`_ *or one of the many tool-specific channels we have on Slack.*

-----------------------
Show us your workflows!
-----------------------

Speaking of docs-as-code, and task management for that matter, there was another great discussion this month about how to map docs-as-code to software development workflows, with special reference to agile.

Most of the conversation revolved around how to map pull requests in Github to issue tracking in tools such as Jira. Several folks who track issues with Jira start with basic issue scoring based on estimated effort (or t-shirt sizing as some people call it), and then assign tickets on a per-sprint cycle. A couple of teams mentioned using a Fibonacci sequence to determine story points for relative effort (for more information, see `Atlassian's article on story points and agile estimation <https://www.atlassian.com/agile/project-management/estimation/>`_).

When a PR is started, Jira tickets then move through specified phases (in one case, "In Progress", "Tech Review", "Editorial Review", "Revision", "Ready to Release", "Published") that map to the phases of PR review.

Some teams work on the same schedule as dev and test -- that is, docs are completed during the same sprint. Other teams work on their own sprint schedules, add a week or two, or add an entire sprint cycle, to accommodate documentation lag. Sprint duration seems to range from 1-3 weeks.

Another common practice is for writers to be included in sprint planning meetings, so that the documentation and development of features are agreed on up front.

TL;DR: The closer the docs team gets to dev/code, the easier it seems to be to get a docs-as-code workflow to fall into place.

*Looking for more perspectives on how best to manage docs-as-code? We've got just the channel for you:* `#docs-as-code <https://writethedocs.slack.com/messages/docs-as-code>`_


---------------------
Featured job postings
---------------------

`Technical Writer <https://jobs.writethedocs.org/job/79/technical-writer/>`__
 Circonus, Inc., Full-time, remote

`Technical Writer – Robotics & Fulfillment Automation <https://jobs.writethedocs.org/job/76/technical-writer-robotics-fulfillment-automation/>`_
 6 River Systems, Short-term contract

`Director of Documentation <https://jobs.writethedocs.org/job/73/director-of-documentation/>`_
 MongoDB, Full-time

`Technical Writer <https://jobs.writethedocs.org/job/75/technical-writer/>`__
 Adyen, Full-time

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

-------------------------
Upcoming community events
-------------------------

October 09 – Ottawa, Alberta, Canada – `Structured Writing with Mark Baker <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyxnbmb/>`_

October 14 – Moscow, Russia – `Second Meetup <https://www.meetup.com/Write-the-Docs-Moscow/events/255163318/>`_

October 15 – Amsterdam, Netherlands – `To CMS or Not To CMS <https://www.meetup.com/Write-The-Docs-Amsterdam/events/255018670/>`_

October 15 – Salt Lake City, Utah, USA – `Accessibility Best Practices <https://www.meetup.com/Write-the-Docs-SLC/events/255125405/>`_

October 16 – Denver, Colorado, USA – `Hacktoberfest! Contribute to open source docs with pizza, beer, and prizes. <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/254987098/>`_

October 16 – Portland, Oregon, USA – `Joint Meetup with PSU & Support Driven: A Day in the Life <https://www.meetup.com/PDX-Support-Driven-Meetup/events/254842347/>`_

October 17 – Bradford, West Yorkshire, UK – `Hacktoberfest! Join us in a basement in Bradford! <https://www.meetup.com/Write-the-Docs-North/events/254988997/>`_

October 24 – Austin, Texas, USA – `Engineering/Developer-focused Content: Stories and Tools for Practitioners <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/255188139/>`_

October 25 – Remote (Australia time) – `Remote: Teaching engineers about content strategy <https://www.meetup.com/Write-the-Docs-Australia/events/253769102/>`_

November 6 – Ottawa, Alberta, Canada – `Monthly Ottawa Shopify Meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/254735859/>`_

**November 15 – Melbourne, Australia –** `Write the Docs Australia <http://www.writethedocs.org/conf/australia/2018/>`_

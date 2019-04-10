.. post:: March 14, 2018
   :tags: newsletter


########################################
Write the Docs Newsletter – March 2018
########################################

Hi y'all,

Kelly O. here, wishing you a very happy middle of the week! We had what I hope were the last throes of London winter last week, and I'm starting to get stoked for proper springtime. Not just because it means warmer temperatures for me, but also because it means Write the Docs Portland is getting closer and closer!

Look out for the full conference schedule to go live here soon, and make sure you pop over and `get your tickets <http://www.writethedocs.org/conf/portland/2018/tickets/>`_, as we'll likely sell out a few weeks before the event.

Here in the newsletter we've got a few good highlights from the last month of Slack conversations, our usual listing of Meetups happening this month, and also something new! We've recently launched the `Write the Docs Job Board <https://jobs.writethedocs.org/>`_. Any featured job listings on the board will also be included in one issue of the newsletter, as you'll see below. If your company is looking to fill a docs-related role, `register on the job board <https://jobs.writethedocs.org/>`_ and get the listing in front of the whole Write the Docs community!

In the meantime, on to the stories!

------------------------------------------------------------
Selling Yourself Short: Impostor Syndrome among Tech Writers
------------------------------------------------------------

This month, documentarians gathered around the #watercooler for a *legendary* discussion of impostor syndrome. Is there more impostor syndrome among technical writers than other tech professionals? Do writers shortchange themselves by saying things like “that's too technical for me" in work discussions? Does this contribute to a lack of respect for technical writers?

The consensus seemed to be a resounding "YES" to all three questions, and people offered many thoughtful ideas about why tech writers might experience impostor syndrome more keenly than most:

- Writing is an ‘endemic skill,’ meaning it’s practically universal, to at least a basic degree. That can make it challenging for people to recognize mastery because, on the surface, it's hard to distinguish mastery from what everyone else is doing.

- This underlying, "anyone can write" assumption gets particularly troublesome when used to justify the opinion that tech writers' chief value is that they free up engineers to write code.

- Technical writers’ knowledge gaps are front-and-center because they typically rely on subject matter experts to confirm what they write, as well as to provide feedback and corrections.

- Technical writing has historically been female-dominated, and even the most accomplished women sometimes rely on self-deprecating language to shield themselves from criticism.

- Technical writing roles don’t always have clear lines of specialization like other roles in the tech environment.

And that’s just a thin summary of this rich conversation! Although we don't usually share out the transcripts of the conversations we highlight, this one so clearly struck a chord that we thought we'd save – and anonymize – the whole thing, It's available in `this gist <https://gist.github.com/mjang/c49474fb7bbccbf06a9f47e7db096456>`_, if you want to read the whole discussion, including some ideas for impostor syndrome relief.

--------------------------------------------
Docs-as-code and its discontents: Versioning
--------------------------------------------

A particularly in-depth exploration of content versioning came up this month, which we thought was worth sharing. The question that sparked the conversation was specifically about how and whether folks versions their docs content separately from their overall documentation site. From there a discussion evolved around managing multiple versions of docs with a static site generator (SSG).

One approach that was suggested was `this Jekyll-based versioning solution <https://github.com/justwriteclick/versions-jekyll>`_ `This discussion  of the CoreOS docs <https://github.com/coreos/docs/issues/1082>`_ was also cited as a useful resource. Someone else suggested using git submodules to fetch different versions. But eventually most folks agreed: SSGs are not the optimal solution if you need to serve multiple versions of your content.

Suggestions for other solutions included:

* `Sphinx <http://www.sphinx-doc.org/en/master/>`_
* `DocFX <https://dotnet.github.io/docfx/>`_
* `Antora <https://antora.org/>`_ (an Asciidoctor toolchain)
* `MadCap Flare <https://www.madcapsoftware.com/products/flare/>`_


---------------------------------------
The whys and wherefores of tagging docs
---------------------------------------

A question this month about developing a meaningful tagging strategy produced both some useful ideas for strategy and the inevitable reminder that maintaining doc sets over time is challenging. Some folks wanted to provide tags to integrate with search, to provide more sophisticated results than exact string matching. Others saw tagging as little more than help for SEO. The original poster was looking for a system to check for consistency across doc sets. In other words, a way to correlate tags in metadata both within a single doc set and across multiple doc sets. Topics with shared tags could then be checked to make sure that information complements and doesn't compete or conflict across topics.

Most people who had tried tagging, though, agreed that it was difficult to maintain consistent tagging over time, even with small content sets. Automated tagging tends to produce too many tags. Controlled terminology seems like part of the answer, but it's also a huge project to maintain. Conclusion: you need a big compelling reason to undertake the long-term maintenance that a really useful tagging strategy requires. But in the right circumstances, it could help maintain clarity and consistency across multiple large doc sets.

---------------------
Featured job postings
---------------------

*To post or apply for a job*, visit the `Write the Docs job board <https://jobs.writethedocs.org/>`_.

* `Looking for a Documentarian in Berlin <https://jobs.writethedocs.org/job/50/looking-for-a-documentarian-in-berlin/>`_
   NetworkedAssets GmbH, Full-time

-------------------------
Upcoming community events
-------------------------

*New meetup* March 14 – Herzliya, Israel – `Kickoff meeting <https://www.meetup.com/Write-The-Docs-Herzliya/events/248189800/>`_

March 14 – Leeds, UK – `SEO Optimisation for a New Jekyll Install <https://www.meetup.com/Write-the-Docs-Leeds-Bradford/events/247184981/>`_

*New meetup* March 14 – Köln, Germany – `First meetup <https://www.meetup.com/WTD-Rhineland/events/248194015/>`_

March 15 – San Fransisco (East Bay), California, USA – `Hands-On Demo: How Do I Get into Open Source Projects? <https://www.meetup.com/Write-the-Docs-SF/events/248482881/>`_

March 18 – Novosibirsk, Siberia, Russia – `Confluence: От первых шагов до основного инструмента разработки документации <https://www.meetup.com/Write-the-Docs-Siberia/events/248458984/>`_

March 19 – Amsterdam, Netherlands – `March Meetup <https://www.meetup.com/Write-The-Docs-Amsterdam/events/248478377/>`_

March 19 – Berlin, Germany – `Mixing things up: Playing with form in technical writing <https://www.meetup.com/Write-The-Docs-Berlin/events/248465625/>`_

March 20 – Fredericton, New Brunswick, Canada – `March Lunch Meetup <https://www.meetup.com/Write-The-Docs-YFC-Fredericton/events/248507804/>`_

March 21 – Perth, Western Australia – `Moving from Word to the Web | Contributing to open source docs <https://www.meetup.com/Write-the-Docs-Australia/events/246830725/>`_

March 22 – Boise, Idaho, USA – `First meetup of 2018 <https://www.meetup.com/Write-the-Docs-Boise/events/246900941/>`_

March 27 – Boston, Massachusetts, USA – `Moving Docs to Sphinx <https://www.meetup.com/Write-the-Docs-BOS/events/247849315/>`_

March 29 – San Francisco, CA, USA – `Hack-A-Thon! Swimming in the deep water: a lone writer’s survival guide <https://www.meetup.com/Write-the-Docs-SF/events/248343809/>`_

April 5 – Los Angeles, CA, USA – `Meetup at Reaction Commerce in Santa Monica <https://www.meetup.com/Write-the-Docs-LA/events/248245722/>`_

April 9 – Karlsruhe, Germany – `Get Started with Docs as Code! <https://www.meetup.com/Write-the-Docs-Karlsruhe/events/247953294/>`_

April 11 – Austin, Texas, USA – `Monthly Meeting <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/246590115/>`_

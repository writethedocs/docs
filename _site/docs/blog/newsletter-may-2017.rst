.. post:: May 2, 2017
   :tags: newsletter, snippets, agile, accessibility, teaching

************************************
Write the Docs Newsletter - May 2017
************************************

Write the Docs Portland is in Less than 2 Weeks!
################################################

`Write the Docs Portland <http://www.writethedocs.org/conf/na/2017/>`_ is almost here! If you're coming, we're looking forward to welcoming you. If you can't make it, maybe `Write the Docs Prague <http://www.writethedocs.org/conf/eu/2017/>`_ in September? Just a thought...

The Portland conference is now **sold out**. Thanks to everyone who has registered, and we look forward to seeing you in Portland in a couple weeks!

Now, on to this month's newsletter, packed with gems we collected from the WTD Slack channel throughout the last 30-ish days.

------------------------------------------

Partner Highlight: Support Driven
#################################

We're trying something new this month,
where we're highlighting another community and conference that is doing great work.
We're happy to help promote `Support Driven <https://supportdriven.com/>`_,
a community built specifically around making customer support the best it can be.
They have a Slack channel,
newsletter,
`SUPCONF <http://supconf.supportdriven.com/>`_,
and now they're launching a new event workshop-focused event called `SDX <https://www.kickstarter.com/projects/supportdriven/sdx-take-your-support-skills-to-the-next-level/?utm_source=readthedocs>`_.

Here is a bit of info from them:

    Support lives and dies by it’s documentation. That’s why we’ll have several workshops on documentation at SDX - a new event in Portland that’s focused on learning and applying skills to advance your career. Check SDX out on `Kickstarter <https://www.kickstarter.com/projects/supportdriven/sdx-take-your-support-skills-to-the-next-level/?utm_source=writethedocs>`_.

------------------------------------------

Replaceable Content in Code Snippets
####################################

This month in WTD Slack, the question arose of how best to handle replaceable content in code snippets – in other words, any situation where we're prompting users to replace 'username' and 'password' with, y'know, their username and password. As usual, the discussion resulted in many creative solutions.

Some approaches were pretty lightweight and focused on adding clarity without introducing any coding behind the scenes:

* Choose a formatting convention for any example data, so the replaceable parts of the snippet are easy to pick out visually.
* Build up a small cast of fictional characters that you can write about throughout your docs. This lets you use a realistic name and password combo that your readers will have some context for.
* Expand on the basic 'username' and 'password' with more expressive strings like, 'example_username', 'your_username', 'replace_with_username', and so on

If you're looking for more dynamic solutions to the same problem, we've got some good options for you on that front as well:

* Automate the formatting for replaceable content by defining your own classes. DocBook, for example, will let you do this with the <replaceable> tag, and for Markdown, the same effect can be achieved with some help from `hercule <https://github.com/jamesramsay/hercule>`_ and bash scripts.
* If you're using fictional characters, you can take it a step further and create actual accounts for them in your system. Then, whenever your real-life users try to execute something with a fictional account's data, you can throw an error message to prompt them to swap in their actual details.
* You could also build in a prompt at the top of your docs asking for the relevant details, then use that info to generate personalized code samples that are ready to go, right out of the gate. With this option, there are some authentication and security concerns to address, but `Stripe's API docs <https://stripe.com/docs>`_ are a great example of how this might look.

------------------------------------------

The Challenges of Documentation in an Agile Environment
#######################################################

How can writers work with Agile dev teams? It's a perennial question that arose again this month and produced some excellent discussion. TL;DR: there are many models, and writers have to figure out what works best for their particular teams, processes, and products. Here's a round-up of the approaches that the WTD community came up with:

* With teams that perform regression testing and user acceptance testing (UAT) after a scheduled sprint, docs are sometimes developed during these post-sprint cycles. In this kind of workflow, docs and testing are often closely allied.

* Some writers are embedded on Agile dev teams, attend standups, and work on the regular sprint cycle, with stories assigned for doc; others work with parallel sprints, and devs/PMs serve as stakeholders.

* Some of the "embedded" writers document features at the start of development, but doc is not released until the feature is complete. Other writers find that features change too much during dev cycles for this approach to be worthwhile.

* Several folks who serve as lone writers wrestle with documenting multiple products or conditional doc sets addressed to different audiences. Some manage by getting developers more involved with helping produce doc content.

-----------------------------

Screen Readers and Accessibility
################################

A question about dividing a complicated data model into clickable sub-parts brought up an interesting secondary question: can screen readers parse .svg flowcharts?

According to one Slack member, probably not. She explained, screen readers tend to go top-to-bottom, left-to-right, reading all the words and links. They can also read alphabetically by first letter and hierarchical by H1, H2, H3. But more complex stuff (like reading SVG flowcharts) is probably beyond the capability of common screen readers. For complex flowcharts, consider offering a text explanation along with the image.

If you're interested in improving doc accessibility, check out @susanf's `list of accessibility resources <https://docs.google.com/document/d/19crjGz7lryYlvaIEzK8KTX_oMLAxzxx1AwGsjlsymgs/edit>`_. For an alt-text-centered guide, try Allen Flavell's article, `Use of ALT texts in IMGs <http://www.alanflavell.org.uk/alt/alt-text.html>`_.

To address the original question about dividing a large data model into clickable sub-parts, commenters mentioned quite a few SVG tools:

* `SVGOMG <https://jakearchibald.github.io/svgomg>`_
* `Snapsvg <http://snapsvg.io/>`_
* `Animatron <https://www.animatron.com/>`_
* `Inkscape <https://inkscape.org/>`_
* `Tom Sawyer <https://www.tomsawyer.com>`_
* `Linkurious <https://linkurio.us>`_
* `Neo4j <https://neo4j.com/>`_
* ...and good old `Visio <https://products.office.com/en-us/visio/flowchart-software>`_

------------------------------------------

Peer-to-Peer Teaching
#####################

When you're tasked with leading a workshop that will help your non-tech-writing colleagues write in clear, plain English, how can you help without embarrassing or alienating anyone? The discussion produced many thoughtful suggestions, including offering up some of your own writing for the group to dissect, but one idea stood out: peer-to-peer teaching using a whiteboard carousel. Here's how it works:

1. Place whiteboards or large flipcharts throughout the room.
2. Write a complex or unclear sentence at the top of each whiteboard.
3. Assign one group of participants per whiteboard.
4. Give the groups 5 minutes to write a simpler, easier-to-understand version of the sentence on the whiteboard.
5. After 5 minutes, rotate the groups and have them try the next sentence.

The groups will learn from reading each other's revisions as they rotate around to each whiteboard. Then, when all groups have tried every sentence, you can sit down together and talk about how each revision improves the complex sentence.

------------------------------------------

Last, but not Least
###################

Finally, you might be interested in this great series of tips and tricks for static sites by WTD Slack channel participant (and designer and writer at Balsamiq), @leonbarnard (with help from @annegentle):

`Part 1: Multiple product versions <http://docslikecode.com/articles/balsamiq-case-study-part-1/>`_

`Part 2: Animated GIFs Pause and Play <http://docslikecode.com/articles/balsamiq-case-study-part-2/>`_

`Part 3: Lists Get a Makeover <http://docslikecode.com/articles/balsamiq-case-study-part-3/>`_

------------------------------------------

Looking Ahead
#############

Did we mention that `Write the Docs Prague <http://www.writethedocs.org/conf/eu/2017/>`_ is coming down the pike? We just announced the `call for proposals <http://www.writethedocs.org/conf/eu/2017/news/announcing-cfp>`_. There are a few changes this year, so check it out and submit your proposal! You have until midnight CET on May 31.

If you see a discussion in the WTD Slack channels that you'd like to see highlighted here in the WTD newsletter, there's a new tool for that! We're now using the `Reacji Channeler <https://reacji-channeler.builtbyslack.com>`_. If you see a helpful or enjoyable discussion and think it would make a good item in the newsletter, just tag one of the messages with the `newsletter` emoji:

.. image:: news.png
    :width: 128px
    :align: left
    :height: 128px
    :alt: emoji for tagging newsletter suggestions

And with Slack magic, the message will be copied into a special channel of suggestions. We look forward to reading your suggestions!

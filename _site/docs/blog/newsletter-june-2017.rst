.. post:: June 5, 2017
   :tags: newsletter

**************************************
Write the Docs Newsletter - June 2017
**************************************

Write the Docs Portland 2017 Is History
#######################################

`Write the Docs Portland <http://www.writethedocs.org/conf/na/2017/>`_ was another sold-out success! Many thanks to everyone who attended, presented, hiked, shared, discussed, and made it another great event. `Videos <https://www.youtube.com/playlist?list=PLZAeFn6dfHpkBld-70TsOoYToM3CaTxRC>`_ of the presentations are now available! 

Now, it's time to gear up for `Write the Docs Prague <http://www.writethedocs.org/conf/eu/2017/>`_ in September!

This month's newsletter is the first one that relies on your `Reacji Channeler <https://reacji-channeler.builtbyslack.com>`_ suggestions! If you missed it last month, here's the gist: you can tag messages as suggestions for the newsletter with the *newsletter* emoji:

.. image:: news.png
    :alt: emoji for tagging newsletter suggestions


And thank you for all of your suggestions!

------------------------------------------

Writing for Write the Docs on Writing Day
#########################################

In Portland this year, for the first time ever, we ran a WTD session on writing day! In addition to learning a *lot* about how to run writing day sessions :), we worked with around a dozen helpful attendees to improve the WTD website in `various ways <https://github.com/writethedocs/www/issues?utf8=%E2%9C%93&q=label%3Awritingday%20>`_:

* Lots of progress toward a unified talk video archive
* Cleaned up many broken links and build warnings
* Improved the information on how to build the site on Windows
* Added links to write-ups of the 2016 Portland conference

Thanks to everyone who helped out--see you at the WTD table in Prague or back in Portland next year!

------------------------------------------

Getting a Grip on Static Site Generators
########################################

Static site generators have been a popular topic for some time, but there are a lot of moving parts that can be intimidating for new users. One Slack participant wondered how static site tools like Sphinx, Asciidoctor, restructured text (rST), Jekyll, and Markdown fit together--or don't. Here's the insight from our community:

* Sphinx, Jekyll, and Asciidoctor are parsing engines; rST, Markdown, and AsciiDoc are source file formats; and Python and Ruby are programming languages. So you can write in rST to publish with Sphinx, which is written in Python. Or, you can write in Markdown to publish in Jekyll, which is written in Ruby.
* In general, Sphinx parses rST, and Jekyll parses Markdown.
* There are also plugins out there to make Markdown work with Sphinx (like `recommonmark <http://recommonmark.readthedocs.io/en/latest/>`_), or to make rST work with GitBook.
* All static site generators generate output in HTML, along with some that generate PDF, ePub, HTML inside JSON, and other formats.

`This blog <https://davidwalsh.name/introduction-static-site-generators>`_ by David Walsh is a great primer on static site generators, especially if you're interested in the plusses and minuses. The `Docs as Code <http://docsascode.com/>`_ book and articles have a lot of great content around this as well.

------------------------------------------

Podcast Alert
#############

The latest `Write the Docs podcast <http://podcast.writethedocs.org/2017/04/30/episode-5-where-do-we-belong>`_ is available! It's all about where technical writers fit in different organizations. Check it out!

------------------------------------------

How Do YOU Crop Your Screenshots?
#################################

This month, a documentarian asked the group about the rules they follow for cropping and resizing large screenshots in documentation. Several people agreed that when you have multiple screenshots in a single document, they should be as close to the same size as possible. For example, reduce all screenshots by the same percentage, or apply a single fixed width (with the height set to "auto") to all screenshots. Another suggestion was using cropped versions of large screenshots that readers can click to open the original full-size image, perhaps in a pop-up window. Others resize to standardized sizes based on the image content, such as resizing all full-screen captures to 800px width.

Others suggested avoiding cropping altogether and using shading to highlight specific areas on screenshots. 

If you do end up cropping or resizing, here are a few more tips people mentioned:

* Avoid cropping out any on-screen context that readers might need to make sense of your screenshots.
* Use center-alignment for images to make and size differences less obvious.
* Try to make sure screenshots represent "stable" work (or at least balance the amount of work you spend on perfecting screenshots against the risk that the interface will change).

------------------------------------------

WTD Meetup Framework
####################

The Portland WTD meetup leader, @mikejang, attended the WTD meetup in Austin and walked away with ideas for how to hold a successful WTD meetup. Fortunately for us, Mike shared them in Slack! Here's what the Austin meetup leader, @meker, did to leave a great impression:

1) Greeted everyone who came
2) Introduced the meetup with slides
3) Gave participants a few seconds to talk about themselves and the theme
4) Used the help she had for working the equipment and making sure the speakers were ready
5) Introduced each of the panelists in a way that boosted their confidence

Great job, @meker!

------------------------------------------

The Enforcer: UI Style Guides Edition
#####################################

Finally this month, a member of our community asked for advice for enforcing the UI style guide. What do you do when product owners want to keep their 20-word descriptions, but you're supposed to be gently tipping it toward short and sweet? Here's what folks recommended:

* Compromise! For example, use short descriptors as the default. When the product team strongly feels like users will need a longer explanation, include a help symbol that users can click or mouse-over to display the longer explanation.
* Strengthen your case with ideas about `progressive disclosure <https://en.wikipedia.org/wiki/Progressive_disclosure>`_: basically, providing the least amount of information that will do the trick (in this case, help users do what they whatever it is they want to do). WTD documentarian Mike Jang also offered up `the slides from his OSCON 2017 presentation <http://slides.com/mike-1/osconjang>`_ about simplicity in UI text. And `here is a source <https://insidegovuk.blog.gov.uk/2014/08/04/sentence-length-why-25-words-is-our-limit/>`_ that cites studies about how long sentences detract from reader comprehension.
* Instead of enforcing word counts, think in terms of thoughts per phrase--limit it to 2 concepts per blob of UI text. One participant suggested following a guideline like "as short as possible, but no shorter."
* If you can't make progress against the pushback, you'll need to talk to the product director and explain what's going on. If product owners are resistant, all you may be able to do is make suggestions that they may or may not follow.

------------------------------------------

Onward
######

Proposals are in for `Write the Docs Prague <http://www.writethedocs.org/conf/eu/2017/>`_, and we expect to announce the schedule by mid-June. Stay tuned! 

The `WTD meetup groups <http://www.writethedocs.org/meetups/>`_ are planning some interesting events--maybe there's one near you. If not...consider `starting a WTD meetup <http://www.writethedocs.org/organizer-guide/meetups/starting/>`_ in your area!

**US**

* Portland, June 13: `The story of the Internet Archive or Wayback Machine <https://www.meetup.com/Write-The-Docs-PDX/events/239993859/>`_
* New York, June 20: `Notes and scribbles--what counts as documentation? <https://www.meetup.com/WriteTheDocsNYC/events/240583297/>`_
* Austin, June 21: `Tech conference roundup and discussion <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/239897479/>`_

**Europe**

* Berlin, June 14: `What your user guide can learn from a chocolate cake <https://www.meetup.com/Write-The-Docs-Berlin/events/240361283/>`_

**Australia**

* Brisbane, June 7: `Writing for localisation and From Word to Markdown <https://www.meetup.com/Write-the-Docs-Australia/events/239682736/>`_
* Sydney, June 22: `Interviewing techniques, Making docs more visual, and WTD Portland Wrap-up <https://www.meetup.com/Write-the-Docs-Australia/events/239444710/>`_
* Melbourne, June 29: `Experimental documentation and Storyboarding <https://www.meetup.com/Write-the-Docs-Australia/events/239719358/>`_


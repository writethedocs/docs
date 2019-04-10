.. post:: July 11, 2017
   :tags: newsletter

#####################################
Write the Docs Newsletter – July 2017
#####################################

Hi everybody!

Hope summer (or winter, for those of you south of the equator) is treating you well. It's Kelly O. here, back behind the editorial helm after taking a few months off (to move to London!). If you, like me, have been enjoying the newsletter these last few months, please direct your thanks and props to Hillary Fraley (@hillaryfraley on Slack). She was kind enough to look after the newsletter while I was caught up in the move, and she did an *awesome* job of it.

Also, speaking of amazing volunteers, we're looking to expand our little newsletter editorial team. If you already spend a lot of time on the Write the Docs Slack, and you want to help us tag insightful Slack conversations and turn them into mini-features, we'd be very interested in hearing from you! Drop me a message on Slack @kobrien042!

One last note before we dive in. As I've been slowly tuning back into Slack this month, and starting to look ahead to Write the Docs Prague, I've been reminded of how lucky we are to have such a lively, knowledgeable, collaborative community. So many of the conversations that go on every day resonate with or bring new perspective to my own work and experience, and I just wanted to take a minute to recognize how cool and valuable it is.

And what better way to recognize it than to hit some of the highlights from this past month of discussions? Let's do it!

****************************************
Keep your jokes out of my documentation!
****************************************

This month, we discussed a fresh angle on the perennial question of tone in technical documentation: Does humor ever belong in docs? What if a project stakeholder is pressuring you to add it? What if it's *really* funny? Can **anyone** report a good experience with humor in tech docs? Survey says, no.

Contributors to the conversation noted the following problems with humor:

* Variable sense of humor among readers; what one reader finds funny, another reader finds annoying
* Risk of unintended offense
* Humor doesn't translate or localize well
* Readers need tech docs to help them *do things*, and humor gets in the way
* Humor quickly becomes outdated

Commenters offered these links for backup: a `Stack Exchange answer from Mark Baker <https://writers.stackexchange.com/a/21095>`_; a `blog post by Neal Kaplan <https://customersandcontent.com/2013/10/22/using-humor-in-your-documentation-or-not/>`_ that covers translation, corporate voice, and clarity issues; a `thesis about humor in tech docs <http://stars.library.ucf.edu/cgi/viewcontent.cgi?article=3683&context=etd>`_ with accompanying `forum discussion <https://productforums.google.com/forum/#!topic/websearch/a8wm46bg8m0>`_; and Sarah Karp's `WTD Europe 2016 talk about voice <http://www.writethedocs.org/conf/eu/2016/speakers/#speaker-eu-2016-sarah-karp>`_. Fortunately for the WtD newsletter crew, the group did agree that (attempts at) humor can work in less formal content, like presentations and...newsletters. Phew!

*****************************
Documenting unlabeled buttons
*****************************

Many of us work in interfaces that are riddled with unlabeled buttons, putting us in the unenviable position of figuring out how to refer to them in text. Describing them is risky. Statements like "click the button that looks like a stack of books with a lightning bolt" wear thin pretty quickly. But including inline button images comes with its own set of pitfalls. Thanks to the Slack hivemind, we arrived at some best practices to keep in mind.

The overall feeling was that including images was better than relying on (often questionable) descriptions, but with a couple of important caveats:

* Make sure you get your font and icon sizes working together so the inline images don't disrupt your line height. If you need to get some dev help to work a little stylesheet magic, do it. It's worth it. *NOTE: It was this common problem that initially sparked the unlabeled button discussion.*
* Be aware that the downside to including icon images is maintainablity – one change to the UI usually means dozens+ changes to the docs, which can be hard to sort out.
* Alt text for your icon images is not optional. Not only is it critical for keeping your docs accessible, but it also helps with the maintenance problem. If your icons have consistent alt text, you at least have a search term to use when updates need to be made.

One other point surfaced during the discussion – font icons. While they neatly bypass the line-height problem, you might have to work a little harder at making them accessible (since you can't just drop in alt text) and they have their own maintenance challenges, over the long-term.

***************************
Who's running this content?
***************************

Sometimes a product manager or someone else from outside the docs team might ask you to remove information from your documentation that you'd consider useful or even necessary. Figuring out how to respond when conflicts like this come up can be tricky to manage. Fortunately, the community had some useful advice to share!

* Do everything you can to understand the rationale behind the request – knowing where it's coming from can help diffuse tension/frustration.
* Consider whether the information itself is the problem, or just the place that it lives. See if moving or reorganizing it will satisfy the person requesting the change.
* Try couching the discussion in neutral terms, rather than simply pitting your opinion against theirs. For example, explain that if you remove the information, it will increase the load on the support team. If you've got any metrics to lean on here, that's helpful.
* Recognize that sometimes there are going to be legal, strategic, or just political pressures that take choice out your hands.
* But also keep in mind that sometimes opinions change with time. Keep a copy of any content you remove, in case you have the opportunity to restore it later.

*********************************
Struggles with dates and versions
*********************************

Another conversation that cropped up this month centered around whether and how to include a 'last updated' date on each page of your docs. If you don't include it, your readers have little to go on when gauging the freshness of the content. If you do include one, it can still be misleading – does 'last updated June 1' mean that everything on the page is current as of June 1st, or does it just mean someone started their month by correcting a typo? As one contributor put it, "these dates can tell me when to distrust something for sure, but never when to trust something."

Adding version information, rather than last updated dates, was one proposed solution. By noting the version of the product that the docs pertain to, you can equip your readers with much more reliable context about the relevance of what they're reading. However, this is dependent on your product having big, distinct version releases. If you're writing for SaaS products, this is probably a bad fit. It also doesn't help when navigating community or third-party content, which is unlikely to have any consistent version information included (but may have some sort of published date).

Overall, the takeaways were: Versioning information is great, if you can pull it off. Datelines are valuable, if imperfect. And squeezing in some context about content updates – 'This page was due for review in 2015.', 'This page was created but never edited.', etc. – is definitely worthwhile.

*************************
Upcoming community events
*************************

In this last section of the newsletter, we try to call out community goings-on out in the real world. We've got three local meetups happening this week alone! Mark your calendars!

**EU CONFERENCE COUNTDOWN: Two Months Left!**
Make sure you `get your tickets soon <http://www.writethedocs.org/conf/eu/2017/tickets/>`_, so you can join us in Prague, Sept 10-12!

Upcoming Meetups
----------------

* **Today!** July 11 – Portland, OR, USA – `History of the New Relic Documentation Site, Part One <https://www.meetup.com/Write-The-Docs-PDX/events/240771894/>`_
* July 12 – Cambridge, UK – `Finding the right work to do: Lessons learnt from a year at a startup <https://www.meetup.com/Write-The-Docs-Cambridge/events/240634929/>`_
* July 13 – Montreal, CA – `First Write the Docs Montreal Meetup! <https://www.meetup.com/WriteTheDocsMTL/events/240350356/>`_
* July 19 – Broomfield, CO – `Building navigation for your doc site: 5 best practices <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/241431528/>`_

Thanks to all our wonderful organizers who are putting these events together!

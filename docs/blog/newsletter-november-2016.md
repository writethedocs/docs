```eval_rst

.. post:: Nov 3, 2016
   :tags: newsletter, november, 

```

# Write the Docs Newsletter - November 2016

## Community conversations and milestones

Hello, Write the Docs! Let me tell ya, it's been a jam-packed month for interesting conversations in the community. It's been really exciting to see so much activity and engagement on the Slack channel. It's even got us thinking about bumping the frequency of these dispatches up to twice a month, just so we can include more good stuff.

But that's a decision for the future. For right now, we have an exciting milestone to celebrate: **The Write the Docs Slack community officially cleared 1000 members last week!!** Considering it's only been around since the 2014 North American conference, that's not too shabby! Thanks to all of you for making the Write the Docs Slack such an inquisitive, creative, supportive place to hang out.

(If you haven't joined us on Slack yet, we'd love to have you. [Just click here.](http://slack.writethedocs.org/))

Now, let's get down to the stories for this month. Folks have had some really interesting chats on a great variety of topics – read on for some of the highlights!

_NOTE: Remember,  we'll be keeping an eye on the #general channel for newsletter content, but if you see a conversation elsewhere on Slack (or Twitter or wherever) that you think is a good fit, ping our editor, Kelly O'Brien (@kobrien042)._

## A quick guide to style guides

One of the perks of the Write the Docs community is having a group of people available to help figure out tricky style questions, when we run into them. This month, one such query led to a big discussion about what style and usage resources people use when they have questions.

Although lots of folks default to a simple Google search and go with the most common usage, there were some other suggestions for good places to start:
* [Merriam-Webster Dictionary](http://www.merriam-webster.com/), always a good start
* [18F's in-house Content Guide](https://pages.18f.gov/content-guide/)
* [MailChimp's Style Guide](http://styleguide.mailchimp.com/)
* And, in fact, according to the Poll the Docs survey from last year, most of the 100 respondents, regardless of the size of their team, used some kind of in-house style guide.

In general, the recommendation was to pick one authoritative style guide and stick to it. This can be a little tricky since there's a scarcity of up-to-date TechComm style guides to work with. (The [Microsoft Manual of Style](https://www.amazon.com/Microsoft-Manual-Style-4th-Corporation/dp/0735648719) got honorable mention, but the most recent edition is still 4 years old.) Non-technical style guides like the Associated Press or Chicago Manual of Style are even more fraught, since they tend to lag seriously behind on the current technical lexicon.

If you're looking for more style guide resources:
* Thursday Bram (@thursday) made her style guide template available on her blog:  [http://www.thursdaybram.com/download-my-in-house-style-guide-template-to-use-however-you-want]( http://www.thursdaybram.com/download-my-in-house-style-guide-template-to-use-however-you-want) It makes an _excellent_ starting point if you're developing your own style guide.
* This forum post from last year also has some style guide suggestions for documentarians: [http://writethedocs.discoursehosting.net/t/style-guides-for-documentarians/112](http://writethedocs.discoursehosting.net/t/style-guides-for-documentarians/112)

## How do documentation and content strategy intersect?

A really interesting discussion about content strategy in technical writing emerged this month. Content strategy, historically, has been strongly associated with the marketing communications side of things. But the line between marketing content and technical communication seem to be getting blurrier by the day.

The high-level takeaway was that the definition of 'Content Strategy' as a practice seems to be shifting pretty significantly. People talked about seeing content strategy encompassing one, some, or all of the following:
* Marketing communications
* Documentation
* In-product help text
* UI naming conventions
* Sales copy
* Virtually any customer-facing content, in any context

There was also a huge range in the types of job positions that were considered the responsible party when it came to content strategy. Everything from the very on-the-nose 'Chief Content Officer' role to something that sneaks onto a Product Manager's plate (sometimes while they're not looking). But one way or another, content strategy did seem to play a role in most people's documentation work, whether they are overtly responsible for it or not.

## Doc-friendly toolchains and CMSs

As we're all aware, tooling is a big deal. We all have specific needs to get our optimal workflows humming along, and those needs shift and evolve. Finding the ideal setup for getting your docs written and published takes time and effort (and funds). So, it was no surprise to see a discussion spark up around what kinds of doc tools are out there, and what you can (and can't) expect from them.

The general consensus is that it's still quite a challenge to find a solution (or combination of solutions) that suits your requirements, workflow, and budget, out of the box. As a result, many companies opt to build their own tools, in-house, instead of investing the time or money into bending one or more of the available tools to their will.

All of that said, a handful of solutions and platforms were mentioned in the conversation, if you're looking to check out some of the options:
* [Read the Docs](https://readthedocs.org/) – open source documentation hosting platform based on Sphinx
* [Deconst](https://github.com/deconst/) – open source tool from Rackspace, based on RTD + support for Sphinx and Jekyll
* [Contentful](https://www.contentful.com/) — developer-friendly, API-forward content management platform
* [Forestry](https://forestry.io/) – builds a CMS from a repo of your Jekyll or Hugo project
* [CraftCMS](https://craftcms.com) – user-friendly CMS, handy if you have non-techy folks contributing to your docs


## Using abbreviations and acronyms in documentation

What started as a quick poll about how to abbreviate "input/output" – 'I/O' won handily over 'IO', 18:3 — quickly turned into a broader discussion about abbreviations in documentation on the whole. Here were some of the key questions and takeaways that emerged:

* **For common abbreviations and acronyms, are definitions necessary?** The consensus on this point seemed to be yes, a definition is needed, even for common abbreviations and acronyms. Folks leaned away from assuming that your readers are familiar with terminology and abbreviations. ("Assumption is the mother of all feckups," as one participant put it!) Basically, you never know who is reading your docs, so it's dangerous to assume that every reader will understand undefined abbreviations and acronyms.
* **Does the intended audience affect whether you define abbreviations and acronyms?** Maybe you've heard something like "anyone ready to look at [X] documentation would already know what [Y] means." The general feeling on this point was that even if you think the audience knows what you do and understands the terminology, it's a mistake to disregard the readers who are new to the field or aren't as familiar.
* **Can you count on readers to find definitions for acronyms via web searches?** It's easy enough to search for unfamiliar acronyms, but what if an acronym has more than one meaning? If you don't define what the acronym means in the context of your docs, readers could easily settle on a different meaning based on their searches. Take "CI" as an example. The most likely meaning might be "continuous integration," but there are more than 200 possible meanings… and [TheFreeDictionary.com](http://www.thefreedictionary.com/)'s list of the most common meanings doesn't include "continuous integration" at all!
* **What does "define at first use" mean these days?** With so many technical documents published online, you might need to rethink the rule about defining acronyms at first use. Defining once "per document" doesn't make much sense when the document isn't a printed manual, there's no "beginning" to flip back to, and there's no index to check. Recommendations included spelling out acronyms at their first use in each section of documentation or in the overviews for sets of functions. The takeaway was that document structure and format will determine the best way to define acronyms.

There was also an entertaining discussion of how the "everyone knows THAT" perspective can lead to problems, if you're not careful. Go have a read about [the location of the ancient Land of Punt](http://www.pbs.org/wgbh/nova/ancient/egypt-punt.html) or phenomenon like [iconography that doesn't make sense anymore]( http://www.hanselman.com/blog/TheFloppyDiskMeansSaveAnd14OtherOldPeopleIconsThatDontMakeSenseAnymore.aspx).

## Need more documentation goodness?

For any of you who might have your eyes set on this year's [Linux.Conf.Au](https://linux.conf.au), there will be a one-day miniconf called 'Doc Down Under' the day before LCA kicks off. Their call for proposals is open right now and is very relevant to Write the Docs' interests. So if you've been looking for an excuse to visit Hobart, Tasmania in January, go [check out their CFP](https://linux.conf.au/schedule/presentation/3/)!

Although our next Write the Docs conference doesn't come around 'til the spring, you can always check to see if there's a [Write the Docs meetup](http://www.writethedocs.org/meetups/) near you! (And if there's not, [think about starting one up](https://www.youtube.com/watch?v=ZwQ8Kd48d0w)!)


.. post:: September 6, 2017
   :tags: newsletter

##########################################
Write the Docs Newsletter – September 2017
##########################################

Hi everybody!

Kelly O'Brien here, your friendly neighborhood newsletter editor, wishing you all a very happy September! As it happens, September is Be Kind to Editors & Writers Month (h/t @monique.semp for the discovery)! So make sure you take a moment to be kind to yourself and to the documentarians around you!

Another exciting fact about September: Write the Docs Prague happens this month! In fact, the pre-conference festivities get underway this weekend! Folks have started to make their way to Prague (I'm hopping on a train this afternoon!), and the conference chatter is starting to pick up in the #wtd-conferences channel on Slack, if you're of a mind to tune in.

In the meantime, we've had another month of interesting conversations and insights from the Write the Docs Slack. Read on, and enjoy!

*********************************
Storing and Testing Code Snippets
*********************************
How do you work with code samples? Is it better to keep them in your doc source files or store them externally? How do you make sure your code examples are always up-to-date and working? In other words, how do you test them?

Documentarians tackled this thorny question recently, and as usual the answer was "it depends." Nobody had a perfect solution, but we did come up with an excellent list of items to consider:

* If you keep your snippets in your documentation, you need to export for testing. If the writing team works closely with tests, great, but more often you'll need to work with a separate dev team. Coordination and communication can get complicated (and therefore error-prone), but this approach is more reliable for figuring out what needs to change in the explanatory docs.

* If you maintain your code examples externally, testing can be smoother, but keeping the docs up-to-date with changed examples is more challenging. This approach might work better for large sets of examples.

* Other variables to consider: how often the sample code changes, how comfortable writers are with code, and how comfortable devs are with docs. Although the general feeling was that an automated approach tends to work best, one bold contributor suggested that manual copy-and-paste might be the right solution in some environments.

***************************************************************
Crowdsourced Documentation, Plus Sunsetting Stack Overflow Docs
***************************************************************
This month, the `Stack Overflow Documentation beta shutdown <https://meta.stackoverflow.com/questions/354217/sunsetting-documentation>`_ prompted a conversation about crowdsourced docs and whether they can ever work well. Folks mentioned `Django <https://docs.djangoproject.com/en/1.11/>`_, `Wikipedia <https://www.wikipedia.org>`_, and `Ubuntu <https://help.ubuntu.com>`_ as examples of effective crowdsourced documentation. And on the otherside you have open-source software companies like OpenOffice and Mozilla, who tried volunteer-only docs but eventually hired writers.

So what *does* it take to make crowdsourced docs work? They seem to work best when companies clearly value documentation – even to the point of requiring developers to write it before they can commit code. Others mentioned that it's vital to provide lots of detail about the content contributions you're looking for. Finding the right model is important too: some companies have all-volunteer-created docs, and others solicit volunteer contributions that are eventually reviewed and curated by an in-house writing team. Crowdsourcing is also a good way to dig up questions that real users have so you can explicitly address them in your documentation.

People also had some interesting perspectives on why the Stack Overflow (SO) effort failed:

* No clear vision communicated for SO documentation
* Return on investment for SO docs was too low to pursue
* Docs are a hard sell--it's not easy to get people to volunteer to write or curate them
* SO shut the Docs beta down before it had time to catch on
* SO wasn't seen as the "right" place to go for docs (even if a company's official docs aren't well done)
* No easy or effective way to address gaps in official docs in the SO environment (which is problem:solution-based)

If you're interested in a lengthier dicsussion about the SO Documentation beta sunsetting and crowdsourced docs in general, check out last month's episode of the `Write the Docs podcast <http://podcast.writethedocs.org/2017/08/22/stack-overflow-failure-open-source-challenges/>`_!

*************************************
Doc Portfolios: A Perpetual Conundrum
*************************************
If you're job hunting, you've probably spent some time sprucing up your writing portfolio. But much more than, say, a journalist or a graphic designer, documentarians have to tread carefully when assembling our work samples. Much of the work we do is either so context-dependent that sharing our samples might not tell a prospective employer anything useful...or it's straight-up proprietary, in which case we can't share them at all. Maintaining a portfolio that's applicable, fresh, and accessible is a problem that, as one documentarian pointed out this month, is a "perpetual conundrum" we all face.

The pitfalls of assembling and submitting a docs portfolio are varied. Content can be out of date or apply to outdated technologies. Depending on where the content was published and who by, it might no longer be available online. And if your work was done for internal audiences, it may well be that sharing it would be a breach of your contract. But even with all that, portfolios are often a mandatory part of the interview process.

But just as the community was able to identify the problems with portfolio submissions, they were also able to brainstorm some solutions:

* Ask your previous employers if they'd be comfortable with you sharing a small snippet of your work.
* Edit all proprietary names and information out of your content before including it in your portfolio.
* Consider contributing to an open source project and including those contributions in your portfolio.
* If you're struggling to find online samples to link to, ask if the organization will accept a file submission instead of an online portfolio.
* If you're having a hard time finding work that used to be published, use the `Wayback Machine <https://archive.org/web/>`_, or a similar tool.

***********************************
Resources for Documentation Metrics
***********************************

If you haven't explored any of the topic-specific channels on Slack, you definitely should. We've got channels for introducing yourself to the community (#intros), getting and giving advice on job-hunting (#career-advice), and writing API docs (#documenting-apis), as well as a raft of tool- and location-specific channels. But one of the channels I've been particularly enjoying lately has been the #analytics channel, where folks go to talk about docs metrics!

In the last few weeks, folks have shared some valuable resources to help us think about how we track and measure the success of our documentation efforts:

* Looking for a place to start with Google Analytics? One of our members - @wouter – shared a dashboard for measuring user docs engagement in Google Analytics. You can import it into the property for your docs on Google Analytics and start poking around. It's not a finished product, for sure, but if you're looking for a place to start, this would be a good one. `Download the dashboard here.  <https://analytics.google.com/analytics/gallery/#posts/search/%3F_.term%3Duser%20documentation%26_.start%3D0%26_.viewId%3Dja0-XZQsSB-GH7K3Hw3BWw/>`_
* Another member – @docsbydesign – has been sharing a series of blog posts on measuring technical content. Also in-depth, and platform agnostic, they're a great way to get yourself oriented in metrics-land. Here are `part 1 <http://docsbydesign.com/2017/08/24/measuring-your-technical-content-part-1/>`_, `part 2 <http://docsbydesign.com/2017/08/27/measuring-your-technical-content-part-2/>`_, and `part 3 <http://docsbydesign.com/2017/08/29/measuring-your-technical-content-part-3/>`_
* If you're looking for a deep dive, @tfranko came across  `Improving the User Experience through Practical Data Analytics  <https://www.safaribooksonline.com/library/view/improving-the-user/9780128006351/>`_, which looks like an interesting, in-depth read on digging into your user data.

*************************
Upcoming community events
*************************

**EU CONFERENCE COUNTDOWN: Just a few days left!**
We're so excited that the conference is almost here! If you'll be joining us (or even if you just want to conf vicariously), have a look at `our most recent pre-conference update  <http://www.writethedocs.org/conf/eu/2017/news/2week-info/>`_!

**Upcoming Events**

September 10-12 – Prague, Czech Republic – `Write the Docs Conference Prague <http://www.writethedocs.org/conf/eu/2017/>`_
September 19 – Cambridge, UK – `Prague Conference Share & Tell (Cambridge)  <https://www.meetup.com/Write-The-Docs-Cambridge/events/240634962/>`_
September 19 – London, UK – `Prague Conference Share & Tell (London) <https://www.meetup.com/Write-The-Docs-London/events/243010607/>`_

Rather a light month for meetups this month, huh? Want to see one in your neighborhood? Reach out to `your local group on meetup.com <https://www.meetup.com/>`_ or `start one of your own <https://www.youtube.com/watch?v=ZwQ8Kd48d0w&>`_!

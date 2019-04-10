.. post:: December 18, 2017
   :tags: newsletter


#########################################
Write the Docs Newsletter – December 2017
#########################################

Hi everybody! Kelly O. here, with our last issue of 2017! It's been a gigantic year for the Write the Docs community. Just in the last month, our members have gotten up to some amazing stuff, including:

* A very successful first Australian event! To catch up on how it went, `watch the videos <https://www.youtube.com/channel/UCPhWNEFb53x6PjnpRIYf1yg/videos>`_ or `read all about it <https://ffeathers.wordpress.com/2017/11/25/doc-sprint-at-write-the-docs-day-australia/>`_.
* A lively and informative third API the Docs event in Amsterdam – `check out the recaps! <https://pronovix.com/api-docs-amsterdam-2017>`_.
* And two new podcast episodes, `one focused on the Mozilla Developer Network's Web Docs Project <http://bit.ly/wtdpodcastepisode11>`_ and `the other featuring an interview with WTD organizers Eric Holscher and Mikey Ariel as guests  <http://podcast.writethedocs.org/2017/12/13/founding-principles-of-write-the-docs/>`_!

Not only are we ending the year on a high note, but we also have a TON of great stuff coming up in 2018 as well!

* We're already in full planning mode for the Portland and Prague conferences. The `call for proposals for Portland <http://www.writethedocs.org/conf/portland/2018/cfp/>`_ is open until January 10th, so if you haven't started your talk proposal, now's the time!
* We've also started to line up sponsors for both conferences, so if your company is interested in showing off its love for good docs, drop us a line at `sponsorship@writethedocs.org <mailto:sponsorship@writethedocs.org>`_. You can read about our sponsorship packages in our `Portland <http://www.writethedocs.org/conf/portland/2018/sponsors/prospectus/>`_ and `Prague <http://www.writethedocs.org/conf/prague/2018/sponsors/prospectus/>`_ prospectuses (prospecti?).
* And finally, early in 2018 we'll be launching a brand new Write the Docs Job Board! Our goal is to make it easy for documentarians to find their dream gigs, and employers to find their dream documentarians. If you'd be interested in helping us beta test the board in January – either as an employer or an applicant – we'd love to hear from you at `jobs@writethedocs.org <mailto:jobs@writethedocs.org>`_.

Whew! Hopefully that gives you some things to look back on or forward to with excitement!

Please note that the newsletter will be taking January off, to give our editorial crew a little break. We'll be back in the saddle with the February issue. In the meantime, have a happy holiday season and enjoy one last round of 2017 documentation stories, below!

****************************************
Help your contributors help your project
****************************************

Contribution guidelines are an important part of any open source project. A discussion about writing good contribution guidelines came up on Slack this month, and yielded some pearls of wisdom:

* Contribution guidelines can range from a few pithy sentences to multi-page instructions including a style guide, process instructions, and pull request templates. Small projects will require less detail, but as your project and/or community of contributors grows, it's worth scaling your guidelines accordingly.

* When determining the level of detail to go into, keep in mind how many maintainers you have. Remember that your guidelines will need maintenance just like any other contribution.

* Consider starting with a contribution template when creating your guidelines. Even if you don't have much guidance beyond the template itself, it gives people a place to start. (`Check out this one <https://github.com/nayafia/contributing-template/blob/master/CONTRIBUTING-template.md>`_ for an example!)

* Think about including code of conduct as part of your contribution guidelines. It's helpful to set expectations about conduct as early as possible, and a clear and visible code of conduct can help your community grow the way you want it to.

If you're looking for inspiration, this `explanation of Node.js's contribution policy (2016) <https://medium.com/the-node-js-collection/healthy-open-source-967fa8be7951>`_ is a great place to start.

****************************
It's just documentation, man
****************************

An interesting discussion cropped up on `Hacker News <https://news.ycombinator.com/item?id=15779382>`_ this month, about "man pages" (short for command line user **man**-uals). The story made the rounds in a couple of Write the Docs spaces and sparked some lively conversations.

In the original HN conversation, diverse opinions were expressed on a range of subjects. For example, should man pages include tutorial-type information? Is the traditional structure of Synopsis, Description, Options, and Examples at all useful? Should command-line parameters be sorted or grouped? Do you need to be able to jump to a particular command-line option without resorting to wildcard search?

There was plenty of `bike-shedding <https://en.wiktionary.org/wiki/bikeshedding>`_ along the way, including statements that what really mattered was the particular \*Nix variant the man page was in, that "info pages" are really where it's at, that `roff <https://en.wikipedia.org/wiki/Roff_(computer_program>`_ was the "way forward," and even that really, the man pages were fine but the *real* problem is that people don't know how to use them...

Inevitably, some people suggested that crowd-sourcing would be the solution, while others maintained that man pages already were crowd-sourced, along with the rest of the \*Nix variant.

In short, the man pages discussion turned out to be an almost perfect microcosm of many of the classic documentation debates we all find ourselves in. Of course, if all you really wanted from the HN discussion was just some insight into "better" man pages, we recommend taking a look at the admirably named `tldr <https://tldr.sh/>`_ project.

********************************************************************************
'Canceled' vs. 'cancelled' and other adventures in American and British English
********************************************************************************

One documentarian's quest to help a dev brush up on differences between British and American usage produced a list of websites with helpful advice on the subject. Lucky for us, she shared it! The next time you're wondering whether "power point" means the same thing on both sides of the Atlantic (hint: aside from Microsoft, it does not), try one of these links to get to the bottom of it:

* `Bored Panda's pictoral guide <https://www.boredpanda.com/british-american-english-differences-language/>`_
* `Oxford Dictionaries' British and American terms <https://en.oxforddictionaries.com/usage/british-and-american-terms>`_
* `Six differences from Voice of America's Learning English <https://learningenglish.voanews.com/a/six-difference-between-britsh-and-american-english/3063743.html>`_
* `Pictorial guide to 20 British words that mean something different in the US <http://www.bigstockphoto.com/blog/20-british-words-that-mean-something-totally-different-in-the-us>`_

As one keen observer pointed out, even `Apple's API docs <https://pbs.twimg.com/media/DPbb0TKUIAA_hL6.png>`_ need help with this now and then!

*********************************************
Thinking hard about API reference docs layout
*********************************************

Out of a larger discussion of tools and workflows for specific API documentation requirements emerged a somewhat surprising critique of the popular three-column layout for API reference documentation.

Several folks pointed out that it's almost impossible to coordinate the content of the second column – the explanations of resources, endpoints, request and response objects, parameters - with the example requests and responses provided in the third column.

Questions also arose about usability and readability: with three columns, it can be difficult for readers to know where to focus their attention, especially on a smaller screen, and they have to work hard to map the explanations to the examples. It can be tricky for doc authors to figure out where to put tab selectors if examples are provided in multiple languages, too.

But other contributors to the discussion pointed to research that suggests the three-column layout not only meets with the favor of API producers, it's also effective for API consumers. The research is an interesting read, and definitely worth it, if you want to dive deeper into the topic. You can `download the full paper <http://journals.sagepub.com/doi/abs/10.1177/0047281617721853>`_ or watch one of its authors `present on the content at Write the Docs Prague 2016. <https://www.youtube.com/watch?v=soQSOBwiXdA>`_

******************
Community calendar
******************

The deadline for proposals to speak at Write the Docs Portland closes on **January 10, 2018 at midnight PST.** You can `read about the CFP and submit your proposal on the conference website <http://www.writethedocs.org/conf/portland/2018/cfp/>`_.

Our monthly meetups have mostly wound down for the year, but there are a few on the books already for 2018. Since the newsletter won't be back til early February, make sure you keep an eye on your local meetup's calendar for other January events that get scheduled in the interim!

January 9 – Portland, OR, USA – `Networking with a side of Write the Docs proposals <https://www.meetup.com/Write-The-Docs-PDX/events/243555894/>`_

January 10 – Austin, TX, USA – `Monthly meetup <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/244942450/>`_

January 23 – London, UK – `January Meetup, guest speaker <https://www.meetup.com/Write-The-Docs-London/events/245808440/>`_

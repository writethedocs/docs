.. post:: May 04, 2020
   :tags: newsletter

####################################
Write the Docs Newsletter – May 2020
####################################

Hello, documentarians; it's Beth here with the May edition of the Write the Docs newsletter. I hope you're all holding up okay under lockdown.

We just announced last week that we're cancelling our on-site conferences in Portland and Prague, and moving online. Virtual Portland will be in August, with exact dates to be announced soon; and virtual Prague will be in the autumn, with dates announced in summer. There's a lot more detail in `the blog post </blog/moving-portland-prague-2020-online/>`__, including what to do if you've already got a Portland ticket.

To help you entertain yourself between now and August, there's some good news from the Write the Docs website. We've got an extensive archive of conference talks and newsletter articles, covering all sorts of topics, but up until now it's been a bit difficult to browse them all. So I'm delighted to introduce the `Write the Docs content index </topics/>`__. If there's a topic you'd like to spend some time learning about, check out the index and see if your topic is there!

Plus, if you spot something in Slack that isn't written up or in the index, but you think should be - as ever, please do tag it with the ``:suggest-for-newsletter:`` reaction to bring it to our attention :)

Onto our articles!

----------------------------------
To answer, or not to answer: FAQs?
----------------------------------

A recent poll about whether to include a topic called "Frequently Asked Questions" in documentation produced the not entirely surprising result that nearly 2/3 of respondents opposed the idea vehemently. The conversation that ensued, however, was considerably more nuanced, thoughtful, and useful.

Some folks used questions as topic titles, or grouped small sets of questions into single topics, but resolutely eschewed the monolithic "junk drawer" approach (as one contributor so nicely put it). They also pointed out that maintaining a large set of FAQs becomes a nightmare because of its grab-bag approach and the fact that it's rarely the first place people look for information.

Sometimes, however, in spite of near-universal suspicion of an FAQ approach, good use cases do develop for FAQs. For example, in environments where docs and support report into different parts of the organization, docs-produced FAQs can help supplement support articles, or address a small handful of genuinely frequent questions that are unlikely to change over time.

FAQs can also supplement docs between releases if you don't work in a continuous publishing environment. They can provide summary lists of problems users often encounter, with pointers to more detailed official docs. Or they can provide a handy format for one-off purposes such as pre-sales, where the intent is not to replace or even supplement the official docs but to summarize content for a different audience.

All too often, though, FAQs exist because they can be easier than figuring out where content should go in a large or elaborate doc set. More than one contributor pointed to the UK GDS post `FAQs: why we don't have them <https://gds.blog.gov.uk/2013/07/25/faqs-why-we-dont-have-them/>`_. Ultimately, though, the Write the Docs community concluded that "it depends" - on context, on use case, on quality. As is so often the case!

---------------------------
Getting more info from SMEs
---------------------------

No documentarian is an island: interacting with subject matter experts (SMEs) is often crucial to getting our jobs done. But what if the information these SMEs provide is too brief or incomplete? Here are some ideas on how to gather detailed and helpful information from these key team members:

* Remember to have empathy. If SMEs don’t provide the answers you want, it doesn’t mean they don’t care. They’re busy people who know their areas deeply; short answers make perfect sense to them as they already have a strong grounding in the topic. Understand what’s important to them and their managers. Align your goals and user’s goals with theirs. The best way to communicate is to understand.
* Allow them to see things from the user’s perspective so they understand the need for accurate documentation. If possible, attend a user interview with the SMEs. Have a follow-up meeting where you brainstorm ideas around issues that arose in the interview.
* Coordinate with the SMEs and their managers. If the document is high priority and requires SMEs’ input before it can be completed, the manager should make it clear in the ticketing system. This way, everyone can see how the missing input would affect the project. Point out what the repercussions might be if it isn’t clear.
* Adjust your communication style. Whether it’s through face-to-face meetings, calls, emails, or instant messages, select the communication method that your SMEs prefer. You’ll get more information from them this way. Incorporate this info into your question until you get to the bottom of it.
* Depending on the topic, combine your series of questions into one long query. Provide a preferred response date and a reason for that date.
* Share what you understand about the topic, and ask the SMEs for their input. Phrase it as a “yes/no” question (eg, “This is how I think X works. Is this right?”). If you’re correct, they’ll agree. If you’re wrong, they’ll correct you. This approach is known as Cunningham’s Law: "the best way to get the right answer on the internet is not to ask a question; it's to post the wrong answer".

-------------------------------------
Tips for creating quality screenshots
-------------------------------------

Love them - because they make it easier for readers to find things in the UI? Loathe them - because of the maintenance burden? Either way, many of us work a little or a lot with screenshots. And if you're going to have them, it's worth doing them well; so here are a few tips for taking good screenshots:

*   As long as the area of focus is up to date in a screenshot or GIF, updates to other areas shown aren't as urgent. You can wait until the UI changes are highly noticeable or cause confusion.
*   Consider using a disclaimer to explain possibly confusing differences between your screenshots and your user's screen (for example, due to versioning or feature enablement).
*   `Simplified UI Screenshots <https://www.techsmith.com/blog/simplified-user-interface/>`__ (where you remove or cover UI elements that you aren't referring to) can require fewer updates and save on translation costs.
*   Some community members had tried using line drawings instead of screenshots, to be less affected by small UI changes. But they can be even more difficult to maintain than screenshots, so carefully consider how useful one is before creating it.
*   If you've got a large number of screenshots to maintain, look into automating your screen captures with Selenium.

Screen capture tool recommendations:

*   `Snagit from Techsmith <https://www.techsmith.com/screen-capture.html>`__ (Paid)
*   `Skitch from Evernote <https://evernote.com/products/skitch>`__ (Free, MacOS & iOS only)
*   `Greenshot <https://getgreenshot.org/>`__ (Free, OSS)
*   `Screenpresso <https://www.screenpresso.com/>`__ (Free)
*   `LightShot <https://app.prntscr.com/en/index.html>`__ (Free)
*   `Adobe Illustrator <https://www.adobe.com/products/illustrator.html>`__ (Paid)
*   `Adobe Photoshop <https://www.adobe.com/products/photoshop.html>`__ (Paid)

Join us in `#doctools <https://app.slack.com/client/T0299N2DL/C4EPE8332>`__ if you have any other tool recommendations!

---------------------------------------------
Choosing the right learning level for a topic
---------------------------------------------

This month, the `#learn-tech-writing <https://app.slack.com/client/T0299N2DL/C7YJR1N02>`__ book club had some interesting discussion based on *Every Page is Page One*, on the topic of topics: how do you decide what should go in one? And what's the right level to pitch it at?

Baker’s premise in the relevant chapters (chapters 12 to 13) is that the reader always arrives at the documentation qualified to read and retain the topic they’re searching about; therefore, writing to personas of varying knowledge levels (novice/intermediate/advanced) is not necessary. He argues that although there are several layers of information  available for subjects, the reader is already set on how much information they want to absorb. This can make it challenging to decide when to cover the big picture and when to cover the details.

The book club members listed overviews and "getting started" guides as big picture topics, and setup/requirement instructions and permission levels as details, along with any learning goals relating to “competency.”

Some writers found using precise, clear titles helps keep them focused on the topic at hand; focusing on the title helps you see that anything that falls outside the title’s scope should be assigned its own article. This is more of a gut determination than one based on metrics, though. It boils down to figuring out the user’s objective: so knowing the persona you are writing to is important when defining what topics to cover and in what depth. Do you write based on user knowledge level? How do you define what a novice is? Someone who could be new to the software may still be an expert in the industry that the software services - it's not exactly fair to describe them as a novice.

This is a good opportunity to think about cross-role collaboration, too. It can be argued when writing documentation, a technical writer should simply present the information as it is; and when developing learning paths, an instructional designer can help with building the path and deciding on the appropriate learning level.

---------
Job posts
---------

* `Technical Writer <https://jobs.writethedocs.org/job/197/technical-writer/>`__
   Semaphore, remote, full- or part-time
* `Developer Documentation Specialist <https://jobs.writethedocs.org/job/198/developer-documentation-specialist/>`__
   BigCommerce, Austin, full-time

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

--------------------------
Community events coming up
--------------------------

Not all of these have said they'll be virtual, but it's likely they will be.

- 05 May - Ottawa, Canada (virtual) - `Neil Perlin on Information 4.0 <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/270382478/>`__
- 08 May - Barcelona, Spain (virtual) - `API Docs with OpenAPI 3.0 <https://www.meetup.com/Write-the-Docs-Barcelona/events/269989029/>`__
- 12 May - Ottawa, Canada - `WTD Ottawa Shopify Meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqybchbqb/>`__
- 20 May - Toronto, Canada - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqybchbbc/>`__
- 4 June - Leeds, UK - `Book club <https://www.meetup.com/Write-the-Docs-North/events/268851380/>`__

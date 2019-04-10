.. post:: May 4, 2018
   :tags: newsletter, AB testing, imperatives, API definitions


####################################
Write the Docs Newsletter – May 2018
####################################

Hello everyone!

Kelly O. here, hoping it's been a good week for you all. We're just hours away from our first conference of the year. The Portland event marks the beginning of the community's busiest year yet!

The Prague conference may seem a long way off, in September, but the CFP is open for only a few more weeks. If you're interested in speaking, `have a look at the guidelines and submit your proposal <http://www.writethedocs.org/conf/prague/2018/cfp/>`_ by **midnight CET on May 15th**. As usual, we're interested in speakers of any experience level on any topic relevant to software documentation. Hit us with your best ideas!

We also have two other Write the Docs events to look forward to in 2018!

* On Aug 18-22, Write the Docs is teaming up with `Open Help <http://openhelp.cc/>`_ to put on 5-day event in Cincinnati that combines 2 days of talks and discussion with 3 days documentation sprints. We're really excited to try out this new format – `have a look at the website! <http://www.writethedocs.org/conf/cincinnati/2018/>`_
* Then from November 15-16, Write the Docs Australia will be returning for a second year as a full two-day conference. Check out what they're doing for year two on `the conference page! <http://www.writethedocs.org/conf/australia/2018/>`_

In addition, our network of meetups is alive and busy! The London group, for example, is partnering with the UK Government Digital Service to put on a `full-day meetup <https://www.meetup.com/Write-The-Docs-London/events/248304896/>`_ on June 5th about building a career in documentation. One of the organizers is running a short survey about documentation roles, in order to present his findings at the event. If you have a few minutes and want to participate, you'll find it here: `http://www.smartsurvey.co.uk/s/ZXSGG/ <http://www.smartsurvey.co.uk/s/ZXSGG/>`_

*Full disclosure: I am one of the co-organizers of the London meetup group. If you run a meetup and ever need community-wide exposure for a project or a community event, feel free to drop me an email at: `newsletter@writethedocs.org <mailto:newsletter@writethedocs.org>`_ I'm happy to help boost the signal.*

Now, after all that excitement out in the physical world, let's have a look at what folks have been talking about in the virtual one.

-----------------------------
A/B testing for stronger docs
-----------------------------

Measuring doc success is an evergreen topic on Slack. This month's installment started with a question about the possibilities of A/B testing your docs. It produced a nice range of thoughtful responses, from recommendations for tools to more detailed ideas about measuring the effectiveness your documentation updates:

* One contributor described a small-scale, hands-on approach that provides an old doc to a small sample set and asks the sample members to perform a specified task according to the doc. Measure how long it took them to complete the task, then run the same study again with the new doc and a different sample set of readers/testers. Reduced 'time to competency' = increased doc efficacy.

* If you'd rather run full on A/B testing out in the wild (as opposed to a controlled test environment), you might want to look into marketing tools like `Optimizely <https://www.optimizely.com/>`_. Caution, though – you need upwards of 50 users to get anything like a valid indication, and much higher is better.

* A modicum of statistical savvy is useful when designing your A/B tests. If you're measuring a big difference between docsets, a smaller test population can give you useful insights. If you're trying to assess the effect of smaller changes, you need a larger test population. And it's important to know just what it is you expect to change – time to complete a task, improved expressions of customer satisfaction, something else.

* When trying to ascertain results, beware of relying on traditional web analytics. Bounce rate and time on page, for example, require too much extrapolation. In other words, you can't assume that a short visit means the docs are no good, and you can't assume a longer visit means they work well. You could associate such data with other measures, but by themselves they don't tell us much.

TL;DR: It's hard to provide reliable testing of docs effectiveness – but that won't stop us from trying!

*For more conversations about measuring the success of your docs, pop into* `#analytics <https://writethedocs.slack.com/messages/analytics>`_

----------------------------------
Using imperatives in documentation
----------------------------------

English has no shortage of complexities, idiosyncrasies, and fine distinctions. Navigating them to come up with clear, concise content is at the heart of the documentarian's job. The Write the Docs Slack can be a great resource when you need a hand with that navigation. For example, this month one documentarian asked about the difference between 'must' and 'have to', sparking a plentiful thread about not only the difference but also important considerations when using them in your docs.

There is a canonical rule for their distinct usages. While both convey an obligation to the reader, 'must' is for *specific* requirements, while 'have to' refers to more general rules. You can read more about this definition in the `"Must vs Have to" post on Gymglish <https://www.gymglish.com/en/english-grammar/must-vs-have-to>`_.

But how does that play out in the docs? A lot of it has to do with the different tone that each verb carries. 'Must' is more formal, more inescapable. It's usually a good fit for procedural content when talking about necessary actions the reader must take. 'Have to' is better for guiding your readers towards best practices or broader expectations they should be keeping in mind.

*If you find yourself with other grammar or usage questions,* `#general <https://writethedocs.slack.com/messages/general>`_ *has many word-folks waiting to help you out.*

--------------------------------
Distinguishing one API from many
--------------------------------

When writing about APIs, it's not always clear where one API stops and another begins. Some teams treat their API as singular entity that covers everything, but others treat it as a collection of APIs instead, separated by product area, function, user segment, etc. So when the question arose – How do you decide whether you're writing about one API with broad functionality or multiple individual, more targeted APIs? – the community attempted to achieve some clarity.

After a thought-provoking discussion, some recurring (though not universal) definitions emerged:

* Everything that lives under one hostname is one API
* Everything that lives under one base URL and uses the same authentication specification is one API
* Even an API with broad-ranging capabilities, loads of endpoints, and a collection of related resources is still just one API, if it's all for the same application

There were some interesting examples of when teams have chosen to run contrary to these rules. For example, Twilio's Voice and Messaging APIs use the same base URL, but are treated as separate APIs because they're intended for different channels.

To help sort out the question for your team, an API-centric product manager and good API design are crucial. One strongly recommended resource on API design was `Phil Sturgeon's APIs You Won't Hate <https://apisyouwonthate.com/>`_.

*If you work with APIs and want to bounce some ideas around,* `#documenting-apis <https://writethedocs.slack.com/messages/documenting-apis>`_ *is the place for you.*

---------------------
Featured job postings
---------------------
**Hiring? Want to get your job posting in front of real, live, in-person documentarians?**
Any jobs posted on the `Write the Docs job board <https://jobs.writethedocs.org/>`_ by noon PST on Monday, May 7th, will be printed out and displayed at the inaugural Write the Docs job fair at the Portland conference.

If you're currently job hunting and will be joining us in Portland, here's a taste of what to expect at the `job fair <http://www.writethedocs.org/conf/portland/2018/job-fair/>`_ on Tuesday morning. The jobs below are from Oracle, our headline sponsor for the event.

`Principal Technical Writer <https://jobs.writethedocs.org/job/63/principal-technical-writer/>`_
Oracle, Full-time, Oakland, CA

`Senior Technical Writer <https://jobs.writethedocs.org/job/64/senior-technical-writer/>`_
Oracle, Full-time, San Francisco, CA

`Technical Writer 4 <https://jobs.writethedocs.org/job/62/technical-writer-4/>`_
Oracle, Full-time, Seattle, WA

`Technical Writer, Senior Manager <https://jobs.writethedocs.org/job/61/technical-writer-senior-manager/>`_
Oracle, Full-time, Seattle, WA

-------------------------
Upcoming community events
-------------------------

May 8 – Tel Aviv, Israel – `Kick-off meetup <https://www.meetup.com/Write-The-Docs-Herzliya/events/250109002/>`_

May 12 – Salt Lake City, UT, USA – `May Mixer Meetup <https://www.meetup.com/Write-the-Docs-SLC/events/249982393/>`_

May 17 – Berkeley, CA, USA – `Hack-a-thon: Working with Managers When You're a Lone Writer <https://www.meetup.com/Write-the-Docs-SF/events/250413818/>`_

May 21 – Leeds, UK – `Social and discussion meetup <https://www.meetup.com/Write-the-Docs-Yorkshire/events/249578837/>`_

May 22 – Budapest, Hungary – `Github: Why it will change the world of technical communication <https://www.meetup.com/Budapest-Technical-content-creators/events/249115186/>`_

May 24 – Los Angeles, CA, USA – `Documenting APIs, the Symantec way! <https://www.meetup.com/Write-the-Docs-LA/events/249946913/>`_

May 28 – Amsterdam, Netherlands – `May meetup <https://www.meetup.com/Write-The-Docs-Amsterdam/events/249028095/>`_

May 31 – Brussels, Belgium – `Process first! <https://www.meetup.com/Write-The-Docs-Brussels/events/250299512/>`_

June 5 – London, UK – `Build your Docs career: All-Day Event, in partnership with GDS <https://www.meetup.com/Write-The-Docs-London/events/248304896/>`_

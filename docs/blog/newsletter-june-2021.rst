
.. post:: June 03, 2021
   :tags: newsletter

#####################################
Write the Docs Newsletter – June 2021
#####################################

Hi everybody! It's Beth here, writing to you from my gloriously sunny balcony (thank *goodness* rainy May is over). I hope you're all enjoying the weather wherever you are.

The big thing I want to shout about this month is the `Prague Call for Proposals </conf/prague/2021/cfp/>`__. If you were even sort-of entertaining the thought of submitting a talk idea, take this as your sign to go for it! My favourite thing about giving a conference talk is the conversations the talk starts. It's awesome for helping you find people who care about the same things as you; so if there's something you'd really like to see a talk about this year, I really encourage you to submit your idea. And if you'd like a bit of help working on your proposal idea, the EMEA WTD meetup is hosting a `proposal workshop and discussion on 10th June <https://www.meetup.com/Write-The-Docs-Berlin/events/277872402/>`__ - check it out.

On to the stories from Slack! This month we've been talking about prioritization, the challenges of having busy colleagues, and much much more.

-----------------------------------------------------------
Priorities: Document new features or improve existing docs?
-----------------------------------------------------------

What would you prioritize: customer-requested improvements to existing documentation or working on new feature documentation? We discussed it on Slack this month as an interview question; for many documentarians though, the tension between prioritizing new vs. existing docs is a day-to-day reality. Mostly, this means prioritizing which to work on *first* - because neither releasing new features without documentation nor neglecting to update existing documentation are good options.

One reason to prioritize new features is if they are difficult or impossible to use without documentation. In this month's discussion though, prioritizing improvements to existing docs had the most support.

When you prioritize improvements to existing documentation, you raise the bar for new docs. The quality of your documentation rises as new docs are written to the higher standard. Making improvements implies figuring out what's wrong to begin with, so you'll be able to fix problems instead of repeating them. It's also easier to overlook or even forget low-quality content, whereas missing docs for new features are obvious. It makes sense to address existing customers' frustrations with existing docs. Even when poor docs do not represent a safety concern, they discourage current and potential customers. As one writer put it, "bad documentation is like breaking a promise".

It's not just about keeping users happy, though, because your work has a business impact beyond providing the necessary documentation. For example, technical writers serve as a proxy for new users, so they can provide valuable insights from a user's perspective. The informal testing that writers often do during the documentation process can uncover bugs and usability issues to pass along to the product team. And good docs encourage self-service and reduce the number of customer support contacts. The benefits of good documentation spiral out to many other aspects of the business!

--------------------------------------
Restricting docs to authorized readers
--------------------------------------

A long-time community member started a new job recently, and among the novelties to explore they're figuring out how to allow only authorized users access to some of the docs.

The community had plenty to suggest. Options ranged from suggestions of platforms, to details of how to roll your own or integrate different identity providers or workflows. They also mentioned making sure the solution was well-documented for future contributors to the docs!

Here are all the options folks contributed to the discussion:

* If you're writing docs in Confluence or knowledge base articles in Zendesk, both tools support limited access
* You can implement per-location authentication requirements in an NGINX server. This supports SSO with JWT (Json Web Tokens)
* Netlify offers an `identity and RBAC (role-based access control) solution <https://login-to-gated-site.netlify.app/>`_
* Work with a combination of feature flags and allowlists
* In Apache, you can use the `.htaccess` config file and user credentials
* KnowledgeOwl lets you specify which pages users can see without logging in (or what Google indexes), with groups to manage access
* Last but not least, Redocly offers a RBAC option for configuring developer portals

------------------------------
Dealing with busy stakeholders
------------------------------

How do you finish the documentation for a feature when a key stakeholder is too busy? What can you do to get the information you need from an unavailable stakeholder before the project's deadline? This month, the Write the Docs community discussed ways to progress on documentation projects when dealing with an unavailable stakeholder.

First, try writing as much as you can before contacting the stakeholder for help. This allows you to provide detailed information when emailing them about the hold-up. If the question is time-sensitive, it's well worth including a preferred deadline for an answer. As an alternative, try finding another stakeholder who has the knowledge and time to answer your questions. If, despite your efforts, the stakeholder remains unresponsive, you could notify your manager so they can speak with the stakeholder's manager. Finally, consider taking time to build rapport via light and informal chat with the stakeholder. Discussions that aren't *just* about chasing them for help can help establish a trusting relationship, and relieve tension and frustration.

Although these suggestions may help, it is important to remember that there is no one-size-fits-all solution when dealing with too-busy stakeholders. While a simple conversation may resolve some issues, others may necessitate escalation. It's okay to find this difficult - these situations can be complex and stressful!

There are more tips in `this blog post by Ian Haynes <https://www.wrike.com/blog/4-strategies-dealing-difficult-stakeholders/>`__, and we'll close with one point from there: if you can, stay positive and professional, to avoid burning any bridges. With luck, you will get the information you need!

-----------------------------------
The state of software documentation
-----------------------------------

If you're interested to get a sense of the overall state of software documentation, you're in luck, because we had some great resources shared this month. There's a lot of handy data about how docs are perceived, by both our developer audiences and by the folks who write the docs, with particular detail in the space of API documentation.

* `DigitalOcean Currents Q3 2018 report <https://currents.nyc3.cdn.digitaloceanspaces.com/DigitalOcean-Currents-Q3-2018.pdf>`__ - in particular, "What factors does your company consider while making business decisions around when to use open source for a particular project?"
* `SmartBear 2020 State of API report <https://static1.smartbear.co/smartbearbrand/media/pdf/smartbear_state_of_api_2020.pdf>`__, and Tom Johnson's `analysis of this report <https://idratherbewriting.com/blog/smartBear-2020-state-of-api-docs-review/>`__
* `Postman 2020 State of the API report <https://www.postman.com/state-of-api/>`__
* `The Content Wranger's 2019 State of Technical Communication <http://public2.brighttalk.com/resource/core/217857/the-state-of-technical-communication_474463.pdf>`__
* `Tom Johnson's 2020 Developer documentation survey <https://idratherbewriting.com/learnapidoc/slides/devdoctrends_results.html#/>`__

---------------------------------
What we're reading & listening to
---------------------------------

The #bipoc group's been discussing the following materials on diversity, inclusion, and equity. Want to join the conversation? Join us in the `#bipoc slack channel <https://app.slack.com/client/T0299N2DL/C016STMEWJD>`__!

For a short read: This `twitter thread <https://twitter.com/HeyChelseaTroy/status/1396503832255942656?s=19>`__ from @HeyChelseaTroy breaks down why approaching inclusion like other business initiatives often fails.

Have a little more time: Check out `this article on CNBC <https://www.cnbc.com/amp/2021/02/19/how-to-support-asian-american-colleagues-amid-anti-asian-violence.html>`__ about ways you can show support for your Asian American colleagues. Even though this starts with news about Anti-Asian American violence, the advice about support can easily be applied to anyone in need.

If you have 50 minutes: Check out this episode of `WorkLife with Adam Grant featuring John Amaechi <https://www.stitcher.com/show/worklife-with-adam-grant/episode/building-an-anti-racist-workplace-83305366>`__. The two talk about building an anti-racist workplace with a key takeaway of: “your culture is defined by the worst behavior you tolerate”.

.. ----------------
.. From our sponsor
.. ----------------

.. This month's newsletter is sponsored by SPONSOR:

.. .. raw:: html

..     <hr>
..     <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
..       <tbody>
..         <tr>
..           <td width="75%">
..               <p>
..               CONTENT
..               </p>
..           </td>
..           <td width="25%">
..             <a href="https://www.LINK.COM">
..               <img style="margin-left: 15px;" alt="SPONSOR" src="/_static/img/sponsors/IMAGE.png">
..             </a>
..           </td>
..         </tr>
..       </tbody>
..     </table>
..     <hr>

.. *Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured job posts
------------------

- `Technical Writer, Software Engineering <https://jobs.writethedocs.org/job/384/technical-writer-software-engineering/>`__, Pomerium Inc (Remote - North America)
- `Technical Writer <https://jobs.writethedocs.org/job/386/technical-writer/>`__, Carted (Remote - Sydney, Australia)
- `Technical Writer <https://jobs.writethedocs.org/job/389/technical-writer/>`__, Vistar Media (Remote - New York)
- `Content Lead <https://jobs.writethedocs.org/job/390/content-lead/>`__,  NetSpring Data, Inc (Remote - Mountain View, California)
- `Senior Technical writer for APIs <https://jobs.writethedocs.org/job/393/senior-technical-writer-for-apis-full-time-part-time-of-contractor-accepted-to-start/>`__,  ALIAS/CODE IS LAW (Remote - CET or EST)
- `Technical Documentation Writer <https://jobs.writethedocs.org/job/395/technical-documentation-writer/>`__, Chainlink Labs
- `Senior Technical Content Writer <https://jobs.writethedocs.org/job/394/senior-technical-content-writer/>`__, ThousandEyes (a part of Cisco), (Remote - London, UK)
- `Senior Technical Writer <https://jobs.writethedocs.org/job/401/senior-technical-writer/>`__, Schrödinger (New York or Portland)
- `Technical writer <https://jobs.writethedocs.org/job/402/technical-writer/>`__, Kandra Labs (Zulip), (Remote)
- `Digital Transformation with the TAAP No Code Low Code Applications Platform <https://jobs.writethedocs.org/job/404/digital-transformation-with-the-taap-no-code-low-code-applications-platform/>`__, TAAP (Remote)
- `Senior Technical Writer - Distributed US <https://jobs.writethedocs.org/job/405/senior-technical-writer-distributed-us/>`__, Cockroach Labs (Remote)
- `Technical Evangelist, Developer Experience & APIs <https://jobs.writethedocs.org/job/408/technical-evangelist-developer-experience-apis/>`__, Envestnet (Raleigh, NC, USA)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 08 June, 8:30am EDT (Florida) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsyccjblb/>`__
- 10 June, 7pm CEST (Europe) - `EMEA Write the Docs Proposals Workshop and Discussion <https://www.meetup.com/Write-The-Docs-Berlin/events/277872402/>`__
- 16 June, 12pm AEST (Australia) - `Docs as code - Part 2 <https://www.meetup.com/Write-the-Docs-Australia/events/276294734/>`__
- 21 June, 7pm EDT (Detroit) - `Using Notebooks for Documentation <https://www.meetup.com/write-the-docs-detroit-windsor/events/277649685/>`__
- 22 June, 8:30am EDT (Florida) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsyccjbdc//>`__
- 24 June, 7pm CEST (Europe) - `Open source tools for API documentation <https://www.meetup.com/Write-The-Docs-Berlin/events/277847849/>`__

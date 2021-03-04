
.. post:: March 05, 2021
   :tags: newsletter

######################################
Write the Docs Newsletter – March 2021
######################################

Hey everyone! It's your friendly neighbourhood WTD newsletter team, with our March edition.

Spring is here and the year is racing on, and can you believe it's getting close to conference time? We've just announced `speakers for our virtual Portland conference </conf/portland/2021/news/announcing-speakers/>`__, which is coming up on 25th-27th April. If you think those speakers look great (which of course you do!), you can get your tickets `here </conf/portland/2021/tickets/>`__.

And if Portland can't come soon enough, the West Coast Quorum meetup is holding its first virtual event this month! The event is about "The Product is Docs: A Look Inside" and will be held on Thursday 18th March at 19:00 Pacific Time. If you're interested, `sign up to attend <https://www.meetup.com/virtual-write-the-docs-west-coast-quorum/events/276616460/>`__.

This month we've seen a quite a number of style guide and "how do I write this" discussions, so we're trying something new: a newsletter on a theme! We hope you enjoy it :)

------------------------------------
A best practice by any other name...
------------------------------------

Is there an alternative for the term "best practices" in documentation? It's a commonly used and understood term (not to mention a commonly searched term), but sometimes it doesn't quite fit. It can sound authoritative -- who's to say that anyone knows the *best* practice for everyone else's environment? Also, best practices can change over time: what works best right now might not work as well as the months or years go by. And when users really need proscriptive instructions, best practices are probably too imprecise for the occasion.

If best practices are too inexact to satisfy user needs, try to reconfigure the information-formerly-known-as-best-practices as a narrow range of scenarios with a single solution. For example, instead of "Best practices for software installation, configuration, and testing", try topics like "Choose the installation method", "Configure the agent after installation", or "Confirm the agent is correctly installed." This covers the information users need and provides a definitive pathway they can follow.

For a straightforward terminology swap with a less-authoritative tone, consider these suggestions:

- Good practices
- Tips (and the variation "implementation tips")
- Guidelines (and the variation "implementation guidance")
- Proven methods
- Recommendations

These alternatives might work in some situations, but it's difficult to find an all-purpose replacement that readers will understand just as handily. For better or worse, "best practices" is meaningful because it communicates a common idea in any context without requiring wordy explanations. The search for an ideal replacement continues...but if you've grappled with this question yourself and came up with a better term, please do share it in the #general channel!

--------------------------------------------
And etcetera and et cetera. And so forth ...
--------------------------------------------

Are documentarians for or against latinisms like etc? A recent question on this produced a remarkable consensus - the newsletter team are so used to the answer "it depends"! 

So: don't use "etc" was the fairly unaninmous response: it's just too likely that readers will not know what it means. However, there was much less of a consensus on what to replace it with. Some, in the spirit of the widely recognized ban on latinisms, simply translated it into English, most commonly into "and so on." Others recommended writing around the term, typically in the form "such as <example_1> or <example_2>" to replace "<example_1>, <example_2>, etc."

Most agreed it's not worth making special effort to edit for only this offense. As some said, "it's in the backlog's backlog's backlog ..." So while nobody seems to like "etc", most acknowledged they let such things go more often than not, unless thez can see that these terms have become real stumbling blocks for users.

---------------------------
How to indicate UI elements
---------------------------

What's your style for marking UI elements in text? It's common to want to emphasize that something is (for example) a button so it stands out, whether you write it as the Save, *Save* or **Save** button. Why? It helps users to scan the document; and if your button is well-named, it should also match up to something the user is trying to find for the task at hand. Plus if UI text is in sentence case, this can result in confusing phrasing in docs, and emphasis can help the reader parse the sentence.

The difference between bold and italics isn't huge, but there is a bit of a choice here. Some contributors to the conversation felt that bolding really jumps off the page, and was the fastest way to get the reader's attention. (It's also what the Microsoft Manual of Style recommends.) In contrast, italics are a little subtler, and maybe better used for more general emphasis. Regardless of which you choose, you may want to mark up UI elements with a specific class or inline style, to make sure they're always styled the same way.

You've got to be a little careful, because a page filled with one or both types of emphasis gets pretty noisy. It's one reason that just following a style guide might not be enough - sometimes it's a judgement call about what makes a doc too busy and distracting.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by UX Writers Collective:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
              <a href="https://uxwriterscollective.com/ux-writing-for-tech-writers/">Add UX writing to your skillset.</a> In the new UX Writing for Technical Writers course from UX Writers Collective, you’ll learn key strategies to power up your docs, write for UI components, and how to advocate for better UX.
              </p>
              <p>
              Ready to become a hybrid writer? <a href="https://uxwriterscollective.com/ux-writing-for-tech-writers/">Explore the course syllabus.</a>
              </p>
          </td>
          <td width="25%">
            <a href="https://uxwriterscollective.com/">
              <img style="margin-left: 15px;" alt="UX Writers Collective" src="/_static/img/sponsors/uxwriters.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured job posts
------------------

- `DevRel Engineer - Documentation <https://jobs.writethedocs.org/job/277/devrel-engineer-documentation/>`__,  Teleport (remote)
- `Documentation Lead <https://jobs.writethedocs.org/job/291/documentation-lead/>`__, Hiro (remote)
- `Technical Writer <https://jobs.writethedocs.org/job/281/technical-writer/>`__, Datacoral Inc
- `API technical writer <https://jobs.writethedocs.org/job/290/api-technical-writer-contractor-f-m-d/>`__, Upvest (contract, remote)
- `Documentation Manager <https://jobs.writethedocs.org/job/287/documentation-manager/>`__, Timescale (remote)
- `Content Developer 2 <https://jobs.writethedocs.org/job/292/content-developer-2/>`__, Microsoft (remote / Redmond)
- `Part-time Documentation Contractor  <https://jobs.writethedocs.org/job/285/part-time-documentation-contractor/>`__, Tidelift (contract, remote US)
- `Technical Content Writer <https://jobs.writethedocs.org/job/294/technical-content-writer-b2b-opensource-sre-performance-testing/>`__, Load Impact AB (remote)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 08 March, 5pm GMT (Ireland) - `Virtual coffee chat <https://www.meetup.com/Write-The-Docs-Ireland/events/276735089/>`__
- 09 March, 6pm EST (Ottawa) - `WTD Ottawa Shopify Meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyccfbmb/>`__
- 09 March, 7:30pm MST (Calgary) - `March 2021 Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/275761130/>`__
- 10 March, 12pm GMT+11 (Australia) - `Remote: GitHub Open Source docs | The Doc Product Owner <https://www.meetup.com/Write-the-Docs-Australia/events/276122418/>`__
- 16 March, 8:30am EDT (Boston) - `Morning social <https://www.meetup.com/boston-write-the-docs/events/hqvdfsyccfbvb/>`__
- 18 March, 7pm GMT+1 (Barcelona) - `Git Basics Workshop with Anna Skoulikari <https://www.meetup.com/Write-the-Docs-Barcelona/events/276686508/>`__
- 18 March, 7pm PDT (West Coast US) - `The Product is Docs: A Look Inside <https://www.meetup.com/virtual-write-the-docs-west-coast-quorum/events/276616460/>`__
- 30 March, 8:30am EDT (Florida) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsyccfbnc/>`__
- 13 April, 8:30am EDT (Florida) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsyccgbrb/>`__
- 13 April, 6pm EDT (Ottawa) - `WTD Ottawa Shopify Meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyccgbrb/>`__
- 17 April, 7pm EDT (Toronto) - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/rwphwryccfbwb/>`__

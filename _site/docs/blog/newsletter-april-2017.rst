.. post:: April 3, 2017
   :tags: newsletter, bug report, metrics, git, cli, survey, stackoverflow

**************************************
Write the Docs Newsletter - April 2017
**************************************

Spring has Sprung!
##################

In the Northern Hemisphere, anyway. In the Southern Hemisphere, Fall has...fallen? Sounds good, let's go with it!

In both hemispheres, `Write the Docs Portland <http://www.writethedocs.org/conf/na/2017/>`_ approaches! We've announced the `presentations and speakers <http://www.writethedocs.org/conf/na/2017/news/announcing-presentations/>`_, and you can `get your ticket here <https://ti.to/writethedocs/write-the-docs-na-2017/>`_. We don't expect to sell out for another couple of weeks, but if you haven't made plans for May 14-16 yet, the perfect time is **soon**.


------------------------------------------

The Art of the Bug Report
#########################

First up this month, someone asked the channel for a good example of how to document a bug. The community came through with suggestions for a template that includes:

* Environment: affected software and versions
* Summary in narrative form, such as "While testing feature *x*, I encountered *z*."
* Steps to reproduce the bug
* Results and impacts, including severity level
* Workarounds
* Relevant diagnostics

But how to get that info into release notes? One participant reported his team's process:

1. Collect all JIRA issues (especially customer-reported issues)
2. Filter out internal code issues and QA tests
3. Rewrite the issue title so it's easy for readers to scan
4. Label issues so they're easy to sort
5. Use `this script <https://github.com/markcraig/release-notes-list-builder>`_ to transpose the issues (in JSON format) from JIRA into a DocBook block element for release notes

------------------------------------------

Documentation Metrics: What to Track and How
############################################

An interesting topic was swatted around the #watercooler this month: documentation metrics. Capturing the right information can definitely help us make targeted doc improvements, but the identifying that information – and capturing it – can be a bear. Some of the suggestions that came up included:

* Using referral links to track which docs people engage with the most and the least
* Tagging support requests to find the most relevant docs
* Using an analytics platform to identify which search terms are used most (or searched for but not found) and which results are most-clicked
* Adding :thumbsup: and :thumbsdown: rating options to collect helpfulness ratings from users

For a take on how one support team tracked the relationship between support and content, check out `this blog post from Campaign Monitor <https://www.campaignmonitor.com/blog/company/2013/09/yoda-our-support-ally/>`_.

-----------------------------

Starter Kit for Command Line Git
################################

Toward the end of the month, a request for an expert to help with learning command line Git resulted in an avalanche of resources. Here's what folks suggested for learning Git:

* `Git workshop at Write the Docs in May <http://www.writethedocs.org/conf/na/2017/speakers/#speaker-na-2017-matthew-desmond>`_
* `tryGit <https://try.github.io>`_
* `The SilverLogic Git Fire Drill <https://tsl.io/git-fire-drill/>`_
* `Pro Git by by Scott Chacon and Ben Straub <https://www.git-scm.com/book/en/v2>`_
* `Learn Git Branching <http://learngitbranching.js.org>`_

Also noted: there's nothing wrong with using Git in a desktop app or on the web! Folks mentioned `SourceTree <https://www.sourcetreeapp.com/>`_ and `Bitbucket <https://bitbucket.org/>`_ as GitHub alternatives.

The advice for those who want to feel more at home using command line Git? Practice, practice, practice--repetition makes perfect.

------------------------------------------

2017 Stack Overflow Developer Survey
####################################

The annual Stack Overflow Developer survey was released this month! https://stackoverflow.com/insights/survey/2017/. Among 2017's tidbits – which include findings on the most dreaded coding language and the feasibility of sharing an office with a noisy-keyboard-user – **more than 80% of respondents said that they use official documentation to learn**. That was even higher than the number who used Stack Overflow, who did the survey!

------------------------------------------

Looking Ahead
###############

Write the Docs Portland is right on the horizon, and Write the Docs Prague isn't going to be far behind! We'll be opening the CFP up shortly, so now is a great time to be thinking about a talk you might want to submit! In the meantime, if May (or September) are just too far away to bear, remember you can always check out `your nearest meetup <http://www.writethedocs.org/meetups/>`_, or `start one yourself <http://www.writethedocs.org/organizer-guide/meetups/starting/>`_!

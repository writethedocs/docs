.. post:: November 04, 2019
   :tags: newsletter

#########################################
Write the Docs Newsletter – November 2019
#########################################

Hello, everyone - it's the November edition of the newsletter!

The `Sydney conference </conf/australia/2019/>`__ is coming up in just a few short weeks, on 14th-15th November. Tickets are now sold out, but if you can't make it, don't worry - videos of the talks will be up on YouTube shortly after the conference.

Looking forward to next year, the site for `Portland 2020 </conf/portland/2020/>`__ is live, as is the `Call For Proposals </conf/portland/2020/cfp>`__. We'd love to hear all your awesome talk ideas, so get working on them! The CFP closes on 10th January, 2020.

Finally, we're formalizing how we change policies, by introducing `Write the Docs Enhancement Proposals </blog/introducing-weps/>`__. The community has mostly grown organically, but there have been some growing pains as we've expanded. Our processes are only loosely defined, which makes it harder for new people to understand who makes decisions and join in leadership positions. So we're trying WEPs, an idea taken from the open-source ecosystem, to formalize our decision-making. If you're interested, take a look at the `introduction blog post </blog/introducing-weps/>`__, which goes into more depth.

Onto this month's articles!

--------------------------------------
The strengths of different backgrounds
--------------------------------------

One of our most wide-ranging discussions this month put the breadth of documentarians' educational and work backgrounds on full display. It made pretty clear that technical documentation draws folks with an incredible variety of education and experience. Here's just a sample of some of the different backgrounds, and the strengths people feel they gained through them:

* Culinary arts and restaurants: experience with managing stress, coping in sink-or-swim situations, and working with diverse groups of people
* Customer support and tech support: lots of practice at explaining things; appreciation for the value of writing things down
* Education: well prepared to develop training curriculum and knowledge base content
* History, philosophy, religion, and ethics: strong reading, writing, and arguing skills, and especially the ability to write *quickly*
* Library and information science: familiar with information architecture, tools, and technologies
* Sociology and anthropology: keen human-centric insight and user-focused perspective
* Technical writing certification or degree: allowed to grow into the role; driven to constantly improve

We could fill an entire newsletter describing the paths people took to their roles in documentation. But no matter how our documentarians all found their way here, we're glad they did ❤️

---------------------------------------------------
Docs and design: When docs can't fix all the things
---------------------------------------------------

Much as we'd wish otherwise, we don't usually document perfectly usable software. (Is there such a thing?) And sometimes, the software we're documenting has major usability problems. A plaintive question about how to document a poorly designed product generated a range of responses - from how to provide feedback about the design and try to improve it, to how to hide or make less prominent less usable portions of the product.

So if you've got features that "don't make sense" or don't seem to fit into the rest of the product you're tasked with documenting, try these tips from our always-creative community:

- See whether you can persuade the product dev team to remove not-very-sensible features, or features that seem to have been included by mistake.
- Create an "Advanced Features" section of the docs and bury information about the features there.
- Keep the docs about the problematic thing short, but also provide brief warnings about any consequences of trying to use a feature - for example, if it works poorly or has unexpected consequences.
- Include a recommendation to contact Support before using the problem features (a bit passive-aggressive, but participants agreed that desperate times can call for desperate measures). If you do this, make sure to mention it to Support first!

-------------------------------------------
The challenge of giving difficult feedback 
-------------------------------------------

Learning how to give constructive criticism - which often really means "negative feedback" - is really important, but not easy, especially with colleagues you don't know well yet. A manager asked this month, and the community had this advice.

Firstly, giving negative feedback is painful, but you have to own it. Don't distance yourself by saying you're passing on other people's feedback when you believe it to be correct. And putting it off won't help in the long run. The longer you leave it, the more you're tacitly approving, and the more of a surprise the feedback will be.

You can help by making the feedback about behaviour and its outcomes, not the person or how you feel about them. A useful acronym here is BIO: say what Behavior you’re observing (with specific examples), the Impact it has, and give Options for doing it differently. On the impact: for example, if a writer isn't being concise enough, show how the longwindedness affects the reader. The extra information doesn't help the user achieve their goals, and actually gets in the way. 

And make sure you're also giving positive feedback when your report does things well! It can be tough when the only feedback you hear from your manager is negative.

Finally, if you're concerned about your report taking the feedback badly, it could be worth keeping documentation. If you're getting complaints about your report from colleagues, get those in writing, and write notes of your meetings with them too.

---------------------------------------------
"You"-sing the second person in documentation
---------------------------------------------

Referring to the reader in the `second person <https://en.wikipedia.org/wiki/Grammatical_person>`__ can make your writing feel more natural and friendly - but is it always the right choice? There are no hard and fast rules, but here are some guidelines.

In most end-user documentation, you can use the second person ("you should do the thing") rather than the third person ("the administrator should do the thing", when the admin is your audience). But there are some situations where second person doesn't work so well. It might be less appropriate if you're writing in a more formal context. If there are multiple types of readers / users of your system (for example, sysadmins and end users), it might be better to specify which one you're referring to, as "you" could be ambiguous.

You can sometimes avoid specifying the person altogether by writing in the imperative. (e.g., "To configure a new foo, use the set command.") This is good as it's clear and instructive, and often shorter. "You" and the imperative mood aren't mutually exclusive as the second person is the only possible implied subject.

But only using the imperative can sometimes seem a bit curt. If you like using the second person, but you're worried about having too many instances of the word "you" in a document, try mixing the second person with the imperative.

When in doubt, identify your audience, and see what your style guide has to say!

---------------------------------------------
From our sponsor: A survey on authoring tools
---------------------------------------------

This month's newsletter is sponsored by `JetBrains <https://www.jetbrains.com/>`__:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
              "Following the discussion on tools in the last newsletter: JetBrains is a cutting-edge software vendor specializing in the creation of intelligent development tools, who sponsored this year's Write The Docs Prague. They're running a survey about help authoring tools and markup languages that are popular among technical writers: <a class="reference external" href="https://surveys.jetbrains.com/s3/authoring-tools-nl">surveys.jetbrains.com/s3/authoring-tools-nl</a>. Please take a moment to share your experience, to help JetBrains get a bird’s eye view of the documentation developer ecosystem."
              </p>
          </td>
          <td width="25%">
            <a href="https://surveys.jetbrains.com/s3/authoring-tools-nl">
              <img alt="JetBrains" src="/_static/img/sponsors/jetbrains.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

---------
Job posts
---------

* `Software Documentation Evangelist <https://jobs.writethedocs.org/job/155/software-documentation-evangelist-m-f-d/>`__
   Contact Software GmbH - Bremen, Cologne or Berlin
* `Senior Technical Writer <https://jobs.writethedocs.org/job/160/senior-technical-writer/>`__
   NGINX - San Francisco
* `Senior Technical Writer <https://jobs.writethedocs.org/job/159/senior-technical-writer/>`__
   Klarna GmbH - Berlin
* `Senior Technical Content Writer <https://jobs.writethedocs.org/job/162/senior-technical-content-writer/>`__
   Instabase - Remote (North America)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

--------------------------
Community events coming up
--------------------------

- 5 November - Tel Aviv, Israel - `GitHub and Jira and Docs - oh my! <https://www.meetup.com/Write-The-Docs-TAplus/events/265349233/>`__
- 5 November - New York, NY, USA - `Lightning talks <https://www.meetup.com/WriteTheDocsNYC/events/265751514/>`__
- 6 November - Leeds, UK - `JAMStack for docs: a deep dive into Antora <https://www.meetup.com/Write-the-Docs-North/events/265096599/>`__
- 7 November - Austin, TX, USA - `ATX lunch meetup <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/265377459/>`__
- 9 November - Bengaluru, India - `Documentation, design and driving initiatives <https://www.meetup.com/Write-the-Docs-India/events/265991392/>`__
- 12 November - Bellevue, WA, USA - `Eastside morning social <https://www.meetup.com/Write-The-Docs-Seattle/events/265937099/>`__
- 14 November - Sydney, Australia - `Write the Docs Australia conference 2019! </conf/australia/2019/>`__
- 14 November - London, UK - `Localisation and Guerilla graphics <https://www.meetup.com/Write-The-Docs-London/events/265681650/>`__
- 14 November - Indianapolis, IN, USA - `November meetup <https://www.meetup.com/Write-the-Docs-Indy/events/265907667/>`__
- 14 November - Los Angeles, CA, USA - `Sean Marquez and TODO task management <https://www.meetup.com/Write-the-Docs-LA/events/265804790/>`__
- 19 November - Austin, TX, USA - `ATX happy hour meetup <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/265298825/>`__
- 19 November - Boston, MA, USA - `Collaborating with UX Designers <https://www.meetup.com/Write-the-Docs-BOS/events/266142147/>`__
- 20 November - Toronto, Canada - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqyzpbbc/>`__
- 21 November - Stockholm, Sweden - `UX and technical writing <https://www.meetup.com/Write-the-Docs-Stockholm/events/265899795/>`__
- 26 November - Ottawa, Canada - `Ottawa Shopify meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyzpbqb/>`__
- 27 November - Dublin, Ireland - `Minimalism in technical communication <https://www.meetup.com/Write-The-Docs-Ireland/events/266134530/>`__
- 04 December - Chicago, IL, USA - `Holiday meetup <https://www.meetup.com/Write-the-Docs-Chicago/events/263576210/>`__

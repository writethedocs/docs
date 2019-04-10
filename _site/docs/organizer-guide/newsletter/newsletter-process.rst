Write the Docs Newsletter
#########################

At the beginning of every month, we put out an email newsletter to the community. It's built around a handful of stories that we capture and write-up from the Slack team, and also includes an overview of what the org team is working on and a calendar listing of upcoming events.

In this doc, we'll cover all of the pieces that go into putting the newsletter out each month.

Tag stories in Slack (throughout the month)
********************************************

The newsletter team keeps an eye on the WTD Slack and flags conversations they think might be a good fit by tagging them with the ``:newsletter:`` emoji. We've added the 'Reacji Channeler' plug-in to automatically send the tagged post to the #newsletter-slushpile channel.

The editor will have the slushpile channel set to send notifications, so they have a chance to copy and paste conversation into a txt file locally. (So nothing gets swallowed up by the Slack limit.)

We look for a variety of conversations topics, and usually end up capturing ~10 or so, from which we end up picking 4.

Some of the things we look for are:

* conversations that yield a lot of practical advice about a topic
* conversations that clearly strike a chord with the audience
* conversations that highlight two sides of a docs problem/topic

Assign stories (7-10 days before shipping)
*******************************************

A week before the planned ship date, the editor will go through the conversations they've captured, and do two things:

* Flag four conversations they think would make good stories (looking for a good balance and some fresh or timely topics).
* Add a copy of all of the conversation to the shared 'Slushpile' dropbox folder.

From there, in the #newsletter channel on Slack, they'll @mention their writers and ask them to pick a story for the month. They'll point them to the slushpile folder so they can have a look, and set a deadline to have drafts back, 2-3 days before shipping.

Assemble & review the newsletter (2-3 days before shipping)
************************************************************

Once all the story drafts have come in, it's time to assemble. They'll start with the ``newsletter-TEMPLATE-2017.rst`` document, and start to fill it in.

The top section is an Editor's letter, which just serves as a quick greeting and introduction, and touches on any big things happening in the community during the month. This usually clocks in at 100-150 words.

Next comes the stories. They should be edited for length and clarity and tone, as well as to make sure they've followed the :doc:`editorial-guidelines`.

Finally, the upcoming events sections covers any upcmoing community events or conferences, and then lists out any meetups that are scheduled for the next month. It's important to include any meetups that happen in the first week or so of the following month, since the newsletter doesn't usually go out right on the first.

Gathering the meetup dates is done (for now – we're working on a better process) by going to Meetup.com and searching for "Write the Docs", selecting 'Any Distance' next to your location, and selecting 'All Meetups' from the filters in the sidebar. Then go through the list and copy out the date, location, and title for the meetup, and link it to the specific event page.

When the content for the newsletter is all in place, upload the file to a new branch on GitHub in ``www/docs/blog``. Create a pull request and share in the #newsletter channel for review.

Allow 1-2 days for folks to review and leave comments. (Not *everyone* has to review it, but 2-3 sets of extra eyeballs is ideal.)

Resolve all comments, and then when you're ready to send it, merge your Pull Request (which will take it live on the WTD site).

Ship the newsletter (no days before shipping)
**********************************************

Once you've finalized the newsletter in GitHub, you'll use MailChimp to send it out. You'll need the a MailChimp login, and to be added to the Write the Docs organization.

#. Login to MailChimp
#. Click the **Create** or **Create Campaign** button.
#. On the next screen, choose **Email**.
#. Name the campaign 'Write the Docs Newsletter - [MONTH - YEAR]'
#. In the 'To' section, click **Add recipients**.
#. From the **List** dropdown select 'Write the Docs Community`.
#. From **Segment or tag** choose 'Newsletter folks'.
#. Click the **Save** button.
#. In the 'From' section, click **Edit From**.
#. Change the **Name** to 'Write the Docs Newsletter'.
#. Change the **Email address** to 'newsletter@writethedocs.org'.
#. Click the **Save** button.
#. In the 'Subject' section, click **Add subject**.
#. In **Email Subject**, add 'Write the Docs Newsletter - [MONTH - YEAR]'
#. In **Preview  Text** add the first two sentences of the newsletter (ish – whatever makes a nice intro).
#. Click the **Save** button.
#. In the 'Content' section, click **Design Email**.
#. On the 'Select a template' screen, switch to the 'Saved themes' tab.
#. Choose the 'WTD Newsletter 2018' template.
#. On the next screen, hover over the body of the newsletter and click the **Edit** button.
#. Switch to Github, and open the newsletter file in 'Preview' mode.
#. Select the whole newsletter and copy.
#. Switch back to MailChimp and paste it in body textbox.
#. Give it a read through in the preview pane. Usually the paste in from GH introduces a little bit of weirdness.
#. Click the **Save & Close** button in the editor.
#. Then hit the big **Save & Close** button at the bottom of the page.
#. Click the **Send a test email** link under the little (pointless?) preview window.
#. Select a couple of emails from the list and click **Send Test**.
#. Review the test emails, check all the links, fix any typos, etc.
#. When you're ready to go, flip back to Mailchimp and click the **Send** button.
#. Contemplate the monkey-hand button for a second, and then click **Send Now**.
#. High five the monkey (you know you want to), and enjoy the rest of your day.

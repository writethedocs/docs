Learn Git by editing the Write the Docs website
===============================================

Identify the page you want to edit
----------------------------------

1. Find an `existing issue`_, or a page you want to improve.
2. In the repo UI, find the file that corresponds to the page. For
   example:
   https://www.writethedocs.org/documentarians/ is produced by
   ``/docs/documentarians.rst``. (You’ll need this filename later for
   making changes on your local copy.)
3. This is a ReStrucuredText (``.rst``) file, so you may want to review the
   `RST documentation`_. Other common markup formats are Markdown (``.md``)
   and AsciiDoc (``.adoc``).

Prerequisites
-------------

1. `Create a GitHub account`_.
2. `Download and install Git`_.
3. Open a terminal window and follow the instructions to `associate your
   GitHub username with your local Git installation`_.

   1. In macOS: Open the **Terminal** app.
   2. In Windows: From the Start Menu, open **Git Bash**.

Start using Git and modify the source file of a page
----------------------------------------------------

1.  Visit the `Write the Docs www project`_.

2.  Click the **Fork** button in the upper-right corner to create a
    copy of the project in your GitHub account. The new page for the
    forked project opens.

3.  Click the **Clone or download** button and copy the https URL from
    the project page.

4.  Open a terminal window so that you can run ``git`` commands.

    1. In macOS: Open the **Terminal** app.
    2. In Windows: From the Start Menu, open **Git Bash**.

5.  In your terminal window, type ``git clone``, followed by a space,
    and then paste the project URL:

    ::

       git clone https://github.com/myname/www.git

6.  Press Enter. The command copies files from GitHub to a folder named
    ``www`` on your local machine.

7.  In the terminal window, go to the ``www`` directory.

    ::

       cd www

8.  Create and switch to a branch. Using the commands below,
    replace ``branch-name`` with a name that briefly describes the
    changes you’ll make, preferably use dashes between words. For
    example, ``important-typo-fix``.

    a. Create a branch with:

       ::

          git branch branch-name

       Switch to the branch:

       ::

          git checkout branch-name

    b. Alternatively, use one command to perform both steps at once:

       ::

          git checkout -b branch-name

9. Open the ``www`` folder on your computer.

10. | Open the file you wish to edit using a text editor like `Sublime
      Text`_ or `Visual Studio Code`_, then save the file.

11. In your terminal window, type:

    ::

       git status

    This will show you all the files that you have updated.

12. If your changes look accurate, enter the following in your terminal window:

   ::

      git add -A

   This will add any new and changed files to your local project.

13. To save your changes, enter the following in your terminal window:

   ::

      git commit -m "Your message"

   This will save all of your edited files. Replace ``Your message``
   with a description of the update you made. *Protip*: Learn how
   to `write a good commit message`_.

   You can repeat the same process to add multiple commits in your
   branch.

14. Send your commit(s) to your GitHub project using ``git push``. Enter the following in your terminal window:

   ::

      git push -u origin branch-name

15. Create a `GitHub pull request`_ in the `Write the Docs www project`_.


.. _existing issue: https://github.com/writethedocs/www/issues
.. _RST documentation: https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html
.. _Create a GitHub account: https://github.com/join
.. _Download and install Git: https://git-scm.com/downloads
.. _associate your GitHub username with your local Git installation: https://help.github.com/en/articles/setting-your-username-in-git
.. _Write the Docs www project: https://github.com/writethedocs/www
.. _Sublime Text: https://www.sublimetext.com
.. _Visual Studio Code: https://code.visualstudio.com/
.. _write a good commit message: https://chris.beams.io/posts/git-commit/
.. _GitHub pull request: https://help.github.com/en/articles/creating-a-pull-request
.. _Write the Docs www project: https://github.com/writethedocs/www

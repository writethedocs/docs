Testing your Documentation
==========================

Testing your documentation allows you to make sure it is in a consistent state.
Doing this gives your users a better experience,
and reduces stress around common issues as a writer.

This `article <https://opensource.com/business/15/7/continuous-integration-and-continuous-delivery-documentation>`_ by Anne Gentle is a good place to start to understand this concept.

Continuous Integration
----------------------

The most useful tests are run on each commit of your project.
This is called **Continuous Integration**,
and is a common practice in the software development world.

We recommend checking out the following tools to get started:

* `Travis CI <http://travis-ci.org>`_ (GitHub only, free for open source)
* `AppVeyor <https://www.appveyor.com/>`_ (Windows support, free for open source)

Build Errors
------------

The easiest automated check to do is to make sure your documentation builds
properly. This requires simply running your documentation tool, and checking
that it has properly built your documentation.

Most tools will return an *error code* of 0 if the process is successful. This
means you should just be able to do a normal build of your tool, and your
testing tool will know if it is successful or not.

If your build tool has a *picky* mode that flags warnings that *might* be
problematic as well as errors, it might make sense to switch it on, but you'll
want to make sure that your documentation is in good shape before you do.

* Sphinx has `nitpicky mode <http://www.sphinx-doc.org/en/stable/config.html#confval-nitpicky>`_.
* Jekyll has `strict mode <https://jekyllrb.com/docs/configuration/#liquid-options>`_.

Link Testing
------------

Making sure all the hyperlinks in your docs are working is a really great place to start.
This makes sure your users don't hit dead ends,
and is quite simple in terms of automation.

You can either:

* Use a tool provided with your documentation tools
* Treat your rendered documentation as a normal website, and use a website link checker

These are the tools we know with proper link checking:

Sphinx
~~~~~~

Sphinx ships with a ``linkcheck`` `builder <http://www.sphinx-doc.org/en/stable/builders.html>`_ as a default.
You can run it with a simple::

    make linkcheck

It's output looks something like this:

.. image:: /_static/img/guide/sphinx-linkcheck.png

Jekyll
~~~~~~

Jekyll has a few plugins that support link checking:

* https://github.com/endymion/link-checker
* https://github.com/fastly/jekyll-sanity-checker

HTMLProofer
~~~~~~~~~~~

`HTMLProofer <https://github.com/gjtorikian/html-proofer>`_ checks links in
HTML, as well as images, titles and tag validity.

Style Guide Checking and Linting
----------------------------------

Linters are tools that automatically verify specific rules against your code or
documentation. This is useful for enforcing a style guide,or for catching
commonly mitaken branding issues.

Here are a few links that might be interesting:

* https://www.mapbox.com/blog/retext-mapbox-standard/
* https://krausefx.com/blog/writing-automated-tests-for-your-documentation


Vale
----

Vale is a syntax-aware linter for prose built for speed and extensibility.

https://github.com/errata-ai/vale

It ships with the following default styles:

* `Proselint <https://github.com/amperser/proselint>`_
* `Write-good <https://github.com/btford/write-good>`_
* `Joblint <https://github.com/rowanmanning/joblint>`_

Several organizations have also created styles for use with Vale. Some of these
styles have been collected in the following repository: https://github.com/testthedocs/vale-styles .

To configure Vale, follow the instructions in the README. If needed, install
the *vale* binary as an executable in your $PATH, so you can run *vale* directly
from the command line. For example, on UNIX/Linux systems, you can copy vale
to the /usr/local/bin directory.

After installing Vale, run the following commands to check for proper installation:

$ vale
$ vale dc

If you see empty JSON in the output to the second command, you've successfully
installed Vale.

Now to configure Vale, you'll need a .vale or a .vale.ini configuration file. For some
examples, see

* https://github.com/writethedocs/www/blob/master/.vale
* https://github.com/cockroachdb/docs/blob/master/.vale.ini
* https://github.com/linode/docs/blob/develop/.vale.ini

While it's possible to install the Vale configuration file in different locations,
it may be most convenient to install it in the root directory of your target
repository, as shown in the noted examples.

Once configured for your repository, you should be able to navigate to your
repository path, and then run `vale dc` to confirm your configuration.

You can then apply Vale as a grammar linter directly to your source files, with
a command like:

$ vale /path/to/someText.md

Hint: Vale even works with XML files, such as those in DocBook and DITA, as long
as you've included *.xml in the Vale configuration file.
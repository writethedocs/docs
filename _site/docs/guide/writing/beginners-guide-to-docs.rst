A beginner's guide to writing documentation
===========================================

.. note:: This is a write up of a `Presentation <https://speakerdeck.com/ericholscher/writing-docs-a-beginners-guide-to-writing-documentation>`_ .
          Please provide feedback to `@ericholscher`_.
          You can view the source on `GitHub`_.

.. _@ericholscher: http://twitter.com/ericholscher
.. _GitHub: https://github.com/writethedocs/www/blob/master/docs/guide/writing/beginners-guide-to-docs.rst

..

	| Camera pans from stage left.
	| It shows a text editor, open to a blank page.
	| A person hunched in front, head to desk.

The scene above is well known to everyone who writes for a living;
the mixed emotions of a blank page.
Full of excitement, fresh with a new beginning.
Yet also full of despair, where do you even start?

I am here to stop this scene from playing out.

This is a guide to documenting your first project.
The first time is always the hardest,
and I hope this guide will get you started down the righteous path.
At the end,
you should have a project that is ready for public release.

Feel free to read this document straight through,
or simply use it as a reference.

.. _why:

Why write docs
--------------

You will be using your code in 6 months
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code that you wrote 6 months ago is often indistinguishable from code that someone else has written.
You will look upon a file with a fond sense of remembrance.
Then a sneaking feeling of foreboding,
knowing that someone less experienced, less wise, had written it.

As you go through this selfless act of untangling things that were obvious or clever months ago,
you will start to empathize with your users.
If only I had written down why I had done this.
Life would be so much simpler.
Documentation allows you to transfer the *why* behind code.
Much in the same way code comments explain the *why*,
and not the *how*,
documentation serves the same purpose.

.. sidebar::  Sidebar on open source

	There is a magical feeling that happens when you release your code.
	It comes in a variety of ways, but it always hits you the same.
	*Someone is using my code?!*
	A mix of terror and excitement.

		| I made something of value!
		| What if it breaks?!
		| I am a real open source developer!
		| Oh god, someone else is using my code..

	Writing good documentation will help alleviate some of these fears.
	A lot of this fear comes from putting something into the world.
	My favorite quote about this is something along these lines:

		| Fear is what happens when you're doing something important.
		| If you are doing work that isn't scary,
		| it isn't improving you or the world.

	Congrats on being afraid!
	It means you're doing something important.

You want people to use your code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have written a piece of code,
and released it into the world.
You have done this because you think that others might find it useful.
However,
people need to understand why your code might be useful for them,
before they decide to use it.
Documentation tells people that this project is for them.

	| If people don't know why your project exists,
	| they won't use it.
	| If people can't figure out how to install your code,
	| they won't use it.
	| If people can't figure out how to use your code,
	| they won't use it.

There are a small number of people who will source dive and use any code out there.
That is a vanishingly small number of people,
compared to people who will use your code when properly documented.
If you really love your project,
document it,
and let other people use it.


You want people to help out
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open source is this magical thing right?
You release code,
and the code gnomes come and make it better for you.

Not quite.

There are lots of ways that open source is amazing,
but it doesn't exist outside the laws of physics.
You have to put work in,
to get work out.

	| You only get contributions after you have put in a lot of work.
	| You only get contributions after you have users.
	| You only get contributions after you have documentation.

Documentation also provides a platform for your first contributions.
A lot of people have never contributed before,
and documentation changes are a lot less scary than code changes.
If you don't have documentation,
you will miss out on a whole class of contributors.

You want your code to be better
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's really easy to have an idea in your head that sounds perfect,
but the act of putting words to paper requires a distillation of thought that may not be so easy.

Writing documentation improves the design of your code.
Talking through your API and design decisions on paper allows you to think about them in a more formalized way.
A nice side effect is that it allows people to contribute code that follows your original intentions as well.

You want to be a better writer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writing documentation is a different form of writing than most people have experience with.
Technical writing is an art that doesn't come naturally.
Writing documentation will start you down the road to being a better technical writer,
which is a useful skill to have as a programmer.

Writing also becomes easier over time.
If you don't write for many months,
it is a lot harder to start writing again.
Keeping your projects documented will keep you writing at a reasonable cadence.

Starting simple is the best way to achieve actual results.
I will present a well-paved path to walk down,
and after you have the basic idea,
you can expand your scope.
The tools should be powerful and easy to use.
This removes obstacles to actually putting words on the page.

.. _markup_languages:

.. sidebar:: Sidebar on markup languages.

   The examples in this document are both valid `Markdown`_ and `reStructuredText`_.
   reStructuredText is a bit harder to use,
   but is more powerful.
   I recommend that you check them both out,
   and decide which you want to use going forward.

.. _reStructuredText: http://sphinx-doc.org/rest.html#rst-primer
.. _Markdown: http://daringfireball.net/projects/markdown/

Version controlled plain text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As programmers we live in a world of plain text.
Our documentation tooling should be no exception.
We want tools that turn plain text into pretty HTML.
We also have some of the best tooling available for tracking changes to files.
Why would we forgo using those tools when writing documentation?
This workflow is powerful, and familiar to developers.


Basic Example
~~~~~~~~~~~~~

::

	Resources
	---------

	* Online documentation: http://docs.writethedocs.org/
	* Conference: http://conf.writethedocs.org/

This will render into a header,
with a list underneath it.
The URLs will be hyperlinked automatically.
It's easy to write,
still makes sense as plain text,
and renders nicely into HTML.

README
~~~~~~

Your first steps in documentation should go into your README.
Code hosting services will render your README into HTML automatically if you provide the proper extension.
It is also the first interaction that most users will have with your project.
So having a solid README will serve your project well.

Some people even go as far as to `start your project with a README`_

.. _start your project with a README: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html

.. _write:

What to write
-------------

Now we're getting down to the brass tacks.
Making sure that you give your users all the information that they need,
but not too much.

First, you need to ask yourself who you're writing for.
At first,
you generally just need to appeal to two audiences:

* Users
* Developers

Users are people who simply want to use your code,
and don't care how it works.
Developers are people who want to contribute back to your code.

What problem your project solves
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lot of people will come to your docs trying to figure out what exactly your project is. Someone will mention it, or they'll google a phrase randomly. You should explain what your project does and why it exists. Fabric_ does a great job of this.

.. _Fabric: http://docs.fabfile.org/

A small code example
~~~~~~~~~~~~~~~~~~~~

Show a telling example of what your project would normally be used for. Requests_ does a great example of this.

.. _Requests: http://docs.python-requests.org/en/latest/index.html

A link to your code & issue tracker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People like to browse the code sometimes. They might be interested in filing bugs against the code for issues they've found. Make it really easy for people who want to contribute back to the project in any way possible. I think the `Python Guide`_ does a good job with the link to the code portion.

.. _Python Guide: http://docs.python-guide.org/en/latest/index.html

Frequently Asked Questions (FAQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lot of people have the same problems. If things happen all the time, you should probably fix your documentation or the code, so that the problems go away. However, there are always questions that get asked about your project, things that can't be changed, etc. Document those, and **keep it up to date**. FAQs are generally out of date, but when done well, they are a golden resource. Tastypie_ did a great job with this, with their "Cookbook" concept.

.. _Tastypie: http://django-tastypie.readthedocs.org/en/latest/cookbook.html

How to get support
~~~~~~~~~~~~~~~~~~

Mailing list? IRC Channel? Document how to get help and interact with the community around a project. Django_ does a great job with this.

.. _Django: https://docs.djangoproject.com/en/1.8/faq/help



Information for people who want to contribute back
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People usually have standards for how they expect things to be done in their projects. You should document these so that if people write code, they can do things in the norm of the project. `Open Comparison`_ does a great job of this.

.. _Open Comparison: http://opencomparison.readthedocs.org/en/latest/contributing.html


Installation instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

Once people figure out whether they want to use your code or not, they need to know how to actually get it and make it run. Hopefully your install instructions should be a couple lines for the basic case. A page that gives more information and caveats should be linked from here if necessary. I think at `Read the Docs`_ we do a good job with this.

.. _Read the Docs: http://read-the-docs.readthedocs.org/en/latest/install.html


Your project's license
~~~~~~~~~~~~~~~~~~~~~~~

BSD? MIT? GPL? This stuff might not matter to you, but the people who want to use your code will care about this a whole lot. Think about what you want to accomplish with your license, and please only pick one of the standard licenses that you see around the web.

.. _template:


Next Steps
----------

After you follow the above guide,
we know your project will be successful!
For further reading,
check out this post on `how to maintain an open source project`_.

.. _how to maintain an open source project: https://medium.com/p/aaa2a5437d3a

Template
--------

A simple template for you to start with,
for your ``README``.
Name the file ``README.md`` if you want to use markdown,
or ``README.rst`` if you want to use reStructuredText.
More information about these can be found in the :ref:`sidebar on markup <markup_languages>`.

::

	$project
	========

	$project will solve your problem of where to start with documentation,
	by providing a basic explanation of how to do it easily.

	Look how easy it is to use:

	    import project
	    # Get your stuff done
	    project.do_stuff()

	Features
	--------

	- Be awesome
	- Make things faster

	Installation
	------------

	Install $project by running:

	    install project

	Contribute
	----------

	- Issue Tracker: github.com/$project/$project/issues
	- Source Code: github.com/$project/$project

	Support
	-------

	If you are having issues, please let us know.
	We have a mailing list located at: project@google-groups.com

	License
	-------

	The project is licensed under the BSD license.

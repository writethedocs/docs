=================================================
Introduction to reStructuredText
=================================================

What is reStructuredText?
----------------------------

`reStructuredText <http://docutils.sourceforge.net/rst.html>`_ is a lightweight markup language that is used in static site generators like :doc:`Sphinx <../tools/sphinx>`. It contains robust tools for semantic markup, reusing content, and content filters for different kinds of outputs. It's also easily extendible using `custom directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_ that you can create yourself, allowing you to satisfy a wide variety of documentation needs.

reStructuredText is widely used for Python documentation---both for the `Python language itself <https://docs.python.org/3/tutorial/index.html>`_ and for Python libraries.

Why use reStructuredText?
----------------------------

reStructuredText is a lightweight markup language, so it's easier to read in plain-text format compared to heavier markup languages like DITA and other XML-based formats. You can easily find text editors that render reStructuredText with syntax highlighting and live previews, without having to invest in complex tools.

Compared to some other lightweight markup languages like :doc:`MarkDown <Markdown_basics>`, reStructuredText contains stronger semantic markup tools. `Some writers <http://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/>`_ also prefer reStructuredText because the markup standards are more well-defined compared to MarkDown.

How to use reStructuredText
-----------------------------------

Formatting the main text
~~~~~~~~~~~~~~~~~~~~~~~~~~

Paragraphs in reStructuredText are blocks of text separated by at least one blank line. All lines in the paragraph must be indented by the same amount.

Inline markup for font styles is similar to MarkDown:

* Use one asterisk (``*text*``) for italics
* Use two asterisks (``**text**``) for bolding
* Use two backticks (````text````) for code samples.
* Links to external sites contain the link text and a bracketed URL in backticks, followed by an underscore: ```Link to Write the Docs <http://www.writethedocs.org/>`_``.

Headers
~~~~~~~~~~~~~~~~~~~

Headers are demarcated by non-alphanumeric characters like dashes, equal signs, or tildes. Use the same character for headers at the same level. The following creates a header::

  ===============
  Chapter 1
  ===============

If inserted in the same document, this creates a header at a different level::

  Section 1.1
  ------------------

Having an underline-only is acceptable, as is having both an underline and an overline. If you use the same non-alphanumeric character for underline-only and underline-and-overline headers, they will be considered to be at *different* levels.

The row of non-alphanumeric characters should have at least as long as the header text.


Lists
~~~~~~~~~~~~~~

For enumerated lists, use a number or letter followed by a period, or followed by a right-bracket, or surrounded by brackets::

  1. Use this format the numbers in your list like 1., 2., etc.

  A. To make items in your list go like A., B., etc. Both uppercase and lowercase letters are acceptable.

  I. Roman numerals are also acceptable, uppercase or lowercase.

  (1) Numbers in brackets are acceptable.

  1) So are numbers followed by a bracket.

For bulleted lists, use indentation to indicate the level of nesting of a bullet point. You can use ``-``, ``+``, or ``*`` as a bullet point character::

  * Bullet point
    
    - nested bullet point
      
      + even more nested bullet point

Code Samples
~~~~~~~~~~~~~~~~~~~

To display code samples, or any text that should not be formatted, end the paragraph prior to the code sample with two colons (``::``) and indent the code sample::

  This is the paragraph preceding the code sample::

    #some sample code


 
Resources
-------------------

* `A ReStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_
* `reStructuredText Primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Cheatsheet <https://github.com/ralsina/rst-cheatsheet>`_

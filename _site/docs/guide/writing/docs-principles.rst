Documentation Principles
========================

Software development benefits from `philosophies`_ and `principles`_ such as
`DRY`_, `KISS`_, `code reuse`_, and many more. With these commonly understood
and accepted standards, developers can hold themselves and each other
accountable to producing high-quality code.

.. _philosophies: https://en.wikipedia.org/wiki/Category:Software_development_philosophies
.. _principles: https://en.wikipedia.org/wiki/Category:Programming_principles
.. _DRY: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
.. _Don't Repeat Yourself: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
.. _KISS: https://en.wikipedia.org/wiki/KISS_principle
.. _Code Reuse: https://en.wikipedia.org/wiki/Code_reuse

This set of principles seeks to define similar standards for software
*documentation* that, when practiced, will foster clean and intuitive
content. The end goal is ultimately to delight and empower readers by
making information easier for them to acquire.

Overview, by component
----------------------

All documentation
~~~~~~~~~~~~~~~~~

In general, documentation should be...

* `Precursory <#precursory>`__
* `Participatory <#participatory>`__

Content
~~~~~~~

*"Content" is the conceptual information within documentation.*

**Content** should be...

* `ARID <#arid>`__
* `Skimmable <#skimmable>`__
* `Exemplary <#exemplary>`__
* `Consistent <#consistent>`__
* `Current <#current>`__

Sources
~~~~~~~

*A "source" refers to a system used to store and edit content.
Examples of sources include: text files written using
reStructuredText or Markdown, HTML content in a CMS database, help
text stored within strings in application code, code comments to be
assembled later into formalized documentation, and others too.*

All **sources** should be...

* `Nearby <#nearby>`__
* `Unique <#unique>`__


Publications
~~~~~~~~~~~~

*A "publication" refers to a single, cohesive tool that readers use to consume
documentation.
It may be static or interactive — digital or paper. Multiple
publications may be created from a single source (such as web and PDF
versions of the same manual). Although rarer, multiple sources may
be used to create a single publication. More examples of
publications include: API reference, man page, command line
``--help`` output, in-application help tips, online tutorials,
internal engineering manuals, and others too.*

Each **publication** should be...

* `Discoverable <#discoverable>`__
* `Addressable <#addressable>`__
* `Cumulative <#cumulative>`__
* `Complete <#complete>`__
* `Beautiful <#beautiful>`__

Body
~~~~

*A "body" refers to the collection of all the publications within a software
project and any of its sub-projects*

A documentation **body** should be...

* `Comprehensive <#comprehensive>`__


===============================================================================


In general, documentation should be...
--------------------------------------

Precursory
~~~~~~~~~~

*Begin documenting before you begin developing.*

Before coding, write requirements and specifications that also serve as
the first draft of documentation. These texts no doubt will need a bit
of clean up before publishing, but by front-loading the documentation,
you lay a clear path forwards. Early documentation also helps facilitate
peer feedback and group decisions to guide your work. This model is the
sentiment behind :ref:`documentation-driven-design`.

Participatory
~~~~~~~~~~~~~

*In the documentation process, include everyone from developers to end
users.*

Integrate documentation into the standard workflow of developers, and
seek to reduce silos that solicit documentation from only a subset of
the software's contributors. Developers and engineers are the people
with the best access to in-demand information, and getting them to
document it will help foster a *culture* of documentation.

As well, documentation *readers* (i.e., users) should have clear avenues
towards involvement in documentation. A good first step is to give
readers the ability to offer feedback in the form of comments or
suggestions. Allowing readers to edit documentation directly (e.g., in a
wiki) can also be effective but must be weighed against the need and
capacity for editorial oversight.

Encourage *everyone* to become a :doc:`documentarian </documentarians>`!

Content should be...
--------------------

ARID
~~~~

*Accept (some) Repetition In Documentation.*

If you want to write good code, `Don't Repeat Yourself`_. But
if you adhere strictly to this DRY principle when writing documentation,
you won't get very far. *Some* amount of business logic described by
your code will need to be described *again* in your documentation.

In an ideal world, an automated system would generate documentation from
the software's source code, *and* the system would be smart enough to
generate *good* documentation without any additional input.
Unfortunately we do not (yet) live in that world, and today the best
documentation is hand-written, which means that just by writing *any*
documentation, you are repeating yourself. Sure, `documentation generators`_
exist and are useful, but it's important to acknowledge that they still
require input from humans to function.

.. _documentation generators: http://en.wikipedia.org/wiki/Comparison_of_documentation_generators

The pursuit of *minimizing* repetition remains valiant! ARID does not mean
`WET`_, hence the word choice. It means: try to keep things *as DRY as possible*
but also recognize that you'll inevitably need some amount of "moisture"
to produce documentation.

.. _WET: https://en.wikipedia.org/wiki/Don't\_repeat\_yourself#DRY\_vs\_WET\_solutions

Cultivating an awareness of this inconvenient truth will hopefully be a
helpful step toward reminding developers that a need often exists to
update documentation along with code.

Skimmable
~~~~~~~~~

*Structure content to help readers identify and skip over concepts which
they already understand or see are not relevant to their immediate
questions.*

Burying concepts in prose and verbiage demands more time from readers
seeking answers to specific questions. Save your readers' time by
writing like a newspaper instead of a novel.

Specifically:

-  Headings — should be descriptive and concise.
-  Hyperlinks — should surround words which describe the link itself
   (and never phrases like "click here" or "this page").
-  Paragraphs and list items — should begin with identifiable concepts
   as early as possible.

Exemplary
~~~~~~~~~

*Include (some) examples and tutorials in content.*

Many readers look first towards examples for quick answers, so including
them will help save these people time. Try to write examples for the
most common use cases, but not for everything. Too many examples can
make the documentation less `skimmable <#skimmable>`__. Also, consider
separating examples and tutorials from more dense reference information
to further help readers skim.

Consistent
~~~~~~~~~~

*Use consistent language and formatting in content.*

The more content editors you have, the more important a `style guide`_
becomes in facilitating consistency. Consistency also helps make documentation
`skimmable <#skimmable>`__ and `beautiful <#beautiful>`__.

.. _style guide: http://www.writethedocs.org/guide/writing/style-guides/

Current
~~~~~~~

*Consider incorrect documentation to be worse than missing
documentation.*

When software changes faster than its documentation, the users suffer.
Keep it up to date.

Make every effort to write content that is version-agnostic and thus in
less need of maintenance. For example, generalize version numbers of
software when they occur in tutorials (such as extracting a source code
tarball with the version number in the file name).

Be aware as well that some users will remain on older versions of your
software, and thus require older versions of your documentation. Proper
documentation platforms will accommodate such needs gracefully.

Sources should be...
--------------------

Nearby
~~~~~~

*Store sources as close as possible to the code which they document.*

Give developers systems which allow them to easily make documentation
changes along with their code changes. One way is to store documentation
content in comment blocks within application source code. Another is to
store it in separate text files but within the same repository as the
application's source code. Either way, the goal is merge (as much as
possible) the workflows for development and documentation.

Unique
~~~~~~

*Eliminate content overlap between separate sources.*

Storing content in different sources is okay, as long as the scope of
each source is clearly defined and disjoint with other sources. The goal
here is to prevent any parallel maintenance (or worse — *lack* of
maintenance) of the same information across multiple sources.

Each publication should be...
-----------------------------

Discoverable
~~~~~~~~~~~~

*Funnel users intuitively towards publications through all likely
pathways.*

Try to identify everywhere the user might go looking for documentation,
and in all of those places, insert helpful pointers for them to find it.
Documentation need not *exist* in all of these places, just pointers to
it.

If a user manual is published in the woods, and no one is around to read
it, does it exist? `Discoverability`_ says "no".

.. _Discoverability: https://en.wikipedia.org/wiki/Discoverability

Addressable
~~~~~~~~~~~

*Provide addresses to readers which link directly to content at a
granular level.*

The ability to reference *specific* sections deep within a body of
documentation facilitates productive communication about the
documentation, even with one's self. These addresses can take the form
of URLs, page numbers, or other forms depending on the publication
medium. Readers may wish to bookmark certain sections, share them with
other users, or provide feedback to the authors. The more granular this
ability, and the easier it is to access, the better.

Cumulative
~~~~~~~~~~

*Content should be ordered to cover prerequisite concepts first.*

Can a reader follow your entire body of documentation, linearly, from
start to finish without getting confused? If so, the documentation is
perfectly "cumulative", which is great, but not always possible. It's
something to strive for, especially in tutorials and examples. If you
have separated your tutorials and examples from the reference
documentation, then put the tutorials and examples first. Then, content
within the reference information section may be ordered alphabetically
or topically without regard to prerequisite needs.

The goal of cumulative ordering is not to encourage readers to consume
your documentation linearly — rather it is to help them narrow their
search for information when filling in gaps in their knowledge. If a
reader arrives with *some* knowledge of the software and begins reading
the documentation at the 25% mark, they are likely to "rewind" when
confused.

Complete
~~~~~~~~

*Within each publication, cover concepts in-full, or not at all.*

Picture some documentation of software like a map of a neighborhood. If
the map displays roads, readers will expect it to display *all* roads
(which exist and are of the same *type* being displayed). Perhaps the
map does not display *railroads*, for example. Thus, a reader
approaching the map to look for railroads will find zero and then seek a
different map — but the map is still "complete", even with this
shortcoming. "Complete" does not mean that the map must describe *all*
characteristics of the land. It means simply that, for the
characteristics it chooses to describe, it should describe *all* of
them. A map that displays fifty out of one hundred fire hydrants in a
neighborhood is *worse* than a map which displays none.

As a good example, ``iconv`` is a command line tool for working with
character encodings. Its `man page`_ covers *all*
of its available options but *none* of the possible character encodings
accepted as values to these options. Instead, the man page instructs the
user to run ``iconv -l`` to produce a list of character encodings. In
this example, the man page and the list are separate publications, both
of which are complete, which is good!

.. _man page: http://man7.org/linux/man-pages/man1/iconv.1.html

Publishing partially completed documentation must be done cautiously. To
avoid misleading readers, make every effort to clearly state, up front,
that a particular concept is only covered partially.

Beautiful
~~~~~~~~~

*Visual style should be intentional and aesthetically pleasing.*

Aesthetics don't matter to everyone — but (consciously or not) some
readers will struggle to find comfort in documentation that lacks
attention to visual style. Even in text-only documentation such as
``--help`` output, visual style is still present in the form of spacing
and capitalization. If visual style is not important to you personally,
then consider soliciting stylistic improvements from others for whom it
is.

A documentation body should be...
---------------------------------

Comprehensive
~~~~~~~~~~~~~

*Ensure that together, all the publications in the body of documentation
can answer all questions the user is likely to have.*

We can never create enough documentation to satisfy *all* questions,
however obscure, that might arise from users — but satisfying the
*likely* questions is certainly attainable and thus should be the goal
of a body of documentation. "Likely" is admittedly a blurry term, but
it's also relative, which means that a body of documentation which
answers very unlikely questions while failing to answer likely ones is
somewhat out of balance.

Answering some questions may require the user to read multiple
publications, which is okay.

:template: {{year}}/generic.html

Sponsors
========

We are seeking corporate partners to help us create the best conference possible.
You can find more information in our :doc:`prospectus`.

Sponsors
--------

The conference wouldn't be nearly as great as it is without our wonderful corporate sponsors.
Thanks to these folks for supporting the community.

.. raw:: html

    {% macro sponsors() %}
    {% include "include/2018/australia-sponsors.html" %}
    {% endmacro %}
    {{ sponsors()|indent(4) }}

In Kind Sponsors
----------------

Write the Docs is also helped out by companies that give their employees time to work on the conference.

.. raw:: html

    {% macro inkindsponsors() %}
    {% include "include/2018/portland-sponsors-in-kind.html" %}
    {% endmacro %}
    {{ inkindsponsors()|indent(4) }}

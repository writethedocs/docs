:template: {{year}}/generic.html

Sponsors
========

We are seeking corporate partners to help us create the best conference possible.
Contact us at sponsorship@writethedocs.org for more information on sponsoring Write the Docs.

Sponsors
--------

The conference wouldn't be nearly as great as it is without our wonderful corporate sponsors.
Thanks to these folks for supporting the community.

.. raw:: html

    {% macro sponsors() %}
    {% include "include/2018/prague-sponsors.html" %}
    {% endmacro %}
    {{ sponsors()|indent(4) }}

In Kind Sponsors
----------------

Write the Docs is also helped out by companies that give their employees time to work on the conference.

.. raw:: html

    {% macro sponsors() %}
    {% include "include/2018/prague-sponsors-in-kind.html" %}
    {% endmacro %}
    {{ sponsors()|indent(4) }}


Media Sponsors
--------------

These amazing media professionals have teamed up with us to capture the Write the Docs experience.

.. raw:: html

    {% macro sponsors() %}
    {% include "include/2018/prague-sponsors-media.html" %}
    {% endmacro %}
    {{ sponsors()|indent(4) }}
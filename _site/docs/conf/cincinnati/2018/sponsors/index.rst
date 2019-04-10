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
    {% include "include/" + year|string + "/" + shortcode + "-sponsors.html" %}
    {% endmacro %}
    {{ sponsors()|indent(4) }}

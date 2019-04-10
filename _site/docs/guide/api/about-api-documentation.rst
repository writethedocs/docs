============
Introduction
============

API documentation is the first thing users will encounter when they want to work with your API. Your API is only as good as its documentation! ::

  From the perspective of a user,
  if a feature is not documented, it does not exist.
  If a feature is documented incorrectly, then it is broken.
  - The internet, paraphrased

If your API already exists, automated reference documentation can be useful to document the API as it currently is. If your API is still being implemented, API documentation can perform a vital function in the design process.

Automated Reference Docs
------------------------

Reference documentation can be automatically created with tools like Swagger that will look directly at the API code.

While these tools help you with the technical details, they don't create good descriptions and explanations. The additional content is what separates your document from a collection of glorified code comments to a useful developer resource. ::

  The best API docs are written by hand - Peter Hilton

.. _documentation-driven-design:

Test-Driven Documentation
-------------------------

Test-driven documentation aims to improve upon the typical approaches to automated documentation. It allows you to write the bulk of the documentation by hand while also ensuring its accuracy by using your API's tests to generate some of the content.

Projects such as `Spring REST Docs <https://spring.io/projects/spring-restdocs>`_ use your API's tests to generate small snippets of documentation that can be included in hand-written API documentation. The accuracy of the documentation is ensured by the tests – if the API's documentation becomes inconsistent with its implementation the tests that generate the snippets will fail.

Documentation Driven Design
---------------------------

If your API still has to be built, you can create API documentation to help with the design process. The documentation driven design philosophy comes down to this: ::

  Documentation changes are cheap, code changes are expensive.

By designing your API through documentation, you can easily get feedback and iterate your design before any development has to happen.

Some API documentation formats have the added benefit of being machine readable. This opens the door to a multitude of additional tools that can help during the entire lifecycle of your API:

  * Create a mock server to help during the initial API design
  * Test your API before deployment to ensure that the API and the documentation matches
  * Create interactive documentation that allows developers to perform demo requests to your API

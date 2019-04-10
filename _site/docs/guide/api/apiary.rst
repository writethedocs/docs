======
Apiary
======

Hosting Docs
------------

Apiary provides a service for creating and hosting API documentation described in the API Blueprint or Swagger format. Once the API description is complete, Apiary generates interactive documentation in a three column layout. Example requests and responses are shown for every endpoint in multiple programming languages. It also enables the user to make requests to your live API. 

.. _apiary-building-docs:

Building Docs
-------------

To build Apiary style docs locally, you need to install the Apiary CLI Tools. The full instructions are available `here. <https://help.apiary.io/tools/apiary-cli/>`_

Once it is installed, navigate to the directory containing your ``.apib`` file and run::

  apiary preview --path="myfile.apib" --output="myfile.html"

This will validate your ``.apib`` file and create the HTML file. You can then view the document in your browser.

=============
API Blueprint
=============

API Blueprint is a high level language for describe web APIs. The syntax is a combination of Markdown and MSON syntax and the files are saved with a `.apib` extension. Markdown is a lightweight text formatting syntax. `MSON <https://github.com/apiaryio/mson>`_ is an extension of Markdown for describing data objects.

The goal of the API Blueprint format is to enable the design-first philosophy for REST APIs, however, the format works just as well for documenting existing APIs.

Getting Started
---------------

The quickest way to get started is to use Apiary to edit and view your documentation. Apiary is a service that allows you to edit and host documentation online. Start by signing up for an account `on Apiary. <https://login.apiary.io/register>`_
Next, continue with the `API Blueprint Tutorial. <https://apiblueprint.org/documentation/tutorial.html>`_ It provides a good overview of how to describe a basic API.

Writing Docs
------------

The structure for an ``.apib`` file is::

  Metadata
  API Name
  Resource Group
    Resource
      Action
      Action
    Resource
  Resource Group
  Data Structures

``Metadata``:
  describes the API Blueprint version

``API Name``:
  is your API name

``Resource Groups``:
  describes a collection of related API endpoints

``Resources``:
  describes a specific API endpoint

``Actions``:
  describes specific http verb actions to an endpoint

``Data Structures``:
  describes data used in your API requests/responses. By defining them in a separate section, they can easily be reused.

Building Docs
-------------

The two most popular tools for generating documents from API Blueprints are Apiary and Aglio.

* :ref:`apiary-building-docs` with Apiary.

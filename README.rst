Climbing Gear API
=======================

What's that?
-------------------

This a training project (at least for now) aiming to create a web application for climbers of all sorts.
The app allows to collect, manage and describe your climbing gear as well as track its usage. The project
is at the very beginning of development. It will be dockerized and deployed when the MVP version will be ready.

Domain vocabulary
-------------------


- *Climber* is a user who can authenticate, manage its account, create, delete, update *Gear*
- *Gear* represents all *Climber's* climbing gear
- *GearCategory* describes the kind of *Gear*
- *Brand* is a company which manufactured a given piece of *Gear*
- *Made* is the name of given *Gear* model
- *Usage* describes dates and locations when given piece of *Gear* was used
- *Image* shows *Gear* in current condition



MVP
-------------------

- Authentication
- Simple CRUD API for *Climbers* and *Gear* (only simple info like *Brand* or *Make*)
- Test covering the most crucial parts of the application


Run
---

Running pipenv:

::

    $ pipenv shell


Install dependencies

::

    $ pipenv install

Development
-----------

Install pre-commit hooks
^^^^^^^^^^^^^^^^^^^^^^^^

Install pre-commit (system wide):

::

    $ pip install pre-commit black bandit isort flake8

Install hooks from project root directory:

::

    $ pre-commit install

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command

::

    $ python manage.py createsuperuser

Adding new packages
^^^^^^^^^^^^^^^^^^^

* To add new package run:

::

    $ pipenv install <package-name>


Tests
^^^^^

Running tests:

::

    $ pytest

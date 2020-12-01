{{cookiecutter.project_name}}
=============================

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|

The ``README.rst`` file should start with a brief description of the repository,
which sets it in the context of other repositories under the ``edx``
organization. It should make clear where this fits in to the overall edX
codebase.

{{ cookiecutter.project_short_description}}

Overview (please modify)
------------------------

The ``README.rst`` file should then provide an overview of the code in this
repository, including the main components and useful entry points for starting
to understand the code in more detail.

Documentation
-------------

(TODO: `Set up documentation <https://openedx.atlassian.net/wiki/spaces/DOC/pages/21627535/Publish+Documentation+on+Read+the+Docs>`_)

Development Workflow
--------------------

One Time Setup
~~~~~~~~~~~~~~
.. code-block::

  # Clone the repository
  git clone git@github.com:edx/{{ cookiecutter.repo_name }}.git
  cd {{ cookiecutter.repo_name }}

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  mkvirtualenv -p python3.8 {{ cookiecutter.repo_name }}


Every time you develop something in this repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

  # Activate the virtualenv
  workon {{ cookiecutter.repo_name }}

  # Grab the latest code
  git checkout master
  git pull

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  vim …

  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit …
  git push

  # Open a PR and ask for review.

License
-------

The code in this repository is licensed under the {{ cookiecutter.open_source_license }} unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

How To Contribute
-----------------

Contributions are very welcome.
Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.
Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for all Open edX projects.

The pull request description template should be automatically applied if you are creating a pull request from GitHub. Otherwise you
can find it at `PULL_REQUEST_TEMPLATE.md <.github/PULL_REQUEST_TEMPLATE.md>`_.

The issue report template should be automatically applied if you are creating an issue on GitHub as well. Otherwise you
can find it at `ISSUE_TEMPLATE.md <.github/ISSUE_TEMPLATE.md>`_.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

If you're having trouble, we have discussion forums at https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack invitation`_, then join our `community Slack workspace`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx-slack-invite.herokuapp.com/
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help

.. |pypi-badge| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/edx/{{ cookiecutter.repo_name }}/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/edx/{{ cookiecutter.repo_name }}/actions
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/edx/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :target: https://codecov.io/github/edx/{{ cookiecutter.repo_name }}?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest
    :target: https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/{{ cookiecutter.repo_name }}.svg
    :target: https://github.com/edx/{{ cookiecutter.repo_name }}/blob/master/LICENSE.txt
    :alt: License

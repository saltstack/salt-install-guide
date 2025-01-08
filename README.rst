==================
Salt install guide
==================

.. image:: https://img.shields.io/badge/slack-Salt%20Project-blue.svg?logo=discord
   :alt: Salt Project Discord Community
   :target: https://discord.gg/YVQamSwV3g

.. image:: https://img.shields.io/pypi/dm/salt?label=pypi%20downloads
   :alt: PyPi Package Downloads
   :target: https://pypi.org/project/salt

.. image:: https://img.shields.io/reddit/subreddit-subscribers/saltstack?style=social
   :alt: Salt Project subreddit
   :target: https://www.reddit.com/r/saltstack/

.. image:: https://img.shields.io/twitter/follow/Salt_Project_OS?style=social&logo=twitter
   :alt: Follow SaltStack on Twitter
   :target: https://twitter.com/intent/follow?screen_name=Salt_Project_OS

.. image:: https://img.shields.io/badge/stackoverflow-Salt%20Project-orange.svg
   :target: https://stackoverflow.com/questions/tagged/salt-stack+or+salt-cloud+or+salt-creation+or+salt-contrib?sort=Newest

If you're looking to install Salt, you've come to the right place!

- `View the Sphinx-built documentation here <https://docs.saltproject.io/salt/install-guide/en/latest/>`__
- `View the source repo here <https://github.com/saltstack/salt-install-guide>`__

About the Salt install guide
============================

The Salt Install Guide supplements and extends the core documentation for the
`Salt Project <https://github.com/saltstack/salt>`__. This guide is intended to
help Salt users install ``salt`` in their environment.

Contributions from anyone inside the Salt project community are always welcome.
Please read the :ref:`contributing` for more information. The contributing
guide can also be found in the source repository:

* `CONTRIBUTING.rst <https://github.com/saltstack/salt-install-guide/-/blob/master/CONTRIBUTING.rst>`__


Related links
=============
Check out the following links also related to the Salt Install Guide:

* `Salt Project <https://github.com/saltstack/salt>`__ - The repository for the
  Salt Project.
* `Salt Project Home Page <https://saltproject.io/>`_ - The web portal for
  Salt community events and resources.
* `Contributing Guide <https://saltstack.gitlab.io/open/docs/salt-install-guide/topics/contributing.html>`_ -
  For information about contributing to the Salt Install Guide and other Salt
  documentation projects, including how to set up your environment and other
  policies around submitting merge requests or issues.
* `Salt Style Guide <https://saltstack.gitlab.io/open/docs/docs-hub/topics/style-guide.html>`__ -
  For general guidance about using Salt Project terms and other style or
  formatting conventions.
* `rST guide <https://saltstack.gitlab.io/open/docs/docs-hub/topics/rst-guide.html>`_ -
  For conventions and guidelines about formatting reStructured Text (rST) in
  Salt documentation.



Other Salt documentation
------------------------
The following documentation is part of the Salt Project documentation:

* `Salt Project documentation <https://docs.saltproject.io/en/latest/contents.html>`__:
  Includes the full documentation for the Salt Project.
* `Module documentation <https://docs.saltproject.io/en/latest/py-modindex.html>`__:
  The Salt modules and state modules explain the use cases and arguments needed
  to execute the Salt modules.
* `Salt User Guide <https://docs.saltproject.io/salt/user-guide/en/latest/>`__:
  The Salt User Guide supplements and extends the core documentation for the
  Salt Project. This guide is intended to help Salt users learn about Salt's
  core concepts and features. It was originally authored by Alan Cugler and
  reviewed as a cross-collaborative effort between many Salt experts.


Overview of the toolchain
=========================
This repository uses the following tools:

* The Salt Install Guide documentation is composed in
  `reStructured text (rST) <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__,
  which is a version of Markdown that is generally used in Python-based projects.
* The rST is then run through `Sphinx <https://www.sphinx-doc.org/en/master/>`__,
  a static site generator that converts the rST into HTML for publication on the
  web.
* Sphinx applies the
  `Furo Theme for Sphinx <https://pradyunsg.me/furo/>`__ to render the site.
* The guide is hosted directly on GitHub using the
  `GitHub pages <https://pages.github.com/>`__ feature.
* GitHub Actions handle the
  `CI/CD pipelines <https://github.com/saltstack/salt-install-guide/actions>`__
  for the project.

Release Process
===============

New releases of the ``salt-install-guide`` are required in order to ensure the latest docs changes
make it into ``docs.saltproject.io``, which are collectively published via a private repository
called ``builddocs``. ``builddocs`` will do the following:

* Downloads the latest tarball builds from GitHub Releases of target docs repos
    * ``salt-install-guide``
    * ``salt-user-guide``
* Build reference docs from ``salt`` repo for supported release versions

To cut a new release of ``salt-install-guide``:

* Create and push a new tag via git
* The new tag will trigger a GitHub Action workflow which will create a new release
    * The new release will include the latest built tarball!
* Upon completion of a new ``salt-install-guide`` release, a new workflow must be launched
  via ``builddocs`` if wanting these changes to be immediately live

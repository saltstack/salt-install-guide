==================
Salt install guide
==================

.. image:: https://img.shields.io/badge/slack-@saltstackcommunity-blue.svg?logo=slack
   :target: https://join.slack.com/t/saltstackcommunity/shared_invite/zt-3av8jjyf-oBQ2M0vhXOhJpNpRkPWBvg

.. image:: https://img.shields.io/twitch/status/saltprojectoss
   :target: https://www.twitch.tv/saltprojectoss

.. image:: https://img.shields.io/reddit/subreddit-subscribers/saltstack?style=social
   :target: https://www.reddit.com/r/saltstack/

.. image:: https://img.shields.io/twitter/follow/Salt_Project_OS?style=social&logo=twitter
   :target: https://twitter.com/intent/follow?screen_name=Salt_Project_OS

.. image:: https://img.shields.io/badge/stackoverflow-saltstack-orange.svg
   :target: https://stackoverflow.com/questions/tagged/salt-stack+or+salt-cloud+or+salt-creation+or+salt-contrib?sort=Newest

If you're looking to install Salt, you've come to the right place!

- `View the Sphinx-built documentation here <https://saltstack.gitlab.io/open/docs/salt-install-guide>`__
- `View the source repo here <https://gitlab.com/saltstack/open/docs/salt-install-guide>`__

About the Salt install guide
============================

The Salt Install Guide supplements and extends the core documentation for the
`Salt Project <https://github.com/saltstack/salt>`__. This guide is intended to
help Salt users install ``salt`` in their environment, ultimately superseding
documentation where applicable:

* Install directions on `repo.saltproject.io <https://repo.saltproject.io/>`__
* Install directions on `docs.saltproject.io <https://docs.saltproject.io/en/master/topics/installation/index.html>`__

Contributions from anyone inside the Salt project community are always welcome.
Please read the :ref:`contributing` for more information. The contributing
guide can also be found in the source repository:

* `CONTRIBUTING.rst <https://gitlab.com/saltstack/open/docs/salt-install-guide/-/blob/master/CONTRIBUTING.rst>`__


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
* `Salt Style Guide <https://saltstack.gitlab.io/open/docs/salt-user-guide/topics/style-guide.html>`__ -
  For general guidance about using Salt Project terms and other style or
  formatting conventions.
* `Writing Salt documentation (rST guide) <https://saltstack.gitlab.io/open/docs/salt-user-guide/topics/writing-salt-docs.html>`_ -
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
* `Salt User Guide <https://saltstack.gitlab.io/open/docs/salt-user-guide/>`__:
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
* The guide is hosted directly on GitLab using the
  `GitLab pages <https://docs.gitlab.com/ee/user/project/pages/>`__ feature.
* GitLab handles the
  `CI/CD pipeline <https://gitlab.com/saltstack/open/docs/salt-install-guide/-/pipelines>`__
  for the project.

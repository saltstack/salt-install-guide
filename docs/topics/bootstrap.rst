.. _install-bootstrap:

======================
Bootstrap installation
======================

.. include:: _includes/install-method.rst


About the Salt bootstrap installation
=====================================

The `Salt Bootstrap project <https://github.com/saltstack/salt-bootstrap>`_ maintains a
Bash shell script that installs Salt on Linux/macOS, and a PowerShell script that installs on
Windows platforms. The script can install ``salt-master``, ``salt-minion``, and other
system packages while enabling Salt services automatically.

For most installations, the best options are typically ``stable`` and a version. ``stable``
will install the official packages that are fully tested with Salt's included version of Python
and dependencies (AKA ``onedir``) from `relenv <https://github.com/saltstack/relenv/>`__, and
are functional across a wide range of operating systems.

For example:

.. parsed-literal::

    bootstrap-salt.sh stable |minor-one-version|

The source code and reference documentation for the bootstrap scripts are in the
``salt-bootstrap`` repository:

* `bootstrap-salt.sh (for Linux and macOS) <https://github.com/saltstack/salt-bootstrap/blob/develop/bootstrap-salt.sh>`__
* `bootstrap-salt.ps1 (for Windows) <https://github.com/saltstack/salt-bootstrap/blob/develop/bootstrap-salt.ps1>`__

Learn more
==========

The most up-to-date instructions for how to use ``salt-bootstrap`` can be found in the
`salt-bootstrap README <https://github.com/saltstack/salt-bootstrap/blob/develop/README.rst>`__,
including:

* How to download Salt bootstrap for Windows and Linux
* How to install Salt package builds from the Salt Project official package repositories
* How to install Salt via alternative means (``pip``, ``git``, etc.)
* All arguments available for bootstrap

.. warning::

    Older versions of Salt prior to 3006 are no longer supported by this bootstrap script as they
    have reached their End-Of-Life. Only onedir-based architecture versions of Salt are supported
    by this bootstrap script.

.. _salt-python-version-support:

===========================
Support for Python versions
===========================

Starting with Salt 3006 LTS, the Salt Project pins to a specific major version series
of Python to test and ship with Salt via ``relenv`` (onedir). This means the version of Python shipped may not
be with the very latest version of Python itself, but will be a version of Python still
under the `Python support lifecycle <https://devguide.python.org/versions/#supported-versions>`_
(versions supported `Python Software Foundation <https://www.python.org/psf/>`_).

Fully supported
===============

The Salt Project team provides **full support** for the package-installed versions of Salt via
``package.broadcom.com`` (which are packaged with ``relenv`` instead of via ``pip`` or ``git``).

``relenv`` is currently pinned to the following major Python versions in Salt:

- Salt |major-one-version-text|: |relenv-one-python-version|
- Salt |major-two-version-text|: |relenv-two-python-version|

Reasonable-effort support
=========================

Users installing Salt via ``pip``, ``git``, or other methods will be running Salt in a way that
Salt is not developed or tested against. This means that the user experience will vary when not
using what Salt ships via ``relenv``.

Environments with these alternative installations of Salt, such as pip-based or git-based installations, are
considered being under **Reasonable-effort support.** The fully supported versions of Salt would be the
packages Salt Project provides from their repositories, due to their test, build, upgrade/downgrade testing suites
working with the ``relenv``-based installs of Salt.

Resources
=========

Source code repositories for projects used to build and ship isolated onedirs with Salt:

- `relenv GitHub source repo <https://github.com/saltstack/relenv/>`__
- `ppbt: Portable Python Build Toolchain <https://github.com/saltstack/ppbt>`__

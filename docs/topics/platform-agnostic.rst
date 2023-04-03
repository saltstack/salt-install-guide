.. _install-platform-agnostic:

====================================
Platform agnostic installation (pip)
====================================

.. include:: _includes/install-method.rst


About platform agonistic installation
=====================================

Salt can be installed in a platform-agnostic way using the Python package
installer ``pip`` from `pypi.org <https://pypi.org>`_.

You can use ``pip`` to install other packages that will complement your Salt
code.

A benefit of using ``pip`` is the ability to install Salt in Python virtual
environments and Conda environments.

.. Warning::
    If you pip install a library using the salt-pip install method, the Python
    package installs into the onedir file location. Any scripts installed by the
    Python library will not be accessible from the usual system Python paths.
    Scripts installed by the Python library need to be called directly using the
    full path to the command.


Install Salt using `pip`
========================

#.  Install package:

    .. code-block:: bash

       pip3 install salt

    .. Note::
        You can use ``pip`` and ``pip3`` interchangeably, depending on the
        platform's support for Python 3.

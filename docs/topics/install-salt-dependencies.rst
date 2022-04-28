.. _install-salt-dependencies:

=========================
Install Salt dependencies
=========================

Before you install Salt on your infrastructure, you must first install:

* The version of Python that is required by the version of Salt you are
  installing.
* Salt's core dependencies.
* (Optional) Install any dependencies required by the Salt modules you plan to
  use regularly in your system.

.. Note::
    Installing Salt dependencies is optional if you have upgraded your system to
    use the Salt Tiamat packages (available in Salt version 3005 and later). The
    Salt Project **strongly** recommends upgrading to Tiamat to continue
    receiving Salt version updates. See :ref:`upgrade-to-tiamat` for more
    information.


Install Python
==============
Salt |release| requires Python 3.5 or higher.

For information about downloading and installing Python on your specific
operating system, use the official Python documentation:

* `Python downloads <https://www.python.org/downloads/>`_
* `Installing packages (Python packaging user guide) <https://packaging.python.org/en/latest/tutorials/installing-packages/>`_


Install Salt dependencies
=========================
See `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.9/linux.txt>`_
for a list of Salt's current dependencies.


Install Salt module dependencies
================================
Various Salt modules might require additional dependencies beyond the dependencies
needed for Salt's core functionality. See the
`module documentation <https://docs.saltproject.io/en/latest/py-modindex.html>`_
for the specific modules you intend to use for a list of required dependencies.

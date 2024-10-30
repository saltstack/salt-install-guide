.. _upgrade-to-onedir:

=================
Upgrade to onedir
=================

Onedir is the Salt Project's new packaging system. Beginning with the release of
Salt 3006 LTS (Sulfur), the Salt Project will only offer onedir packages.

.. _what-is-onedir:

What is onedir?
===============
Onedir stands for "one directory" because the goal is to provide a single
directory containing all the executables that Salt needs. It includes the
version of Python needed by Salt and its required dependencies.

Onedir packages simplify the installation process because they allow you to
use Salt out of the box without installing Python or other dependencies first.

Onedir packages are self-contained binaries of Salt. Onedir packages include:

.. list-table::
  :widths: 40 60
  :header-rows: 1

  * - What is installed
    - For more information

  * - The version of Python needed by Salt
    - :ref:`salt-python-version-support`

  * - Salt's required dependencies
    - `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.10/linux.txt>`_


.. Warning::
    The dependencies included with onedir are required for Salt's core
    functionality only. If you are using a Salt module that has an additional
    dependency, you will need to additionally install any dependencies required
    by that specific module. See the
    `module documentation <https://docs.saltproject.io/en/latest/py-modindex.html>`_
    for that specific module for a list of required dependencies.


How to upgrade to onedir
========================
To upgrade to onedir, if you are upgrading from a Salt older than Salt 3006 LTS:

#. On your Salt infrastructure (masters, minions, etc.), update the repository
   paths to point to the new ``packages.broadcom.com`` endpoints. See
   :ref:`install-by-operating-system-index` for the specific commands.

#. After the repository files are updated, import the appropriate GPG key.
   :ref:`install-deb` involves running a ``curl`` command, while RHEL-like
   systems will automatically pick up the new GPG key on your behalf when you
   update the repository configuration (`salt.repo`).

#. Upgrade your Salt packages.

   After upgrading your Salt packages, your Salt services should automatically
   restart. If you need to restart them manually for any reason, you can use
   these commands:

   .. code-block:: bash

       systemctl start salt-master
       systemctl start salt-minion

   See :ref:`restart-upgrade-minions-used-in-state-runs` for additional
   considerations.

#. Use Salt to reinstall any existing third party Python packages. Reinstalling
   the packages ensures they are installed in the correct onedir path.

   .. Admonition:: How do I know which packages need to be reinstalled?

      You can use ``salt-call pip.list`` to view existing modules that may need
      to be installed.

      See also `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.10/linux.txt>`_
      for a list of the packages that are installed with onedir. Any package
      that is not on this list needs to be reinstalled.

   You can use two possible methods to reinstall packages:

   * ``salt-pip install <package name>``
   * Use the ``pip.installed`` Salt state.

   .. Note::
       In order to install software such as Python libraries and Salt
       extensions, you'll need to use ``salt-pip`` to install packages into the
       onedir directory. For more information, see the
       `pip.state module documentation <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pip_state.html#module-salt.states.pip_state>`_.

#. After upgrading, you might need to update any state files that use
   ``pip.installed`` if you need to install Python packages into the system
   Python environment. In the state file, provide the ``pip_bin`` or ``bin_env``
   to the pip state module.

   For example:

   .. code-block:: yaml

       lib-foo:
         pip.installed:
           - pip_bin: /usr/bin/pip3
       lib-bar:
         pip.installed:
           - bin_env: /usr/bin/python3

#. After upgrading, you might also need to update any salt ``gitfs`` formula
   branches if the formula has changed because of onedir-specific fixes.


.. Warning::
   After installing Salt using the onedir packages, do not add Salt to any
   library search paths, such as ``LD_LIBRARY_PATH`` on Linux. Onedir has
   already been built in a way that allows it to find the executables it needs.
   Adding Salt to the library search path could cause errors due to incompatible
   versions of system packages.

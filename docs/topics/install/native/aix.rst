.. _install-aix:

===
AIX
===

.. important::

    The latest release of the |aix-native-minion| is version |aix-version|.

    This version will be used throughout this documentation, except for where
    version-specific differences need to be specified.

Welcome to the |aix-native-minion| installation guide. This installation
guide explains the process for installing a Salt native |minion| |aix-version|
on |aix| UNIX systems. This guide is intended for system administrators with the
general knowledge and experience required in the field.

.. note::
    There are separate builds for AIX v7.1 and AIX v7.2.


.. _aix-preinstall:

Pre-installation
================

Supported hardware and firmware versions
----------------------------------------
The following systems are supported:

.. list-table::
   :header-rows: 1

   * - Device
     - Supported Firmware
     - Supported Salt versions
   * - AIX 7.1 and greater
     - Power 7 and greater
     - Salt v3002.1 and greater (Python 2)
   * - AIX 7.1 and greater
     - Power 8 and greater
     - Salt v3003.1 and greater
   * - AIX 7.2 and greater
     - Power 8 and greater
     - Salt v3004 and greater


.. Warning::
    Be aware that |aix| utilities may not be the same as a standard Linux
    environment. For example, the version of ``tar`` does not support ``-z`` in
    |aix|.


Prerequisites
-------------
Before installing the |aix-native-minion|:

* Check that your |aix| UNIX system is supported.
* Ensure that ports 4505 and 4506 are open on the applicable |aix| UNIX systems.

Salt uses ports 4505 and 4506 for communication between |masters| and |minions|.
The |aix-native-minion| uses a direct connection to the |aix| UNIX system and
uses the network interfaces for communication. For that reason, ports 4505 and
4506 need to be open on the appropriate network interfaces.


Download and verify files
-------------------------
The |aix-native-minion| package is a tarball containing an installation and
removal script and an |aix| bff package.

.. warning::

    If upgrading to Salt ``v3003.3``, or newer, the following requirements need to be met:

    - If upgrading from Salt ``v3000.4``, which was Python 2, an upgrade requires
      **uninstalling Python 2.**
    - If upgrading from Salt ``v3003.1``, Salt needs to be forcefully uninstalled before reinstalling
      with Salt ``v3003.3`` or newer. A forceful uninstall can be done via: ``install_salt.sh -u -f``
    - Salt ``v3003.1`` releases, and newer, will only work on **Power 8 or greater processors.**

.. grid:: 2

    .. grid-item-card:: Download Salt v3004 (v7.1)
        :link: https://repo.saltproject.io/salt/py3/aix/7/powerpc/3004/salt_3004-1.tar.gz

        :bdg-primary:`Python 3`
        :bdg-secondary:`Power 8 or Greater Processors`
        :bdg-success:`Latest`

    .. grid-item-card:: Download Salt v3004 (v7.2)
        :link: https://repo.saltproject.io/salt/py3/aix/7.2/powerpc/3004/salt_3004-1.tar.gz

        :bdg-primary:`Python 3`
        :bdg-secondary:`Power 8 or Greater Processors`
        :bdg-success:`Latest`

    .. grid-item-card:: Download Salt v3003.3 (v7.1)
        :link: https://repo.saltproject.io/salt/py3/aix/7/powerpc/3003/salt_3003.3-1.tar.gz

        :bdg-primary:`Python 3`
        :bdg-secondary:`Power 8 or Greater Processors`

    .. grid-item-card:: Download Salt v3003.1 (v7.1)
        :link: https://repo.saltproject.io/salt/py3/aix/7/powerpc/3003/salt_3003.1-1.tar.gz

        :bdg-primary:`Python 3`
        :bdg-secondary:`Power 8 or Greater Processors`

    .. grid-item-card:: Download Salt v3002.1 (v7.1)
        :link: https://repo.saltproject.io/salt/py3/aix/7/powerpc/3002/salt_3002.1-1.tar.gz

        :bdg-primary:`Python 3`
        :bdg-info:`Power 7 and Greater Processors`

    .. grid-item-card:: Download Salt v3000.4 (v7.1)
        :link: https://repo.saltproject.io/salt/py2/aix/7/powerpc/3000/salt_3000.4-1.tar.gz

        :bdg-warning:`Python 2`
        :bdg-info:`Power 7 and Greater Processors`

..
  .. include:: ../_includes/verify-download-native-minions.rst

.. note::

    Unsupported versions can be found in the `archive repository <https://archive.repo.saltproject.io/salt/py2/>`__.


Transfer files
--------------
Once the file is verified, transfer the file to the network device. For example:

.. code-block:: bash
   :substitutions:

   gzip --decompress salt_|aix-version|.tar.gz
   tar -xvf salt_|aix-version|.tar


.. Note::
    If installing on a virtual machine, consult the documentation for your
    hypervisor as the commands might differ slightly.

.. _aix-install:

Installation
============

Before you begin the |aix-native-minion| installation process, ensure you have
read and completed the :ref:`aix-preinstall` steps.

The |aix-native-minion| package installs:

* The |minion-salt| service
* The salt-call service

.. Note::
    The salt-ssh and salt-proxy services are not installed with this package.


|minion-salt| package installation
----------------------------------
To install the package:

#. Ensure that you have sufficient privileges to install packages on the |aix|
   UNIX system.

#. In the terminal on the |aix| device, navigate to the ``salt_|aix-version|``
   directory.

   .. Note::
       This directory name may change slightly depending on the latest version
       of Salt. Currently, the latest stable version is |aix-version|.

#. Run the following command to install the package:

   .. code-block:: bash

       ./install_salt.sh

   You'll see a message that indicates the installation is running. You can see
   a more detailed output if you install the package in verbose mode.

After installing |aix-native-minion|, continue to the next step.


Configure and test the |aix-native-minion|
------------------------------------------
To configure the |aix-native-minion| to connect with its |master-salt|:

#. Edit the ``/etc/salt/minion`` file to update the |minion| configuration with
   your environment's specific details, such as the |master|’s IP address, the
   |minion| ID, etc. For example, to set the |minion| name:

   .. code-block:: bash

       id: your-aix-minion-name

#. Edit the file to indicate the IP address of the |master| that is managing
   this |minion|. For example:

   .. code-block:: yaml

       master: 192.0.2.1

#. Start the |aix-native-minion| with the following command:

   .. code-block:: bash

       startsrc -s salt-minion

#. To check that the |aix-native-minion| is installed correctly and is running,
   use the following command:

   .. code-block:: bash

       lssrc -g salt

   If the |aix-native-minion| is installed and running, the output will be
   similar to the following:

   .. code-block:: bash

       Subsystem         Group            PID          Status
       salt-minion       salt             20110110     active

   .. Note::
       If the output reads ``salt-inoperative``, that means the |minion| has not
       yet been started.

       An alternative method to restart the |minion| is to use the command
       ``/etc/rc.d/init.d/salt-minion start`` but this method is not preferred.

#. Once the |aix-native-minion| has been started and is running, you can use
   the command ``salt-key`` to verify the |master| has received a request for the
   |minion| key.

#. On the |master|, accept the |minion|'s key with the following command,
   replacing the placeholder test with the correct |minion| name:

   .. code-block:: bash

       salt-key -y -a your-aix-minion-name

#. After waiting a small period of time, verify the connectivity between the
   |master| and the |aix-native-minion| using simple commands. For example, try
   running the following commands:

   .. code-block:: bash

       salt your-minion-name test.versions
       salt your-minion-name grains.items
       salt your-minion-name cmd.run ‘ls -alrt /’
       salt-call --local test.versions


You can now use the |aix-native-minion|. See :ref:`using-aix` for more
information.


|aix-native-minion| package removal
-----------------------------------
To uninstall the |minion-salt| package, run the following command:

.. code-block:: bash

    ./install_salt.sh -u


Alternatively, to remove any trace of salt on the system , run the following
command:

.. code-block:: bash

    ./install_salt.sh -u -f


.. Warning::
    If ``install_salt.sh`` fails to uninstall Salt and you intend to install
    a new version, you must uninstall using an alternate method. Otherwise
    the previous package may remain in the cache.

    The install script install_salt.sh as a number of self-explanatory
    options, which can be accessed using the -h option: ``./install_salt.sh -h``

.. _using-aix:

Using the |aix-native-minion|
=============================

You can access the Salt command line interface on the |aix-native-minion| using
wrapper scripts. These wrapper scripts execute with environmental variable
overrides for library and Python paths. The wrapper scripts are located in the
``/usr/bin`` folder, which is typically included in the environmental variable
PATH.

.. Note::
    The |aix-native-minion| |aix-version| currently has a wrapper script for:

    * ``salt-minion``
    * ``salt-call``

Salt command line functionality is available through the use of these wrapper
scripts. For example, to start the |minion| as a daemon:

.. code-block:: bash

    [/usr/bin/]salt-minion -d


If ``srcmster`` is active, you can use AIX System Resource Controller commands
to start, stop, and list the ``salt-minion`` daemon with ``startsrc``,
``stopsrc`` and ``lssrc``.

To start the |minion|:

.. code-block:: bash

    startsrc -s salt-minion


To stop the |minion|:

.. code-block:: bash

    stopsrc -s salt-minion


To check if the |minion| is running:

.. code-block:: bash

    lssrc -g salt


If the |aix-native-minion| is installed and running, the output will be
similar to the following:

.. code-block:: bash

    Subsystem         Group            PID          Status
    salt-minion       salt             20110110     active


.. Note::
    If the output reads ``salt-inoperative``, that means the |minion| has not
    yet been started.


Additional resources
--------------------
For more information about |aix|, see the following links on the IBM Knowledge
Center:

* `AIX Commands
  <https://www.ibm.com/support/knowledgecenter/ssw_aix_71/navigation/commands.html>`_

* `AIX System Resource Controller
  <https://www.ibm.com/support/knowledgecenter/ssw_aix_72/osmanagement/sysrescon.html>`_

.. _install-aix:

===
AIX
===

Welcome to the AIX native minion installation guide. This installation
guide explains the process for installing a Salt native minion on AIX UNIX
systems. This guide is intended for system administrators with the general
knowledge and experience required in the field.

.. card:: Browse the repo for AIX packages
    :link: https://repo.saltproject.io/salt/py3/aix/
    :width: 50%

    :bdg-primary:`AIX`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-a-native-minion.rst


Before you start
================
Before installing the AIX native minion:

* Ensure that you have sufficient privileges to install packages on the AIX
  UNIX system.
* Check that your AIX UNIX system is supported. See :ref:`aix-supported` for
  more information.
* Ensure that ports 4505 and 4506 are open on the applicable AIX UNIX systems.

Salt uses ports 4505 and 4506 for outbound communication from the master to the
minions. The AIX native minion uses a direct connection to the AIX UNIX system
and uses the network interfaces for communication. For that reason, ports 4505
and 4506 need to be open on the appropriate network interfaces.


Install Salt on AIX
===================
The AIX native minion package installs:

* The salt-minion service
* The salt-call service

.. Note::
    The salt-ssh and salt-proxy services are not installed with this package.


Salt minion package installation
--------------------------------
To install the package:

#. Download, verify, and transfer the AIX installation files from
   `repo.saltproject.io <https://repo.saltproject.io/salt/py3/aix/>`_. The AIX
   native minion package is a tarball containing an installation and removal
   script and an AIX bff package.

#. In the terminal on the AIX device, navigate to the ``salt_|aix-version|``
   directory.

   .. Note::
       This directory name may change slightly depending on the latest version
       of Salt. Currently, the latest stable version is |release|.

#. Run the following command to install the package:

   .. code-block:: bash

       ./install_salt.sh

   You'll see a message that indicates the installation is running. You can see
   a more detailed output if you install the package in verbose mode.

After installing the AIX native minion, continue to the next section.


Configure and test the AIX native minion
----------------------------------------
To configure the AIX native minion to connect with its Salt master:

#. Edit the ``/etc/salt/minion`` file to update the minion configuration with
   your environment's specific details, such as the master’s IP address, the
   minion ID, etc. For example, to set the minion name:

   .. code-block:: bash

       id: your-aix-minion-name

#. Edit the file to indicate the IP address of the master that is managing
   this minion. For example:

   .. code-block:: yaml

       master: 192.0.2.1

#. Start the AIX native minion with the following command:

   .. code-block:: bash

       startsrc -s salt-minion

#. To check that the AIX native minion is installed correctly and is running,
   use the following command:

   .. code-block:: bash

       lssrc -g salt

   If the AIX native minion is installed and running, the output will be
   similar to the following:

   .. code-block:: bash

       Subsystem         Group            PID          Status
       salt-minion       salt             20110110     active

   .. Note::
       If the output reads ``salt-inoperative``, that means the minion has not
       yet been started.

       An alternative method to restart the minion is to use the command
       ``/etc/rc.d/init.d/salt-minion start`` but this method is not preferred.

#. Once the AIX native minion has been started and is running, you can use the
   command ``salt-key`` to verify the master has received a request for the
   minion key.

#. On the master, accept the minion's key with the following command,
   replacing the placeholder test with the correct minion name:

   .. code-block:: bash

       salt-key -y -a your-aix-minion-name

#. After waiting a small period of time, verify the connectivity between the
   master and the AIX native minion using simple commands. For example, try
   running the following commands:

   .. code-block:: bash

       salt your-minion-name test.versions
       salt your-minion-name grains.items
       salt your-minion-name cmd.run ‘ls -alrt /’
       salt-call --local test.versions


You can now use the AIX native minion. See `Using the AIX native minion`_ for
more information.


AIX native minion package removal
---------------------------------
To uninstall the Salt minion package, run the following command:

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



Using the AIX native minion
===========================

You can access the Salt command line interface on the AIX native minion using
wrapper scripts. These wrapper scripts execute with environmental variable
overrides for library and Python paths. The wrapper scripts are located in the
``/usr/bin`` folder, which is typically included in the environmental variable
PATH.

.. Note::
    The AIX native minion |release| currently has a wrapper script for:

    * ``salt-minion``
    * ``salt-call``

Salt command line functionality is available through the use of these wrapper
scripts. For example, to start the minion as a daemon:

.. code-block:: bash

    [/usr/bin/]salt-minion -d


If ``srcmster`` is active, you can use AIX System Resource Controller commands
to start, stop, and list the ``salt-minion`` daemon with ``startsrc``,
``stopsrc`` and ``lssrc``.

To start the minion:

.. code-block:: bash

    startsrc -s salt-minion


To stop the minion:

.. code-block:: bash

    stopsrc -s salt-minion


To check if the minion is running:

.. code-block:: bash

    lssrc -g salt


If the AIX native minion is installed and running, the output will be similar to
the following:

.. code-block:: bash

    Subsystem         Group            PID          Status
    salt-minion       salt             20110110     active


.. Note::
    If the output reads ``salt-inoperative``, that means the minion has not
    yet been started.


Additional resources
====================
For more information about AIX, see the following links on the IBM Knowledge
Center:

* `AIX Commands
  <https://www.ibm.com/support/knowledgecenter/ssw_aix_71/navigation/commands.html>`_

* `AIX System Resource Controller
  <https://www.ibm.com/support/knowledgecenter/ssw_aix_72/osmanagement/sysrescon.html>`_

.. _install-solaris:

=======
Solaris
=======

Welcome to the Solaris native minion installation guide. This installation
guide explains the process for installing a Salt native minion on Solaris UNIX
systems. This guide is intended for system administrators with the general
knowledge and experience required in the field.

.. card:: Browse the repo for Solaris packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/solaris/
    :width: 50%

    :bdg-primary:`Solaris`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-a-native-minion.rst


Before you start
================
Before installing the Solaris native minion:

* Ensure that you have sufficient privileges to install packages on the Solaris
  system.
* Check that your Solaris UNIX system is supported. See :ref:`solaris-supported`
  for more information.
* Ensure that ports 4505 and 4506 are open on the applicable Solaris UNIX
  systems.

Salt uses ports 4505 and 4506 for outbound communication from the master to the
minions. The Solaris native minion uses a direct connection to the Solaris UNIX
system and uses the network interfaces for communication. For that reason, ports
4505 and 4506 need to be open on the appropriate network interfaces.


Install Salt on Solaris
=======================
The Solaris native minion package installs:

* The salt-minion service
* The salt-call service

.. Note::
    The salt-ssh and salt-proxy services are not installed with this package.


Salt minion package installation
--------------------------------
The steps to install the Solaris native minion differ for Solaris 10 vs. Solaris
11. Ensure that you are using the correct set of instructions for your system.

If installing on a virtual machine, consult the documentation for your
hypervisor as the commands might differ slightly.

.. tab:: Solaris 10

    To install the package on Solaris 10:

    #. Ensure that you have sufficient privileges to install packages on the
       Solaris system.

    #. In the terminal on the Solaris device, add the packages from the
       uncompressed tarball using the following command (including the dot):

       .. code-block:: bash
          :substitutions:

            pkgadd -d .


.. tab:: Solaris 11

    To install the package on Solaris 11:

    #. Ensure that you have sufficient privileges to install packages on the
       Solaris system.

    #. In the terminal on the Solaris device, install Salt from the p5p archive.
       For example:

       .. code-block:: bash
            :substitutions:

            pkg install -g file:///<path to p5p archive>/salt-|solaris-version|_solaris11_sparc.p5p  library/python/salt-minion

    #. Use the following command to disable the salt-minion service, which is
       automatically started when installed:

       .. code-block:: bash

            svcadm disable salt-minion


Configure and test the Solaris native minion
--------------------------------------------
To configure the Solaris native minion to connect with its Salt master:

#. Edit the ``/opt/local/etc/salt/minion`` file to update the minion configuration with
   your environment's specific details, such as the master's IP address, the
   minion ID, etc. For example, to set the minion name:

   .. code-block:: bash

        id: your-solaris-minion-name

#. Edit the file to indicate the IP address of the master that is managing this
   minion. For example:

   .. code-block:: yaml

        master: 192.0.2.1

#. Start the Solaris native minion with the following command:

   .. code-block:: bash

        svcadm enable salt-minion

#. Once the Solaris native minion has been started and is running, you can use
   the command ``salt-key`` to verify the master has received a request for the
   minion key.

#. On the master, accept the minion's key with the following command, replacing
   the placeholder test with the correct minion name:

   .. code-block:: bash

        salt-key -y -a your-solaris-minion-name

#. After waiting a small period of time, verify the connectivity between the
   master and the Solaris native minion using simple commands. For example,
   try running the following commands:

   .. code-block:: bash

        salt your-minion-name test.versions
        salt your-minion-name grains.items
        salt your-minion-name cmd.run 'ls -alrt /'
        salt-call --local test.versions


You can now use the Solaris native minion. See
`Using the Solaris native minion`_ for more information.


Salt minion package removal
---------------------------

.. tab:: Solaris 10

    To uninstall the Salt minion package on Solaris 10, run the following command:

    .. code-block:: bash

        pkgrm salt

.. tab:: Solaris 11

    To uninstall the Salt minion salt package on Solaris 11, run the following
    command:

    .. code-block:: bash

        pkg uninstall library/python/salt-minion


Using the Solaris native minion
===============================
You can access the Salt command line interface on the Solaris native minion
using executable Python scripts. These scripts execute with environmental
variable overrides for library and Python paths. The wrapper scripts are located
in the ``/usr/bin/salt-call`` and ``/usr/bin/salt-minion`` respectively.

.. Note::

    The Solaris native minion |release| currently has scripts for:

    * ``salt-minion``
    * ``salt-call``

Salt command line functionality is available through the use of these scripts.

To start the minion:

.. code-block:: bash

    svcadm enable salt-minion


To stop the minion:

.. code-block:: bash

    svcadm disable salt-minion


You can also start the minion as a daemon using the following command:

.. code-block:: bash

    [/usr/bin/]salt-minion -d

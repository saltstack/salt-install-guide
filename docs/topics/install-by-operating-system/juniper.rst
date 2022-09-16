.. _install-juniper:

=======
Juniper
=======

Welcome to the Juniper native minion installation guide. This installation
guide explains the process for installing a Salt native minion on Juniper
network devices. This guide is intended for system administrators with the
general knowledge and experience required in the field, such as administering
network devices running `Junos OS
<https://www.juniper.net/documentation/product/en_US/junos-os/>`__.

.. card:: Browse the repo for Juniper packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/juniper/
    :width: 50%

    :bdg-primary:`Juniper`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-a-native-minion.rst


Before you start
================
Before installing the Juniper native minion:

* Check that your network device and firmware are supported. See
  :ref:`juniper-supported` for more information.
* Ensure that ports 4505 and 4506 are open on the applicable Juniper switches
  or routers.

Salt uses ports 4505 and 4506 for outbound communication from the master to the
minions. The Juniper native minion uses a direct connection to the Juniper switch
or router and uses the Management Interface on the switch/router for
communication. For that reason, ports 4505 and 4506 need to be open on the
appropriate Management Interfaces.


.. _juniper-install:

Installation
============
Juniper network devices run *Junos OS*, which includes the *Junos CLI*. When
connecting to a Juniper network device, you start at the OS-level. To run
commands within Junos OS command-line interface (CLI), you need to first run the
CLI command.


Shell pre-configuration
-----------------------
Before you can install the Juniper native minion, you need to set up your
shell pre-configuration:

#. Run the following command within the shell:

   .. code-block:: bash

       mkdir -p /var/local/salt/etc

#. Save the following configuration in ``/var/local/salt/etc/proxy``:

   .. code-block:: yaml

       master: <ip of salt master>
       proxy:
         proxytype: junos
         host: localhost

       beacons:
         junos_rre_keys:
           -  interval:
                43200

       ping_interval: 2

       loop_interval: 1

       enable_fqdns_grains: False


.. Note::
    You may also use the standard configuration commands for Salt if needed.


Proxy pre-configuration
-----------------------
The ``beacons`` portion of the configuration is needed on routing platforms with
`dual Routing Engines
<https://www.juniper.net/documentation/en_US/junos/topics/concept/routing-engine-redundacny-overview.html>`__.
The beacon configuration ensures the following directories and files are copied
to the backup Routing Engine:

.. list-table::
  :widths: 35 65
  :header-rows: 1

  * - Directory
    - Description

  * - ``/var/local/salt/etc/pki``
    -  The directory where the master and minion keys reside. If the Routing
       Engine master changes, the master still recognizes the new Routing Engine
       due to configuration existing by both Routing Engines.

  * -  ``/var/local/salt/etc/proxy``
    -  Copying this file to the backup Routing Engine ensures that the same
       configuration exists in both Routing Engines without additional steps
       needed on the network device.

The ``interval`` property is defined in a measurement of *seconds*, dictating
how often files are copied to the backup Routing Engine.

.. note::

   When the Juniper native minion is installed, log rotation for the native
   minion log file ``/var/log/salt/proxy`` is automatically installed,
   with:

   * A limit of 7 compressed files.
   * Log rotation if the log file exceeds 200 KB.


CLI pre-configuration
---------------------
To configure your CLI:

#. Run the following commands within the CLI at the edit prompt:

   .. code-block::

       edit
       set system services ssh root-login allow
       set system services netconf ssh
       set system extensions providers saltstack license-type customer deployment-scope commercial

#. To confirm these commands were successful, run:

   .. code-block::

       show system extensions providers

   This command provides an expected output of:

   .. code-block::

       saltstack {
         license-type customer deployment-scope commercial;
       }

#. If the command was successful, commit the changes with:

   .. code-block::

       commit


Juniper native minion installation and configuration
----------------------------------------------------
To install and configure the Juniper native minion:

#. Download, verify, and transfer the Juniper installation files from
   `repo.saltproject.io <https://repo.saltproject.io/salt/py3/juniper/>`_. The
   Juniper is a tarball.

#. Run the following commands within the CLI at the edit prompt:

   .. code-block::

       run request system software add /var/tmp/<salt-native-minion>.tgz
       exit

#. Edit the ``/var/local/salt/etc/salt/proxy`` file to update the minion
   configuration with your environment's specific details, such as the
   master’s IP address, the minion ID, etc.

#. (Optional): If your router does not have the ability to use Reverse DNS
   lookup to obtain the Fully Qualified Domain Name (fqdn) for an IP Address,
   you'll need to change the ``enable_fqdns_grains`` setting in the
   configuration file to ``False`` instead. For example:

   .. code-block:: bash

       enable_fqdns_grains: True


   .. Note::
       This setting needs to be changed because all IP addresses are processed
       with underlying calls to ``socket.gethostbyaddr``. These calls can take
       up to 5 seconds to be released after reaching ``socket.timeout``. During
       that time, there is no fqdn for that IP address. Although calls to
       ``socket.gethostbyaddr`` are processed asynchronously, the calls still
       add 5 seconds every time grains are generated if an IP does not resolve.

#. In the ``/var/local/salt/etc/salt/proxy`` configuration file, change the
   following settings to:

   .. code-block:: bash

       ping_interval: 2
       loop_interval: 1


Installing the Juniper native minion:

* Creates ``/var/db/scripts/commit/salt.slax``
* Creates ``/var/db/scripts/event/salt_event.py``
* Creates ``/var/db/scripts/op/salt_dualrengine.slax``
* Creates ``/var/db/scripts/event/salt_log.slax``
* Creates a backup in the ``/config/SaltBackup`` directory
  * This backup is referenced during native minion upgrades
* Configures:
  * *saltstack* super-user
  * Event-options SALT_POLICY and *salt_event.py* event script
  * *salt.slax* commit script
  * Copies above scripts to the other dual routing engine, if it exists
  * Configures log rotation of ``/var/log/salt/proxy`` automatically



Enabling and starting Salt as a service
---------------------------------------
The next step in the installation process is to enable and start Salt as a
service on the Juniper native minion:

#. Run the following commands within the CLI at the edit prompt:

   .. code-block::

       set system extensions extension-service application file salt-junos arguments minion daemonize

#. To confirm these commands were successful, run:

   .. code-block:: bash

       show system extensions extension-service

   This command provides an expected output of:

   .. code-block::

       application {
         file salt-junos {
           arguments minion;
           daemonize;
         }
       }

#. If the command was successful, commit the changes with:

   .. code-block::

       commit


Verifying the installation
--------------------------
A running native minion will typically have three processes running
*salt-junos*. To check the initial health of the new installation:

#. Run the following command within the CLI at the edit prompt:

   .. code-block::

      show system processes extensive| match salt


   This command provides a similar output to:

   .. code-block::

       57858 - I 0:00.00 /var/run/scripts/jet/salt-junos minion
       57859 - I 0:00.49 /var/run/scripts/jet/salt-junos minion
       57861 - S 0:39.39 /var/run/scripts/jet/salt-junos minion


#. To retrieve the local native minion version, run the following within the
   CLI:

   .. code-block::

       show version | match salt


   Depending on the version output, the resulting output is similar to the
   following format:

   .. code-block::
      :substitutions:

       Salt Minion |release| for JUNOS [|juniper-file-version|]


#. To see the super-user created by, and used to manage, the native minion:

   .. code-block::

       show configuration system login user saltstack


Post-installation
=================
Once the key for the Juniper network device has been accepted by your master,
Salt can be used to manage the native minion. To validate that Salt is managing
the minion, run some basic Salt commands to retrieve baseline information:

.. code-block:: bash

   salt <juniper-target> test.ping
   salt <juniper-target> test.version

.. note::

   To use the Junos Automation Enhancements, you must install the
   software bundle that contains Enhanced Automation. See `Running Junos
   OS with Enhanced Automation
   <https://www.juniper.net/documentation/en_US/junos/topics/concept/junos-flex-overview.html>`__.


Starting and stopping the Juniper native minion
-----------------------------------------------
After installation, you can disable (start) and enable (stop) the Juniper native
minion using the following commands from the edit prompt:

.. code-block:: bash

    deactivate system extensions extension-service application file salt-junos
    commit

To restart the Juniper native minion, use the following commands from the edit
prompt:

.. code-block:: bash

    activate system extensions extension-service application file salt-junos
    commit


Additional references
---------------------
For Junos OS specific modules that can be used against Junos native minions from
a master, refer to the following:

-  `Junos OS Execution Module
   <https://docs.saltstack.com/en/master/ref/modules/all/salt.modules.junos.html>`__

-  `Junos OS State Modules
   <https://docs.saltstack.com/en/master/ref/states/all/salt.states.junos.html>`__

-  `Junos OS Grains
   <https://docs.saltstack.com/en/master/ref/grains/all/salt.grains.junos.html>`__


Additional documentation endpoints for reference:

-  `JetEZ reference docs
   <https://www.juniper.net/documentation/product/en_US/juniper-extension-toolkit>`__

-  `PyEZ reference docs
   <https://www.juniper.net/documentation/product/en_US/junos-pyez>`__

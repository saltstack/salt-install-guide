.. _install-juniper:

=======
Juniper
=======

.. important::

    The latest release of the |juniper-native-minion| is version |juniper-version|.

    This version will be used throughout this documentation, except for where
    version-specific differences need to be specified.

Welcome to the |juniper-native-minion| installation guide.

This installation guide explains the process for installing a Salt native
|minion| |juniper-version| on |juniper| network devices. This guide is intended
for NetOps engineers with the general knowledge and experience required in the
field, such as administering network devices running `Junos
OS <https://www.juniper.net/documentation/product/en_US/junos-os/>`__.

.. _juniper-preinstall:

Pre-installation
================

Supported hardware and firmware versions
----------------------------------------
The following systems are supported:

.. list-table::
   :header-rows: 1

   * - Device
     - Supported Firmware
   * - QFX Series Switches
     - **17.3R2-S6** and greater
   * - MX Series Routers
     - **17.4R2-S6** and greater


.. Note::
    During development of the native |minion| for |juniper|, an issue was found
    on |juniper| software which required a fix: |juniper| PR 1515432 : REST-API
    PUT POST RPC call failing, which has been fixed in 17.4R2-S12 and 17.3R3-S9.
    Use these versions or higher for use with the native |minion|.


Prerequisites
-------------
Before installing the |juniper-native-minion|:

* Ensure your network device and firmware are supported.
* Ensure that ports 4505 and 4506 are open on the applicable |juniper| switches
  or routers.

Salt uses ports 4505 and 4506 for communication between |masters| and |minions|.
The |juniper-native-minion| uses a direct connection to the |juniper| switch or
router and uses the Management Interface on the switch/router for communication.
For that reason, ports 4505 and 4506 need to be open on the appropriate
Management Interfaces.


Download and verify files
-------------------------
The |juniper-native-minion| package is a **tgz** file.

.. grid:: 3

   .. grid-item-card:: Download Salt v3003.3
       :link: https://repo.saltproject.io/salt/py3/juniper/x86_64/3003/salt-junos-x86-64-20210827-213932.tgz

       :bdg-primary:`Python 3`
       :bdg-success:`Latest`

   .. grid-item-card:: Download Salt v3003.1
       :link: https://repo.saltproject.io/salt/py3/juniper/x86_64/3003/salt-junos-x86-64-20210729-172533.tgz

       :bdg-primary:`Python 3`

   .. grid-item-card:: Download Salt v3002
       :link: https://repo.saltproject.io/salt/py3/juniper/x86_64/3002/salt-junos-x86-64-20201026-235317.tgz

       :bdg-primary:`Python 3`

   .. grid-item-card:: Download Salt v3001.2
       :link: https://repo.saltproject.io/salt/py3/juniper/x86_64/3001/salt-junos-x86-64-20200911-161120.tgz

       :bdg-primary:`Python 3`

..
  .. include:: ../_includes/verify-download-native-minions.rst

Transfer files
--------------
Once the file is verified, transfer the file to the network device:

.. code-block:: bash

    scp <salt-native-minion>.tgz root@<juniper-device>:/var/tmp

.. _juniper-install:

Installation
============

Before you begin the |juniper-native-minion| installation process, ensure you
have read and completed the :ref:`juniper-preinstall` steps.

|juniper| network devices run *Junos OS*, which includes the *Junos CLI*. When
connecting to a |juniper| network device, you start at the OS-level. To run
commands within Junos OS command-line interface (CLI), you need to first run the
CLI command.

With this in mind, this uses the following terms to refer to different
environments:

-  **CLI** for Junos OS executed commands **WITHIN** the Junos CLI

-  **Shell** for Junos OS executed commands **NOT WITHIN** the Junos CLI

Examples:

**Shell**

.. code-block:: bash

   mkdir -p /var/local/salt/etc

**CLI**

.. code-block::

    show security


Shell pre-configuration
-----------------------
Before you can install the |juniper-native-minion|, you need to set up your
shell pre-configuration:

1. Run the following command within the shell:

   .. code-block:: bash

       mkdir -p /var/local/salt/etc

2. Save the following configuration in ``/var/local/salt/etc/proxy``:

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


Explanation of proxy configuration
++++++++++++++++++++++++++++++++++
The ``beacons`` portion of the configuration is needed on routing platforms with
`dual Routing Engines
<https://www.juniper.net/documentation/en_US/junos/topics/concept/routing-engine-redundacny-overview.html>`__.
The beacon configuration ensures the following directories and files are copied
to the backup Routing Engine:

**/var/local/salt/etc**

-  **/var/local/salt/etc/pki**

   -  This directory is where the |master| and |minion| keys reside. If the
      Routing Engine |master| changes, the |master| still recognizes the new
      Routing Engine due to configuration existing by both Routing Engines.

-  **/var/local/salt/etc/proxy**

   -  Copying this file to the backup Routing Engine ensures that the same
      configuration exists in both Routing Engines without additional steps
      needed on the network device.

The ``interval`` property is defined in a measurement of *seconds*, dictating
how often files are copied to the backup Routing Engine.

.. note::

   When the |juniper-native-minion| is installed, log rotation for the native
   |minion| log file ``/var/log/salt/proxy`` is automatically installed,
   with:

   - A limit of 7 compressed files.
   - Log rotation if the log file exceeds 200 KB.


CLI pre-configuration
---------------------
To configure your CLI:

1. Run the following commands within the CLI at the edit prompt:

   .. code-block::

       edit
       set system services ssh root-login allow
       set system services netconf ssh
       set system extensions providers saltstack license-type customer deployment-scope commercial

2. To confirm these commands were successful, run:

   .. code-block::

       show system extensions providers

   This command provides an expected output of:

   .. code-block::

       saltstack {
         license-type customer deployment-scope commercial;
       }

3. If the command was successful, commit the changes with:

   .. code-block::

       commit


|juniper-native-minion| installation and configuration
------------------------------------------------------
To install and configure the |juniper-native-minion|:

1. Run the following commands within the CLI at the edit prompt:

   .. code-block::

       run request system software add /var/tmp/<salt-native-minion>.tgz
       exit

2. Edit the ``/var/local/salt/etc/salt/proxy`` file to update the |minion|
   configuration with your environment's specific details, such as the
   |master|’s IP address, the |minion| ID, etc.

3. (Optional): If your router does not have the ability to use Reverse DNS
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

4. In the ``/var/local/salt/etc/salt/proxy`` configuration file, change the
   following settings to:

   .. code-block:: bash

       ping_interval: 2
       loop_interval: 1


Explanation of the installation
+++++++++++++++++++++++++++++++
Installing the |juniper-native-minion| does the following:

-  Creates **/var/db/scripts/commit/salt.slax**

-  Creates **/var/db/scripts/event/salt_event.py**

-  Creates **/var/db/scripts/op/salt_dualrengine.slax**

-  Creates **/var/db/scripts/event/salt_log.slax**

-  Creates a backup in the **/config/SaltBackup** directory

   -  This backup is referenced during native |minion| upgrades

-  Configures:

   -  *saltstack* super-user

   -  Event-options SALT_POLICY and *salt_event.py* event script

   -  *salt.slax* commit script

   -  Copies above scripts to the other dual routing engine, if it exists

   -  Configures log rotation of /var/log/salt/proxy automatically


Enabling and starting Salt as a service
---------------------------------------
The next step in the installation process is to enable and start Salt as a
service on the |juniper-native-minion|:

1. Run the following commands within the CLI at the edit prompt:

   .. code-block::

       set system extensions extension-service application file salt-junos arguments minion daemonize

2. To confirm these commands were successful, run:

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

3. If the command was successful, commit the changes with:

   .. code-block::

       commit


Verifying the installation
--------------------------
A running native |minion| will typically have three processes running
*salt-junos*. To check the initial health of the new installation:

1. Run the following command within the CLI at the edit prompt:

   .. code-block::

      show system processes extensive| match salt


   This command provides a similar output to:

   .. code-block::

       57858 - I 0:00.00 /var/run/scripts/jet/salt-junos minion
       57859 - I 0:00.49 /var/run/scripts/jet/salt-junos minion
       57861 - S 0:39.39 /var/run/scripts/jet/salt-junos minion


2. To retrieve the local native |minion| version, run the following within
   the CLI:

   .. code-block::

       show version | match salt


   Depending on the version output, the resulting output is similar to the
   following format:

   .. code-block::
      :substitutions:

       Salt Minion |juniper-version| for JUNOS [|juniper-file-version|]


3. To see the super-user created by, and used to manage, the native |minion|:

   .. code-block::

       show configuration system login user saltstack

.. _juniper-postinstall:

Post-installation
=================

Once the key for the |juniper| network device has been accepted by your
|master|, Salt can be used to manage the native |minion|. To validate that Salt
is managing the |minion|, run some basic Salt commands to retrieve baseline
information:

.. code-block:: bash

   salt <juniper-target> test.ping
   salt <juniper-target> test.version

.. note::

   To use the Junos Automation Enhancements, you must install the
   software bundle that contains Enhanced Automation. See `Running Junos
   OS with Enhanced Automation
   <https://www.juniper.net/documentation/en_US/junos/topics/concept/junos-flex-overview.html>`__.


Starting and stopping the |juniper-native-minion|
-------------------------------------------------
After installation, you can disable (start) and enable (stop) the
|juniper-native-minion| using the following commands from the edit prompt:

.. code-block:: bash

    deactivate system extensions extension-service application file salt-junos
    commit

To restart the |juniper-native-minion|, use the following commands from the edit
prompt:

.. code-block:: bash

    activate system extensions extension-service application file salt-junos
    commit


Additional references
---------------------
For Junos OS specific modules that can be used against Junos native |minions|
from a |master|, refer to the following:

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

.. _install-arista:

======
Arista
======

Welcome to the Arista native minion installation guide. This installation
guide explains the process for installing a Salt native minion on Arista UNIX
systems. This guide is intended for system administrators with the general
knowledge and experience required in the field.

.. card:: Browse the repo for Arista packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/arista/
    :width: 50%

    :bdg-primary:`Arista`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-a-native-minion.rst


Before you start
================

Before installing the Arista native minion:

* Check that your network device and firmware are supported. See
  :ref:`arista-supported` for more information.
* Ensure that ports 4505 and 4506 are open on the applicable Arista switches
  or routers.

Salt uses ports 4505 and 4506 for outbound communication from the master to the
minions. The Arista native minion uses a direct connection to the Arista switch
or router and uses the Management Interface on the switch/router for
communication. For that reason, ports 4505 and 4506 need to be open on the
appropriate Management Interfaces.


Installation
============
Arista network devices run *Arista EOS*, which includes the *Arista CLI*. When
connecting to an Arista network device, you start at the OS-level. Arista has a
mode called *Arista CLI privileged mode* in which you can enter a Bash shell if
needed. The command ``enable`` enters privileged mode. With this in mind, this
guide assumes all commands are entered into the Arista CLI.


Minion SWIX package installation
--------------------------------
To install the SWIX package:

#. Download, verify, and transfer the Arista installation files from
   `repo.saltproject.io <https://repo.saltproject.io/salt/py3/arista/>`_. The
   Arista native minion package is SWIX file.

   .. Note::
       If installing on a virtual machine, consult the documentation for your
       hypervisor as the commands might differ slightly.

#. Once the Arista native minion is available in the ``flash`` directory, enter
   privileged mode and copy the SWIX extension, replacing the placeholder text
   with the correct file name:

   .. code-block:: bash

       copy arista-native-minion-filename.swix extension:

#. View the extensions detail by running the following command:

   .. code-block:: bash

       show extensions detail

   This command returns an output similar to the following example:

   .. code-block:: text
      :substitutions:

              Name: salt-|arista-version|.64.swix
           Version: |arista-version|
           Release: 1
          Presence: available
            Status: not installed
            Vendor:
           Summary: Self contained Salt Minion binary
          Packages:
        Total size: 0 bytes
       Description:
       Self contained Python |arista-python-version| Salt Minion 64-bit binary

#. Install the SWIX package, replacing the placeholder text with the correct
   file name:

   .. code-block:: bash

       extension arista-native-minion-filename.swix

#. View the extensions detail again to verify that the status, package, and file
   size has changed:

   .. code-block:: bash

       show extensions detail

   This command returns an output similar to the following example:

   .. code-block::
      :substitutions:

              Name: salt-|release|.64.swix
           Version: |release|
           Release: 1
          Presence: available
            Status: installed
            Vendor:
           Summary: Self contained Salt Minion binary
          Packages: salt-|release|.x86_64.rpm |release|/1
        Total size: 222446843 bytes
       Description:
       Self contained Python |arista-python-version| Salt Minion 64-bit binary

#. Run the following commands:

   .. code-block:: bash

       bash
       sudo su

#. Edit the ``/etc/salt/minion`` file to update the minion configuration with
   your environment's specific details, such as the master’s IP address, the
   minion ID, etc.

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


#. Verify that Salt is running:

   .. code-block:: bash

       ps -ef | grep salt

   If the minion is installed correctly and is disabled, the output is similar
   to the following:

   .. code-block:: bash

       * salt-minion.service - The Salt Minion
          Loaded: loaded (/usr/lib/systemd/system/salt-minion.service; disabled; vendor preset: disabled)
          Active: inactive (dead)
            Docs: man:salt-minion(1)
                  file:///usr/share/doc/salt/html/contents.html
                  https://docs.saltproject.io/en/latest/contents.html

#. Start the Arista native minion as a daemon and check its status with the
   following command:

   .. code-block:: bash

       systemctl start salt-minion

   The output should be similar to the following:

   .. code-block:: bash

       * salt-minion.service - The Salt Minion
          Loaded: loaded (/usr/lib/systemd/system/salt-minion.service; disabled; vendor preset: disabled)
          Active: active (running) since Wed 2020-09-02 16:22:11 UTC; 4s ago
            Docs: man:salt-minion(1)
                  file:///usr/share/doc/salt/html/contents.html
                  https://docs.saltproject.io/en/latest/contents.html
        Main PID: 4259 (salt-minion)
          Memory: 81.7M (limit: 250.0M)
          CGroup: /system.slice/salt-minion.service
                  |-4259 /bin/bash /usr/bin/salt-minion
                  |-4267 /opt/saltstack/salt/run/run minion
                  |-4268 /opt/saltstack/salt/run/run minion
                  |-4273 /opt/saltstack/salt/run/run minion KeepAlive MultiMinionProcessManager MinionProcessManager
                  |-4275 /opt/saltstack/salt/run/run minion KeepAlive MultiprocessingLoggingQueue

   .. Note::
      Alternatively, you can check whether Salt is running with the command:
      ``ps -ef | grep salt``.

#. Once the Arista native minion has been started and is running, you can use
   the command ``salt-key`` to verify the master has received a request for the
   minion key.

#. On the master, accept the minion's key with the following command, replacing
   the placeholder test with the correct minion name:

   .. code-block:: bash

       salt-key -y -a your-minion-name

#. After waiting a small period of time, verify the connectivity between the
   master and minion using simple commands. For example, try running the
   following commands:

   .. code-block:: bash

       salt your-minion-name test.versions
       salt your-minion-name grains.items
       salt your-minion-name cmd.run ‘ls -alrt /’

   If the key is accepted and the binding process is complete, you might see an
   output similar to the following example:

   .. code-block:: bash
      :substitutions:

       salt-master# salt arista-423 test.versions
       arista64-423:
           Salt Version:
                   Salt: |release|

           Dependency Versions:
                       cffi: 1.14.2
                   cherrypy: Not Installed
                   dateutil: Not Installed
                  docker-py: Not Installed
                      gitdb: Not Installed
                  gitpython: Not Installed
                     Jinja2: 2.11.2
                    libgit2: Not Installed
                   M2Crypto: 0.36.0
                       Mako: Not Installed
               msgpack-pure: Not Installed
             msgpack-python: 1.0.0
               mysql-python: Not Installed
                  pycparser: 2.14
                   pycrypto: Not Installed
               pycryptodome: 3.9.8
                     pygit2: Not Installed
                     Python: |arista-python-version|
               python-gnupg: Not Installed
                     PyYAML: 5.3.1
                      PyZMQ: 19.0.2
                      smmap: Not Installed
                    timelib: Not Installed
                    Tornado: 4.5.3
                        ZMQ: 4.3.2

            System Versions:
                       dist: centos 7 Core
                     locale: utf-8
                    machine: x86_64
                    release: 4.9.122.Ar-15352225.4232F
                     system: Linux
                    version: CentOS Linux 7 Core


Enabling Arista eAPI access for the minion
------------------------------------------
The Arista native minion uses the pyeapi library to communicate with the Arista
device. The pyeapi library is provided and installed by default with the Arista
native minion. However, it is not installed by default with the standard Salt
minion package.

.. Note::
    This document makes a distinction between a proxy minion connecting
    remotely to an Arista device and a standard minion making a remote
    connection. In general, the Arista native minion behaves more like the
    proxy minion. The native minion has its own Salt keys, can be targeted
    with grains, and can report back.

To enable eAPI access:

#. Turn on the Arista API using the following commands:

   .. code-block:: bash

       arista # config
       arista(config) # management API http-commands
       arista(config-mgmt-api-http-cmds) # protocol unix-socket
       arista(config-mgmt-api-http-cmds) # no shutdown
       arista(config-mgmt-api-http-cmds)
       arista(config-mgmt-api-http-cmds) # exit
       arista(config) # exit
       arista # write


#. Open the minion configuration file at ``/etc/salt/minion`` and add the
   following section:

   .. code-block:: yaml

       pyeapi:
         username: <name of admin or eAPI user>
         password: <password of admin or eAPI user>
         transport: socket
         enablepwd: <password for enable mode, optional>


#. Restart the salt-minion service on the device with the following command:

   .. code-block:: bash

       sudo systemctl restart salt-minion

#. Connect the Arista native minion to its master and ensure its key has
   has been accepted, as explained in `Minion SWIX package installation`_.

#. Run the following command, replacing the placeholder text with the minion ID
   for the Arista native minion:

   .. code-block:: bash

       salt arista-minion-ID test.ping

#. If this command returns a value of ``True``, you can execute eAPI commands in
   the shell. For example:

   .. code-block:: bash

       salt-master# salt arista64-423 pyeapi.get_config
       arista64-423:
           - ! Command: show running-config
           - ! device: veos64-423 (vEOS, EOS-4.23.2F)
           - !
           - ! boot system flash:/vEOS-lab.swi
           - !
           - transceiver qsfp default-mode 4x10G
           - !
           - hostname veos64-423
           - ip name-server vrf default 8.8.8.8
           - !
           - spanning-tree mode mstp
           - !
           - no aaa root
           - !
           - username admin role network-admin secret sha512 $6$jm1wk44bKE2rRHfP$fc.OCS7/jqgNgHPymxo370c1XgoaS6V894tff02YIlgV2B.7kGczXpgpa0HDQs3tn.5eBcmIpwNiNszXqfSEf.
           - !
           - interface Ethernet1
           - !
           - interface Ethernet2
           - !
           - interface Ethernet3
           - !
           - interface Management1
           -    ip address 10.0.2.63/24
           - !
           - no ip routing
           - !
           - ip route 0.0.0.0/0 10.0.2.2
           - !
           - management api http-commands
           -    protocol unix-socket
           -    no shutdown
           - !
           - end

       salt-master#


For more documentation on the capabilities of pyeapi, see the
`Salt Arista pyeapi module documentation
<https://docs.saltproject.io/en/latest/ref/modules/all/salt.modules.arista_pyeapi.html>`_.


Configure the Napalm module
---------------------------

The napalm library is provided and installed by default with the Arista native
minion. However, it is not installed by default with the standard Salt minion
package.

To configure the native minion to use the napalm module:

#. Open the minion configuration file at ``/etc/salt/minion`` and add the
   following section:

   .. code-block:: yaml

       napalm:
         username: <name of admin or user>
         password: <password of admin or user>
         host: localhost
         driver: eos
         provider: napalm_netacl

#. Restart the salt-minion service on the device with the following command:

   .. code-block:: bash

       sudo systemctl restart salt-minion

#. Connect the Arista native minion to its master and ensure its key has
   has been accepted, as explained in `Minion SWIX package installation`_.

#. Run the following command to test that the module is configured correctly:

   .. code-block:: bash

       salt veos-420 napalm.alive


   This command should have an output similar to the following:

   .. code-block:: bash

       veos-420:
          ----------
          comment:
          out:
             ----------
             is_alive:
                 True

          result:
              True


See `Salt Proxy Napalm module documentation
<https://docs.saltproject.io/en/latest/ref/proxy/all/salt.proxy.napalm.html>`_
for more information about this module.


Minion SWIX package removal
---------------------------
Removing the SWIX pack is similar to installation. The main difference is that
the prefix ``no`` is prepended to certain commands.

.. Note::
    For more information, see the
    `Arista documentation on extensions removal
    <https://www.arista.com/en/um-eos/eos-section-6-8-managing-eos-extensions#ww1259266>`_.

To remove the SWIX package:

#. Run the following command:

   .. code-block:: bash

       show extensions detail

   The output should be similar to the following example:

   .. code-block:: bash
      :substitutions:


              Name: salt-|release|.64.swix
           Version: |release|
           Release: 1
          Presence: available
            Status: installed
            Vendor:
           Summary: Self contained Salt Minion binary
          Packages: salt-|release|.x86_64.rpm |release|/1
        Total size: 222446843 bytes
       Description:
       Self contained Python |release| Salt Minion 64-bit binary


#. Remove the SWIX package by running the following command, replacing the
   placeholder file with the correct file name:

   .. code-block:: bash

       no extension arista-native-minion-filename.swix

#. View the extensions detail again to verify that the status, package, and file
   size has changed by running the following command:

   .. code-block:: bash

       show extensions detail

   This command returns an output similar to the following example:

   .. code-block:: bash
      :substitutions:

              Name: salt-|release|.64.swix
           Version: |release|
           Release: 1
          Presence: available
            Status: not installed
            Vendor:
           Summary: Self contained Salt Minion binary
          Packages:
        Total size: 0 bytes
       Description:
       Self contained Python |release| Salt Minion 64-bit binary


Post-installation
=================

This reference section includes additional resources for porting the salt-minion
service to Arista devices.


Starting and stopping the Arista native minion
----------------------------------------------
After installation, you can disable (start) and enable (stop) the Arista native
minion using the following commands:

.. code-block:: bash

    systemctl stop salt-minion

To restart the Arista native minion, use the following command:

.. code-block:: bash

    systemctl start salt-minion


Dependencies and known issues
-----------------------------
The Arista native minion is a self-contained binary that includes Salt |release|
with pyeapi and other Naplam dependencies that internally use
|native-minion-python-version|. All Python 3 utf-8 considerations are handled
internally leveraging Python PEP 538 and 540 and hence can function in locales
which only support ‘C’ and POSIX without issue.

.. Note::
    The 64-bit Arista native minion uses Python |native-minion-python-version|.

Since the Arista native minion is a self contained binary, there are no
external dependencies to be considered.

.. Note::
   The deprecations are warnings of functionality that will be removed in
   Python 3.9. These deprecations do not affect current
   functionality and will be resolved in future versions of Salt.

The issue with the napalm grains also occurs on standard minions. It will be
resolved in a future release of Salt.


Additional reference
--------------------
For reference, see:

-  `Arista EOS/Networking Tips
   <http://aristaeos.blogspot.com/2019/03/install-arista-eos-swix-image.html>`_

-  `Arista documentation on Extensions
   <https://www.arista.com/en/um-eos/eos-section-6-7-managing-eos-extensions>`_

- `Configuring VirtualBox (video)
  <https://www.youtube.com/watch?time_continue=8&v=nbDF7hzBPM0>`_

- `Port forwarding (video)
  <https://www.youtube.com/watch?v=QEmHqHpeoZM>`_

- `Enable SSH (Arista Forums)
  <https://eos.arista.com/forum/enable-ssh-2/>`_

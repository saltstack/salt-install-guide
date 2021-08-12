.. _install-solaris:

=======
Solaris
=======

.. important::

    The latest release of the |solaris-native-minion| is version |solaris-version|.

    This version will be used throughout this documentation, except for where
    version-specific differences need to be specified.

Welcome to the |solaris-native-minion| installation guide. This installation
guide explains the process for installing a Salt native |minion|
|solaris-version| on |solaris| UNIX systems. This guide is intended for system
administrators with the general knowledge and experience required in the field.

.. _solaris-preinstall:

Pre-installation
================


Supported hardware and firmware versions
----------------------------------------
The following systems are supported:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Device
     - Supported Firmware
   * - Solaris 10 update 8 and higher
     - Intel and SPARC processors
   * - Solaris 11.2 and higher
     - Intel and SPARC processors


Prerequisites
-------------
Before installing the |solaris-native-minion|:

* Check that your |solaris| UNIX system is supported.
* Ensure that ports 4505 and 4506 are open on the applicable |solaris| UNIX
  systems.

Salt uses ports 4505 and 4506 for communication between |masters| and |minions|.
The |solaris-native-minion| uses a direct connection to the |solaris| UNIX
system and uses the network interfaces for communication. For that reason, ports
4505 and 4506 need to be open on the appropriate network interfaces.


Download and verify files
-------------------------

The |solaris-native-minion| package file is available in the following file
formats:

.. grid:: 2

  .. grid-item-card:: Downloads for Solaris 11 (i386)
      :link: https://repo.saltproject.io/salt/py2/solaris/11/i386

      :bdg-warning:`Python 2`
      :bdg-info:`i386`

      ``p5p`` files containing the ``salt-minion`` for Solaris 11.

  .. grid-item-card:: Downloads for Solaris 11 (SPARC)
      :link: https://repo.saltproject.io/salt/py2/solaris/11/sparc

      :bdg-warning:`Python 2`
      :bdg-secondary:`SPARC`

      ``p5p`` files containing the ``salt-minion`` for Solaris 11.

  .. grid-item-card:: Downloads for Solaris 10 (x86)
      :link: https://repo.saltproject.io/salt/py2/solaris/10/x86

      :bdg-warning:`Python 2`
      :bdg-info:`x86`

      Tarballs containing the ``salt-minion`` for Solaris 10.

  .. grid-item-card:: Downloads for Solaris 10 (SPARC)
      :link: https://repo.saltproject.io/salt/py2/solaris/10/sparc

      :bdg-warning:`Python 2`
      :bdg-secondary:`SPARC`

      Tarballs containing the ``salt-minion`` for Solaris 10.

..
  .. include:: ../_includes/verify-download-native-minions.rst

.. note::

    Unsupported versions can be found in the `archive repository <https://archive.repo.saltproject.io/salt/py2/>`__.

Transfer files
--------------
Once the file is verified, transfer the file to the network device.

.. tab:: Solaris 10

    For example, to transfer and extract the tarball file for Solaris 10:

    .. code-block:: bash
       :substitutions:

        scp salt-|solaris-version|-solaris-sparc.tar.gz user@solaris_server:test/
        gzip --decompress salt_|solaris-version|.tar.gz
        tar -xvf salt_|solaris-version|.tar

.. tab:: Solaris 11

    For example, to transfer the p5p file for Solaris 11:

    .. code-block:: bash
       :substitutions:

        scp salt-|solaris-version|_solaris11_sparc.p5p user@solaris_server:test/

.. Note::
    If installing on a virtual machine, consult the documentation for your
    hypervisor as the commands might differ slightly.

.. _solaris-install:

Installation
============

Before you begin the |solaris-native-minion| installation process, ensure you
have read and completed the :ref:`solaris-preinstall` steps.


|minion-salt| package installation
----------------------------------
The steps to install the |solaris-native-minion| are different for |solaris|
10 vs. |solaris| 11. Ensure that you are using the correct set of instructions
for your system.

.. tab:: Solaris 10

    To install the package on |solaris| 10:

    #. Ensure that you have sufficient privileges to install packages on the
       |solaris| system.

    #. In the terminal on the |solaris| device, add the packages from the
       uncompressed tarball using the following command (including the dot):

       .. code-block:: bash
          :substitutions:

            pkgadd -d .


.. tab:: Solaris 11

    To install the package on |solaris| 11:

    #. Ensure that you have sufficient privileges to install packages on the
       |solaris| system.

    #. In the terminal on the |solaris| device, install Salt from the p5p archive.
       For example:

       .. code-block:: bash
            :substitutions:

            pkg install -g file:///<path to p5p archive>/salt-|solaris-version|_solaris11_sparc.p5p  library/python/salt-minion

    #. Use the following command to disable the |minion-service|, which is
       automatically started when installed:

       .. code-block:: bash

            svcadm disable salt-minion


Configure and test the Solaris native minion
--------------------------------------------
To configure the |solaris-native-minion| to connect with its |master-salt|:

#. Edit the ``/etc/salt/minion`` file to update the |minion| configuration with
   your environment's specific details, such as the |master|’s IP address,
   the |minion| ID, etc. For example, to set the |minion| name:

   .. code-block:: bash

        id: your-solaris-minion-name

#. Edit the file to indicate the IP address of the |master| that is managing
   this |minion|. For example:

   .. code-block:: yaml

        master: 192.0.2.1

#. Start the |solaris-native-minion| with the following command:

   .. code-block:: bash

        svcadm enable salt-minion

#. Once the |solaris-native-minion| has been started and is running, you can use
   the command ``salt-key`` to verify the |master| has received a request for
   the |minion| key.

#. On the |master|, accept the |minion|'s key with the following command,
   replacing the placeholder test with the correct |minion| name:

   .. code-block:: bash

        salt-key -y -a your-solaris-minion-name

#. After waiting a small period of time, verify the connectivity between the
   |master| and the |solaris-native-minion| using simple commands. For example,
   try running the following commands:

   .. code-block:: bash

        salt your-minion-name test.versions
        salt your-minion-name grains.items
        salt your-minion-name cmd.run ‘ls -alrt /’
        salt-call --local test.versions


You can now use the |solaris-native-minion|. See :ref:`using-solaris` for more
information.


|minion-salt| package removal
-----------------------------

.. tab:: Solaris 10

    To uninstall the |minion-salt| package on Solaris 10, run the following command:

    .. code-block:: bash

        pkgrm salt

.. tab:: Solaris 11

    To uninstall the |minion-salt| package on Solaris 11, run the following command:

    .. code-block:: bash

        pkg uninstall library/python/salt-minion


.. _using-solaris:

Using the |solaris-native-minion|
=================================

You can access the Salt command line interface on the |solaris-native-minion|
using executable Python scripts. These scripts execute with environmental
variable overrides for library and Python paths. The scripts are located in the
``/opt/salt folder`` and are named ``/opt/salt/salt-minion`` and
``/opt/salt/salt-call`` respectively.

.. Note::

    The |solaris-native-minion| |solaris-version| currently has scripts for:

    * ``salt-minion``
    * ``salt-call``

Salt command line functionality is available through the use of these scripts.
For example, to start the |minion| as a daemon:

.. code-block:: bash

    [/usr/bin/]salt-minion -d


To start the |minion|:

.. code-block:: bash

    svcadm enable salt-minion


To stop the |minion|:

.. code-block:: bash

    svcadm disable salt-minion


You can also start the |minion| as a daemon using the following command:

.. code-block:: bash

    /opt/salt/salt-minion -d

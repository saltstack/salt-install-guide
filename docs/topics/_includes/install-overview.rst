.. _install-overview:

.. admonition:: The Salt install guide is in a draft state

   This install guide is currently in a draft state, intended for the Salt 3005
   Phosphorus release. All documentation is written as though 3005 is the
   current version. Your feedback on this draft is welcome! Leave feedback
   on this issue: `Community feedback needed on new Salt Install Guide <https://gitlab.com/saltstack/open/docs/salt-install-guide/-/issues/33>`_.


.. sidebar:: **Supported Salt releases**

    |release-badge| |supported-release-1-badge| |supported-release-2-badge|

    **See also**

    * `Release notes <https://docs.saltproject.io/en/latest/topics/releases/index.html>`_
    * :ref:`announcements`
    * `RSS feeds <https://saltproject.io/rss-feeds/>`_

Welcome to the Salt install guide! This guide provides instructions for
installing Salt on :ref:`salt-supported-operating-systems`. It also explains
how to configure Salt, start Salt services, and verify your installation.

Salt packages can be accessed from
`repo.saltproject.io <https://repo.saltproject.io/>`_.

.. Warning::
    Beginning with the 3005 (Phosphorus) release of Salt, the Salt Project is
    changing its packaging system to **onedir**. Any new operating systems added
    in 3005 will only have onedir packages. The Salt Project will phase out the
    old Salt package builds for currently supported operating systems by 3006.
    See :ref:`what-is-onedir` for more information.

    Begin planning your migration or consider updating your Salt infrastructure
    to the new onedir packages as soon as possible. See :ref:`upgrade-to-onedir`
    for instructions.


Standard installation overview
==============================
Using the standard installation method is recommended for most organizations,
especially if you are just starting out with Salt. The standard installation
will make using Salt easier and provides functionality that isn't available in
masterless/agentless Salt configurations.

.. list-table::
  :widths: 5 50 45
  :align: left
  :header-rows: 1
  :stub-columns: 1

  * -
    - Process
    - For more information

  * - 1
    - Before you start the installation, check the system requirements to ensure
      your platform is supported in the latest version of Salt and open the
      required network ports.
    -  * :ref:`check-system-requirements`
       * :ref:`check-network-ports`
       * :ref:`salt-supported-operating-systems`
       * :ref:`salt-version-support-lifecycle`
       * :ref:`salt-python-version-support`

  * - 2
    - Install the ``salt-master`` service on the node that will manage your
      other nodes, meaning it will send commands to other nodes. Then, install
      the ``salt-minion`` service on the nodes that will be managed by the Salt
      master.

      For Linux-based operating systems, the recommended installation method is
      to use the bootstrap script or you can manually install Salt using the
      instructions for each operating system.

      For Windows or macOS operating systems, you need to download and run the
      installer file for that system.
    - **For Linux-based systems:**
       * :ref:`install-bootstrap`
       * :ref:`install-by-operating-system-index`

      **For macOS or Windows:**
       * :ref:`install-macos`
       * :ref:`install-windows`

      **For all operating systems:**
       * :ref:`install-by-operating-system-index`

  * - 3
    - Configure the Salt minions to add the DNS/hostname or IP address of the
      Salt master they will connect to. You can add additional configurations to
      the master and minions as needed.
    -  * :ref:`configure-master-minion`
       * `Configuring the minion <https://docs.saltproject.io/en/latest/ref/configuration/minion.html>`_

  * - 4
    - Start the service on the master, then the minions.
    - :ref:`start-salt-services`

  * - 5
    - Accept the minion keys after the minion connects.
    - :ref:`accept-keys`

  * - 6
    - Verify that the installation was successful by sending a test ping.
    - :ref:`verify-install`


Alternative installations and configurations
============================================
In general, you should only use alternative installation and configuration
options if you are an intermediate or advanced Salt user.

Although the standard Salt configuration model is the master/minion
(master/client) model, minions do not necessarily have to have a master to be
managed. Salt also gives additional options for managing minions:

.. list-table::
  :widths: 25 45 30
  :align: left
  :header-rows: 1

  * - Type
    - Description
    - For more information

  * - Masterless
    - Running a masterless salt-minion lets you use Salt's configuration
      management for a single machine without calling out to a Salt master on
      another machine.
    - `Salt masterless quickstart <https://docs.saltproject.io/en/latest/topics/tutorials/quickstart.html>`_

  * - Salt cloud
    - Provisions and manages systems on cloud hosts or hypervisors. It uses the
      Saltify drive to install Salt on existing machines (virtual or bare
      metal).
    -  * `Salt cloud <https://docs.saltproject.io/en/latest/topics/cloud/>`_
       * `Getting started with Saltify <https://docs.saltproject.io/en/latest/topics/cloud/saltify.html>`_

  * - Proxy minions
    - Send and receive commands from minions that, for whatever reason, can't
      run the standard ``salt-minion`` service.
    - `Proxy minions <https://docs.saltproject.io/en/latest/topics/proxyminion/index.html>`_

  * - Agentless
    - Use SSH to run Salt commands on a minion without installing an agent.
    -  `Salt SSH <https://docs.saltproject.io/en/latest/topics/ssh/index.html>`_

  * - Install Salt for development
    - If you plan to contribute to the Salt codebase, use this installation
      method.
    - `Installing Salt for development <https://docs.saltproject.io/en/latest/topics/development/hacking.html>`_

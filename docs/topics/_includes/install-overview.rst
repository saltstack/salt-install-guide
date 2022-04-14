.. _install-overview:

.. sidebar:: **Latest Salt release**

    |release| (|latest-release-date|)

    **More info:**

    * :ref:`announcements`
    * `RSS feeds <https://saltproject.io/rss-feeds/>`_

Welcome to the Salt install guide! This guide provides instructions for
installing Salt on :ref:`salt-supported-operating-systems`. It also explains
how to configure Salt, start Salt services, and verify your installation.

Salt packages can be accessed from
`repo.saltproject.io <https://repo.saltproject.io/>`_.

.. Note::
    Pay close attention to package versions when navigating
    `repo.saltproject.io <https://repo.saltproject.io/>`_. For example,
    if you are using a RedHat 7 variant, make sure you select RedHat and then
    select version 7. Otherwise, you will get the wrong repo and will install
    RedHat 8 Salt packages on a RedHat 7. Version incompatibility will throw
    unknown errors.


Standard installation overview
==============================

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

  * - 2
    - Install the ``salt-master`` service on the node that will manage your
      other nodes, meaning it will send commands to other nodes.
    -  * :ref:`install-by-operating-system-index`
       * :ref:`install-by-method-index`

  * - 3
    - Install the ``salt-minion`` service on the nodes that you want to manage,
      meaning it will receive commands from the Salt master.
    - * :ref:`install-by-operating-system-index`
      * :ref:`install-by-method-index`

  * - 4
    - Configure the Salt master and minions.
    - :ref:`configure-master-minion`

  * - 5
    - Start the service on the minions, then the master.
    - :ref:`start-salt-services`

  * - 6
    - Accept the minion keys after the minion connects.
    - :ref:`accept-keys`

  * - 7
    - Verify that the installation was successful.
    - :ref:`verify-install`


Alternative installations and configurations
============================================
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

  * - Masterless (agentless)
    - Uses Salt SSH to manage minions.
    - `Salt SSH <https://docs.saltproject.io/en/latest/topics/ssh/index.html>`_

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

  * - Run commands locally
    - You can also allow a minion to execute commands locally with ``salt-call``.
      For example: ``salt-call --local [module.function]``.
    - `Salt-call <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>`_

  * - Install Salt for development
    - If you plan to contribute to the Salt codebase, use this installation
      method.
    - `Installing Salt for development <https://docs.saltproject.io/en/latest/topics/development/hacking.html>`_



Using the standard installation method is recommended for most organizations,
especially if you are just starting out with Salt. The standard installation
will make using Salt easier and provides functionality that isn't available in
masterless/agentless Salt configurations.

In general, you should only use alternative installation and configuration
options if you are an intermediate or advanced Salt user.

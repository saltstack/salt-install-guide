.. _configure-master-minion:

=====================================
Configure the Salt master and minions
=====================================

For a basic Salt setup, you only need to edit the Salt minion's configuration
file to add the IP address of the Salt master it will connect to. See
`Basic minion configuration`_ for more information.

This page will explain other configuration options or considerations if needed.

.. Note::
    Before you can configure the Salt master and minions, you must first install
    the ``salt-master`` and ``salt-minion`` services on your nodes. For
    installation instructions, see :ref:`overview`.



Basic master configuration
==========================
* The ``salt-master`` service comes with default server configurations.
* The default master YAML configuration at ``/etc/salt/master`` contains all the
  commented settings.
* Recommended: you can add custom settings in YAML to ``/etc/salt/master.d/`` as ``.conf``
  files on the Salt master.
* Use the default master file as a reference for various settings as needed.


Best practices
--------------
While the ``/etc/salt/master`` file can accept configuration settings, the best
practice is to use the ``/etc/salt/master.d/`` configuration directory. Using
this directory allows you to put configuration options into logical separations.

For example, if you want to set up a different number of ``worker_threads``, you
could store those configurations in the ``/etc/salt/master.d/tuning.conf``
directory and keep all tuning-related configurations in that file.

.. Warning::
    When using multiple ``.conf`` files, take care not to use duplicate
    configuration settings. (For example, setting the number of worker threads
    in more than one configuration file.)

    Salt applies the settings from the last ``.conf`` file it evaluates and it
    evaluates the files in alphabetical order. If you use duplicate
    configuration settings, you could accidentally override the setting you
    intended to apply.



Salt master network settings
----------------------------
By default, the master binds to all available network interfaces, then listens
on ports ``4505`` and ``4506``.

This example overrides the default settings:

.. code-block:: yaml
    :caption: /etc/salt/master.d/network.conf

    # The network interface to bind to
    interface: 192.0.2.20

    # The Request/Reply port
    ret_port: 4506

    # The port minions bind to for commands, aka the publish port
    publish_port: 4505


Salt master process management
------------------------------
If your cluster has thousands of minions, and your minion reports are stalling,
the master might be timing out the job's minion responses. This may mean that
the minions failed their job, but it could instead mean that the master doesn’t
have enough worker threads to process all the reports.

To manage the ``salt-minion`` return calls, the master threads out worker
processes with the ``worker_threads`` setting. The default limit for the
processes is five workers. The minimum limit is three workers.

Example setting in a master configuration file:

.. code-block:: yaml
    :caption: /etc/salt/master.d/thread_options.conf

    worker_threads: 5

Standards for busy environments:

* Use one worker thread per 200 minions.
* The value of ``worker_threads`` should not exceed 1½ times the available CPU
  cores.


Basic minion configuration
===========================
* The ``salt-minion`` service comes with a DNS/hostname configuration setup by
  default.
* The default minion YAML configuration at ``/etc/salt/minion`` contains all the
  commented settings.
* Recommended: you can add custom settings in YAML to ``/etc/salt/minion.d/``
  as ``.conf`` files on the minion.
* Use the default minion file as a reference for various settings as needed.


Best practices
--------------
While ``/etc/salt/minion`` file can accept configuration settings, the best
practice is to use the ``/etc/salt/minion.d/`` configuration directory. Using
this directory allows you to put configuration options into logical separations.

.. Warning::
    When using multiple ``.conf`` files, take care not to use duplicate
    configuration settings. (For example, setting the number of worker threads
    in more than one configuration file.)

    Salt applies the settings from the last ``.conf`` file it evaluates and it
    evaluates the files in alphabetical order. If you use duplicate
    configuration settings, you could accidentally override the setting you
    intended to apply.



Connecting to the Salt master
-----------------------------
By default, the minions assume that the Salt master can be resolved in DNS
using the hostname ``salt``.

An example that overrides the master default setting:

.. code-block:: yaml
    :caption: /etc/salt/minion.d/master.config

    master: 192.0.2.20


Declaring the minion ID
-----------------------
The ``salt-minion`` will identify itself to the master by the system’s hostname
unless explicitly set:

.. code-block:: yaml
    :caption: /etc/salt/minion.d/id.conf

    id: rebel_1

Most strings are allowed. If you decide to customize your minion IDs, try to
keep the ID brief but descriptive of its role. For example, you could use
``apache-server-1`` to name one of your web servers or you could use
``datacenter-3-rack-2`` after its location in a datacenter. The goal is to make
the names descriptive and helpful for future reference.


Additional configuration files
==============================

In addition to the standard Salt master and minion configuration files, you can
create the Saltfile and the ``~/.saltrc`` file for configuration purposes.


Saltfile
--------
The ``~/.salt/Saltfile`` is a separate configuration file that is read at
runtime by the CLI client in use. It can help automate processes if you find
yourself running the same options over and over again in the CLI.

It uses the following format:

.. code:: yaml

  <client>:
    <option>: <setting>

For example:

.. code:: yaml

  salt:
    log_level: debug
  salt-call
    log_level: debug


This example configuration causes both the ``salt`` client and the ``salt-call``
client to output debug level logging to the CLI interface.


The ``~/.saltrc`` file
----------------------
Along with Saltfile, ``~/.saltrc`` file can pass options to the ``salt`` command
line option only. It uses the standard YAML ``key: value`` pair settings.

Salt will automatically look for a ``.saltrc`` configuration file in either
of these locations:

* The home directory
* ``~/.config/saltrc``
* The path set with SALT_MASTER_CONFIG


Common configuration options
============================

.. list-table::
  :widths: 20 80
  :header-rows: 1
  :class: test

  * - Field
    - Description

  * - `worker_threads <https://docs.saltproject.io/en/latest/ref/configuration/master.html#worker-threads>`_
    - This setting helps to prevent the master from getting overtaxed. Sometimes
      you might see a warning message that instructs you to increase the
      master's worker thread count.

      Be aware that you should not set the number of worker threads to be more
      than 1.5 times the number of CPUs a system has. Otherwise, you can cause
      the master to become overtaxed, which was the very problem you tried to
      fix. If you must increase it, you should also consider increasing the
      number of CPUs your system has as well.

  * - `keep_jobs <https://docs.saltproject.io/en/latest/ref/configuration/master.html#keep-jobs>`_
    - This setting is useful when you need to tune a heavily used system. It
      sets the number of hours that jobs are kept before the cleanup operations
      begin for those jobs.

  * - `presence_events <https://docs.saltproject.io/en/latest/ref/configuration/master.html#presence-events>`_
    - Presence events are part of the event system. They help ensure the minions
      remain present and stay actively connected to the master. Presence events
      are if your minions will be parting from and joining the master
      frequently.

  * - `ping_on_rotate <https://docs.saltproject.io/en/latest/ref/configuration/master.html#ping-on-rotate>`_
    - The master uses two different keys when communicating with minions:

      * The minion/master key, which is used for authentication
      * An AES key that is used for communication

      The AES key is rotated in either of these conditions:

      * Every 24 hours on the master
      * When the master is restarted
      * When a minion key deleted.

      The key rotation allows the master to lock out minions that are not
      authenticated and it allows system-wide communication encryption.

      However, sometimes a minion doesn’t pick up the rotated AES key because it
      lagged behind. This option tells the master to ping all minions, forcing
      them to update the AES Key. Enabling ping on rotate can avoid the
      situation where minions don’t respond on the first command after a couple
      of days of inactivity.

For more information
====================
See `Configuring the minion <https://docs.saltproject.io/en/latest/ref/configuration/minion.html>`_
in the core Salt docs for a more detailed list of configuration options.


Next steps
==========
After configuring the Salt minion, you'll need to:

* :ref:`start-salt-services`
* :ref:`accept-keys`

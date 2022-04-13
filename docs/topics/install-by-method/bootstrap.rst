.. _install-bootstrap:

======================
Bootstrap installation
======================

.. include:: ../_includes/install-method.rst


About the Salt bootstrap installation
=====================================
The `Salt Bootstrap project <https://bootstrap.saltproject.io>`_ maintains a
shell script that installs Salt on any Linux/Unix platform. The script installs
``salt-master`` and ``salt-minion`` system packages and enables Salt services
automatically.

This script only works on Unix-like operating systems such as FreeBSD and Linux.
For most installation, the best options are typically ``stable`` and a version.

``-P`` is also needed for Ubuntu-based distributions. If the bootstrap script
can't find a package for a needed file, ``-P`` then installs it through pip.
See `Reference: bootstrap script flags`_ for more information.

For example:

.. code-block:: bash

    bootstrap.sh -P stable 3004.1


Install using the bootstrap script
==================================
The bootstrap script can be used to install specific services:

.. code-block:: bash

    # Download the install script
    curl -o bootstrap-salt.sh -L https://bootstrap.saltproject.io

    # Install minion service (default)
    ./bootstrap-salt.sh

    # Install both the Salt master and minion
    ./bootstrap-salt.sh -M

    # Install just the Salt master service
    ./bootstrap-salt.sh -M -N

    # Perform a pip-based installation
    ./bootstrap-salt.sh -P

    # Download and run
    curl -L https://bootstrap.saltproject.io | sudo sh -s --

    # Download and install a specific git branch/version
    curl -L https://bootstrap.saltproject.io | sudo sh -s -- git develop

    # Make the install script executable
    chmod +x bootstrap-salt.sh



Reference: bootstrap script flags
=================================

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - Flag
    - Description

  * - ``-M``
    - Install the ``salt-master`` service

  * - ``-P``
    - Install from packages. Use ``pip`` if that fails.

  * - ``-U``
    - Update all packages through the operating systems package manager before
      installing.

  * - ``-A <IP address>``
    - The ``-A`` flag needs to be followed by an argument that includes the Salt
      master's IP address. This flag creates the
      ``/etc/salt/minion.d/99-master-address.conf`` file with the content that
      lists the master's IP address: ``master: <IP address>``.

  * - ``-i <minion ID>``
    - The ``-i`` flag sets the ``/etc/salt/minion_id`` file to the minion ID you
      want to assign a custom ID to the Salt minion. Setting a minion ID allows
      you to use a different minion identifier besides the hostname.

      Most strings are allowed. If you decide to customize your minion IDs, try
      to keep the ID brief but descriptive of its role. For example, you could
      use ``apache-server-1`` to name one of your web servers or you could use
      ``datacenter-3-rack-2`` after its location in a datacenter. The goal is to
      make the names descriptive and helpful for future reference.

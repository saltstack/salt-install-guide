.. _install-bootstrap:

======================
Bootstrap installation
======================

.. include:: _includes/install-method.rst


About the Salt bootstrap installation
=====================================
The `Salt Bootstrap project <https://bootstrap.saltproject.io>`_ maintains a
Bash shell script that installs Salt on any Linux/Unix platform. The script
installs ``salt-master`` and ``salt-minion`` system packages and enables Salt
services automatically.

This script only works on Unix-like operating systems such as FreeBSD and Linux.
For most installation, the best options are typically ``stable`` and a version.

``-P`` is also needed for Ubuntu-based distributions. If the bootstrap script
can't find a package for a needed file, ``-P`` then installs it through pip.

For example:


.. parsed-literal::

    bootstrap-salt.sh -P stable |release|

For more information, see:

* `Installation types`_
* `Commonly used bootstrap script options`_
* `Additional bootstrap script options`_

The source code and reference documentation for the bootstrap script is on the
`salt-bootstrap <https://github.com/saltstack/salt-bootstrap/blob/develop/bootstrap-salt.sh>`_
repository.

.. Warning::
    The bootstrap script can only install packages that are on
    `repo.saltproject.io <https://repo.saltproject.io/>`__. It will not work
    with packages on `archive.repo.saltproject.io <https://archive.repo.saltproject.io/>`__,
    which contains the old packages for unsupported versions.


Install using the bootstrap script
==================================
The bootstrap script can be used to install specific services:

#. Download the install script using the following command:

   .. code-block:: bash

       curl -o bootstrap-salt.sh -L https://bootstrap.saltproject.io

   .. Note::
       Alternatively, to download the bash script and run it immediately, use:

       .. code-block:: bash

           curl -L https://bootstrap.saltproject.io | sudo sh -s --


#. Optional: Use the following command to make the bootstrap script executable:

   .. code-block:: bash

       chmod +x bootstrap-salt.sh

#. Run the bash script to install Salt services. Add option flags as needed to
   customize the installation. See `Commonly used bootstrap script options`_
   and `Additional bootstrap script options`_ for more information.

   For example, to run the default, which only installs the minion service:

   .. code-block:: bash

       ./bootstrap-salt.sh

   To install both the Salt master and minion services:

   .. code-block:: bash

       ./bootstrap-salt.sh -M

   To install just the Salt master service:

   .. code-block:: bash

       ./bootstrap-salt.sh -M -N

   To perform a pip-based installation:

   .. code-block:: bash

       ./bootstrap-salt.sh -P


.. Tip::
    The `Salt bootstrap README <https://github.com/saltstack/salt-bootstrap>`_
    provides additional examples for a variety of installation scenarios.
    Consider reading it for more information.


Installation types
==================

.. list-table::
  :widths: 20 40 40
  :header-rows: 1

  * - Type
    - Description
    - Arguments

  * - ``stable``
    - Installs the latest stable release, which is the default installation
      type.
    - If you don't provide an argument, the latest stable release is used by
      default.

      Example:

      .. code-block:: bash

          bootstrap-salt.sh stable

  * - ``stable [version]``
    - Install a specific version. Only supported for packages available at
      `repo.saltproject.io <https://repo.saltproject.io/>`__. To pin a 3xxx
      minor version, specify it as ``3xxx.0``.
    - Pass the version number of Salt release that you want to install.

      Example:

      .. parsed-literal::

          bootstrap-salt.sh -P stable |release|
          bootstrap-salt.sh stable v3004.2

  * - ``testing``
    - This installation type is specific to the RHEL-family of operating
      systems. Use this to configure EPEL testing repository.
    - No arguments.

      Example:

      .. code-block:: bash

          bootstrap-salt.sh testing

  * - ``git``
    - Install from the head of the default branch (master or main).
    - If you don't provide an argument, the latest head from the default branch
      is used by default.

      Example:

      .. code-block:: bash

          bootstrap-salt.sh git
          bootstrap-salt.sh git develop


  * - ``git [ref]``
    - Install from any git reference (such as a branch, tag, or commit).
    - Pass in a git reference, such as a branch, tag, or commit to install from.

      Example:

      .. code-block:: bash

          bootstrap-salt.sh git 3003.3
          bootstrap-salt.sh git v3002.7



Commonly used bootstrap script options
======================================
You can combine options that don't take arguments together, if needed. For
example:

.. code-block:: bash

    ./bootstrap-salt.sh -MNP

The following are the most commonly used bootstrap options:

.. list-table::
  :widths: 20 40 40
  :header-rows: 1

  * - Option
    - Description
    - Arguments

  * - ``-M``
    - Install the ``salt-master`` service.
    - No arguments.

  * - ``-P``
    - Install from packages. Use ``pip`` if that fails.
    - No arguments.

  * - ``-U``
    - Update all packages through the operating systems package manager before
      installing. NOTE: Running this operation may take a long time.
    - No arguments.

  * - ``-A <IP address>``
    - Declares the IP address or FQDN of the Salt master that the Salt minion
      will connect to and be eventually managed by. When the Salt minion service
      first starts, the minion will send its key to the Salt master at this
      IP address or hostname (FQDN) for acceptance.
    - The ``-A`` flag needs to be followed by an argument that includes the Salt
      master's IP address. This flag creates the
      ``/etc/salt/minion.d/99-master-address.conf`` file with the content that
      lists the master's IP address or FQDN.

      Example:

      .. parsed-literal::

          bootstrap-salt.sh -A 192.0.2.1 stable |release|
          bootstrap-salt.sh -A fqdn.example.com stable |release|

  * - ``-i <minion ID>``
    - The ``-i`` flag sets the ``/etc/salt/minion_id`` file to the minion ID you
      want to assign a custom ID to the Salt minion. The minion ID is the name
      that the master uses to identify the minion. When the minion ID is set up
      automatically, it defaults to the minion's hostname (FQDN). However, you
      can use this option to set a custom minion ID using whatever datatype or
      naming convention you prefer.
    - Most strings are allowed. If you decide to customize your minion IDs, try
      to keep the ID brief but descriptive of its role.

      Example:

      .. parsed-literal::

          bootstrap-salt.sh -i apache-server-1 stable |release|
          bootstrap-salt.sh -i center-3-rack-2 stable |release|

  * - ``-R``
    - Specify a custom repository URL if you have created a mirror repository
      for your Salt packages. This option assumes the custom repository URL
      points to a repository that mirrors Salt packages located at
      `https://repo.saltproject.io/ <repo.saltproject.io>`_. The option passed
      with ``-R`` replaces the ``repo.saltproject.io``. If ``-R`` is passed,
      ``-r`` is also set. Currently only works on CentOS/RHEL and Debian-based
      distributions. You could also use this option to point to
      `https://archive.repo.saltproject.io/ <archive.repo.saltproject.io>`_.
    - Pass the URL of the mirror repository that the node should use for Salt
      packages. This option assumes the repository exists.

      Example:

      .. code-block:: bash

          bootstrap-salt.sh -R repo.example.com

  * - ``-r``
    - Disable all repository configurations performed by this script. This
      option assumes all the necessary repository configurations are already
      present on the system.
    - No arguments.


Additional bootstrap script options
===================================
For a slightly more comprehensive list of options, see the source code and
reference documentation on the
`salt-bootstrap <https://github.com/saltstack/salt-bootstrap/blob/develop/bootstrap-salt.sh>`_
repo.


.. list-table::
  :widths: 10 45 45
  :header-rows: 1

  * - Option
    - Description
    - Arguments

  * - ``-a``
    - Pip install all Python pkg dependencies for Salt. Must be used with ``-V``
      to install all pip packages into the virtualenv. (Only available for
      Ubuntu-based distributions).
    - No arguments.

  * - ``-b``
    - Assume that dependencies are already installed and software sources are
      set up. If the ``git`` installation type is selected, git tree is still
      checked out as dependency step.
    - No arguments.

  * - ``-c``
    - Temporary configuration directory. Used with `-k` and `-K`.
    - Pass in a directory path.

  * - ``-C``
    - Only run the configuration function. Implies ``-F`` (forced overwrite).
      To overwrite Master or Syndic configs, ``-M`` or ``-S``, respectively,
      must also be specified. Salt installation will be omitted, but some of the
      dependencies could be installed to write configuration with ``-j`` or
      ``-J``.
    - No arguments.

  * - ``-d``
    - Disables checking if Salt services are enabled to start on system boot.
      You can also do this by touching ``/tmp/disable_salt_checks`` on the
      target host.
    - No arguments.

  * - ``-D``
    - Show the debug output in the CLI.
    - No arguments.

  * - ``-f``
    - Only used for git installation types. This option forces shallow cloning
      for git installations. Rather than cloning an entire repository, it only
      includes the portion of the repository that you are interested in to
      improve performance. Note that this option may result in an ``n/a`` in the
      version number.
    - No arguments.

  * - ``-F``
    - Allow copied files to overwrite existing (config, init.d, etc.).
    - No arguments.

  * - ``-g``
    - Salt Git repository URL. It defaults to the Salt repository at
      `https://repo.saltproject.io/ <repo.saltproject.io>`_.
    - No arguments.

  * - ``-H``
    - Use the specified HTTP proxy for all download URLs (including https://).
    - Pass in the URL for the HTTP proxy. For example:
      ``http://myproxy.example.com:3128``.


  * - ``-I``
    - If set, allow insecure connections while downloading any files. For
      example, pass ``--no-check-certificate`` to ``wget`` or ``--insecure`` to
      ``curl``. On Debian and Ubuntu, using this option with ``-U`` allows
      obtaining  GnuPG archive keys insecurely if the distribution has changed
      release signatures.
    - No arguments.

  * - ``-j``
    - Replace the minion configuration file with data passed in as a JSON
      string. If a minion configuration file is found, a reasonable effort will
      be made to save the file with a ``.bak`` extension. If used in conjunction
      with ``-C`` or ``-F``, no ``.bak`` file will be created as either of
      those options will force a complete overwrite of the file. When formatting
      JSON strings, it might be helpful to use a JSON checking and conversion
      tools that are available online.
    - Include a JSON string. For example: ``JSONSTRING='{"grains":{"roles":"test"}}'``

  * - ``-J``
    - Replace the master configuration file with data passed in as a JSON
      string. If a master configuration file is found, a reasonable effort will
      be made to save the file with a ``.bak`` extension. If used in conjunction
      with ``-C`` or ``-F``, no ``.bak`` file will be created as either of those
      options will force a complete overwrite of the file. When formatting
      JSON strings, it might be helpful to use a JSON checking and conversion
      tools that are available online.
    - Include a JSON string. For example: ``JSONSTRING='{"grains":{"roles":"test"}}'``

  * - ``-k``
    - Temporary directory holding the minion keys which will pre-seed the
      master.
    - Pass in a path for a directory that has minion keys in it.

  * - ``-K``
    - If set, keep the temporary files in the temporary directories specified
      with ``-c`` and ``-k``.
    - No arguments.

  * - ``-l``
    - Disable ssl checks. When passed, switches ``https`` calls to ``http``
      where possible.
    - No arguments.

  * - ``-L``
    - Also install salt-cloud and required python-libcloud package.
    - No arguments.

  * - ``-n``
    - No colors.
    - No arguments.

  * - ``-N``
    - Do not install salt-minion.
    - No arguments.

  * - ``-p``
    - Extra-package to install while installing Salt dependencies. One package
      per ``-p`` flag. You are responsible for verifying the correct package
      name. The bootstrap script will not provide an error message if the
      package cannot be installed.
    - Provide the virtual package name for the system you are using.

  * - ``-q``
    - Quiet salt installation from git: ``setup.py install -q``. The log will
      display less messages unless there is an error.
    - No arguments.

  * - ``-s``
    - Sleep time used when waiting for daemons to start/restart and when
      checking for the services running. The default is 3.
    - Pass in a number (in seconds) for how long the sleep time should be.

  * - ``-S``
    - Also install salt-syndic.
    - No arguments.

  * - ``-v``
    - Display script version.
    - No arguments.

  * - ``-V``
    - Install Salt into virtualenv. Only available for Ubuntu-based
      distributions.
    - No arguments.

  * - ``-X``
    - Do not start daemons after installation.
    - No arguments.

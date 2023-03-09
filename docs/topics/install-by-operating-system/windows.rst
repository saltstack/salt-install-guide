.. _install-windows:

=======
Windows
=======

This page provides download files and instructions for installing Salt on
Windows.

* `Windows downloads`_
* `Important information about installing on Windows`_
* `Install Salt on Windows`_
* `Windows Nullsoft EXE install options`_
* `Windows MSI install options`_


Windows downloads
=================

.. include:: ../_includes/windows-downloads.rst

.. card:: Browse the repo for Windows packages
    :link: https://repo.saltproject.io/windows/
    :width: 50%

    :bdg-primary:`Windows`
    :bdg-secondary:`Python3`



Important information about installing on Windows
=================================================
Windows has two installer options:

* A Nullsoft (.exe) installer
* An MSI (.msi) installer

If you are unsure which installer to use, use the Nullsoft (EXE) installer.

Onedir packages are currently only available for the Nullsoft (EXE) installer.

.. include:: ../_includes/warning-about-old-packages.rst


Install directory locations
---------------------------
In versions of Salt prior to Salt 3004, Nullsoft (EXE) Windows installer only
installed Salt in the root C drive directory: ``C:\Salt``.

In versions 3004 and later, the Nullsoft (EXE) installer defaults to installing
Salt in the ``C:\Program Files\Salt Project\Salt`` directory path. The install
directory stores Salt binary data. If you choose a custom install directory
path, Salt registers that directory as the ``install_dir``.

.. Note::
    You can choose a custom install directory path from the command line using
    the ``/install-dir`` option. See `Windows Nullsoft EXE install options`_
    for more information.


Also in versions 3004 and later, the Nullsoft (EXE) installer creates a second
directory in ``C:\ProgramData\Salt Project\Salt`` called the config directory.
The config directory is where Salt stores non-binary data such as configuration
files, logs, and the cache. This path cannot be customized. Salt registers that
directory as the ``root_dir``.

By default, the installer will not move configuration data that is stored in
the old ``C:\Salt`` directory for older installations. However, the installer
can move an older, existing Salt configuration directory from the old location
to ``ProgramData`` by passing the ``/move-config`` option on the command line.
Additionally, if the installer detects an existing config in the old location,
the user interface displays a checkbox with the option to move the ``root_dir``
to ``ProgramData``.

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Windows
=======================
To install Salt on Windows:

#. Download the Salt installation file for Windows. See `Windows downloads`_ for
   a list of the latest downloads.

#. Run the file to install Salt with a graphical user interface.

   You can optionally run the file from the command line. One advantage of
   running the file from the command line is that you can add various options
   for a custom installation. See `Windows Nullsoft EXE install options`_ or
   `Windows MSI install options`_ for more information.

   The following is an example of running a silent installation from the command
   line:

   .. tab-set::

       .. tab-item:: Nullsoft (EXE) installer

          .. parsed-literal::

              |windows-install-exe-example| /S /master=yoursaltmaster /minion-name=yourminionname

          See `Windows Nullsoft EXE install options`_ for more information about
          options and additional examples.

       .. tab-item:: MSI installer

           .. parsed-literal::

               msiexec /i |windows-install-msi-example| /quiet /norestart MASTER=yoursaltmaster MINION_ID=yourminionname

           See `Windows MSI install options`_ for more information about options.


   .. Admonition:: Salt install directory

       See `Install directory locations`_ for information about where Salt is
       installed by default and how you can customize that setting.

.. include:: ../_includes/post-install-by-os.rst


Windows Nullsoft EXE install options
====================================
The most commonly used install options are:

* ``/master``
* ``/minion-name``
* ``/S``


.. list-table::
  :widths: 20 50 30
  :header-rows: 1

  * - Option
    - Description
    - Example input

  * - ``/?``
    - Displays this help screen with the install option documentation.
    - ``.\Salt-Minion-3005-1-Py3-AMD64-Setup.exe /?``

  * - ``/custom-config=``
    - Pass in a string specifying the name of a custom configuration file. The
      file path must be in the same path as the installer or it should be the
      full path.

      If ``/master`` and/or ``/minion-name`` is also passed, those values will
      be used to update the new custom configuration file.

      Any existing configuration files will be backed up by appending a timestamp
      and a ``.bak`` extension, including the minion file and the ``minion.d``
      directory.
    - * ``/custom-config=my-custom-config.conf``
      * ``/custom-config=C:\Temp\my-custom-config.conf``

  * - ``/default-config``
    - If any existing configuration files are present, this option will
      overwrite the existing configuration and replace it with the default Salt
      configuration file.

      The default is to use the existing configuration file if present. If
      ``/master`` and/or ``/minion-name`` is also passed, those values will be
      used to update the new default configuration file.

      Any existing configuration files will be backed up by appending a
      timestamp and a ``.bak`` extension, including the minion file and the
      ``minion.d`` directory.
    -

  * - ``/install-dir=``
    - Specify the installation location for the Salt binaries. This option will
      be ignored for existing installations. See `Install directory locations`_
      for information about where Salt is installed by default and how you can
      customize that setting.
    - ``/install-dir=C:\Software\salt``

  * - ``/move-config``
    - If a configuration file is found at ``C:\Salt`` it will be moved to
      ``%ProgramData%``.
    -

  * - ``/master=``
    - Sets the master name or IP address. You  may pass a single master or a
      comma-separated list of masters. Setting the master will cause the
      installer to use the default config or a custom config if provided.

      If no master is specified, the default value is ``salt``.

      Be aware that you can only use a master name if you have set up your DNS
      server to resolve the master's name to its IP address. For example, you
      would need to set up ``salt`` to resolve to the IP address in order for
      the default to work correctly.
    - * ``/master=192.0.2.1``

      * ``/master=salt-windows-master-1``

      * ``/master=master.mydomain.com``

      * ``/master=192.0.2.1,192.0.2.2,192.0.2.3``

  * - ``/minion-name=``
    - Sets the minion name. If no minion ID is specified, the default will be
      ``hostname``. Setting the minion name causes the installer to use the
      default config or it will use a custom config if provided.
    - * ``/minion-name=192.0.2.1``

      * ``/minion-name=salt-windows-minion-1``

  * - ``/start-minion=``
    - If you set the value to 1, the installer will start the minion service
      after installation. If set to, it 0 will not. The default is 1.
    - * ``/start-minion=1``

      * ``/start-minion=0``

  * - ``/S``
    - Use this option to install Salt silently.
    - ``Salt-Minion-3005-1-Py3-AMD64-Setup.exe /S``


  * - ``/start-minion-delayed``
    - Use this option to set the minion service to start after installation, but
      to delay for 30-60 seconds, depending on the operating system settings. If
      you use this option, the minion start type will be set to
      ``Automatic (Delayed Start)``.
    - ``Salt-Minion-3005-1-Py3-AMD64-Setup.exe /start-minion-delayed``


Windows MSI install options
===========================
The most commonly used install options are:

* ``MASTER``
* ``MINION_ID``
* ``/quiet``
* ``/norestart``

.. Note::
    For more information about the MSI installer, see the
    `Windows MSI installer repository <https://github.com/saltstack/salt-windows-msi>`_
    repository on GitHub.


The following table describes all available options, listed alphabetically:

.. list-table::
  :widths: 20 50 30
  :header-rows: 1

  * - Option
    - Description
    - Example values

  * - ``ARPSYSTEMCOMPONENT``
    - Set to ``1`` to hide the Salt minion application in ``Programs and
      Features``.
    - ``ARPSYSTEMCOMPONENT=1``

  * - ``CLEAN_INSTALL``
    - Set to ``1`` to remove configuration and clear the cache before an
      installation or upgrade.
    - ``CLEAN_INSTALL=1``

  * - ``CONFIG_TYPE``
    - Set to ``Custom`` or ``Default`` for the installation scenario you want to
      apply. The default value is ``Existing``. See
      `MSI installation scenarios`_ for more information..
    - * ``CONFIG_TYPE=Existing``

      * ``CONFIG_TYPE=Custom``

      * ``CONFIG_TYPE=Default``

  * - ``CUSTOM_CONFIG``
    - This option is only available from the command line and must be used along
      with the ``CONFIG_TYPE=Custom`` option.

      Pass in the name of a custom configuration file. The file path must either
      be in the same path as the installer or it should be the full path.
    - * ``CUSTOM_CONFIG=my-custom-config.conf``

      * ``CUSTOM_CONFIG=C:\Temp\my-custom-config.conf``

  * - ``INSTALLDIR``
    - Use this option to install the binaries to a custom directory path. The
      default value is ``C:\Program Files\Salt Project\Salt``.
    - ``INSTALLDIR=C:\Salt Binaries\``

  * - ``MASTER``
    - Sets the master name or IP address. You may pass a single master or a
      comma-separated list of masters.

      If no master is specified, the default value is ``salt``.

      Be aware that you can only use a master name if you have set
      up your DNS server to resolve the master's name to its IP address. For
      example, you would need to set up ``salt`` to resolve to the IP address
      in order for the default to work correctly.
    - * ``MASTER=192.0.2.1``

      * ``MASTER=salt-windows-master-1``

      * ``MASTER=master.mydomain.com``

      * ``MASTER=192.0.2.1,192.0.2.2,192.0.2.3``

  * - ``MASTER_KEY``
    - Sets the master public key. To use this option, first convert the public
      key converted into one line by removing the first and last line:
      ``-----BEGIN PUBLIC KEY-----`` and ``-----END PUBLIC KEY-----``. Then,
      remove any line breaks.
    - Generally, most public keys start with ``ssh-rsa``, ``ssh-dss``,
      ``ecdsa-sha2-nistp256``, ``ecdsa-sha2-nistp384``, ``ecdsa-sha2-nistp521``,
      ``ssh-ed25519``, ``sk-ecdsa-sha2-nistp256@openssh.com``, or
      ``sk-ssh-ed25519@openssh.com``.

  * - ``MINION_CONFIG``
    - Sets the content that will write to the minion configuration file.

      If you use this option, it operates the same as ``REMOVE_CONFIG=1``. That
      means:

      * All prior minion configuration files and options are overwritten and
        deleted, including all ``minion.d\*.conf`` files and the ``minion_id``
        file.
      * Its content is written to configuration file ``conf\minion``.
      * Use the ``^`` character for line breaks. This character will be replaced
        by line breaks during installation.
    - ``MINION_CONFIG="master: Anna^id: Bob"`` results in:

      .. code-block:: bash

          master: Anna
          id: Bob

  * - ``MINION_ID``
    - Sets the minion name. If no minion ID is specified, the default will be
      the hostname or IP address.
    - * ``MINION_ID=192.0.2.1``

      * ``MINION_ID=salt-windows-minion-1``

  * - ``MOVE_CONF``
    - If a configuration file is found at ``C:\Salt`` it will be moved to
      ``%ProgramData%``.
    - ``MOVE_CONF=1``

  * - ``/norestart``
    - Runs the installer silently. Usually used along with ``/quiet``.
    - ``msiexec /i |windows-install-msi-example| /quiet /norestart``

  * - ``/quiet`` or ``/qn``
    - Runs the installer silently. Usually used along with ``/norestart``.
    - ``msiexec /i |windows-install-msi-example| /quiet /norestart``

  * - ``/passive`` or ``/qb``
    - Runs the installer silently, but displays a progress bar. Usually used
      along with ``/norestart``.
    - ``msiexec /i |windows-install-msi-example| /passive /norestart``

  * - ``REMOVE_CONFIG``
    - Set to ``1`` if you want to remove configuration files on uninstall. When
      you run ``MINION_CONFIG``, this option is automatically run in order to
      delete the existing configuration file that will be replaced by the new
      file. Running this option alone will not create a new configuration file.
    - ``REMOVE_CONF=1``

  * - ``ROOTDIR``
    - Use this option to install the configuration files to a custom directory
      path. The default value is ``C:\ProgramData\Salt Project\Salt``
    - ``ROOTDIR=C:\Salt Configurations\``

  * - ``START_MINION``
    - Starts the minion service after installation. Set this value to ``""`` to
      prevent the start of the ``salt-minion`` service. The default value is
      ``1``, which starts the service.
    - * ``START_MINION``

      * ``START_MINION=1``

      * ``START_MINION=""``


MSI installation scenarios
==========================
The ``CONFIG_TYPE`` option can support three possible installation scenarios.


Existing
--------
The Existing setting is recommended for simple upgrades. It makes no changes to
the existing configuration and only upgrades Salt. For this type of
installation, run the installer with a silent option. If there is no existing
configuration, the installer creates a default configuration. The master and
minion ID are applied if they are passed.


Custom
------
The Custom setting will apply a custom configuration file passed from the
command line. To ensure the custom configuration is applied correctly, the
installer backs up any existing configurations following this order of
operations:

#. The minion configuration file is renamed to ``minion-<timestamp>.bak``.

#. The ``minion_id`` file is renamed to ``minion_id-<timestamp>.bak``.

#. The ``minion.d`` directory renamed to ``minion.d-<timestamp>.bak``

#. The custom config is applied by the installer. If the master and minion ID
   were passed, they will be to the custom configuration file.


Default
-------
This setting will reset the configurations to the default configurations
contained in the package. Therefore, all existing config files should be backed
up first, including:

* The minion configuration file
* The ``minion_id`` file
* The ``minion.d`` directory

.. Warning::
    The MSI installer has a known issue that impacts installers with the ``-X``
    in the file name, such as 3005.1-4. When upgrading these builds, the
    installer creates duplicate entries in Add/Remove Programs. For example, if
    you have 3005.1-1 installed and you use the MSI to upgrade to 3005.1-4, the
    upgrade will complete successfully, but both versions appear in Add/Remove
    Programs.

    The workaround when upgrading between these types of builds using the MSI
    is to uninstall the old version prior to installing the new version.

    Upgrades to and from versions without the ``-X`` will work as expected.

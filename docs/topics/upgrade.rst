.. _upgrade:

============
Upgrade Salt
============

When upgrading Salt, the master(s) should always be upgraded first. Running
minions with versions of Salt newer than their masters is not guaranteed to
function as expected since the minion may include changes not yet available in
the master. Also, whenever possible, backward compatibility between new masters
and old minions will be preserved. Generally, the only exception to this policy
is in case of a security vulnerability.

Salt can be upgraded either through your distribution's package manager or using
PyPI if you have installed Salt with pip, the package installer for Python.

.. Warning::
    For SaltStack Config users: If you initially installed Salt using Salt
    Crystal, you must also upgrade to later versions using Salt Crystal. For
    more information, see
    `How to Upgrade Salt Crystal <https://kb.vmware.com/s/article/50122482?lang=en_US&queryTerm=upgrade%20salt>`_.


Upgrade your Salt infrastructure
================================
To upgrade Salt:

#. Verify the Salt version to check whether your version is supported or not.
   You can verify your installed version of Salt in a few possible ways:

   .. code-block:: bash

       rpm -qi salt
       dpkg-query -l salt\*
       yum list installed salt\*
       salt --versions-report
       salt-call --local test.versions_report

   To check whether your version is supported or not, see
   :ref:`salt-version-support-lifecycle`.

#. Back up your Salt configuration.

   Before upgrading your Salt minion or master, create a backup of your
   ``/etc/salt`` directory. Creating a copy of the directory will create backups
   of the configurations as well as the minion and master keys. If you have
   altered your configuration to use alternative directories, you may consider
   backing those up as well.

#. Before attempting an upgrade, you may need to stop the Salt master daemon or
   minion daemon:

   .. code-block:: bash

       systemctl stop salt-master
       systemctl start salt-minion

   .. Note::
       See `Restart and upgrade minions used in state runs`_ for information
       about troubleshooting starting and stopping minions for an upgrade.


#. Update your package manager's repository configuration.

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Field
        - Description

      * - Update using package manager
        - Configure your package manager to point to the latest release so that
          you are always up to date. For more information, see:

          * :ref:`install-by-operating-system-index`
          * `Pin to a release for updates`_

      * - Update RHEL or CentOS repository configuration
        - To reconfigure your repository from a pinned release to the latest
          release, you can either update the appropriate .repo file or uninstall
          the existing repo RPM and install the latest repo RPM. See
          :ref:`install-rhel` and :ref:`install-centos` for more information.

          For additional information on configuring yum repositories, refer to
          your distribution's documentation.

      * - Update Debian or Ubuntu repository configuration
        - To reconfigure your repository from a previously pinned release to the
          latest release, update the source's configuration from the existing
          source to the latest source listed on :ref:`install-debian` or
          :ref:`install-ubuntu`.

      * - Update macOS or Windows
        - To update Windows or macOS, download the latest installers and run them.
          See :ref:`install-macos` or :ref:`install-windows` for these downloads.

#. If you are upgrading from classic Salt packages to onedir packages, use Salt
   to reinstall any existing third party Python packages. Reinstalling the
   packages ensures they are installed in the correct onedir path.

   .. Admonition:: How do I know which packages need to be reinstalled?

      You can use ``salt-call pip.list`` to view existing modules that may need
      to be installed.

      See also `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.9/linux.txt>`_
      for a list of the packages that are installed with onedir. Any package
      that is not on this list needs to be reinstalled.

   You can use two possible methods to reinstall packages:

   * ``salt pip install <package name>``
   * Use the ``pip.installed`` Salt state.

   .. Note::
       In order to install software such as Python libraries and Salt
       extensions, you'll need to use ``salt-pip`` to install packages into the
       onedir directory. For more information, see the
       `pip.state module documentation <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pip_state.html#module-salt.states.pip_state>`_.


#. With Salt now updated, verify your configuration is correct and restore it
   if necessary.

If you stopped the daemon(s) prior to upgrading, you will need to restart the
daemons. See `Restart and upgrade minions used in state runs`_ for more information.


.. _restart-upgrade-minions-used-in-state-runs:

Restart and upgrade minions used in state runs
==============================================
Be aware that restarting the minion service while in the middle of a state run
interrupts the process of the minion running states and sending results back to
the master.

A common workaround is to schedule restarting the minion service in
the background by issuing a ``salt-call`` command using the ``service.restart``
function. This workaround prevents the minion being disconnected from the master
immediately. Otherwise you would get this error message during a state run:

.. code-block:: bash

    Minion did not return. [Not connected] message


Upgrade without automatic restart
---------------------------------
Most Linux-based operating systems restart the minion service after the package
installation by default. To prevent this, you need to create policy layer that
prevents the minion service from restarting immediately after the upgrade.

The following is an example of a workaround:

.. code-block:: jinja

    {%- if grains['os_family'] == 'Debian' %}

    Disable starting services:
      file.managed:
        - name: /usr/sbin/policy-rc.d
        - user: root
        - group: root
        - mode: 0755
        - contents:
          - '#!/bin/sh'
          - exit 101
        # Do not touch if this already exists
        - replace: False
        - prereq:
          - pkg: Upgrade Salt Minion

    {%- endif %}

    Upgrade Salt minion:
      pkg.installed:
        - name: salt-minion
        - version: 3005{% if grains['os_family'] == 'Debian' %}+ds-1{% endif %}
        - order: last

   Enable Salt minion:
     service.enabled:
       - name: salt-minion
       - require:
         - pkg: Upgrade Salt Minion

   {%- if grains['os_family'] == 'Debian' %}

   Enable starting services:
     file.absent:
       - name: /usr/sbin/policy-rc.d
       - onchanges:
         - pkg: Upgrade Salt Minion

   {%- endif %}


Pin to a release for updates
============================
When you install Salt on your Linux systems, it creates a file that tells the
system where it should download the latest packages for Salt. The exact location
of the file varies by operating system.

When you install Salt, you need to select the repository that you want to pin
for updates. The following sections explain the different options for
repositories you can pin for updates:


.. _onedir:

Onedir
------
Onedir is Salt's new packaging system (as of 3005). Onedir stands for "one
directory" because the goal is to provide a single directory containing all the
executables that Salt needs. It includes the version of Python needed by Salt
and its required dependencies. The onedir packages simplify the installation
process because they allow you to use Salt out of the box without installing
Python or other dependencies first. See :ref:`what-is-onedir` for more
information.

Beginning with the release of Salt 3005 (Phosphorus), the Salt Project will
begin replacing the old packaging system with the Tiamat packaging system.
The Salt Project **strongly** recommends upgrading to onedir to continue
receiving Salt version updates. See :ref:`upgrade-to-onedir` for more
information.


.. _classic:

Classic
-------
Classic packages refer to the old Salt packaging system. These packages will be
provided for Salt for currently supported operating systems for the 3005 and
3006 releases. After that, all Salt packages will be onedir packages.


.. _latest:

Latest
------
Installs the latest release of Salt. Updating installs the latest release even
if it is a new major version.


.. _major:

Major
-----
Installs the latest release. Updating installs the latest minor release but not
a new major version.


.. _minor:

Minor
-----
Installs a specific release. Updating doesn’t change the release that is
installed.

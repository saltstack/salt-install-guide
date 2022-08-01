.. _upgrade-to-onedir:

=================
Upgrade to onedir
=================

Onedir is the Salt Project's new packaging system. Beginning with the release of
Salt 3005 (Phosphorus), the Salt Project will begin replacing the old packaging
system with the onedir packaging system.


.. _what-is-onedir:

What is onedir?
===============
Onedir stands for "one directory" because the goal is to provide a single
directory containing all the executables that Salt needs. It includes the
version of Python needed by Salt and its required dependencies.

Onedir packages simplify the installation process because they allow you to
use Salt out of the box without installing Python or other dependencies first.

Onedir packages are self-contained binaries of Salt. Onedir packages include:

.. list-table::
  :widths: 40 60
  :header-rows: 1

  * - What is installed
    - For more information

  * - The version of Python needed by Salt
    - :ref:`salt-python-version-support`

  * - Salt's required dependencies
    - `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.9/linux.txt>`_


.. Warning::
    The dependencies included with onedir are required for Salt's core
    functionality only. If you are using a Salt module that has an additional
    dependency, you will need to additionally install any dependencies required
    by that specific module. See the
    `module documentation <https://docs.saltproject.io/en/latest/py-modindex.html>`_
    for that specific module for a list of required dependencies.


Timeline for upgrading to onedir packaging
==========================================
In order to avoid disruption of services and continue getting upgraded versions
of Salt, begin planning how you will update your Salt infrastructure to onedir
before the 3007 release. See `How to upgrade to onedir`_ for more information.

.. list-table::
  :widths: 15 85
  :header-rows: 1
  :stub-columns: 1

  * - Salt version
    - Packaging changes

  * - 3005
    -  * The Salt Project will begin to phase out the old, "classic" Salt
         package builds.
       * Both onedir packages and classic Salt package builds will be provided,
         except for operating systems that are newly supported in 3005.
       * See `Platform package support for Salt 3005`_ for more information.

  * - 3006
    -  * Both onedir packages and classic Salt package builds will be provided,
         except for operating systems that are newly supported in 3006.
       * Only classic packages will be provided for platforms that do not
         support Python 3.7 or higher, including Ubuntu 18.04, RHEL 7, RHEL 8,
         Raspbian 9, and Raspbian 10.

  * - 3007
    - The Salt Project will only support onedir packages going forward.


How to upgrade to onedir
========================
To upgrade to onedir:

#. On your Salt infrastructure (masters, minions, etc.), update the repository
   path to point to the new onedir repository paths for your operating system.
   See `Repository paths`_ for more information.

   .. Tip::
       Rather than manually updating the configuration files with the correct
       repository link, you can re-run the installation commands for your
       operating system. When you re-run the commands, make sure you select the
       instructions for the **onedir** version of the package. See
       :ref:`install-by-operating-system-index` for the specific commands.

#. After the repository file is updated, upgrade your Salt packages.

#. Restart the Salt services.

   .. code-block:: bash

       systemctl start salt-master
       systemctl start salt-minion

#. Ensure any 3rd party pip packages are installed in the correct onedir path.

   You can use two possible methods:

   * ``salt pip install <package name>``
   * Using the ``pip.installed`` Salt state.


Repository paths
----------------
The following onedir paths will not be available until the day of the Salt 3005
(Phosphorus) release. The classic (non-onedir) paths are available now.

.. list-table::
  :widths: 10 50 40
  :header-rows: 1
  :stub-columns: 1

  * -
    - Onedir path
    - Classic path

  * - CentOS
    - https://repo.saltproject.io/salt/py3/redhat/
    - https://repo.saltproject.io/py3/redhat/

  * - Debian
    - https://repo.saltproject.io/salt/py3/debian/
    - https://repo.saltproject.io/py3/debian/

  * - Fedora
    - Hosted on Fedora repos
    - Hosted on Fedora repos

  * - MacOS
    - https://repo.saltproject.io/salt/py3/osx/
    - https://repo.saltproject.io/osx/

  * - Raspbian
    - https://repo.saltproject.io/salt/py3/debian/
    - https://repo.saltproject.io/py3/debian/

  * - Redhat
    - https://repo.saltproject.io/salt/py3/redhat/
    - https://repo.saltproject.io/py3/redhat/

  * - Ubuntu
    - https://repo.saltproject.io/salt/py3/ubuntu/
    - https://repo.saltproject.io/py3/ubuntu/

  * - Windows
    - https://repo.saltproject.io/salt/py3/windows/
    - https://repo.saltproject.io/windows/



Platform package support for Salt 3005
======================================

.. list-table::
  :widths: 25 35 40
  :header-rows: 1
  :stub-columns: 1
  :class: checkmarks

  * -
    - New onedir packages
    - Classic packages (non-onedir)

  * - CentOS 8 Streaming
    - Yes
    -

  * - CentOS 9 Streaming
    - Yes
    -

  * - Debian 9
    - Yes
    - Yes

  * - Debian 10
    - Yes
    - Yes

  * - Debian 11
    - Yes
    - Yes

  * - Fedora 35
    - Yes
    - Yes

  * - Fedora 36
    - Yes
    - Yes

  * - MacOS
    - Yes
    - Yes

  * - Raspbian 9
    - Yes
    - Yes

  * - Raspbian 10
    - Yes
    - Yes

  * - Raspbian 11
    - Yes
    - Yes

  * - RedHat 7
    - Yes
    - Yes

  * - RedHat 8
    - Yes
    - Yes

  * - RedHat 9
    - Yes
    - Yes

  * - Ubuntu 18.04
    - Yes
    - Yes

  * - Ubuntu 20.04
    - Yes
    - Yes

  * - Ubuntu 22.04
    - Yes
    -

  * - Windows
    - Yes
    - Yes

.. _install-dependencies:

====================
Install dependencies
====================

Salt and the Salt services require various packages to be present in order to
run effectively. If you host your own custom built repository of Salt, you
must also ensure these packages are present in the repository. For example, if
your system is air-gapped and uses a minimal repository, these packages must be
present in order for the Salt services to run correctly.

The following list the package dependencies for each operating system for
onedir packages.


Installing dependencies in onedir versions of Salt
==================================================
When you install a onedir version of Salt (3006 and later), Salt installs its
own local version of Python and the dependencies needed for the core
functionality of Salt. See `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.9/linux.txt>`_ for a list of packages that come installed with Salt.

After installing a onedir verison of Salt, your system has both a global version
of Python at the system level and a local version of Python used by Salt. This
architecture change means that the Salt onedir paths for Python are different
and you need to change how you install third-party Python dependencies that you
use with Salt, including your state files.

The recommended approach is to install dependencies is to use Salt to reinstall
any existing third-party Python packages. Reinstalling the packages ensures they
are in the correct onedir path:

#. Use ``salt-call pip.list`` to view existing modules that may need to be
   installed.

   .. Note::

      See `Salt dependencies <https://github.com/saltstack/salt/blob/master/requirements/static/pkg/py3.9/linux.txt>`_
      for a list of the packages that are installed with onedir. Any package
      that is not on this list needs to be reinstalled.

#. You can use two possible methods to reinstall packages:

   * ``salt-pip install <package name>``
   * Use the ``pip.installed`` Salt state.

   .. Note::
       In order to install software such as Python libraries and Salt
       extensions, you'll need to use ``salt-pip`` to install packages into the
       onedir directory. For more information, see the
       `pip.state module documentation <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.pip_state.html#module-salt.states.pip_state>`_.

#. After upgrading to onedir, you might need to update any state files that use
   ``pip.installed`` if you need to install Python packages into the system
   Python environment. In the state file, provide the ``pip_bin`` or ``bin_env``
   to the pip state module.

   For example:

   .. code-block:: yaml

       lib-foo:
         pip.installed:
           - pip_bin: /usr/bin/pip3
       lib-bar:
         pip.installed:
           - bin_env: /usr/bin/python3

#. After upgrading to onedir, you might also need to update any salt ``gitfs``
   formula branches if the formula has changed because of onedir-specific fixes.



List of dependencies by operating system
========================================

Amazon Linux 2
--------------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /bin/bash
        * /bin/sh
        * /usr/bin/env
        * config(salt) = 3005.1-2.amzn2
        * dmidecode
        * libc.so.6
        * libdl.so.2
        * libpthread.so.0
        * libz.so.1
        * openssl
        * pciutils
        * rpmlib
        * rtld
        * systemd-units
        * which

   * - salt-minion
     -  * /bin/bash
        * /bin/sh
        * config(salt-minion) = 3005.1-2.amzn2
        * rpmlib
        * salt = 3005.1

   * - salt-master
     -  * /bin/bash
        * /bin/sh
        * config(salt-master) = 3005.1-2.amzn2
        * rpmlib
        * salt = 3005.1-2.amzn2

   * - salt-api
     -  * /bin/bash
        * /bin/sh
        * rpmlib
        * salt-master = 3005.1-2.amzn2

   * - salt-cloud
     -  * /bin/bash
        * config(salt-cloud) = 3005.1-2.amzn2
        * rpmlib
        * salt-master = 3005.1-2.amzn2

   * - salt-ssh
     -  * /bin/bash
        * config(salt-ssh) = 3005.1-2.amzn2
        * rpmlib
        * salt = 3005.1-2.amzn2

   * - salt-syndic
     -  * /bin/bash
        * /bin/sh
        * rpmlib
        * salt-master = 3005.1-2.amzn2


Debian 10
---------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Recommends:

       * lsb-release

       Suggests:

       * ifupdown

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)

       Recommends:

       * debconf-utils
       * dmidecode
       * net-tools

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-api
     - Depends:

       * salt-master

   * - salt-cloud
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * openssh-client

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)


Debian 11
---------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Recommends:

       * lsb-release

       Suggests:

       * ifupdown

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)

       Recommends:

       * debconf-utils
       * dmidecode
       * net-tools

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-api
     - Depends:

       * salt-master

   * - salt-cloud
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * openssh-client

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)


RedHat 7
--------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /bin/bash
        * /bin/sh
        * /usr/bin/env
        * config(salt) = 3005.1-2.el7
        * dmidecode
        * libc.so.6
        * libdl.so.2
        * libpthread.so.0
        * libz.so.1
        * openssl
        * pciutils
        * rpmlib
        * rtld
        * systemd-units
        * which

   * - salt-minion
     -  * /bin/bash
        * /bin/sh
        * config(salt-minion) = 3005.1-2.el7
        * rpmlib
        * salt = 3005.1-2.el7

   * - salt-master
     -  * /bin/bash
        * /bin/sh
        * config(salt-master) = 3005.1-2.el7
        * rpmlib
        * salt = 3005.1-2.el7

   * - salt-api
     -  * /bin/bash
        * /bin/sh
        * config(salt-master) = 3005.1-2.el7
        * rpmlib
        * salt = 3005.1-2.el7

   * - salt-cloud
     -  * /bin/bash
        * config(salt-cloud) = 3005.1-2.el7
        * rpmlib
        * salt-master = 3005.1-2.el7

   * - salt-ssh
     -  * /bin/bash
        * config(salt-ssh) = 3005.1-2.el7
        * rpmlib
        * salt = 3005.1-2.el7

   * - salt-syndic
     -  * /bin/bash
        * /bin/sh
        * rpmlib
        * salt-master = 3005.1-2.el7


RedHat 8
--------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /bin/bash
        * /bin/sh
        * /usr/bin/sh
        * config(salt) = 3005.1-2.el8
        * dmidecode
        * libc.so.6
        * libdl.so.2
        * libpthread.so.0
        * libz.so.1
        * openssl
        * pciutils
        * rpmlib
        * rtld
        * systemd-units
        * which

   * - salt-minion
     -  * /bin/bash
        * /bin/sh
        * config(salt-minion) = 3005.1-2.el8
        * rpmlib
        * salt = 3005.1-2.el8

   * - salt-master
     -  * /bin/bash
        * /bin/sh
        * config(salt-master) = 3005.1-2.el8
        * rpmlib
        * salt = 3005.1-2.el8

   * - salt-api
     -  * /bin/bash
        * /bin/sh
        * rpmlib
        * salt-master = 3005.1-2.el8

   * - salt-cloud
     -  * /bin/bash
        * config(salt-cloud) = 3005.1-2.el8
        * rpmlib
        * salt-master = 3005.1-2.el8

   * - salt-ssh
     -  * /bin/bash
        * config(salt-ssh) = 3005.1-2.el8
        * rpmlib
        * salt = 3005.1-2.el8

   * - salt-syndic
     -  * /bin/bash
        * /bin/sh
        * rpmlib
        * salt-master = 3005.1-2.el8


RedHat 9
--------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /usr/bin/bash
        * /usr/bin/sh
        * config(salt) = 3005.1-2.el9
        * dmidecode
        * libc.so.6
        * libdl.so.2
        * libpthread.so.0
        * libz.so.1
        * openssl
        * pciutils
        * rpmlib
        * rtld
        * systemd-units
        * which

   * - salt-minion
     -  * /bin/sh
        * /usr/bin/bash
        * config(salt-minion) = 3005.1-2.el9
        * rpmlib
        * salt = 3005.1-2.el9

   * - salt-master
     -  * /bin/sh
        * /usr/bin/bash
        * config(salt-master) = 3005.1-2.el9
        * rpmlib
        * salt = 3005.1-2.el9

   * - salt-api
     -  * /bin/sh
        * /usr/bin/bash
        * rpmlib
        * salt-master = 3005.1-2.el9

   * - salt-cloud
     -  * /usr/bin/bash
        * config(salt-cloud) = 3005.1-2.el9
        * rpmlib
        * salt-master = 3005.1-2.el9

   * - salt-ssh
     -  * /usr/bin/bash
        * config(salt-ssh) = 3005.1-2.el9
        * rpmlib
        * salt = 3005.1-2.el9

   * - salt-syndic
     -  * /bin/sh
        * /usr/bin/bash
        * rpmlib
        * salt-master = 3005.1-2.el9


Ubuntu 18.04
------------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Recommends:

       * lsb-release

       Suggests:

       * ifupdown

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)

       Recommends:

       * debconf-utils
       * dmidecode
       * net-tools

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-api
     - Depends:

       * salt-master

   * - salt-cloud
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * openssh-client

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)


Ubuntu 20.04
------------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Recommends:

       * lsb-release

       Suggests:

       * ifupdown

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)

       Recommends:

       * debconf-utils
       * dmidecode
       * net-tools

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-api
     - Depends:

       * salt-master

   * - salt-cloud
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * openssh-client

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)


Ubuntu 22.04
------------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Recommends:

       * lsb-release

       Suggests:

       * ifupdown

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)

       Recommends:

       * debconf-utils
       * dmidecode
       * net-tools

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-api
     - Depends:

       * salt-master

   * - salt-cloud
     - Depends:

       * salt-common (= 3005.1+ds-2)

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * openssh-client

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)

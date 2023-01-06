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
classic and onedir packages, using Salt 3005.1 as an example.


Amazon Linux 2
==============

Onedir
------

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


Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /bin/sh
        * /usr/bin/env
        * /usr/bin/python3
        * config(salt) = 3005.1-1.amzn2
        * pciutils
        * python(abi) = 3.7
        * python3-contextvars
        * python3-distro
        * python3-jinja2
        * python3-jmespath
        * python3-markupsafe
        * python3-msgpack >= 0.4
        * python3-psutil
        * python3-pycurl
        * python3-pyyaml
        * python3-requests
        * python3-rpm
        * python3-six
        * python3-zmq >= 18.0.1
        * python37-pycryptodomex
        * rpmlib
        * systemd-python
        * systemd-units
        * which
        * yum-utils

   * - salt-minion
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-minion) = 3005.1-1.amzn2
        * rpmlib
        * salt = 3005.1-1.amzn2

   * - salt-master
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-master) = 3005.1-1.amzn2
        * rpmlib
        * salt = 3005.1-1.amzn2
        * systemd-python

   * - salt-api
     -  * /bin/sh
        * /usr/bin/python3
        * python3-cherrypy
        * rpmlib
        * salt-master = 3005.1-1.amzn2

   * - salt-cloud
     -  * /usr/bin/python3
        * config(salt-cloud) = 3005.1-1.amzn2
        * python3-libcloud
        * rpmlib
        * salt-master = 3005.1-1.amzn2

   * - salt-ssh
     -  * /usr/bin/python3
        * config(salt-ssh) = 3005.1-1.amzn2
        * rpmlib
        * salt = 3005.1-1.amzn2

   * - salt-syndic
     -  * /bin/sh
        * /usr/bin/python3
        * rpmlib
        * salt-master = 3005.1-1.amzn2


Debian 10
=========

Onedir
------

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


Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Depends:

       * python3-apt
       * python3-dateutil
       * python3-jinja2
       * python3-msgpack (>= 0.4)
       * python3-pkg-resources
       * python3-requests
       * python3-yaml
       * python3-systemd
       * python3-psutil
       * python3-distro
       * python3-pycryptodome
       * python3-zmq (>= 17.0.0)
       * python3-jmespath
       * python3-markupsafe
       * python3:any

       Recommends:

       * lsb-release
       * python3-contextvars
       * python3-croniter

       Suggests:

       * python3-pycurl
       * python3-twisted

       Breaks:

       * python3-mako (<< 0.7.0)

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-1)
       * python3:any

       Recommends:

       * debconf-utils
       * dmidecode

       Suggests:

       * python3-augeas

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-1)
       * python3:any

       Recommends:

       * python3-git

   * - salt-api
     - Depends:

       * salt-master
       * python3:any

       Recommends:

       * python3-cherrypy3

   * - salt-cloud
     - Depends:

       * python3-libcloud
       * salt-common (= 3005.1+ds-1)
       * python3:any

       Recommends:

       * python3-netaddr

       Suggests:

       * python3-botocore

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-1)
       * python3:any

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-1)
       * python3:any


Debian 11
=========

Onedir
------

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


Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     - Depends:

       * python3-apt
       * python3-dateutil
       * python3-jinja2
       * python3-msgpack (>= 0.4)
       * python3-pkg-resources
       * python3-requests
       * python3-yaml
       * python3-systemd
       * python3-psutil
       * python3-distro
       * python3-pycryptodome
       * python3-zmq (>= 17.0.0)
       * python3-jmespath
       * python3-markupsafe
       * python3:any

       Recommends:

       * lsb-release
       * python3-contextvars
       * python3-croniter

       Suggests:

       * python3-pycurl
       * python3-twisted

       Breaks:

       * python3-mako (<< 0.7.0)

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-1)
       * python3:any

       Recommends:

       * debconf-utils
       * dmidecode

       Suggests:

       * python3-augeas

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-1)
       * python3:any

       Recommends:

       * python3-git

   * - salt-api
     - Depends:

       * salt-master
       * python3:any

       Recommends:

       * python3-cherrypy3

   * - salt-cloud
     - Depends:

       * python3-libcloud
       * salt-common (= 3005.1+ds-1)
       * python3:any

       Recommends:

       * python3-netaddr

       Suggests:

       * python3-botocore

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-1)
       * python3:any

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-1)
       * python3:any


RedHat 7
========

Onedir
------

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


Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /bin/sh
        * /usr/bin/env
        * /usr/bin/python3
        * config(salt) = 3005.1-1.el7
        * pciutils
        * python(abi) = 3.6
        * python36-PyYAML
        * python36-contextvars
        * python36-distro
        * python36-jinja2
        * python36-jmespath
        * python36-m2crypto >= 0.31.0
        * python36-markupsafe
        * python36-msgpack >= 0.6
        * python36-psutil
        * python36-pycurl
        * python36-requests
        * python36-rpm
        * python36-six
        * python36-zmq >= 18.0.1
        * rpmlib
        * systemd-units
        * which
        * yum-utils

   * - salt-minion
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-minion) = 3005.1-1.el7
        * rpmlib
        * salt = 3005.1-1.el7

   * - salt-master
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-master) = 3005.1-1.el7
        * rpmlib
        * salt = 3005.1-1.el7
        * systemd-python

   * - salt-api
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-master) = 3005.1-1.el7
        * rpmlib
        * salt = 3005.1-1.el7
        * systemd-python

   * - salt-cloud
     -  * /usr/bin/python3
        * config(salt-cloud) = 3005.1-1.el7
        * python36-libcloud
        * rpmlib
        * salt-master = 3005.1-1.el7

   * - salt-ssh
     -  * /usr/bin/python3
        * config(salt-ssh) = 3005.1-1.el7
        * rpmlib
        * salt = 3005.1-1.el7

   * - salt-syndic
     -  * /bin/sh
        * /usr/bin/python3
        * rpmlib
        * salt-master = 3005.1-1.el7


RedHat 8
========

Onedir
------

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

Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     -  * /bin/sh
        * /usr/bin/python3
        * /usr/bin/sh
        * config(salt) = 3005.1-1.el8
        * pciutils
        * python(abi) = 3.6
        * python3-contextvars
        * python3-distro
        * python3-jinja2
        * python3-m2crypto >= 0.31.0
        * python3-markupsafe
        * python3-msgpack >= 0.4
        * python3-psutil
        * python3-pycurl
        * python3-pyyaml
        * python3-requests
        * python3-rpm
        * python3-six
        * python3-zmq >= 20.0.0
        * python3.6dist(contextvars)
        * python3.6dist(distro) >= 1.0.1
        * python3.6dist(jinja2)
        * python3.6dist(jmespath)
        * python3.6dist(m2crypto) >= 0.33.0
        * python3.6dist(markupsafe)
        * python3.6dist(msgpack) >= 0.5
        * python3.6dist(psutil) >= 5.0.0
        * python3.6dist(pyyaml)
        * python3.6dist(pyzmq) >= 17.0.0
        * python3.6dist(pyzmq) > 19.0.2
        * python3.6dist(pyzmq) <= 20.0.0
        * python3.6dist(requests) >= 1.0.0
        * rpmlib
        * systemd-units
        * which
        * yum-utils

   * - salt-minion
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-minion) = 3005.1-1.el8
        * rpmlib
        * salt = 3005.1-1.el8

   * - salt-master
     -  * /bin/sh
        * /usr/bin/python3
        * config(salt-master) = 3005.1-1.el8
        * python3-systemd
        * rpmlib
        * salt = 3005.1-1.el8

   * - salt-api
     -  * /bin/sh
        * /usr/bin/python3
        * python3-cherrypy >= 3.2.2
        * rpmlib
        * salt-master = 3005.1-1.el8

   * - salt-cloud
     -  * /usr/bin/python3
        * config(salt-cloud) = 3005.1-1.el8
        * python3-libcloud
        * rpmlib
        * salt-master = 3005.1-1.el8

   * - salt-ssh
     -  * /usr/bin/python3
        * config(salt-ssh) = 3005.1-1.el8
        * rpmlib
        * salt = 3005.1-1.el8

   * - salt-syndic
     -  * /bin/sh
        * /usr/bin/python3
        * rpmlib
        * salt-master = 3005.1-1.el8


RedHat 9
========

Onedir
------

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

Classic
-------
Classic packages are not supported for RedHat 9.


Ubuntu 18.04
============

Onedir
------

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


Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left list-with-no-space

   * - Service
     - Packages

   * - salt
     - Depends:

       * python3-apt
       * python3-contextvars
       * python3-dateutil
       * python3-jinja2
       * python3-msgpack (>= 0.4) python3-pkg-resources
       * python3-requests
       * python3-yaml
       * python3-systemd
       * python3-psutil
       * python3-pycryptodome
       * python3-gnupg
       * python3-zmq (>= 17.0.0)
       * python3-distro
       * python3-jmespath
       * python3-markupsafe
       * python3:any (>= 3.3.2-2~)

       Recommends:

       * lsb-release
       * python3-croniter

       Suggests:

       * ifupdown
       * python3-pycurl
       * python3-twisted

       Breaks:

       * python3-mako (<< 0.7.0)

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)
       * python3:any

       Recommends:

       * debconf-utils
       * dmidecode

       Suggests:

       * python3-augeas

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * python3:any

       Recommends:

       * python3-git

   * - salt-api
     - Depends:

       * salt-master
       * python3:any

       Recommends:

       * python3-cherrypy3

   * - salt-cloud
     - Depends:

       * python3-libcloud
       * salt-common (= 3005.1+ds-2)
       * python3:any

       Recommends:

       * python3-netaddr

       Suggests:

       * python3-botocore

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * python3:any


   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)
       * python3:any


Ubuntu 20.04
============

Onedir
------

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

Classic
-------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1
   :class: table-left

   * - Service
     - Packages

   * - salt
     - Depends:

       * python3-apt
       * python3-dateutil
       * python3-jinja2
       * python3-msgpack (>= 0.4)
       * python3-pkg-resources
       * python3-requests
       * python3-yaml
       * python3-systemd
       * python3-psutil
       * python3-pycryptodome
       * python3-gnupg
       * python3-zmq (>= 20.0.0)
       * python3-distro
       * python3-jmespath
       * python3-markupsafe
       * python3:any

       Recommends:

       * lsb-release
       * python3-contextvars
       * python3-croniter

       Suggests:

       * ifupdown
       * python3-pycurl
       * python3-twisted

       Breaks:

       * python3-mako (<< 0.7.0)

   * - salt-minion
     - Depends:

       * bsdmainutils
       * dctrl-tools
       * salt-common (= 3005.1+ds-2)
       * python3:any

       Recommends:

       * debconf-utils
       * dmidecode
       * net-tools

       Suggests:

       * python3-augeas

   * - salt-master
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * python3:any

       Recommends:

       * python3-git

   * - salt-api
     - Depends:

       * salt-master
       * python3:any

       Recommends:

       * python3-cherrypy3

   * - salt-cloud
     - Depends:

       * python3-libcloud
       * salt-common (= 3005.1+ds-2)
       * python3:any

       Recommends:

       * python3-netaddr

       Suggests:

       * python3-botocore

   * - salt-ssh
     - Depends:

       * salt-common (= 3005.1+ds-2)
       * python3:any

   * - salt-syndic
     - Depends:

       * salt-master (= 3005.1+ds-2)
       * python3:any


Ubuntu 22.04
============

Onedir
------

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


Classic
-------
Classic packages are not supported for Ubuntu 22.04.

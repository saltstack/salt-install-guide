.. _salt-supported-operating-systems:

================================
Salt supported operating systems
================================

Together with the :ref:`salt-version-support-lifecycle` guidelines, this
document is intended to clearly define how long a particular version of Salt
will receive official packages, testing, and technical support from the Salt
Project.

.. include:: _includes/supported-os-concepts.rst


Overview of supported operating systems
=======================================

.. list-table::
  :widths: 30 20 10 10 20 10
  :align: center
  :header-rows: 1
  :stub-columns: 1
  :class: slim

  * -
    - `Arch`_
    - `Master`_
    - `Minion`_
    - `Full`_ or `Reasonable-effort`_
    - `Tested`_

  * - `AlmaLinux`_ 8
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `AlmaLinux`_ 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Amazon Linux`_ 2
    - x86_64, aarch64 / arm64
    -
    - Yes
    - Full
    - Yes

  * - `Amazon Linux`_ 2023
    - x86_64, aarch64 / arm64
    -
    - Yes
    - Full
    - Yes

  * - `Arch Linux`_ (latest)
    - x86_64, aarch64
    - Yes
    - Yes
    - Reasonable
    - Yes

  * - `CentOS`_ 7
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `CentOS`_ Stream 8
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

  * - `CentOS`_ Stream 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

  * - `Debian`_ 10
    - amd64, arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Debian`_ 11
    - amd64, arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Debian`_ 12
    - amd64, arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Fedora`_ 37
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Fedora`_ 38
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `FreeBSD`_ 12.4
    -
    - Yes
    - Yes
    - Reasonable
    -

  * - `FreeBSD`_ 13.1
    -
    - Yes
    - Yes
    - Reasonable
    -

  * - `macOS`_ 11
    - x86_64
    -
    - Yes
    - Full
    -

  * - `macOS`_ 12
    - x86_64
    -
    - Yes
    - Full
    -

  * - `openSUSE`_ Leap 15.4
    -
    - Yes
    - Yes
    - Reasonable
    -

  * - `Oracle Linux`_ 7, 8, 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - [#f1]_

  * - `Photon OS`_ 3
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

  * - `Photon OS`_ 4
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -


  * - `RedHat`_ 7
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `RedHat`_ 8
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `RedHat`_ 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `SLES`_ 12 SP5
    -
    - Yes
    - Yes
    - Full
    -

  * - `SLES`_ 15 SP4
    -
    - Yes
    - Yes
    - Full
    -

  * - `Ubuntu`_ 20.04
    - amd64, arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Ubuntu`_ 22.04
    - amd64, arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Windows`_ Desktop 10
    - x86, AMD64
    -
    - Yes
    - Full
    -

  * - `Windows`_ Desktop 11
    - x86, AMD64
    -
    - Yes
    - Full
    -

  * - `Windows`_ 2016
    - x86, AMD64
    -
    - Yes
    - Full
    - Yes

  * - `Windows`_ 2019
    - x86, AMD64
    -
    - Yes
    - Full
    - Yes

  * - `Windows`_ 2022
    - x86, AMD64
    -
    - Yes
    - Full
    - Yes


.. [#f1] Use RedHat or CentOS packages instead.


Support definitions
===================

Arch
----
Arch is short for *architecture.* The Salt Project supports the following
architectures:

.. list-table::
  :widths: 30 30 40
  :header-rows: 1
  :stub-columns: 1

  * - Operating system family
    - Architecture support
    - Example systems

  * - Amazon Linux
    -  * x86_64
       * aarch64 / arm64
    - Amazon Linux

  * - Debian
    -  * amd64
       * arm64
    - Debian, Ubuntu

  * - MacOS
    -  * x86_64
    - MacOS

  * - RedHat
    -  * x86_64
       * aarch64 / amd64
    - RedHat, CentOS, Fedora

  * - Windows
    -  * x86
       * amd64
    - Windows desktop, Windows server


Master
------
Master support is defined as:

* The `salt-master` service can run on this operating system.
* A node running this operating system can act as the Salt master, which means
  it can send commands and communicate with connected Salt minions.


Minion
------
Minion supported is defined as:

* The `salt-minion` service can run on this operating system.
* A node running this operating system can act a Salt minion, which means this
  system or device can be managed by a Salt master.


Full
----
Full support is defined as:

* Packages and all required dependencies created by Salt Project or official
  upstream packager.
* Packages hosted by the Salt Project.
* Tested by the Salt Project.
* The Salt Project provides full technical support for VMware customers.
* The Salt Project will fix bugs for VMware customers.


Reasonable-effort
-----------------
Reasonable-effort support is defined as:

* Packages created and hosted by the Salt Project community.
* Some testing done by the Salt Project.
* The Salt Project provides best-effort technical support for VMware customers.
* The Salt Project may fix bugs for VMware customers.


Tested
------
The full automated test suite is run for the operating system packages.


Full support policy by operating system
=======================================
This section outlines the general support and package creation policy for each
operating system that is listed as having full support by the Salt Project.
These guidelines are intended to help you understand how long a particular
operating system will receive official packages, testing, and technical support.


AlmaLinux
---------
Actively supported versions of AlmaLinux.


Amazon Linux
------------
Amazon Linux 2 and 2023 are supported.


CentOS
------
CentOS versions through Production Phase 3 Support. Versions in ELS are not
supported by the Salt Project.


Debian
------
Debian stable, oldstable, and oldoldstable versions.

https://wiki.debian.org/DebianReleases


Fedora
------
Fedora version support mirrors that of the upstream maintainer.


RedHat
------
RedHat versions through Production Phase 3 Support. Versions in ELS are not
supported by the Salt Project.

https://access.redhat.com/support/policy/updates/errata


macOS
-----
The latest three versions of macOS.


Oracle Linux
------------
Oracle Linux versions 7, 8, and 9.

https://www.oracle.com/technetwork/server-storage/linux/overview/index.html


Photon OS
---------
Photon OS 3.0 as of the 3005 (Phosphorus) release.


SLES
----
SLES versions through General Support. Versions in LTSS are not supported.

https://www.suse.com/lifecycle/



Ubuntu
------
Ubuntu LTS versions through end-of-life. Ubuntu optional Extended Security
Maintenance (ESM) is not supported.

http://www.ubuntu.com/info/release-end-of-life


Windows
-------
Windows versions through Extended Support.

http://windows.microsoft.com/en-us/windows/lifecycle




Reasonable-effort support policy by operating system
====================================================
This section outlines the general support policy for each operating system that
is listed as having reasonable-effort support by the Salt Project. These
guidelines are intended to help you understand how long a particular operating
system might receive reasonable-effort support.

Since the Salt Project does not create or maintain the packages for these
operating systems, no guarantee is made as to availability of packages. These
guidelines are for reasonable-effort support only.


Arch Linux
----------
Latest version of Arch Linux.


FreeBSD
-------
FreeBSD versions through end-of-life.

https://www.freebsd.org/security/


openSUSE
--------
openSUSE version support mirrors that of the upstream maintainer.

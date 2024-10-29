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
    -

  * - `AlmaLinux`_ 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

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

  * - `CentOS`_ Stream 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

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

  * - `Fedora`_ 40
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `macOS`_ 12
    - x86_64
    -
    - Yes
    - Full
    -

  * - `macOS`_ 13
    - x86_64, arm64
    -
    - Yes
    - Full
    -

  * - `openSUSE`_ Leap 15.5
    -
    - Yes
    - Yes
    - Reasonable
    - Yes

  * - `Oracle Linux`_ 8, 9
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - [#f1]_

  * - `Photon OS`_ 4
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

  * - `Photon OS`_ 5
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    -

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

  * - `Rocky Linux`_ 8
    - x86_64, aarch64 / arm64
    - Yes
    - Yes
    - Full
    - Yes

  * - `Rocky Linux`_ 9
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

  * - `SLES`_ 15 SP5
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

  * - `Ubuntu`_ 24.04
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
       * arm64
    - MacOS

  * - RedHat
    -  * x86_64
       * aarch64 / amd64
    - RedHat, CentOS, Rocky Linux, Fedora

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
Only CentOS Stream 9 is supported.


Debian
------
Debian stable, oldstable, and oldoldstable (if it is not EOL) versions.

https://wiki.debian.org/DebianReleases


Fedora
------
Support is for the latest version of Fedora.


RedHat
------
RedHat versions through Production Phase 3 Support. Versions in ELS are not
supported by the Salt Project.

https://access.redhat.com/support/policy/updates/errata


Rocky Linux
-----------
Actively supported versions of Rocky Linux.


macOS
-----
The latest three versions of macOS, including arm64 (M Series).


Oracle Linux
------------
Oracle Linux versions 8 and 9.

https://www.oracle.com/technetwork/server-storage/linux/overview/index.html


Photon OS
---------
Photon OS 4.0 and 5.0.


SLES
----
SLES versions through General Support. Versions in LTSS are not supported.

https://www.suse.com/lifecycle/


Ubuntu
------
Ubuntu LTS versions through end-of-life. Ubuntu optional Extended Security
Maintenance (ESM) is not supported.

https://ubuntu.com/about/release-cycle


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


openSUSE
--------
openSUSE version support mirrors that of the upstream maintainer.

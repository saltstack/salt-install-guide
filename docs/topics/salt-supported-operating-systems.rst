.. _salt-supported-operating-systems:

===========================
Supported operating systems
===========================

Together with the :ref:`salt-version-support-lifecycle` guidelines, this
document is intended to clearly define how long a particular version of Salt
will receive official packages, testing, and technical support from the Salt
Project.

.. include:: _includes/supported-os-concepts.rst


Overview of supported operating systems
=======================================

.. list-table::
  :widths: 30 10 10 10 15 25
  :align: center
  :header-rows: 1
  :stub-columns: 1
  :class: slim

  * -
    - `Master supported`_
    - `Minion supported`_
    - `Full support`_
    - `Reasonable-effort support`_
    - Testing support

  * - `Amazon Linux`_ 2
    -
    - Yes
    - Yes
    -
    - Package only

  * - `Arch`_ (latest)
    - Yes
    - Yes
    -
    - Yes
    - Automated only

  * - `CentOS`_ 7
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `CentOS`_ 8 Streaming
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `CentOS`_ 9 Streaming
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `Debian`_ 10
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `Debian`_ 11
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `Fedora`_ 35
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `Fedora`_ 36
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `Fedora`_ 37
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `FreeBSD`_ 11
    - Yes
    - Yes
    -
    - Yes
    - Package only

  * - `FreeBSD`_ 12.2
    - Yes
    - Yes
    -
    - Yes
    - Package only

  * - `FreeBSD`_ 13
    - Yes
    - Yes
    -
    - Yes
    - Package only

  * - `macOS`_ 10.15
    -
    - Yes
    - Yes
    -
    -

  * - `macOS`_ 11
    -
    - Yes
    - Yes
    -
    -

  * - `macOS`_ 12
    -
    - Yes
    - Yes
    -
    -

  * - `openSUSE`_ Leap 42.3
    - Yes
    - Yes
    -
    - Yes
    - Automated only

  * - `openSUSE`_ 15
    - Yes
    - Yes
    -
    - Yes
    -

  * - `Oracle Linux`_ 7, 8
    - Yes
    - Yes
    - Yes
    -
    - NONE [#f1]_

  * - `Photon OS`_ 3
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `RedHat`_ 7
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `RedHat`_ 8
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `RedHat`_ 9
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `SLES`_ 12
    - Yes
    - Yes
    - Yes
    -
    -

  * - `SLES`_ 12 SP4
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `SLES`_ 15
    - Yes
    - Yes
    - Yes
    -
    - Package only

  * - `SmartOS`_ (latest)
    - Yes
    - Yes
    -
    - Yes
    - Package only

  * - `Ubuntu`_ 18.04
    - Yes
    - Yes
    - Yes
    -
    -

  * - `Ubuntu`_ 20.04
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `Ubuntu`_ 22.04
    - Yes
    - Yes
    - Yes
    -
    - Automated, manual

  * - `Windows`_ Desktop 8.1
    -
    - Yes
    - Yes
    -
    - Package only

  * - `Windows`_ Desktop 10
    -
    - Yes
    - Yes
    -
    - Package only

  * - `Windows`_ Desktop 11
    -
    - Yes
    - Yes
    -
    - Package only

  * - `Windows`_ 2012
    -
    - Yes
    - Yes
    -
    -

  * - `Windows`_ 2012 R2
    -
    - Yes
    - Yes
    -
    -

  * - `Windows`_ 2016
    -
    - Yes
    - Yes
    -
    - Package only

  * - `Windows`_ 2019
    -
    - Yes
    - Yes
    -
    -

  * - `Windows`_ 2022
    -
    - Yes
    - Yes
    -
    -


.. [#f1] Use RedHat or CentOS packages instead.


Master supported
----------------
Master supported is defined as:

* The `salt-master` service can run on this operating system.
* A node running this operating system can act as the Salt master, which means
  it can send commands and communicate with connected Salt minions.


Minion supported
----------------
Minion supported is defined as:

* The `salt-minion` service can run on this operating system.
* A node running this operating system can act a Salt minion, which means this
  system or device can be managed by a Salt master.


Full support
------------
Full support is defined as:

* Packages and all required dependencies created by Salt Project or official upstream packager.
* Packages hosted by the Salt Project.
* Tested by the Salt Project.
* The Salt Project provides full technical support for VMware customers.
* The Salt Project will fix bugs for VMware customers.


Reasonable-effort support
-------------------------
Reasonable-effort support is defined as:

* Packages created and hosted by the Salt Project community.
* Some testing done by the Salt Project.
* The Salt Project provides best-effort technical support for VMware customers.
* The Salt Project may fix bugs for VMware customers.


Full support policy by operating system
=======================================
This section outlines the general support and package creation policy for each
operating system that is listed as having full support by the Salt Project.
These guidelines are intended to help you understand how long a particular
operating system will receive official packages, testing, and technical support.


Amazon Linux
------------
Amazon Linux 2 is supported.


Arch
----
Latest version of Arch.



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
Oracle Linux versions 7 and 8 as of July 2016.

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



FreeBSD
-------
FreeBSD versions through end-of-life.

https://www.freebsd.org/security/


openSUSE
--------
openSUSE version support mirrors that of the upstream maintainer.


SmartOS
-------
Latest version of SmartOS.

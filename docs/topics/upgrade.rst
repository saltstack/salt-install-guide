.. _upgrade:

============
Upgrade Salt
============

The process for upgrading Salt depends on your operating system and your
organization's policies and procedures for updating.


Upgrade Linux systems
=====================
When you install Salt on your Linux systems, it creates a file that tells the
system where it should download the latest packages for Salt. The exact location
of the file varies by operating system.

When you install Salt, you need to select the repository that you want to pin
for updates. The following sections explain the different options for
repositories you can pin for updates:


.. _tiamat:

Tiamat
------
Tiamat is the Salt Project's new packaging system. Beginning with the release of
Salt 3005 (Phosphorus), the Salt Project will begin replacing the old packaging
system with the Tiamat packaging system.

The Tiamat packages simplify the installation process because they allow you to
use Salt out of the box without installing Python or other dependencies first.


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

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

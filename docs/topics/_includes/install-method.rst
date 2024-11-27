The Salt Project provides public repositories for packages on the
public Broadcom Artifactory endpoint:

* `Salt Project RPM Repo <https://packages.broadcom.com/artifactory/saltproject-rpm>`__
* `Salt Project DEB Repo <https://packages.broadcom.com/artifactory/saltproject-deb>`__
* `Salt Project Generic Repo (Windows, MacOS, etc.) <https://packages.broadcom.com/artifactory/saltproject-generic>`__

The preferred method for installing Salt is using distribution packages. This
method ensures that:

* All dependencies are met.
* Salt is installed in a tested and distribution-aligned way.

.. Note::
    Salt is often distributed in split packages, but only the ``salt-master``
    and ``salt-minion`` packages are required for Salt to function. If only
    desiring to run Salt in a masterless setup, then only ``salt-minion`` is
    required.

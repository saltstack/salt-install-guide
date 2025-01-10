.. _install-rpm:

===========
Linux (RPM)
===========

These instructions explain how to install Salt rpms on operating systems that
are RHEL-like (using ``dnf`` install methods).

.. Note::
    Salt packages for SUSE and Photon OS are provided via their own OS package repositories.
    SUSE and Photon OS create their own Salt packages that aren't ``onedir`` (``relenv``) based, and are
    patched to be further integrated with their respective operating systems.

    Salt Project **does not** provide custom directions for working with ``zypper``, ``tdnf``, or other
    non-DNF package managers to install packages from the Salt Project RPM repository.

    RPM packages, hosted by Salt Project, are still tested on SUSE and Photon OS operating systems via our CI/CD.

For a list of supported and tested operating systems, for running Salt,
see :ref:`salt-supported-operating-systems`.

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt RPMs
=================

#. Run the following command to install the Salt Project repository:

   .. code-block:: bash

       curl -fsSL https://github.com/saltstack/salt-install-guide/releases/latest/download/salt.repo | sudo tee /etc/yum.repos.d/salt.repo

   .. Note::
       Because of the presence of classic packages of Salt in EPEL, it's
       possible that when you download the package from EPEL, it instead
       downloads classic packages of older versions of Salt instead of the
       onedir packages.

       During depsolving, when choosing the best provider among several, ``dnf``
       respects the priority of each provider's repository. The value is an
       integer from 1 to 99, with 1 being the most preferred repository and 99
       the least preferred. By default all repositories have the priority of 80.

       EPEL was treating the Salt repository as 99. To resolve this issue, Salt
       has changed its priority level to 10 for RHEL 8 and 9.

#. Run ``sudo dnf clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. warning:: STS not recommended for Production

      Salt Project recommends deploying LTS releases for Production environments.

   .. tab-set::

       .. tab-item:: |major-one-version-text|

            Available installs:

            .. code-block:: bash

                    sudo dnf install salt-master
                    sudo dnf install salt-minion
                    sudo dnf install salt-ssh
                    sudo dnf install salt-syndic
                    sudo dnf install salt-cloud
                    sudo dnf install salt-api

            If wanting to install by a target point release, append the specific Salt
            full release version. For example:

            .. parsed-literal::

                    sudo dnf install salt-master-|minor-one-version|
                    sudo dnf install salt-minion-|minor-one-version|
                    sudo dnf install salt-ssh-|minor-one-version|
                    sudo dnf install salt-syndic-|minor-one-version|
                    sudo dnf install salt-cloud-|minor-one-version|
                    sudo dnf install salt-api-|minor-one-version|

            ``dnf versionlock`` can be used to pin to minor versions, if wanting to be
            excluded during ``dnf upgrade`` runs on a system.

            .. code-block:: bash

                    sudo dnf install 'dnf-command(versionlock)'

            .. code-block:: bash

                    sudo dnf versionlock add salt
                    sudo dnf versionlock add salt-master
                    sudo dnf versionlock add salt-minion
                    sudo dnf versionlock add salt-ssh
                    sudo dnf versionlock add salt-syndic
                    sudo dnf versionlock add salt-cloud
                    sudo dnf versionlock add salt-api

       .. tab-item:: |major-two-version-text|

            If users would like to restrict their installs to the Salt |major-two-version-text| point releases,
            these install steps include enabling Salt |major-two-version-text| release downloads.

            .. parsed-literal::

                    # Enable the Salt |major-two-version-text| repo
                    sudo dnf config-manager --set-disable salt-repo-*
                    sudo dnf config-manager --set-enabled salt-repo-|major-two-version-repo-postfix|

            Available installs:

            .. code-block:: bash

                    sudo dnf install salt-master
                    sudo dnf install salt-minion
                    sudo dnf install salt-ssh
                    sudo dnf install salt-syndic
                    sudo dnf install salt-cloud
                    sudo dnf install salt-api

            If wanting to install by a target point release, append the specific Salt
            full release version. For example:

            .. parsed-literal::

                    sudo dnf install salt-master-|minor-two-version|
                    sudo dnf install salt-minion-|minor-two-version|
                    sudo dnf install salt-ssh-|minor-two-version|
                    sudo dnf install salt-syndic-|minor-two-version|
                    sudo dnf install salt-cloud-|minor-two-version|
                    sudo dnf install salt-api-|minor-two-version|

            ``dnf versionlock`` can be used to pin to minor versions, if wanting to be
            excluded during ``dnf upgrade`` runs on a system.

            .. code-block:: bash

                    sudo dnf install 'dnf-command(versionlock)'

            .. code-block:: bash

                    sudo dnf versionlock add salt
                    sudo dnf versionlock add salt-master
                    sudo dnf versionlock add salt-minion
                    sudo dnf versionlock add salt-ssh
                    sudo dnf versionlock add salt-syndic
                    sudo dnf versionlock add salt-cloud
                    sudo dnf versionlock add salt-api

       .. tab-item:: LATEST Available

            If users would like to leave installs to come from either LTS or STS, whichever
            major version is latest.

            .. code-block:: bash

                    # Enable the Salt LATEST repo
                    sudo dnf config-manager --set-disable salt-repo-*
                    sudo dnf config-manager --set-enabled salt-repo-latest

            Available installs:

            .. code-block:: bash

                    sudo dnf install salt-master
                    sudo dnf install salt-minion
                    sudo dnf install salt-ssh
                    sudo dnf install salt-syndic
                    sudo dnf install salt-cloud
                    sudo dnf install salt-api

            If wanting to install by a target point release, append the specific Salt
            full release version. For example:

            .. parsed-literal::

                    sudo dnf install salt-master-|minor-latest-version|
                    sudo dnf install salt-minion-|minor-latest-version|
                    sudo dnf install salt-ssh-|minor-latest-version|
                    sudo dnf install salt-syndic-|minor-latest-version|
                    sudo dnf install salt-cloud-|minor-latest-version|
                    sudo dnf install salt-api-|minor-latest-version|

            ``dnf versionlock`` can be used to pin to minor versions, if wanting to be
            excluded during ``dnf upgrade`` runs on a system.

            .. code-block:: bash

                    sudo dnf install 'dnf-command(versionlock)'

            .. code-block:: bash

                    sudo dnf versionlock add salt
                    sudo dnf versionlock add salt-master
                    sudo dnf versionlock add salt-minion
                    sudo dnf versionlock add salt-ssh
                    sudo dnf versionlock add salt-syndic
                    sudo dnf versionlock add salt-cloud
                    sudo dnf versionlock add salt-api

#. Enable and start the Salt services:

   Available services:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst

Browse the repo
===============

.. card:: Browse the repo for RPM packages
    :class-card: sd-border-1
    :link: https://packages.broadcom.com/artifactory/saltproject-rpm/
    :width: 50%

    :bdg-primary:`rpm`

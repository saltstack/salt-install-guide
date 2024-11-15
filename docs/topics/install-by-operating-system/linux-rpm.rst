.. _install-rpm:

===========
Linux (RPM)
===========

These instructions explain how to install Salt rpms on operating systems that
are RHEL-like (using ``dnf`` install methods).

For a list of supported and tested operating systems, for running Salt,
see :ref:`salt-supported-operating-systems`.

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt RPMs
=================

#. Run the following command to install the Salt Project repository:

   .. tab-set::

       .. tab-item:: DNF

           .. code-block:: bash

               curl -fsSL https://github.com/saltstack/salt-install-guide/releases/latest/download/salt.repo | sudo tee /etc/yum.repos.d/salt.repo


       .. tab-item:: Zypper

           .. code-block:: bash

               curl -fsSL https://github.com/saltstack/salt-install-guide/releases/latest/download/salt-zypper.repo | sudo tee /etc/zypp/repos.d/salt.repo


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

#. Run the following command to  clear the repository metadata.

   .. tab-set::

       .. tab-item:: DNF

           .. code-block:: bash

               sudo dnf clean expire-cache


       .. tab-item:: Zypper

           .. code-block:: bash

               sudo zypper clean



#. Install the salt-minion, salt-master, or other Salt components:

   .. tab-set::

       .. tab-item:: DNF

           .. tab-set::

               .. tab-item:: 3006 LTS

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

                    .. code-block:: bash

                            sudo dnf install salt-master-3006.9
                            sudo dnf install salt-minion-3006.9
                            sudo dnf install salt-ssh-3006.9
                            sudo dnf install salt-syndic-3006.9
                            sudo dnf install salt-cloud-3006.9
                            sudo dnf install salt-api-3006.9

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

               .. tab-item:: 3007 STS

                    .. warning:: STS not recommended for Production

                        Salt Project recommends deploying LTS releases for Production environments.

                    If users would like to restrict their installs to the Salt 3007 STS point releases,
                    these install steps include enabling Salt 3007 STS release downloads.

                    .. code-block:: bash

                            # Enable the Salt 3007 STS repo
                            sudo dnf config-manager --set-disable salt-repo-*
                            sudo dnf config-manager --set-enabled salt-repo-3007-sts

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

                    .. code-block:: bash

                            sudo dnf install salt-master-3007.1
                            sudo dnf install salt-minion-3007.1
                            sudo dnf install salt-ssh-3007.1
                            sudo dnf install salt-syndic-3007.1
                            sudo dnf install salt-cloud-3007.1
                            sudo dnf install salt-api-3007.1

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

                    .. warning:: STS not recommended for Production

                        Salt Project recommends deploying LTS releases for Production environments.

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

                    .. code-block:: bash

                            sudo dnf install salt-master-3007.1
                            sudo dnf install salt-minion-3007.1
                            sudo dnf install salt-ssh-3007.1
                            sudo dnf install salt-syndic-3007.1
                            sudo dnf install salt-cloud-3007.1
                            sudo dnf install salt-api-3007.1

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

       .. tab-item:: Zypper

           .. tab-set::

               .. tab-item:: 3006 LTS

                    .. warning:: Latest will be installed without locking the package version to the 3006 major version

                        The following commands can be used to lock the major version

                        .. code-block:: bash

                                sudo zypper addlock "salt-minion < 3006" && sudo zypper addlock "salt-minion >= 3007"
                                sudo zypper addlock "salt-master < 3006" && sudo zypper addlock "salt-master >= 3007"
                                sudo zypper addlock "salt-ssh < 3006" && sudo zypper addlock "salt-ssh >= 3007"
                                sudo zypper addlock "salt-syndic < 3006" && sudo zypper addlock "salt-syndic >= 3007"
                                sudo zypper addlock "salt-cloud < 3006" && sudo zypper addlock "salt-cloud >= 3007"
                                sudo zypper addlock "salt-api < 3006" && sudo zypper addlock "salt-api >= 3007"

                    Available installs:

                    .. code-block:: bash

                            sudo zypper install salt-master
                            sudo zypper install salt-minion
                            sudo zypper install salt-ssh
                            sudo zypper install salt-syndic
                            sudo zypper install salt-cloud
                            sudo zypper install salt-api

                    If wanting to install by a target point release, append the specific Salt
                    full release version. For example:

                    .. code-block:: bash

                            sudo zypper install salt-master-3006.9
                            sudo zypper install salt-minion-3006.9
                            sudo zypper install salt-ssh-3006.9
                            sudo zypper install salt-syndic-3006.9
                            sudo zypper install salt-cloud-3006.9
                            sudo zypper install salt-api-3006.9

                    ``zypper addlock`` can be used to pin to minor versions, if wanting to be
                    excluded during ``zypper update`` runs on a system.

                    .. code-block:: bash

                            sudo zypper addlock salt
                            sudo zypper addlock salt-master
                            sudo zypper addlock salt-minion
                            sudo zypper addlock salt-ssh
                            sudo zypper addlock add salt-syndic
                            sudo zypper addlock add salt-cloud
                            sudo zypper addlock add salt-api

               .. tab-item:: 3007 STS

                    .. warning:: STS not recommended for Production

                        Salt Project recommends deploying LTS releases for Production environments.

                    .. warning:: Latest will be installed without locking the package version to the 3007 major version

                        The following commands can be used to lock the major version

                        .. code-block:: bash

                                sudo zypper addlock "salt-minion < 3007" && sudo zypper addlock "salt-minion >= 3008"
                                sudo zypper addlock "salt-master < 3007" && sudo zypper addlock "salt-master >= 3008"
                                sudo zypper addlock "salt-ssh < 3007" && sudo zypper addlock "salt-ssh >= 3008"
                                sudo zypper addlock "salt-syndic < 3007" && sudo zypper addlock "salt-syndic >= 3008"
                                sudo zypper addlock "salt-cloud < 3007" && sudo zypper addlock "salt-cloud >= 3008"
                                sudo zypper addlock "salt-api < 3007" && sudo zypper addlock "salt-api >= 3008"

                        Salt Project recommends deploying LTS releases for Production environments.

                    Available installs:

                    .. code-block:: bash

                            sudo zypper install salt-master
                            sudo zypper install salt-minion
                            sudo zypper install salt-ssh
                            sudo zypper install salt-syndic
                            sudo zypper install salt-cloud
                            sudo zypper install salt-api

                    If wanting to install by a target point release, append the specific Salt
                    full release version. For example:

                    .. code-block:: bash

                            sudo zypper install salt-master-3007.1
                            sudo zypper install salt-minion-3007.1
                            sudo zypper install salt-ssh-3007.1
                            sudo zypper install salt-syndic-3007.1
                            sudo zypper install salt-cloud-3007.1
                            sudo zypper install salt-api-3007.1

                    ``zypper addlock`` can be used to pin to minor versions, if wanting to be
                    excluded during ``zypper update`` runs on a system.

                    .. code-block:: bash

                            sudo zypper addlock salt
                            sudo zypper addlock salt-master
                            sudo zypper addlock salt-minion
                            sudo zypper addlock salt-ssh
                            sudo zypper addlock add salt-syndic
                            sudo zypper addlock add salt-cloud
                            sudo zypper addlock add salt-api

               .. tab-item:: LATEST Available

                    .. warning:: STS not recommended for Production

                        Salt Project recommends deploying LTS releases for Production environments.

                    Available installs:

                    .. code-block:: bash

                            sudo zypper install salt-master
                            sudo zypper install salt-minion
                            sudo zypper install salt-ssh
                            sudo zypper install salt-syndic
                            sudo zypper install salt-cloud
                            sudo zypper install salt-api

                    If wanting to install by a target point release, append the specific Salt
                    full release version. For example:

                    .. code-block:: bash

                            sudo zypper install salt-master-3007.1
                            sudo zypper install salt-minion-3007.1
                            sudo zypper install salt-ssh-3007.1
                            sudo zypper install salt-syndic-3007.1
                            sudo zypper install salt-cloud-3007.1
                            sudo zypper install salt-api-3007.1

                    ``zypper addlock`` can be used to pin to minor versions, if wanting to be
                    excluded during ``zypper update`` runs on a system.

                    .. code-block:: bash

                            sudo zypper addlock salt
                            sudo zypper addlock salt-master
                            sudo zypper addlock salt-minion
                            sudo zypper addlock salt-ssh
                            sudo zypper addlock add salt-syndic
                            sudo zypper addlock add salt-cloud
                            sudo zypper addlock add salt-api



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
    |minor-lts-version-badge|

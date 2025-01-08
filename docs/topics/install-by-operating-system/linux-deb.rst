.. _install-deb:

===========
Linux (DEB)
===========

These instructions explain how to install Salt rpms on operating systems that
are Debian-like (using ``apt-get`` install methods).

For a list of supported and tested operating systems, for running Salt,
see :ref:`salt-supported-operating-systems`.


Install Salt DEBs
=================

#. Run the following command to install the Salt Project repository:

   .. code-block:: bash

       # Ensure keyrings dir exists
       mkdir -p /etc/apt/keyrings
       # Download public key
       curl -fsSL https://packages.broadcom.com/artifactory/api/security/keypair/SaltProjectKey/public | sudo tee /etc/apt/keyrings/salt-archive-keyring.pgp
       # Create apt repo target configuration
       curl -fsSL https://github.com/saltstack/salt-install-guide/releases/latest/download/salt.sources | sudo tee /etc/apt/sources.list.d/salt.sources

#. Run ``sudo apt update`` to update metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. warning:: STS not recommended for Production

      Salt Project recommends deploying LTS releases for Production environments.

   .. tab-set::

       .. tab-item:: |major-one-version-text|

            Populate ``/etc/apt/preferences.d/salt-pin-1001`` in order to restrict upgrades to Salt |major-one-version-text|:

            .. parsed-literal::

                    echo 'Package: salt-*
                    Pin: version |major-one-version|.*
                    Pin-Priority: 1001' | sudo tee /etc/apt/preferences.d/salt-pin-1001

            Available installs:

            .. code-block:: bash

                    sudo apt-get install salt-master
                    sudo apt-get install salt-minion
                    sudo apt-get install salt-ssh
                    sudo apt-get install salt-syndic
                    sudo apt-get install salt-cloud
                    sudo apt-get install salt-api

            If wanting to install by a target point release, append the specific Salt
            full release version. For example:

            .. parsed-literal::

                    sudo apt-get install salt-common=\ |minor-one-version|
                    sudo apt-get install salt-master=\ |minor-one-version|
                    sudo apt-get install salt-minion=\ |minor-one-version|
                    sudo apt-get install salt-ssh=\ |minor-one-version|
                    sudo apt-get install salt-syndic=\ |minor-one-version|
                    sudo apt-get install salt-cloud=\ |minor-one-version|
                    sudo apt-get install salt-api=\ |minor-one-version|

            .. code-block:: bash

                    # Example commands for pinning a current package minor so that
                    # it is skipped during system-wide apt-get upgrade events
                    sudo apt-mark hold salt-master
                    sudo apt-mark hold salt-minion
                    sudo apt-mark hold salt-ssh
                    sudo apt-mark hold salt-syndic
                    sudo apt-mark hold salt-cloud
                    sudo apt-mark hold salt-api

            .. warning:: Salt dependency conflicts

                If going with a non-latest point release of a target major version, you may be
                required to install other salt packages in a pinned fashion. For example, to install
                ``salt-minion``, a user will be required to install ``salt-common`` at the same version:

                .. parsed-literal::

                    sudo apt-get install salt-minion=\ |minor-one-version| salt-common=\ |minor-one-version|


       .. tab-item:: |major-two-version-text|

            Populate ``/etc/apt/preferences.d/salt-pin-1001`` in order to restrict upgrades to Salt |major-two-version-text|:

            .. parsed-literal::

                    echo 'Package: salt-*
                    Pin: version |major-two-version|.*
                    Pin-Priority: 1001' | sudo tee /etc/apt/preferences.d/salt-pin-1001

            Available installs:

            .. code-block:: bash

                    sudo apt-get install salt-master
                    sudo apt-get install salt-minion
                    sudo apt-get install salt-ssh
                    sudo apt-get install salt-syndic
                    sudo apt-get install salt-cloud
                    sudo apt-get install salt-api

            If wanting to install by a target point release, append the specific Salt
            full release version. For example:

            .. parsed-literal::

                    sudo apt-get install salt-common=\ |minor-two-version|
                    sudo apt-get install salt-master=\ |minor-two-version|
                    sudo apt-get install salt-minion=\ |minor-two-version|
                    sudo apt-get install salt-ssh=\ |minor-two-version|
                    sudo apt-get install salt-syndic=\ |minor-two-version|
                    sudo apt-get install salt-cloud=\ |minor-two-version|
                    sudo apt-get install salt-api=\ |minor-two-version|

            .. code-block:: bash

                    # Example commands for pinning a current package minor so that
                    # it is skipped during system-wide apt-get upgrade events
                    sudo apt-mark hold salt-master
                    sudo apt-mark hold salt-minion
                    sudo apt-mark hold salt-ssh
                    sudo apt-mark hold salt-syndic
                    sudo apt-mark hold salt-cloud
                    sudo apt-mark hold salt-api

            .. warning:: Salt dependency conflicts

                If going with a non-latest point release of a target major version, you may be
                required to install other salt packages in a pinned fashion. For example, to install
                ``salt-minion``, a user will be required to install ``salt-common`` at the same version:

                .. parsed-literal::

                    sudo apt-get install salt-minion=\ |minor-two-version| salt-common=\ |minor-two-version|


       .. tab-item:: LATEST Available

            If users would like to leave installs to come from either LTS or STS, whichever
            major version is latest.

            Available installs:

            .. code-block:: bash

                    sudo apt-get install salt-master
                    sudo apt-get install salt-minion
                    sudo apt-get install salt-ssh
                    sudo apt-get install salt-syndic
                    sudo apt-get install salt-cloud
                    sudo apt-get install salt-api

            If wanting to install by a target point release, append the specific Salt
            full release version. For example:

            .. parsed-literal::

                    sudo apt-get install salt-common=\ |minor-latest-version|
                    sudo apt-get install salt-master=\ |minor-latest-version|
                    sudo apt-get install salt-minion=\ |minor-latest-version|
                    sudo apt-get install salt-ssh=\ |minor-latest-version|
                    sudo apt-get install salt-syndic=\ |minor-latest-version|
                    sudo apt-get install salt-cloud=\ |minor-latest-version|
                    sudo apt-get install salt-api=\ |minor-latest-version|

            .. code-block:: bash

                    # Example commands for pinning a current package minor so that
                    # it is skipped during system-wide apt-get upgrade events
                    sudo apt-mark hold salt-master
                    sudo apt-mark hold salt-minion
                    sudo apt-mark hold salt-ssh
                    sudo apt-mark hold salt-syndic
                    sudo apt-mark hold salt-cloud
                    sudo apt-mark hold salt-api

            .. warning::

                If going with a non-latest point release of a target major version, you may be
                required to install other salt packages in a pinned fashion. For example, to install
                ``salt-minion``, a user will be required to install ``salt-common`` at the same version:

                .. parsed-literal::

                    sudo apt-get install salt-minion=\ |minor-latest-version| salt-common=\ |minor-latest-version|


#. Enable and start the Salt services

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

.. card:: Browse the repo for DEB packages
    :class-card: sd-border-1
    :link: https://packages.broadcom.com/artifactory/saltproject-deb/
    :width: 50%

    :bdg-primary:`deb`

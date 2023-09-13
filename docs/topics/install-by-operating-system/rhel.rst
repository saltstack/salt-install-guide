.. _install-rhel:

=============
RedHat (RHEL)
=============

These instructions explain how to install Salt on RedHat (RHEL) operating
systems:

* `Install Salt on RedHat (RHEL) 9 x86_64`_
* `Install Salt on RedHat (RHEL) 9 aarch64 and arm64`_
* `Install Salt on RedHat (RHEL) 8 x86_64`_
* `Install Salt on RedHat (RHEL) 8 aarch64 and arm64`_
* `Install Salt on RedHat (RHEL) 7 x86_64`_
* `Install Salt on RedHat (RHEL) 7 aarch64 and arm64`_

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on RedHat (RHEL) 9 x86_64
======================================
To install Salt on RedHat 9 for x86_64 architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 9 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-latest-gpg-x86_64|\

               curl -fsSL \ |rhel9-latest-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-major-gpg-x86_64|\

               curl -fsSL \ |rhel9-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-minor-gpg-x86_64|\

               curl -fsSL \ |rhel9-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst


   .. Note::
       Because of the presence of classic packages of Salt in EPEL, it's
       possible that when you download the package from EPEL, it instead
       downloads classic packages of older versions of Salt instead of the
       onedir packages.

       During depsolving, when choosing the best provider among several, `yum`
       respects the priority of each provider's repository. The value is an
       integer from 1 to 99, with 1 being the most preferred repository and 99
       the least preferred. By default all repositories have the priority of 80.

       EPEL was treating the Salt repository as 99. To resolve this issue, Salt
       has changed its priority level to 10 for RHEL 7, 8, and 9.


#. Run ``sudo yum clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo yum install salt-master
       sudo yum install salt-minion
       sudo yum install salt-ssh
       sudo yum install salt-syndic
       sudo yum install salt-cloud
       sudo yum install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on RedHat (RHEL) 9 aarch64 and arm64
=================================================
To install Salt on RedHat 9 for aarch64 and arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 9 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-latest-gpg-arm64|\

               curl -fsSL \ |rhel9-latest-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-major-gpg-arm64|\

               curl -fsSL \ |rhel9-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-minor-gpg-arm64|\

               curl -fsSL \ |rhel9-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst


   .. Note::
       Because of the presence of classic packages of Salt in EPEL, it's
       possible that when you download the package from EPEL, it instead
       downloads classic packages of older versions of Salt instead of the
       onedir packages.

       During depsolving, when choosing the best provider among several, `yum`
       respects the priority of each provider's repository. The value is an
       integer from 1 to 99, with 1 being the most preferred repository and 99
       the least preferred. By default all repositories have the priority of 80.

       EPEL was treating the Salt repository as 99. To resolve this issue, Salt
       has changed its priority level to 10 for RHEL 7, 8, and 9.


#. Run ``sudo yum clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo yum install salt-master
       sudo yum install salt-minion
       sudo yum install salt-ssh
       sudo yum install salt-syndic
       sudo yum install salt-cloud
       sudo yum install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on RedHat (RHEL) 8 x86_64
======================================
To install the :ref:`onedir` packages of Salt on RedHat 8 for x86_64
architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 8 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-latest-gpg-x86_64|\

               curl -fsSL \ |rhel8-latest-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-major-gpg-x86_64|\

               curl -fsSL \ |rhel8-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-minor-gpg-x86_64|\

               curl -fsSL \ |rhel8-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

#. Run ``sudo yum clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo yum install salt-master
       sudo yum install salt-minion
       sudo yum install salt-ssh
       sudo yum install salt-syndic
       sudo yum install salt-cloud
       sudo yum install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on RedHat (RHEL) 8 aarch64 and arm64
=================================================
To install the :ref:`onedir` packages of Salt on RedHat 8 for aarch64 and
arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 8 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-latest-gpg-arm64|\

               curl -fsSL \ |rhel8-latest-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-major-gpg-arm64|\

               curl -fsSL \ |rhel8-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-minor-gpg-arm64|\

               curl -fsSL \ |rhel8-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

#. Run ``sudo yum clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo yum install salt-master
       sudo yum install salt-minion
       sudo yum install salt-ssh
       sudo yum install salt-syndic
       sudo yum install salt-cloud
       sudo yum install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on RedHat (RHEL) 7 x86_64
======================================
To install the :ref:`onedir` packages of Salt on RedHat 7 for x86_64
architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 7 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-latest-gpg-x86_64|\

               curl -fsSL \ |rhel7-latest-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 7 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-major-gpg-x86_64|\

               curl -fsSL \ |rhel7-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 7 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-minor-gpg-x86_64|\

               curl -fsSL \ |rhel7-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst


#. Run ``sudo yum clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo yum install salt-master
       sudo yum install salt-minion
       sudo yum install salt-ssh
       sudo yum install salt-syndic
       sudo yum install salt-cloud
       sudo yum install salt-api

#. Enable and start service for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on RedHat (RHEL) 7 aarch64 and arm64
=================================================
To install the :ref:`onedir` packages of Salt on RedHat 7 for aarch64 and
arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 7 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-latest-gpg-arm64|\

               curl -fsSL \ |rhel7-latest-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 7 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-major-gpg-arm64|\

               curl -fsSL \ |rhel7-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: RHEL 7 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-minor-gpg-arm64|\

               curl -fsSL \ |rhel7-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst


#. Run ``sudo yum clean expire-cache`` to clear the repository metadata.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo yum install salt-master
       sudo yum install salt-minion
       sudo yum install salt-ssh
       sudo yum install salt-syndic
       sudo yum install salt-cloud
       sudo yum install salt-api

#. Enable and start service for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Browse the repo
===============

.. card:: Browse the repo for RedHat (RHEL) packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/redhat/
    :width: 50%

    :bdg-primary:`RedHat`
    |supported-release-1-badge|

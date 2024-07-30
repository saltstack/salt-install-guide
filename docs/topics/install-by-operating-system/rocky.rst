.. _install-rocky:

===========
Rocky Linux
===========

For Rocky Linux operating systems (or AlmaLinux, etc.), use the following instructions.

These instructions explain how to install Salt on Rocky Linux operating systems:

* `Install Salt on Rocky Linux 9 x86_64`_
* `Install Salt on Rocky Linux 9 aarch64 and arm64`_
* `Install Salt on Rocky Linux 8 x86_64`_
* `Install Salt on Rocky Linux 8 aarch64 and arm64`_


.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Rocky Linux 9 x86_64
======================================
To install the :ref:`onedir` packages of Salt on Rocky Linux 9 for x86_64
architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Rocky Linux 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **Rocky Linux 9**:

           .. parsed-literal::

               sudo rpm --import \ |rocky9-major-gpg-x86_64|\

               curl -fsSL \ |rocky9-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Rocky Linux 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **Rocky Linux 9**:

           .. parsed-literal::

               sudo rpm --import \ |rocky9-minor-gpg-x86_64|\

               curl -fsSL \ |rocky9-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Salt on Rocky Linux 9 aarch64 and arm64
=================================================
To install the :ref:`onedir` packages of Salt on Rocky Linux 9 for aarch64 and
arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Rocky Linux 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **Rocky Linux 9**:

           .. parsed-literal::

               sudo rpm --import \ |rocky9-major-gpg-arm64|\

               curl -fsSL \ |rocky9-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Rocky Linux 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **Rocky Linux 9**:

           .. parsed-literal::

               sudo rpm --import \ |rocky9-minor-gpg-arm64|\

               curl -fsSL \ |rocky9-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

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



Install Salt on Rocky Linux 8 x86_64
======================================
To install the :ref:`onedir` packages of Salt on Rocky Linux 8 for x86_64
architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Rocky Linux 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **Rocky Linux 8**:

           .. parsed-literal::

               sudo rpm --import \ |rocky8-major-gpg-x86_64|\

               curl -fsSL \ |rocky8-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Rocky Linux 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **Rocky Linux 8**:

           .. parsed-literal::

               sudo rpm --import \ |rocky8-minor-gpg-x86_64|\

               curl -fsSL \ |rocky8-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

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



Install Salt on Rocky Linux 8 aarch64 and arm64
=================================================
To install the :ref:`onedir` packages of Salt on Rocky Linux 8 for aarch64 and
arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Rocky Linux 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **Rocky Linux 8**:

           .. parsed-literal::

               sudo rpm --import \ |rocky8-major-gpg-arm64|\

               curl -fsSL \ |rocky8-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Rocky Linux 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **Rocky Linux 8**:

           .. parsed-literal::

               sudo rpm --import \ |rocky8-minor-gpg-arm64|\

               curl -fsSL \ |rocky8-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Browse the repo
===============

.. card:: Browse the repo for Rocky Linux packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/redhat/
    :width: 50%

    :bdg-primary:`Rocky Linux`
    |supported-release-1-badge|

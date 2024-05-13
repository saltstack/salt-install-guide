.. _install-centos:

======
CentOS
======

These instructions explain how to install Salt on CentOS operating systems:

* `Install Salt on CentOS Stream 9 x86_64`_
* `Install Salt on CentOS Stream 9 aarch64 and arm64`_
* `Install Salt on CentOS Stream 8 x86_64`_
* `Install Salt on CentOS Stream 8 aarch64 and arm64`_
* `Install Salt on CentOS 7 x86_64`_
* `Install Salt on CentOS 7 aarch64 and arm64`_


.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on CentOS Stream 9 x86_64
======================================
To install the :ref:`onedir` packages of Salt on Centos 9 for x86_64
architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-major-gpg-x86_64|\

               curl -fsSL \ |centos9-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: CentOS 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-minor-gpg-x86_64|\

               curl -fsSL \ |centos9-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Salt on CentOS Stream 9 aarch64 and arm64
=================================================
To install the :ref:`onedir` packages of Salt on Centos 9 for aarch64 and
arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-major-gpg-arm64|\

               curl -fsSL \ |centos9-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: CentOS 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-minor-gpg-arm64|\

               curl -fsSL \ |centos9-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

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



Install Salt on CentOS Stream 8 x86_64
======================================
To install the :ref:`onedir` packages of Salt on Centos 8 for x86_64
architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-major-gpg-x86_64|\

               curl -fsSL \ |centos8-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: CentOS 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-minor-gpg-x86_64|\

               curl -fsSL \ |centos8-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

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



Install Salt on CentOS Stream 8 aarch64 and arm64
=================================================
To install the :ref:`onedir` packages of Salt on Centos 8 for aarch64 and
arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-major-gpg-arm64|\

               curl -fsSL \ |centos8-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: CentOS 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-minor-gpg-arm64|\

               curl -fsSL \ |centos8-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

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



Install Salt on CentOS 7 x86_64
===============================
To install Salt on CentOS 7 for x86_64 architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 7 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-major-gpg-x86_64|\

               curl -fsSL \ |centos7-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: CentOS 7 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-minor-gpg-x86_64|\

               curl -fsSL \ |centos7-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Salt on CentOS 7 aarch64 and arm64
==========================================
To install Salt on CentOS 7 for aarch64 and arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 7 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-major-gpg-arm64|\

               curl -fsSL \ |centos7-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: CentOS 7 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-minor-gpg-arm64|\

               curl -fsSL \ |centos7-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

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

.. card:: Browse the repo for CentOS packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/redhat/
    :width: 50%

    :bdg-primary:`CentOS`
    |supported-release-1-badge|

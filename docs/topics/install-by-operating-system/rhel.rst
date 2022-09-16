.. _install-rhel:

=============
RedHat (RHEL)
=============

These instructions explain how to install Salt on RedHat (RHEL) operating
systems:

* `Install onedir packages of Salt on RedHat (RHEL) 9`_
* `Install onedir packages of Salt on RedHat (RHEL) 8`_
* `Install onedir packages of Salt on RedHat (RHEL) 7`_
* `Install classic packages of Salt on RedHat (RHEL) 8`_
* `Install classic packages of Salt on RedHat (RHEL) 7`_


.. card:: Browse the repo for RedHat (RHEL) packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/py3/redhat/
    :width: 50%

    :bdg-primary:`RedHat`
    :bdg-secondary:`Python3`

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install onedir packages of Salt on RedHat (RHEL) 9
==================================================
To install the :ref:`onedir` packages of Salt on RedHat 9:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 9 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-onedir-latest-gpg|\

               curl -fsSL \ |rhel9-onedir-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-onedir-major-gpg|\

               curl -fsSL \ |rhel9-onedir-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-onedir-minor-gpg|\

               curl -fsSL \ |rhel9-onedir-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


.. include:: ../_includes/post-install-by-os.rst


Install onedir packages of Salt on RedHat (RHEL) 8
==================================================
To install the :ref:`onedir` packages of Salt on RedHat 8:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 8 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-onedir-latest-gpg|\

               curl -fsSL \ |rhel8-onedir-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-onedir-major-gpg|\

               curl -fsSL \ |rhel8-onedir-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-onedir-minor-gpg|\

               curl -fsSL \ |rhel8-onedir-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


.. include:: ../_includes/post-install-by-os.rst


Install onedir packages of Salt on RedHat (RHEL) 7
==================================================
To install the :ref:`onedir` packages of Salt on RedHat 7:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 7 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-onedir-latest-gpg|\

               curl -fsSL \ |rhel7-onedir-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-onedir-major-gpg|\

               curl -fsSL \ |rhel7-onedir-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-onedir-minor-gpg|\

               curl -fsSL \ |rhel7-onedir-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo


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


.. include:: ../_includes/post-install-by-os.rst


Install classic packages of Salt on RedHat (RHEL) 8
===================================================

.. include:: ../_includes/warning-about-old-packages.rst

To install Salt on RedHat 8 using the old packaging system:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 8 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-classic-latest-gpg|\

               curl -fsSL \ |rhel8-classic-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Major classic)

           To pin your Salt upgrades to the latest :ref:`major` :ref:`classic`
           package of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-classic-major-gpg|\

               curl -fsSL \ |rhel8-classic-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Minor classic)

           To pin your Salt upgrades to the latest :ref:`minor` :ref:`classic`
           package of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-classic-minor-gpg|\

               curl -fsSL \ |rhel8-classic-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


.. include:: ../_includes/post-install-by-os.rst



Install classic packages of Salt on RedHat (RHEL) 7
===================================================

.. include:: ../_includes/warning-about-old-packages.rst

To install Salt on RedHat 7 using the old packaging system:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 7 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-classic-latest-gpg|\

               curl -fsSL \ |rhel7-classic-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Major)

           To pin your Salt upgrades to the latest :ref:`major` :ref:`classic`
           package of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-classic-major-gpg|\

               curl -fsSL \ |rhel7-classic-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` :ref:`classic`
           package of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-classic-minor-gpg|\

               curl -fsSL \ |rhel7-classic-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


.. include:: ../_includes/post-install-by-os.rst

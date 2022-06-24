.. _install-rhel:

=============
RedHat (RHEL)
=============

These instructions explain how to install Salt on RedHat (RHEL) operating
systems:

* `Install Tiamat packages of Salt on RedHat (RHEL) 9`_
* `Install Tiamat packages of Salt on RedHat (RHEL) 8`_
* `Install Tiamat packages of Salt on RedHat (RHEL) 7`_
* `Install classic packages of Salt on RedHat (RHEL) 8`_
* `Install classic packages of Salt on RedHat (RHEL) 7`_


.. card:: Browse the repo for RedHat (RHEL) packages
    :link: https://repo.saltproject.io/py3/redhat/
    :width: 50%

    :bdg-primary:`RedHat`
    :bdg-secondary:`Python3`

.. include:: ../_includes/what-is-tiamat.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Tiamat packages of Salt on RedHat (RHEL) 9
==================================================
To install the :ref:`tiamat` packages of Salt on RedHat 9:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 9 (Latest Tiamat)

           To pin your Salt upgrades to the :ref:`latest` :ref:`tiamat` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-tiamat-latest-gpg|\

               curl -fsSL \ |rhel9-tiamat-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 9 (Major Tiamat)

           To pin your Salt upgrades to the :ref:`major` :ref:`tiamat` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-tiamat-major-gpg|\

               curl -fsSL \ |rhel9-tiamat-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 9 (Minor Tiamat)

           To pin your Salt upgrades to the :ref:`minor` :ref:`tiamat` package
           of Salt for **RHEL 9**:

           .. parsed-literal::

               sudo rpm --import \ |rhel9-tiamat-minor-gpg|\

               curl -fsSL \ |rhel9-tiamat-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Tiamat packages of Salt on RedHat (RHEL) 8
==================================================
To install the :ref:`tiamat` packages of Salt on RedHat 8:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 8 (Latest Tiamat)

           To pin your Salt upgrades to the :ref:`latest` :ref:`tiamat` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-tiamat-latest-gpg|\

               curl -fsSL \ |rhel8-tiamat-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Major Tiamat)

           To pin your Salt upgrades to the :ref:`major` :ref:`tiamat` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-tiamat-major-gpg|\

               curl -fsSL \ |rhel8-tiamat-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Minor Tiamat)

           To pin your Salt upgrades to the :ref:`minor` :ref:`tiamat` package
           of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-tiamat-minor-gpg|\

               curl -fsSL \ |rhel8-tiamat-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Tiamat packages of Salt on RedHat (RHEL) 7
==================================================
To install the :ref:`tiamat` packages of Salt on RedHat 7:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 7 (Latest Tiamat)

           To pin your Salt upgrades to the :ref:`latest` :ref:`tiamat` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-tiamat-latest-gpg|\

               curl -fsSL \ |rhel7-tiamat-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Major Tiamat)

           To pin your Salt upgrades to the :ref:`major` :ref:`tiamat` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-tiamat-major-gpg|\

               curl -fsSL \ |rhel7-tiamat-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Minor Tiamat)

           To pin your Salt upgrades to the :ref:`minor` :ref:`tiamat` package
           of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-tiamat-minor-gpg|\

               curl -fsSL \ |rhel7-tiamat-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo


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

       .. tab-item:: RHEL 8 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-latest-gpg|\

               curl -fsSL \ |rhel8-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-major-gpg|\

               curl -fsSL \ |rhel8-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 8 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-minor-gpg|\

               curl -fsSL \ |rhel8-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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

       .. tab-item:: RHEL 7 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-latest-gpg|\

               curl -fsSL \ |rhel7-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-major-gpg|\

               curl -fsSL \ |rhel7-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: RHEL 7 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import \ |rhel7-minor-gpg|\

               curl -fsSL \ |rhel7-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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

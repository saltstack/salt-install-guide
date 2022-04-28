.. _install-rhel:

=============
RedHat (RHEL)
=============

These instructions explain how to install Salt on RedHat (RHEL) operating
systems:

* `Install Salt on RedHat (RHEL) 8`_
* `Install Salt on RedHat (RHEL) 7`_


.. card:: Browse the repo for packages
    :link: https://repo.saltproject.io/py3/redhat/
    :width: 50%

    :bdg-primary:`RedHat`
    :bdg-secondary:`Python3`


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on RedHat (RHEL) 8
===============================
To install Salt on RedHat 8:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 8 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **RHEL 8**:

           .. parsed-literal::

               sudo rpm --import \ |rhel8-tiamat-gpg|\

               curl -fsSL \ |rhel8-tiamat-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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

               sudo rpm --import \ |rhel8-major-gpg|\

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


After installing Salt on your operating system, you need to complete the
following post-installation steps:

* :ref:`configure-master-minion`
* :ref:`start-salt-services`
* :ref:`accept-keys`
* :ref:`verify-install`



Install Salt on RedHat (RHEL) 7
===============================
To install Salt on RedHat 7:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: RHEL 7 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **RHEL 7**:

           .. parsed-literal::

               sudo rpm --import  \ |rhel7-tiamat-gpg|\

               curl -fsSL \ |rhel7-tiamat-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


After installing Salt on your operating system, you need to complete the
following post-installation steps:

* :ref:`configure-master-minion`
* :ref:`start-salt-services`
* :ref:`accept-keys`
* :ref:`verify-install`

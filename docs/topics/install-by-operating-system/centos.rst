.. _install-centos:

======
CentOS
======

These instructions explain how to install Salt on CentOS operating systems:

* `Install Salt on CentOS Stream 9`_
* `Install Salt on CentOS Stream 8`_
* `Install Salt on CentOS 7`_


.. card:: Browse the repo for CentOS packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/py3/redhat/
    :width: 50%

    :bdg-primary:`CentOS`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on CentOS Stream 9
===============================
To install the :ref:`onedir` packages of Salt on Centos 9:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 9 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-latest-gpg|\

               curl -fsSL \ |centos9-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: CentOS 9 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-major-gpg|\

               curl -fsSL \ |centos9-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo


       .. tab-item:: CentOS 9 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 9**:

           .. parsed-literal::

               sudo rpm --import \ |centos9-minor-gpg|\

               curl -fsSL \ |centos9-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Salt on CentOS Stream 8
===============================
To install the :ref:`onedir` packages of Salt on Centos 8:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 8 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-latest-gpg|\

               curl -fsSL \ |centos8-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: CentOS 8 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-major-gpg|\

               curl -fsSL \ |centos8-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo


       .. tab-item:: CentOS 8 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 8**:

           .. parsed-literal::

               sudo rpm --import \ |centos8-minor-gpg|\

               curl -fsSL \ |centos8-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Salt on CentOS 7
========================
To install Salt on CentOS 7:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: CentOS 7 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-latest-gpg|\

               curl -fsSL \ |centos7-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: CentOS 7 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-major-gpg|\

               curl -fsSL \ |centos7-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo


       .. tab-item:: CentOS 7 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package of Salt for **CentOS 7**:

           .. parsed-literal::

               sudo rpm --import \ |centos7-minor-gpg|\

               curl -fsSL \ |centos7-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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

.. _install-fedora:

======
Fedora
======

These instructions explain how to install Salt on Fedora operating systems:

* `Install Salt on Fedora 39 x86_64`_
* `Install Salt on Fedora 39 aarch64 and arm64`_

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Fedora 39 x86_64
================================
To install Salt on Fedora 39 for x86_64 architecture:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Fedora 39 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Fedora 39**:

           .. parsed-literal::

               sudo rpm --import \ |fedora39-major-gpg-x86_64|\

               curl -fsSL \ |fedora39-major-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Fedora 39 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Fedora 39**:

           .. parsed-literal::

               sudo rpm --import \ |fedora39-minor-gpg-x86_64|\

               curl -fsSL \ |fedora39-minor-download-x86_64|\  | sudo tee /etc/yum.repos.d/salt.repo

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


Install Salt on Fedora 39 aarch64 and arm64
===========================================
To install Salt on Fedora 39 for aarch64 and arm64 architectures:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Fedora 39 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Fedora 39**:

           .. parsed-literal::

               sudo rpm --import \ |fedora39-major-gpg-arm64|\

               curl -fsSL \ |fedora39-major-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Fedora 39 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Fedora 39**:

           .. parsed-literal::

               sudo rpm --import \ |fedora39-minor-gpg-arm64|\

               curl -fsSL \ |fedora39-minor-download-arm64|\  | sudo tee /etc/yum.repos.d/salt.repo

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

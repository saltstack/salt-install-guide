.. _install-amazon:

==============
Amazon Linux 2
==============

These instructions explain how to install Salt on Amazon Linux 2 operating
systems:

* `Install Salt on Amazon Linux 2`_

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Amazon Linux 2
==============================
To install the :ref:`onedir` packages of Salt on Amazon Linux 2:

#. Run the following commands to install the Salt Project repository and key:

   .. tab-set::

       .. tab-item:: Amazon Linux 2 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-latest-gpg|\

               curl -fsSL \ |amazon-linux2-latest-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Amazon Linux 2 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-major-gpg|\

               curl -fsSL \ |amazon-linux2-major-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Amazon Linux 2 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-minor-gpg|\

               curl -fsSL \ |amazon-linux2-minor-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

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

.. card:: Browse the repo for Amazon Linux 2 packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/amazon/
    :width: 50%

    :bdg-primary:`Amazon Linux 2`
    |supported-release-1-badge|

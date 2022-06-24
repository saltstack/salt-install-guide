.. _install-amazon:

==============
Amazon Linux 2
==============

These instructions explain how to install Salt on Amazon Linux 2 operating
systems:

* `Install Tiamat packages of Salt on Amazon Linux 2`_
* `Install classic packages of Salt on Amazon Linux 2`_


.. card:: Browse the repo for Amazon Linux 2 packages
    :link: https://repo.saltproject.io/py3/amazon/
    :width: 50%

    :bdg-primary:`Amazon Linux 2`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-tiamat.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Tiamat packages of Salt on Amazon Linux 2
=================================================
To install the :ref:`tiamat` packages of Salt on Amazon Linux 2:

#. Run the following commands to install the Salt Project repository and key:

   .. tab-set::

       .. tab-item:: Amazon Linux 2 (Latest Tiamat)

           To pin your Salt upgrades to the :ref:`latest` :ref:`tiamat` package
           of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-tiamat-latest-gpg|\

               curl -fsSL \ |amazon-linux2-tiamat-latest-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

       .. tab-item:: Amazon Linux 2 (Major Tiamat)

           To pin your Salt upgrades to the :ref:`major` :ref:`tiamat` package
           of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-tiamat-major-gpg|\

               curl -fsSL \ |amazon-linux2-tiamat-major-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

       .. tab-item:: Amazon Linux 2 (Minor Tiamat)

           To pin your Salt upgrades to the :ref:`minor` :ref:`tiamat` package
           of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-tiamat-minor-gpg|\

               curl -fsSL \ |amazon-linux2-tiamat-minor-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

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


Install classic packages of Salt on Amazon Linux 2
==================================================

.. include:: ../_includes/warning-about-old-packages.rst

To install Salt on Amazon Linux 2 using the old packaging system:

#. Run the following commands to install the Salt Project repository and key:

   .. tab-set::

       .. tab-item:: Amazon Linux 2 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-latest-gpg|\

               curl -fsSL \ |amazon-linux2-latest-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

       .. tab-item:: Amazon Linux 2 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-major-gpg|\

               curl -fsSL \ |amazon-linux2-major-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

       .. tab-item:: Amazon Linux 2 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Amazon Linux 2**:

           .. parsed-literal::

               sudo rpm --import \ |amazon-linux2-minor-gpg|\

               curl -fsSL \ |amazon-linux2-minor-download|\  | sudo tee /etc/yum.repos.d/salt-amzn.repo

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

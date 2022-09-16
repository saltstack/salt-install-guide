.. _install-debian:

======
Debian
======

These instructions explain how to install Salt on Debian operating systems:

* `Install onedir packages of Salt on Debian 11 (Bullseye)`_
* `Install onedir packages of Salt on Debian 10 (Buster)`_
* `Install classic packages of Salt on Debian 11 (Bullseye)`_
* `Install classic packages of Salt on Debian 11 (Bullseye) ARM64`_
* `Install classic packages of Salt on Debian 10 (Buster)`_


.. card:: Browse the repo for Debian packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/py3/debian/
    :width: 50%

    :bdg-primary:`Debian`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install onedir packages of Salt on Debian 11 (Bullseye)
=======================================================
To install the :ref:`onedir` packages of Salt on Debian 11 (Bullseye):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 11 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-onedir-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-onedir-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-onedir-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-onedir-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-onedir-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-onedir-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

#. Run ``sudo apt-get update`` to update your packages.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo apt-get install salt-master
       sudo apt-get install salt-minion
       sudo apt-get install salt-ssh
       sudo apt-get install salt-syndic
       sudo apt-get install salt-cloud
       sudo apt-get install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


.. include:: ../_includes/post-install-by-os.rst


Install onedir packages of Salt on Debian 10 (Buster)
=====================================================
To install the :ref:`onedir` packages of Salt on Debian 10 (Buster):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 10 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-onedir-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-onedir-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 10 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-onedir-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-onedir-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 10 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-onedir-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-onedir-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

#. Run ``sudo apt-get update`` to update your packages.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo apt-get install salt-master
       sudo apt-get install salt-minion
       sudo apt-get install salt-ssh
       sudo apt-get install salt-syndic
       sudo apt-get install salt-cloud
       sudo apt-get install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


.. include:: ../_includes/post-install-by-os.rst



.. Install onedir packages of Salt on Debian 11 (Bullseye) ARM64
 =============================================================
 To install the :ref:`onedir` packages of Salt on Debian 11 (Bullseye) ARM64:

 #. Run the following commands to import the Salt Project repository key, and to
 create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 11 ARM64 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-onedir-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-arm64-onedir-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 ARM64 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-onedir-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-arm64-onedir-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 ARM64 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Debian 11 ARM64 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-onedir-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-arm64-onedir-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

 #. Run ``sudo apt-get update`` to update your packages.

 #. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo apt-get install salt-master
       sudo apt-get install salt-minion
       sudo apt-get install salt-ssh
       sudo apt-get install salt-syndic
       sudo apt-get install salt-cloud
       sudo apt-get install salt-api

 #. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


 .. include:: ../_includes/post-install-by-os.rst


Install classic packages of Salt on Debian 11 (Bullseye)
========================================================

.. include:: ../_includes/warning-about-old-packages.rst

To install Salt on Debian 11 (Bullseye) using the old packaging system:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 11 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-classic-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-classic-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Major classic)

           To pin your Salt upgrades to the :ref:`major` :ref:`classic` package
           of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-classic-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-classic-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Minor classic)

           To pin your Salt upgrades to the :ref:`minor` :ref:`classic` package
           of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-classic-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-classic-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

#. Run ``sudo apt-get update`` to update your packages.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo apt-get install salt-master
       sudo apt-get install salt-minion
       sudo apt-get install salt-ssh
       sudo apt-get install salt-syndic
       sudo apt-get install salt-cloud
       sudo apt-get install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


.. include:: ../_includes/post-install-by-os.rst


Install classic packages of Salt on Debian 11 (Bullseye) ARM64
==============================================================

.. include:: ../_includes/warning-about-old-packages.rst

To install Salt on Debian 11 (Bullseye) ARM64 using the old packaging system:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 11 ARM64 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-classic-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-arm64-classic-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 ARM64 (Major classic)

           To pin your Salt upgrades to the :ref:`major` :ref:`classic` package
           of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-classic-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |debian11-arm64-classic-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 ARM64 (Minor classic)

           To pin your Salt upgrades to the :ref:`minor` :ref:`classic` package
           of Salt for **Debian 11 ARM64 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-classic-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |debian11-arm64-classic-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

#. Run ``sudo apt-get update`` to update your packages.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo apt-get install salt-master
       sudo apt-get install salt-minion
       sudo apt-get install salt-ssh
       sudo apt-get install salt-syndic
       sudo apt-get install salt-cloud
       sudo apt-get install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


.. include:: ../_includes/post-install-by-os.rst



Install classic packages of Salt on Debian 10 (Buster)
======================================================

.. include:: ../_includes/warning-about-old-packages.rst

To install Salt on Debian 10 (Buster):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 10 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-classic-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-classic-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 10 (Major classic)

           To pin your Salt upgrades to the latest :ref:`major` :ref:`classic`
           package of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-classic-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-classic-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 10 (Minor classic)

           To pin your Salt upgrades to the latest :ref:`minor` :ref:`classic`
           package of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-classic-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-classic-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

#. Run ``sudo apt-get update`` to update your packages.

#. Install the salt-minion, salt-master, or other Salt components:

   .. code-block:: bash

       sudo apt-get install salt-master
       sudo apt-get install salt-minion
       sudo apt-get install salt-ssh
       sudo apt-get install salt-syndic
       sudo apt-get install salt-cloud
       sudo apt-get install salt-api

#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


.. include:: ../_includes/post-install-by-os.rst

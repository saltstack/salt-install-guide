.. _install-ubuntu:

======
Ubuntu
======

These instructions explain how to install Salt on Debian operating systems:

* `Install Salt on Ubuntu 22 (Jammy)`_
* `Install Salt on Ubuntu 22 (Jammy) ARM64`_
* `Install Salt on Ubuntu 20 (Focal)`_
* `Install Salt on Ubuntu 20 (Focal) ARM64`_
* `Install Salt on Ubuntu 18 (Bionic)`_


.. card:: Browse the repo for packages
    :link: https://repo.saltproject.io/py3/ubuntu/
    :width: 50%

    :bdg-primary:`Ubuntu`
    :bdg-secondary:`Python3`


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Ubuntu 22 (Jammy)
=================================
To install Salt on Ubuntu 22 (Jammy):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Ubuntu 22 (Jammy)**:

   .. parsed-literal::

       sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu22-tiamat-gpg|\

       echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu22-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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


Install Salt on Ubuntu 22 (Jammy) ARM64
=======================================
To install Salt on Ubuntu 22 (Jammy) ARM64:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Ubuntu 22 (Jammy) ARM64**:

   .. parsed-literal::

       sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu22-arm64-tiamat-gpg|\

       echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu22-arm64-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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


Install Salt on Ubuntu 20 (Focal)
=================================
To install Salt on Ubuntu 20 (Focal):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 20 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Ubuntu 20 (Focal)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-tiamat-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu20-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 20 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Ubuntu 20 (Focal)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu20-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 20 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Ubuntu 20 (Focal)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu20-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 20 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Ubuntu 20 (Focal)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu20-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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



Install Salt on Ubuntu 20 (Focal) ARM64
=======================================
To install Salt on Ubuntu 20 (Focal) ARM64:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 20 ARM64 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Ubuntu 20 (Focal) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-arm64-tiamat-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu20-arm64-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 20 ARM64 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Ubuntu 20 (Focal) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-arm64-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu20-arm64-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 20 ARM64 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Ubuntu 20 (Focal) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-arm64-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu20-arm64-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 20 ARM64 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Ubuntu 20 (Focal) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu20-arm64-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu20-arm64-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


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


Install Salt on Ubuntu 18 (Bionic)
==================================
To install Salt on Ubuntu 18 (Bionic):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 18 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Ubuntu 18 (Bionic)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu18-tiamat-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |ubuntu18-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Ubuntu 18 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Ubuntu 18 (Bionic)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu18-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu18-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 18 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Ubuntu 18 (Bionic)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu18-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu18-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Ubuntu 18 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Ubuntu 18 (Bionic)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |ubuntu18-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |ubuntu18-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


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

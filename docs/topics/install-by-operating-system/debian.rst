.. _install-debian:

======
Debian
======

These instructions explain how to install Salt on Debian operating systems:

* `Install Salt on Debian 11 (Bullseye)`_
* `Install Salt on Debian 11 (Bullseye) ARM64`_
* `Install Salt on Debian 10 (Buster)`_
* `Install Salt on Debian 9 (Stretch)`_


.. card:: Browse the repo for packages
    :link: https://repo.saltproject.io/py3/debian/
    :width: 50%

    :bdg-primary:`Debian`
    :bdg-secondary:`Python3`


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Debian 11 (Bullseye)
====================================
To install Salt on Debian 11 (Bullseye):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 11 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-tiamat-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 11 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Debian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian11-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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



Install Salt on Debian 11 (Bullseye) ARM64
==========================================
To install Salt on Debian 11 (Bullseye) ARM64:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 11 ARM64 (Tiamat)

           To pin your Salt upgrades to the latest :ref:`tiamat` package of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-tiamat-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |debian11-arm64-tiamat-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 11 ARM64 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |debian11-arm64-latest-download|\ " | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 11 ARM64 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |debian11-arm64-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 11 ARM64 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Debian 11 (Bullseye) ARM64**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-arm64-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=arm64] \ |debian11-arm64-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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



Install Salt on Debian 10 (Buster)
==================================
To install Salt on Debian 10 (Buster):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 10 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Debian 10 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 10 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Debian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian10-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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


Install Salt on Debian 9 (Stretch)
==================================
To install Salt on Debian 9 (Stretch):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Debian 9 (Latest)

           To pin your Salt upgrades to the :ref:`latest` package of Salt for **Debian 9 (Stretch)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian9-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian9-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 9 (Major)

           To pin your Salt upgrades to the latest :ref:`major` package of Salt for **Debian 9 (Stretch)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian9-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian9-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 9 (Minor)

           To pin your Salt upgrades to the latest :ref:`minor` package of Salt for **Debian 9 (Stretch)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian9-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] \ |debian9-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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

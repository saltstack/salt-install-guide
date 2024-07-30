.. _install-ubuntu:

======
Ubuntu
======

These instructions explain how to install Salt on Debian operating systems:

* `Install Salt on Ubuntu 24.04 (Noble) amd64`_
* `Install Salt on Ubuntu 24.04 (Noble) arm64`_
* `Install Salt on Ubuntu 22.04 (Jammy) amd64`_
* `Install Salt on Ubuntu 22.04 (Jammy) arm64`_
* `Install Salt on Ubuntu 20.04 (Focal) amd64`_
* `Install Salt on Ubuntu 20.04 (Focal) arm64`_

.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Ubuntu 24.04 (Noble) amd64
==========================================
To install the :ref:`onedir` packages of Salt on Ubuntu 24.04 (Noble) for
amd64 architecture:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 24.04 (Noble) (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Ubuntu 24.04 (Noble)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu24-major-gpg-amd64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] \ |ubuntu24-major-download-amd64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Ubuntu 24.04 (Noble) (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Ubuntu 24.04 (Noble)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu24-minor-gpg-amd64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] \ |ubuntu24-minor-download-amd64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst


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

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on Ubuntu 24.04 (Noble) arm64
======================================================
To install the :ref:`onedir` packages of Salt on Ubuntu 24.04 (Noble) for
arm64 architecture:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 24.04 (Noble) (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Ubuntu 24.04 (Noble)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu24-major-gpg-arm64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=arm64] \ |ubuntu24-major-download-arm64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Ubuntu 24.04 (Noble) (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Ubuntu 24.04 (Noble)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu24-minor-gpg-arm64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=arm64] \ |ubuntu24-minor-download-arm64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst


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

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on Ubuntu 22.04 (Jammy) amd64
==========================================
To install the :ref:`onedir` packages of Salt on Ubuntu 22.04 (Jammy) for
amd64 architecture:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 22.04 (Jammy) (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Ubuntu 22.04 (Jammy)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu22-major-gpg-amd64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] \ |ubuntu22-major-download-amd64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Ubuntu 22.04 (Jammy) (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Ubuntu 22.04 (Jammy)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu22-minor-gpg-amd64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] \ |ubuntu22-minor-download-amd64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst


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

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on Ubuntu 22.04 (Jammy) arm64
======================================================
To install the :ref:`onedir` packages of Salt on Ubuntu 22.04 (Jammy) for
arm64 architecture:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 22.04 (Jammy) (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Ubuntu 22.04 (Jammy)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu22-major-gpg-arm64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=arm64] \ |ubuntu22-major-download-arm64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Ubuntu 22.04 (Jammy) (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Ubuntu 22.04 (Jammy)**:

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu22-minor-gpg-arm64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=arm64] \ |ubuntu22-minor-download-arm64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst


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

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst



Install Salt on Ubuntu 20.04 (Focal) amd64
=====================================================
To install the :ref:`onedir` packages of Salt on Ubuntu 20.04 (Focal) for
amd64 architecture:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 20.04 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Ubuntu 20.04 (Focal)**:

           .. parsed-literal::

               mkdir /etc/apt/keyrings

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu20-major-gpg-amd64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] \ |ubuntu20-major-download-amd64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Ubuntu 20.04 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Ubuntu 20.04 (Focal)**:

           .. parsed-literal::

               mkdir /etc/apt/keyrings

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu20-minor-gpg-amd64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] \ |ubuntu20-minor-download-amd64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

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

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst


Install Salt on Ubuntu 20.04 (Focal) arm64
======================================================
To install the :ref:`onedir` packages of Salt on Ubuntu 20.04 (Focal) for
arm64 architecture:

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Ubuntu 20.04 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Ubuntu 20.04 (Focal)**:

           .. parsed-literal::

               mkdir /etc/apt/keyrings

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu20-major-gpg-arm64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=arm64] \ |ubuntu20-major-download-arm64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Ubuntu 20.04 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Ubuntu 20.04 (Focal)**:

           .. parsed-literal::

               mkdir /etc/apt/keyrings

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring-2023.gpg \ |ubuntu20-minor-gpg-arm64|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=arm64] \ |ubuntu20-minor-download-arm64|\" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: ../_includes/gpg-keys.rst

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

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst



Browse the repo
===============

.. card:: Browse the repo for Ubuntu packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/ubuntu/
    :width: 50%

    :bdg-primary:`Ubuntu`
    |supported-release-1-badge|

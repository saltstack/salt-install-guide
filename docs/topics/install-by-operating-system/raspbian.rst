.. _install-raspbian:

========
Raspbian
========

Raspbian uses the same packages as Debian systems. These instructions explain
how to install Salt on Raspbian operating systems:

* `Install onedir packages of Salt on Raspbian 11 (Bullseye)`_
* `Install onedir packages of Salt on Raspbian 10 (Buster)`_


.. card:: Browse the repo for Raspbian (Debian) packages
    :link: https://repo.saltproject.io/py3/debian/
    :width: 50%

    :bdg-primary:`Debian`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install onedir packages of Salt on Raspbian 11 (Bullseye)
=========================================================
To install the :ref:`onedir` packages of Salt on Raspbian 11 (Bullseye):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Raspbian 11 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Raspbian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-onedir-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |debian11-onedir-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 11 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Raspbian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-onedir-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |debian11-onedir-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 11 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Raspbian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian11-onedir-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |debian11-onedir-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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


Install onedir packages of Salt on Raspbian 10 (Buster)
=======================================================
To install the :ref:`onedir` packages of Salt on Raspbian 10 (Buster):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Raspbian 10 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Raspbian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-onedir-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |debian10-onedir-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 10 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Raspbian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-onedir-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |debian10-onedir-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 10 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Raspbian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |debian10-onedir-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |debian10-onedir-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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

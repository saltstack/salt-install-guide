.. _install-raspbian:

========
Raspbian
========

Raspbian uses the same packages as Debian systems. These instructions explain
how to install Salt on Raspbian operating systems:

* `Install classic packages of Salt on Raspbian 11 (Bullseye)`_
* `Install classic packages of Salt on Raspbian 10 (Buster)`_


.. card:: Browse the repo for Raspbian (Debian) packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/py3/debian/
    :width: 50%

    :bdg-primary:`Debian`
    :bdg-secondary:`Python3`


.. include:: ../_includes/what-is-onedir.rst

.. include:: ../_includes/intro-install-by-os.rst


Install classic packages of Salt on Raspbian 11 (Bullseye)
==========================================================
To install the :ref:`classic` packages of Salt on Raspbian 11 (Bullseye):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Raspbian 11 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **Raspbian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |raspbian11-classic-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |raspbian11-classic-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 11 (Major classic)

           To pin your Salt upgrades to the :ref:`major` :ref:`classic` package
           of Salt for **Raspbian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |raspbian11-classic-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |raspbian11-classic-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 11 (Minor classic)

           To pin your Salt upgrades to the :ref:`minor` :ref:`classic` package
           of Salt for **Raspbian 11 (Bullseye)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |raspbian11-classic-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |raspbian11-classic-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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


Install classic packages of Salt on Raspbian 10 (Buster)
========================================================
To install the :ref:`classic` packages of Salt on Raspbian 10 (Buster):

#. Run the following commands to import the Salt Project repository key, and to
   create the apt sources list file:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Raspbian 10 (Latest classic)

           To pin your Salt upgrades to the :ref:`latest` :ref:`classic` package
           of Salt for **Raspbian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |raspbian10-classic-latest-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |raspbian10-classic-latest-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 10 (Major classic)

           To pin your Salt upgrades to the :ref:`major` :ref:`classic` package
           of Salt for **Raspbian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |raspbian10-classic-major-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |raspbian10-classic-major-download|\" | sudo tee /etc/apt/sources.list.d/salt.list


       .. tab-item:: Raspbian 10 (Minor classic)

           To pin your Salt upgrades to the :ref:`minor` :ref:`classic` package
           of Salt for **Raspbian 10 (Buster)**:

           .. parsed-literal::

               sudo curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg \ |raspbian10-classic-minor-gpg|\

               echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=armhf] \ |raspbian10-classic-minor-download|\" | sudo tee /etc/apt/sources.list.d/salt.list

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

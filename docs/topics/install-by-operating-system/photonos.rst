.. _install-photonos:

=========
Photon OS
=========

These instructions explain how to install Salt on Photon OS operating systems.

.. card:: Browse the repo for Photon OS packages
    :link: https://repo.saltproject.io/py3/
    :width: 50%

    :bdg-primary:`Photon OS`
    :bdg-secondary:`Python3`


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Photon OS 3
============================
To install Salt on Photon OS 3:

#. Run the following commands to install the Salt Project repository and pin
   your Salt upgrades to the latest :ref:`tiamat` package of Salt for
   **Photon OS 3.0**:

   .. parsed-literal::

       sudo rpm --import \ |photonos3-tiamat-gpg|\

       curl -fsSL \ |photonos3-tiamat-download|\  | sudo tee /etc/yum.repos.d/salt.repo

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

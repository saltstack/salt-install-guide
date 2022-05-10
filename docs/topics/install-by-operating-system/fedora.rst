.. _install-fedora:

======
Fedora
======

These instructions explain how to install Salt on Fedora operating systems.

.. Note::
    Fedora packages are available in the standard Fedora repositories. When you
    install on Fedora, it always installs the latest release. Updating
    installs the latest release even if it is a new major version.


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Fedora
======================
To install Salt on Fedora:

#. Using the packages on the Fedora repository, install the salt-minion,
   salt-master, or other Salt components:

   .. code-block:: bash

       sudo dnf install salt-master
       sudo dnf install salt-minion
       sudo dnf install salt-ssh
       sudo dnf install salt-syndic
       sudo dnf install salt-cloud
       sudo dnf install salt-api


#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api


After installing Salt on Fedora, you need to complete the following
post-installation steps:

* :ref:`configure-master-minion`
* :ref:`accept-keys`
* :ref:`verify-install`

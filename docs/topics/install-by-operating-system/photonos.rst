.. _install-photonos:

=========
Photon OS
=========

These instructions explain how to install Salt on Photon OS operating systems.

.. Note::
    Salt packages for Photon OS are hosted on the Photon OS package repository.
    Photon OS creates its own Salt packages and the Salt Project does not
    publish separate Salt packages for download.


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Photon OS 3
===========================
To install Salt on Photon OS 3:

#. Create the Photon environment and run this command to update the system:

   .. code-block:: bash

       sudo tdnf update

#. Run this command to check whether the latest Salt release is available:

   .. code-block:: bash

       sudo tdnf list salt3

   This command returns a list of available Salt versions for Photon OS.

#. Install packages from the Photon OS repository, such as the salt-minion,
   salt-master, or other Salt components:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Photon OS 3 (Latest)

           To install the latest release of Salt packages that are available in
           the Photon OS repository, run these commands:

           .. code-block:: bash

               sudo tdnf install salt3-master
               sudo tdnf install salt3-minion
               sudo tdnf install salt3-ssh
               sudo tdnf install salt3-syndic
               sudo tdnf install salt3-cloud
               sudo tdnf install salt3-api


       .. tab-item:: Photon OS 3 (Specific releases)

           The following is an example of how to install a specific release of
           Salt based on the list of packages available in the Photon OS
           repository:

           .. code-block:: bash

               sudo tdnf install salt3-master-3005-1.ph3
               sudo tdnf install salt3-minion-3005-1.ph3
               sudo tdnf install salt3-ssh-3005-1.ph3
               sudo tdnf install salt3-syndic-3005-1.ph3
               sudo tdnf install salt3-cloud-3005-1.ph3
               sudo tdnf install salt3-api-3005-1.ph3

           .. Note::
               The file extensions are based on which version of Photon OS you
               are installing Salt services on. For example, the extension for
               Photon OS 3 is ``.ph3`` and the extension for Photon OS 4 is
               ``.ph4``.


#. Enable and start the services for salt-minion, salt-master, or other Salt
   components:

   .. code-block:: bash

       sudo systemctl enable salt-master && sudo systemctl start salt-master
       sudo systemctl enable salt-minion && sudo systemctl start salt-minion


.. include:: ../_includes/post-install-by-os.rst

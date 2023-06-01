.. _install-photonos:

=========
Photon OS
=========

These instructions explain how to install Salt on Photon OS operating systems.

* `Install Salt on Photon OS 4`_
* `Install Salt on Photon OS 3`_

.. card:: Browse the repo for Photon OS packages
    :class-card: sd-border-1
    :link: https://repo.saltproject.io/salt/py3/photon/
    :width: 50%

    :bdg-primary:`Photon OS`
    |supported-release-1-badge|

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Photon OS 4
===========================
To install Salt on Photon OS 4:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Photon OS 4 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Photon OS 4**:

           .. parsed-literal::

               sudo rpm --import \ |photonos4-latest-gpg|\

               curl -fsSL \ |photonos4-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

               tdnf clean all

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Photon OS 4 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Photon OS 4**:

           .. parsed-literal::

               sudo rpm --import \ |photonos4-major-gpg|\

               curl -fsSL \ |photonos4-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

               tdnf clean all

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Photon OS 4 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Photon OS 4**:

           .. parsed-literal::

               sudo rpm --import \ |photonos4-minor-gpg|\

               curl -fsSL \ |photonos4-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

               tdnf clean all

           .. include:: ../_includes/gpg-keys.rst

#. Install packages from the Photon OS repository, such as the salt-minion,
   salt-master, or other Salt components:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Photon OS 4 (Latest)

           To install the latest release of Salt packages that are available in
           the Photon OS repository, run these commands:

           .. code-block:: bash

               sudo tdnf install salt-master
               sudo tdnf install salt-minion
               sudo tdnf install salt-ssh
               sudo tdnf install salt-syndic
               sudo tdnf install salt-cloud
               sudo tdnf install salt-api


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
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst



Install Salt on Photon OS 3
===========================
To install Salt on Photon OS 3:

#. Run the following commands to install the Salt Project repository and key:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Photon OS 3 (Latest onedir)

           To pin your Salt upgrades to the :ref:`latest` :ref:`onedir` package
           of Salt for **Photon OS 3**:

           .. parsed-literal::

               sudo rpm --import \ |photonos3-latest-gpg|\

               curl -fsSL \ |photonos3-latest-download|\  | sudo tee /etc/yum.repos.d/salt.repo

               tdnf clean all

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Photon OS 3 (Major onedir)

           To pin your Salt upgrades to the :ref:`major` :ref:`onedir` package
           of Salt for **Photon OS 3**:

           .. parsed-literal::

               sudo rpm --import \ |photonos3-major-gpg|\

               curl -fsSL \ |photonos3-major-download|\  | sudo tee /etc/yum.repos.d/salt.repo

               tdnf clean all

           .. include:: ../_includes/gpg-keys.rst

       .. tab-item:: Photon OS 3 (Minor onedir)

           To pin your Salt upgrades to the :ref:`minor` :ref:`onedir` package
           of Salt for **Photon OS 3**:

           .. parsed-literal::

               sudo rpm --import \ |photonos3-minor-gpg|\

               curl -fsSL \ |photonos3-minor-download|\  | sudo tee /etc/yum.repos.d/salt.repo

               tdnf clean all

           .. include:: ../_includes/gpg-keys.rst

#. Install packages from the Photon OS repository, such as the salt-minion,
   salt-master, or other Salt components:

   **Click the tab for the Salt version you would like to pin for updates:**

   .. tab-set::

       .. tab-item:: Photon OS 3 (Latest)

           To install the latest release of Salt packages that are available in
           the Photon OS repository, run these commands:

           .. code-block:: bash

               sudo tdnf install salt-master
               sudo tdnf install salt-minion
               sudo tdnf install salt-ssh
               sudo tdnf install salt-syndic
               sudo tdnf install salt-cloud
               sudo tdnf install salt-api


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
       sudo systemctl enable salt-syndic && sudo systemctl start salt-syndic
       sudo systemctl enable salt-api && sudo systemctl start salt-api

   .. include:: ../_includes/install-dependencies-onedir.rst

.. include:: ../_includes/post-install-by-os.rst

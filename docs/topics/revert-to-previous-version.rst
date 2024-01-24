.. _revert-to-previous-version:

====================================
Revert to a previous version of Salt
====================================

This documentation explains how to revert to a previous version of Salt on these
operating systems:

* `Revert Salt on Debian/Ubuntu operating systems`_
* `Revert Salt on RedHat operating systems`_


Revert Salt on Debian/Ubuntu operating systems
==============================================
To revert to a previous version of Salt:

#. Verify the version of Salt you are running. For example:

   .. code-block:: bash

       salt-call --local test.versions
       salt minion test.version
       salt-run --versions-report

   Example output:

   .. code-block:: bash

       minion:
           3006.5

#. Run the following command to overwrite the ``salt.list`` file and pin your
   version of Salt to a previous minor version, replacing the ``X`` in this
   example with the desired previous version number:

   .. tab-set::

       .. tab-item:: Debian 12

           .. code-block:: bash

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] https://repo.saltproject.io/salt/py3/debian/12/amd64/minor/3006.X bookworm main" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: _includes/previous-version-note.rst

       .. tab-item:: Debian 11

           .. code-block:: bash

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] https://repo.saltproject.io/salt/py3/debian/11/amd64/minor/3006.X bullseye main" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: _includes/previous-version-note.rst

       .. tab-item:: Debian 10

           .. code-block:: bash

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] https://repo.saltproject.io/salt/py3/debian/10/amd64/minor/3006.X buster main" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: _includes/previous-version-note.rst


       .. tab-item:: Ubuntu 22.04

           .. code-block:: bash

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] https://repo.saltproject.io/salt/py3/ubuntu/22.04/amd64/minor/3006.X jammy main" | sudo tee /etc/apt/sources.list.d/salt.list


           .. include:: _includes/previous-version-note.rst


       .. tab-item:: Ubuntu 20.04

           .. code-block:: bash

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring-2023.gpg arch=amd64] https://repo.saltproject.io/salt/py3/ubuntu/20.04/amd64/minor/3006.X focal main" | sudo tee /etc/apt/sources.list.d/salt.list

           .. include:: _includes/previous-version-note.rst


#. Run the following command to change your version of Salt and remove all Salt
   services:

   .. code-block:: bash

       apt remove salt-common


#. Run the following commands to update your package manager and install any of
   the Salt services as needed:

   .. code-block:: bash

       apt update
       apt-get install salt-master
       apt-get install salt-minion
       apt-get install salt-ssh
       apt-get install salt-syndic
       apt-get install salt-cloud
       apt-get install salt-api

#. Verify the version of Salt you are running to ensure you are on the previous
   version. For example:

   .. code-block:: bash

       salt-call test.version
       salt minion test.version
       salt-run --versions-report



Revert Salt on RedHat operating systems
=======================================
To revert to a previous version of Salt:

#. Verify the version of Salt you are running. For example:

   .. code-block:: bash

       salt-call --local test.versions
       salt minion test.version
       salt-run --versions-report

   Example output:

   .. code-block:: bash

       minion:
           3006.5

#. Run the following command to overwrite the ``salt.list`` file and pin your
   version of Salt to a previous minor version, replacing the ``X`` in this
   example with the desired previous version number:

   .. tab-set::

       .. tab-item:: RHEL 9

           .. code-block:: bash

               curl -fsSL https://repo.saltproject.io/salt/py3/redhat/9/x86_64/minor/3006.X.repo | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: _includes/previous-version-note.rst

       .. tab-item:: RHEL 8

           .. code-block:: bash

               curl -fsSL https://repo.saltproject.io/salt/py3/redhat/8/x86_64/minor/3006.X.repo | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: _includes/previous-version-note.rst

       .. tab-item:: RHEL 7

           .. code-block:: bash

               curl -fsSL https://repo.saltproject.io/salt/py3/redhat/7/x86_64/minor/3006.X.repo | sudo tee /etc/yum.repos.d/salt.repo

           .. include:: _includes/previous-version-note.rst

#. Run the following command to change your version of Salt and remove all Salt
   services:

   .. code-block:: bash

       yum remove salt

#. Update your package manager and install any of the Salt services as needed:

   .. code-block:: bash

       yum makecache
       yum install salt-master
       yum install salt-minion
       yum install salt-ssh
       yum install salt-syndic
       yum install salt-cloud
       yum install salt-api

#. Restart the salt services:

   .. code-block:: bash

       systemctl restart salt-master
       systemctl restart salt-minion
       systemctl restart salt-ssh
       systemctl restart salt-syndic
       systemctl restart salt-cloud
       systemctl restart salt-api

#. Verify the version of Salt you are running to ensure you are on the previous
   version. For example:

   .. code-block:: bash

       salt-call --local test.versions
       salt minion test.version
       salt-run --versions-report

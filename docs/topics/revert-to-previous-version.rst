.. _revert-to-previous-version:

====================================
Revert to a previous version of Salt
====================================

This documentation explains how to revert to a previous version of Salt on these
operating systems:

* `Revert Salt on Debian/Ubuntu operating systems`_
* `Revert Salt on RedHat operating systems`_

.. warning::

    Salt package repositories do not host versions of Salt older than 3006 LTS. This
    means users will **NOT** be able to revert to older versions such as Salt 3005.

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

#. If needed, first run the following command to restrict to target LTS or STS available packages:

   .. tab-set::

       .. tab-item:: 3006 LTS

           Populate ``/etc/apt/preferences.d/salt-pin-1001`` in order to restrict upgrades to Salt 3006.x LTS:

           .. code-block:: bash

               echo 'Package: salt-*
               Pin: version 3006.*
               Pin-Priority: 1001' | sudo tee /etc/apt/preferences.d/salt-pin-1001

           .. include:: _includes/previous-version-note.rst

       .. tab-item:: 3007 STS

           .. warning:: STS not recommended for Production

               Salt Project recommends deploying LTS releases for Production environments.

           Populate ``/etc/apt/preferences.d/salt-pin-1001`` in order to restrict upgrades to Salt 3006.x LTS:

           .. code-block:: bash

               echo 'Package: salt-*
               Pin: version 3007.*
               Pin-Priority: 1001' | sudo tee /etc/apt/preferences.d/salt-pin-1001

           .. include:: _includes/previous-version-note.rst


#. Run the following commands to remove all Salt services:

   .. code-block:: bash

       apt-get remove salt-common
       apt-get remove salt-master
       apt-get remove salt-minion
       apt-get remove salt-ssh
       apt-get remove salt-syndic
       apt-get remove salt-cloud
       apt-get remove salt-api


#. Run the following commands to update your package manager and install any of
   the Salt services as needed:

   .. code-block:: bash

       apt-get update
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

#. If needed, first run the following command to restrict to target LTS or STS available packages:

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

       dnf remove salt

#. Update your package manager and install any of the Salt services as needed:

   .. code-block:: bash

       dnf makecache
       dnf install salt-master
       dnf install salt-minion
       dnf install salt-ssh
       dnf install salt-syndic
       dnf install salt-cloud
       dnf install salt-api

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

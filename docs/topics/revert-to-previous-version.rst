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

   .. parsed-literal::

       minion:
           |minor-one-version|


#. Run the following commands to remove all Salt services:

   .. code-block:: bash

       apt-get remove salt-common
       apt-get remove salt-master
       apt-get remove salt-minion
       apt-get remove salt-ssh
       apt-get remove salt-syndic
       apt-get remove salt-cloud
       apt-get remove salt-api

#. Refer to the install directions, and restrict to target LTS or STS available packages via :ref:`install-deb`

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

   .. parsed-literal::

       minion:
           |minor-one-version|

#. Run the following command to change your version of Salt and remove all Salt
   services:

   .. code-block:: bash

       dnf remove salt

#. Refer to the install directions, and restrict to target LTS or STS available packages via :ref:`install-rpm`

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

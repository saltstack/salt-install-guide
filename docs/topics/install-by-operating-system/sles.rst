.. _install-sles:

===========
SUSE (SLES)
===========

These instructions explain how to install Salt on AR operating
systems:

.. Note::
    Salt packages for SUSE are hosted on the SUSE package repository. SUSE
    creates its own Salt packages and the Salt Project does not publish separate
    Salt packages for download.


.. include:: ../_includes/intro-install-by-os.rst


Install the stable release of Salt on SUSE
==========================================
Salt is packaged separately for the minion and the master. You only need to
install the appropriate package for the machine's role. Typically, there will be
one master and multiple minions.

#. Run the following command:

   .. code-block:: bash

       zypper install salt-master
       zypper install salt-minion

#. To start the master service:

   .. tab-set::

       .. tab-item:: Open SUSE

           .. code-block:: bash

               systemctl start salt-master.service

           Alternatively, to start the master service at boot time:

           .. code-block:: bash

               systemctl enable salt-master.service

       .. tab-item:: SLES

           .. code-block:: bash

               rcsalt-master start

           Alternatively, to start the master service at boot time:

           .. code-block:: bash

               chkconfig salt-master on


#. To start the minion service:

   .. tab-set::

       .. tab-item:: Open SUSE

           .. code-block:: bash

               systemctl start salt-minion.service

           Alternatively, to start the minion service at boot time:

           .. code-block:: bash

               systemctl enable salt-minion.service

       .. tab-item:: SLES

           .. code-block:: bash

               chkconfig salt-minion on

           Alternatively, to start the minion service at boot time:

           .. code-block:: bash

               rcsalt-minion start


.. include:: ../_includes/post-install-by-os.rst

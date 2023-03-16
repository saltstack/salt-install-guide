.. _install-freebsd:

=======
FreeBSD
=======

Salt is available in the FreeBSD ports tree at
`sysutils/py-salt <https://www.freshports.org/sysutils/py-salt/>`_.

These instructions explain how to install Salt on AR operating
systems:

* `Install Salt on FreeBSD`_
* `Install Salt from FreeBSD ports`_

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on FreeBSD
=======================
To install the stable release of Salt from the official package repository:

#. Check which version is the default version of Python for Salt on
   FreeBSD. See :ref:`salt-python-version-support` for more information.

#. Run the following command, substituting the version of Python as needed. For
   example, to install for Python 3.8:

   .. code-block:: bash

       pkg install py38-salt

#. To activate the master in ``/etc/rc.conf``:

   .. code-block:: bash

       sysrc salt_master_enable="YES"

#. To start the master service:

   .. code-block:: bash

       service salt_master start

#. To activate the minion in ``/etc/rc.conf``:

   .. code-block:: bash

       sysrc salt_minion_enable="YES"

#. To start the minion service:

   .. code-block:: bash

       service salt_minion start


.. include:: ../_includes/post-install-by-os.rst


Install Salt from FreeBSD ports
===============================
To install from FreeBSD ports:

#. Run the following commands:

   .. code-block:: bash

       cd /usr/ports/sysutils/py-salt
       make install

   .. Note::

       Python 3.7 can be used by setting default Python version to 3.7:
       ``echo "DEFAULT_VERSIONS+= python=3.7" >> /etc/make.conf``

.. include:: ../_includes/post-install-by-os.rst

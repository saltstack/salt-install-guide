.. _install-index:

============
Install Salt
============

This section contains instructions to install Salt. If you are setting up your
environment for the first time, you should install a Salt master on a dedicated
management server or VM, and then install a Salt minion on each system that you
want to manage using Salt. For now you don't need to worry about your
architecture, you can easily add components and modify your configuration later
without needing to reinstall anything.

The general installation process is as follows:

#. Install a Salt master using the instructions for your platform or by running
   the Salt bootstrap script. If you use the bootstrap script, be sure to
   include the ``-M`` option to install the Salt master.
#. Make sure that your Salt minions can find the Salt master.
#. Install the Salt minion on each system that you want to manage.
#. Accept the Salt minion keys after the Salt minion connects.

After this, you should be able to run a simple command and receive salt version
returns from all connected Salt minions.

.. code-block:: bash

   salt '*' test.version

Install directions per OS
=========================

.. toctree::
   :maxdepth: 2
   :glob:

   *
   native/index

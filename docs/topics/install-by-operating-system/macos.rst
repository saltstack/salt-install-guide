.. _install-macos:

=====
macOS
=====

This page provides download files and instructions for installing Salt on macOS.


macOS downloads
===============

.. include:: ../_includes/macos-downloads.rst


.. card:: Browse the repo for macOS packages
    :link: https://repo.saltproject.io/salt/py3/macos
    :width: 50%

    :bdg-primary:`macOS`
    |supported-release-1-badge|


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on macOS
=====================

#. Download the Salt installation file for macOS. See `macOS downloads`_ for a
   list of the latest downloads.

   .. Warning::
       `OS X Gatekeeper settings <https://support.apple.com/en-us/HT202491>`_
       may prevent installation of the Salt package. If a warning appears during
       installation, open **System Preferences > Security & Privacy** and click
       **Open Anyway**.

#. Run the file to install Salt.

#. After installation, configure the Salt minion ID, and the Salt master
   location, replacing the placeholder text with custom information:

   .. code-block:: bash

       sudo salt-config -i yourminionname -m yoursaltmaster

   .. Tip::
       See :ref:`configure-master-minion` for more configuration options.

#. Start the minion service. The commands to start and stop services are
   different for macOS than other operating systems.

   To start the minion service:

   .. code-block:: bash

       sudo launchctl start com.saltstack.salt.minion

   To stop the minion service:

   .. code-block:: bash

       sudo launchctl stop com.saltstack.salt.minion


After installing Salt on macOS, you need to complete the following
post-installation steps:

* :ref:`accept-keys`
* :ref:`verify-install`

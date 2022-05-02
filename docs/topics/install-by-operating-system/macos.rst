.. _install-macos:

=====
macOS
=====

This page provides download files and instructions for installing Salt on macOS.


macOS downloads
===============

.. card:: Browse the repo for packages
    :link: https://repo.saltproject.io/osx/
    :width: 50%

    :bdg-primary:`macOS`
    :bdg-secondary:`Python3`


.. list-table::
  :widths: 10 10 10 40 10 10
  :header-rows: 1
  :class: checkmarks

  * - OS
    - Arch
    - File Type
    - Download
    - MD5
    - SHA256

  * - macOS
    - x86_64
    - pkg
    - `salt-3004.1-1-py3-x86_64.pkg <https://repo.saltproject.io/osx/salt-3004.1-1-py3-x86_64.pkg>`_
    - `MD5 <https://repo.saltproject.io/osx/salt-3004.1-1-py3-x86_64.pkg.md5>`_
    - `SHA265 <https://repo.saltproject.io/osx/salt-3004.1-1-py3-x86_64.pkg.sha256>`_


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

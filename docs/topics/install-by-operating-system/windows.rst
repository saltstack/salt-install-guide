.. _install-windows:

=======
Windows
=======

This page provides download files and instructions for installing Salt on
Windows.


Windows downloads
=================

.. include:: ../_includes/windows-downloads.rst

.. card:: Browse the repo for Windows packages
    :link: https://repo.saltproject.io/windows/
    :width: 50%

    :bdg-primary:`Windows`
    :bdg-secondary:`Python3`


.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Windows
=======================

#. Download the Salt installation file for Windows. See `Windows downloads`_ for
   a list of the latest downloads.

#. Run the file to install Salt. You can optionally run the file in silent mode:

   .. tab-set::

       .. tab-item:: EXE silent install

           You can run the installer silently by providing the ``/S`` option at
           the command line. Use the ``/master`` and ``/minion-name`` options
           to configure the master hostname and minion name, respectively.

           The following is an example of running a silent installation from the
           command line:

           .. code-block:: bash

               Salt-Minion-3004.1-1-Py3-AMD64-Setup.exe /S /master=yoursaltmaster /minion-name=yourminionname

       .. tab-item:: MSI silent install

           You can run the installer silently by providing the ``/quiet`` and
           ``/norestart`` option at the command line. Use the ``MASTER`` and
           ``MINION_ID`` options to configure the master hostname and minion
           name, respectively.

           The following is an example of running a silent installation from the
           command line:

           .. code-block:: bash

               msiexec /i Salt-Minion-3004.1-1-Py3-AMD64.msi /quiet /norestart MASTER=yoursaltmaster MINION_ID=yourminionname


.. include:: ../_includes/post-install-by-os.rst

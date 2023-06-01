.. _install-arch:

==========
Arch Linux
==========

Salt (stable) is available through the Arch Linux Official repositories. You can
also get ``-git`` packages in the Arch User repositories (AUR) as well.

These instructions explain how to install Salt on Arch operating systems:

* `Install Salt on Arch Linux`_

.. include:: ../_includes/intro-install-by-os.rst


Install Salt on Arch Linux
==========================
To install the stable release of Salt on Arch Linux:

#. Run the following command:

   .. code-block:: bash

       pacman -S salt

#. To activate the master or minion using ``systemctl``:

   .. code-block:: bash

       systemctl enable salt-master.service
       systemctl enable salt-minion.service

#. To start the master service using ``systemctl``:

   .. code-block:: bash

       systemctl start salt-master

   .. include:: ../_includes/install-dependencies-onedir.rst


.. include:: ../_includes/post-install-by-os.rst

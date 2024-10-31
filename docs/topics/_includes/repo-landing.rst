.. div:: landing-title

    .. grid::
        :reverse:
        :gutter: 2 3 3 3
        :margin: 4 4 1 2

        .. grid-item::
            :columns: 12 3 3 3
            :class: sd-m-auto sd-animate-grow50-rot20

            .. image:: /_static/img/repo-landing-small.png
              :width: 125
              :alt: Salt Project install guide logo

        .. grid-item::
            :columns: 12 9 9 9
            :class: sd-text-white sd-fs-2 sd-text-center

            The Salt install guide

            .. button-link:: https://docs.saltproject.io/en/master/topics/tutorials/walkthrough.html
               :color: light
               :align: center
               :outline:

                New to Salt? Try this tutorial

=======
Welcome
=======

Welcome to the Salt install guide! This guide provides instructions for
installing Salt on :ref:`salt-supported-operating-systems`. It also explains
how to configure Salt, start Salt services, and verify your installation.

Note that the Salt Project has phased out classic package builds for supported
operating systems for 3006 and later. Update your Salt infrastructure to the new
onedir packages as soon as possible. See :ref:`upgrade-to-onedir` for
instructions.

Install Salt
============

.. grid:: 3

    .. grid-item::

        .. button-link:: topics/overview.html
           :color: primary
           :expand:

           Install overview :octicon:`arrow-up-right`

    .. grid-item::

        .. button-link:: topics/bootstrap.html
           :color: primary
           :expand:

           Bootstrap install :octicon:`arrow-up-right`

    .. grid-item::

        .. button-link:: topics/salt-supported-operating-systems.html
           :color: primary
           :expand:

           Supported systems :octicon:`arrow-up-right`

Quick install by operating system
=================================

Operating systems are listed in alphabetical order:

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: Linux (DEB)
       :class-card: sd-border-1
       :link: topics/install-by-operating-system/linux-deb.html

       :bdg-primary:`Debian-like Systems`

    .. grid-item-card:: Linux (RPM)
       :class-card: sd-border-1
       :link: topics/install-by-operating-system/linux-rpm.html

       :bdg-primary:`RHEL-like systems`

    .. grid-item-card:: macOS
       :class-card: sd-border-1
       :link: topics/install-by-operating-system/macos.html

       :bdg-primary:`pkg`

    .. grid-item-card:: Windows
       :class-card: sd-border-1
       :link: topics/install-by-operating-system/windows.html

       :bdg-primary:`exe`
       :bdg-secondary:`msi`

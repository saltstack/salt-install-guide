.. _install-release-candidate:

===========================
Install a release candidate
===========================

You can make an important contribution to the Salt Project by installing and
testing release candidates (RCs) of Salt when they are made available prior to a
release. Testing the RC and reporting any bugs or performance issues helps
ensure code quality and minimizes disruptions to service when Salt users upgrade
their Salt infrastructure.

.. dropdown:: What is a release candidate (RC)?
    :color: primary

    Release candidates are early versions of Salt that are released prior to an
    official Salt release.


Report bugs
===========
To report any bugs you find while testing a release candidate, open an issue on
the `Salt repository on GitHub <https://github.com/saltstack/salt/issues/new?assignees=&labels=Bug%2C+needs-triage&template=bug_report.md&title=%5BBUG%5D>`_
and write ``[RC]`` in the issue title. For example:
``[RC][BUG] Description of bug``.


Install using packages
======================

RC builds are available in the Salt package repositories.

To install release candidate packages:

#. Use the standard minor install instructions for your operating system. See
   :ref:`install-by-operating-system-index`.

#. On the step where you normally enable / restrict to an LTS or STS version,
   restrict to RC: **TBD**

   To install the latest RC, run the following commands:

   .. tab-set::

       .. tab-item:: Linux (RPM)

            TBD

       .. tab-item:: Linux (DEB)

            TBD

       .. tab-item:: Windows

            The following are URLs for the latest release candidate:

            .. include:: ../_includes/windows-downloads-rc.rst

            Download the installer that matches your operating system.
            Double-click the installer to install Salt. You can also install the
            release candidate from the command line using various switches.
            Those can be found by running the ``.exe`` installer with the ``/?``
            option.

            .. parsed-literal::

                |windows-release-candidate-amd64-exe-file-name| /?

            For options for the ``.msi`` installer, see the documentation
            `here <https://docs.saltproject.io/salt/install-guide/en/latest/topics/install-by-operating-system/windows.html#windows-msi-install-options>`__.


Install using bootstrap
=======================
You can install a release candidate of Salt using one of the scripts in the
`Salt bootstrap <https://github.com/saltstack/salt-bootstrap/>`_ project.

.. tab-set::

    .. tab-item:: Linux

        TBD

    .. tab-item:: Windows

        TBD


Install using pip
=================
To install the release candidate using pip from `PyPi <https://pypi.org/>`_:

#. Install the build dependencies:

   To pip install the latest RC release:

   .. tab-set::

       .. tab-item:: RHEL systems

           Run the following commands:

           .. code-block:: bash

               sudo dnf install python3-pip python3-devel gcc gcc-c++

       .. tab-item:: Debian systems

           Run the following commands:

           .. code-block:: bash

               sudo apt-get install python3-pip python3-dev gcc g++

       .. tab-item:: Other systems

           Install:

           * pip
           * Python header libraries
           * C and C++ compilers

       .. tab-item:: Windows

           There are 3 requirements for Salt on Windows:

           * Python (3.10+)
           * VC Redistributable
             - 2013 for Salt 3006.x and below
             - 2022 for Salt 3007.x and above
           * Visual Studio Build Tools

           Install a compatible version of Python and the corresponding version
           of VC Redistributable for the version of Salt you want to install.

           Salt dependencies require Visual Studio Build tools to compile
           properly. The easiest way to install the build tools is with the
           ``install_vs_buildtools.ps1`` powershell script in the Salt repo.
           Run the following command to download and run this script:

           .. parsed-literal::

               Set-ExecutionPolicy RemoteSigned -Scope Process -Force
               [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]'Tls12'
               Invoke-WebRequest -Uri |windows-vs-buildtools-script| -OutFile .\\install_vs_buildtools.ps1
               .\\install_vs_buildtools.ps1

#. Install Salt using the following command:

   .. tab-set::

       .. tab-item:: Linux

           .. code-block:: bash

               sudo pip install salt==$rc_tag_version

       .. tab-item:: Windows

           .. code-block:: pwsh

               pip install salt==$rc_tag_version

   To pip install the latest RC release, using |release-candidate-version| as an
   example:

   .. tab-set::

       .. tab-item:: Linux/macOS

           .. parsed-literal::

               sudo |pip-install-release-candidate|

       .. tab-item:: Windows

           .. parsed-literal::

               |pip-install-release-candidate|

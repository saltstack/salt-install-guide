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
    official Salt release. For LTS releases of Salt, the Salt Project releases
    two RCs in the months leading up to the official LTS release.


Report bugs
===========
To report any bugs you find while testing a release candidate, open an issue on
the `Salt repository on GitHub <https://github.com/saltstack/salt/issues/new?assignees=&labels=Bug%2C+needs-triage&template=bug_report.md&title=%5BBUG%5D>`_
and write ``[RC]`` in the issue title. For example:
``[RC][BUG] Description of bug``.


Install using packages
======================
RC builds for a few major platforms are available at the Salt repository:
https://staging.repo.saltproject.io/salt_rc/

RC builds are typically only available for the latest version of the operating
system at the time the RC is available. Older versions of operating systems
might not get an RC release.

To install release candidate packages:

#. Use the standard minor install instructions for your operating system. See
   :ref:`install-by-operating-system-index`.

#. On the step where you normally import the Salt Project repository key and pin
   the package to a specific version of Salt, insert ``staging`` before ``repo.saltproject.io``
   and ``salt_rc/`` into the URL between the hostname and the remainder of the file path.

   .. Note::
       The gpg key for the 3006.0 release is now named: SALT-PROJECT-GPG-PUBKEY-2023


   For example, for the Salt 3006.0 RC 1, run the following commands:

   .. tab-set::

       .. tab-item:: RHEL 9

           .. parsed-literal::

               sudo rpm --import \ |rhel9-onedir-relenv-gpg|\

               curl -fsSL https://staging.repo.saltproject.io/salt_rc/salt/py3/redhat/9/x86_64/minor/3006.0rc1.repo | sudo tee /etc/yum.repos.d/salt.repo

               echo 'baseurl=https://staging.repo.saltproject.io/salt_rc/salt/py3/redhat/$releasever/$basearch/minor/3006.0rc1' | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: Ubuntu 22.04 (Jammy)

           .. parsed-literal::

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring.gpg \ |ubuntu22-onedir-relenv-gpg|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring.gpg] https://staging.repo.saltproject.io/salt_rc/salt/py3/ubuntu/22.04/amd64/minor/3006.0rc1 jammy main" | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 11 (Bullseye)

           .. parsed-literal::

               sudo mkdir /etc/apt/keyrings

               sudo curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring.gpg |debian11-onedir-relenv-gpg|\

               echo "deb [signed-by=/etc/apt/keyrings/salt-archive-keyring.gpg] https://staging.repo.saltproject.io/salt_rc/salt/py3/debian/11/amd64/minor/3006.0rc1 bullseye main" | sudo tee --append /etc/apt/sources.list.d/salt.list


Install using bootstrap
=======================
You can install a release candidate of Salt using the
`Salt bootstrap <https://github.com/saltstack/salt-bootstrap/>`_ script.

For example for the 3006.0 RC1 release:

.. code-block:: bash

    curl -o install_salt.sh -L https://bootstrap.saltproject.io
    sudo sh install_salt.sh -P -x python3 git v3006.0rc1

To install a master using Salt bootstrap, use the `-M` flag:

.. code-block:: bash

    curl -o install_salt.sh -L https://bootstrap.saltproject.io
    sudo sh install_salt.sh -P -M -x python3 git v3006.0rc1

If you want to install only a master and not a minion using Salt bootstrap, use
the `-M`` and `-N` flags:

.. code-block:: bash

    curl -o install_salt.sh -L https://bootstrap.saltproject.io
    sudo sh install_salt.sh -P -M -N -x python3 git v3006.0rc1


Install using pip
=================
To install the release candidate using pip from `PyPi <https://pypi.org/>`_:

#. Install the build dependencies:

   For example, for the Salt 3006.0 RC 1:

   .. tab-set::

       .. tab-item:: RHEL systems

           Run the following commands:

           .. code-block:: bash

               sudo yum install python-pip python-devel gcc gcc-c++

       .. tab-item:: Debian systems

           Run the following commands:

           .. code-block:: bash

               sudo apt-get install python-pip python-dev gcc g++

       .. tab-item:: Other systems

           Install:

           * pip
           * Python header libraries
           * C and C++ compilers


#. Install Salt using the following command:

   .. code-block:: bash

       sudo pip install salt==$rc_tag_version

   For example, to install the 3006.0 RC1 release:

   .. code-block:: bash

       sudo pip install salt==3006.0rc1

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
https://repo.saltproject.io/salt_rc/

RC builds are typically only available for the latest version of the operating
system at the time the RC is available. Older versions of operating systems
might not get an RC release.

To install release candidate packages:

#. Use the standard minor install instructions for your operating system. See
   :ref:`install-by-operating-system-index`.

#. On the step where you normally import the Salt Project repository key and pin
   the package to a specific version of Salt, after ``https://repo.saltproject.io``
   insert ``salt_rc/`` before the remainder of the file path.

   .. Note::
       The gpg key for the 3006.0 release is now named: SALT-PROJECT-GPG-PUBKEY-2023


   To install the latest RC, run the following commands:

   .. tab-set::

       .. tab-item:: RHEL 9

           .. parsed-literal::

               sudo rpm --import \ |rhel-release-candidate-gpg|\

               curl -fsSL |rhel-release-candidate| | sudo tee /etc/yum.repos.d/salt.repo

       .. tab-item:: Ubuntu 22.04 (Jammy)

           .. parsed-literal::

               sudo mkdir -p /etc/apt/keyrings

               sudo curl -fsSL -o |ubuntu-release-candidate-gpg|\

               echo "deb |ubuntu-release-candidate| | sudo tee /etc/apt/sources.list.d/salt.list

       .. tab-item:: Debian 11 (Bullseye)

           .. parsed-literal::

               sudo mkdir -p /etc/apt/keyrings

               sudo curl -fsSL -o |debian-release-candidate-gpg|

               echo "deb |debian-release-candidate| | sudo tee  /etc/apt/sources.list.d/salt.list


Install using bootstrap
=======================
You can install a release candidate of Salt using the
`Salt bootstrap <https://github.com/saltstack/salt-bootstrap/>`_ script.

Run the following command for the latest RC release, using
|release-candidate-version| as an example:

.. parsed-literal::

    curl -o install_salt.sh -L https://bootstrap.saltproject.io
    sudo sh install_salt.sh -P -x |bootstrap-release-candidate|

To install a master using Salt bootstrap, use the ``-M`` flag. For example:

.. parsed-literal::

    curl -o install_salt.sh -L https://bootstrap.saltproject.io
    sudo sh install_salt.sh -P -M -x |bootstrap-release-candidate|

If you want to install only a master and not a minion using Salt bootstrap, use
the ``-M`` and ``-N`` flags. For example:

.. parsed-literal::

    curl -o install_salt.sh -L https://bootstrap.saltproject.io
    sudo sh install_salt.sh -P -M -N -x |bootstrap-release-candidate|


Install using pip
=================
To install the release candidate using pip from `PyPi <https://pypi.org/>`_:

#. Install the build dependencies:

   To pip install the latest RC release:

   .. tab-set::

       .. tab-item:: RHEL systems

           Run the following commands:

           .. code-block:: bash

               sudo yum install python3-pip python3-devel gcc gcc-c++

       .. tab-item:: Debian systems

           Run the following commands:

           .. code-block:: bash

               sudo apt-get install python3-pip python3-dev gcc g++

       .. tab-item:: Other systems

           Install:

           * pip
           * Python header libraries
           * C and C++ compilers


#. Install Salt using the following command:

   .. code-block:: bash

       sudo pip install salt==$rc_tag_version

   To pip install the latest RC release, using |release-candidate-version| as an
   example:

   .. parsed-literal::

       |pip-install-release-candidate|

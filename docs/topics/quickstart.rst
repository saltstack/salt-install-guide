.. _quickstart:

==========
Quickstart
==========

Welcome to the Salt quickstart! Use this guide to try Salt for the first time
and experiment with some of its features.

Salt is a powerful automation framework and configuration management tool that
can help you reduce costs by improving the efficiency and reliability of your
IT operations.

Salt can automate and cut down on the time spent on common IT tasks, such as:

- Installing and upgrading software
- Configuring and maintaining devices
- Deploying applications and services

You can use Salt with a wide range of platforms, including Linux, Windows, and
MacOS.

.. Tip::
    To learn more about what Salt can do, see `About Salt <https://docs.saltproject.io/en/latest/topics/about_salt_project.html#about-salt>`_.

In this quickstart, you'll get a taste of some of Salt's functionality and learn
how to work with Salt.


Who should do the quickstart tutorial?
======================================
This tutorial is intended for IT professionals, such as systems administrators,
site reliability engineers, and DevOps engineers. You don't need to be an
expert to use Salt, but you should understand some of the basics of working in
this field.

.. Note::
    This tutorial uses a command-line interface (CLI) and you should have a
    certain level of comfort with working in bash, PowerShell, or similar CLI
    interfaces.


Before you start
================
Salt uses a few unique terms. As you work through this tutorial, if you need a
reference guide that explains some of these terms and concepts, see
`Salt system architecture <https://docs.saltproject.io/en/latest/topics/salt_system_architecture.html>`_.


Install Salt with the quickstart script
=======================================
In this step, you will install Salt and try a few commands to demonstrate
how Salt can quickly retrieve helpful information about your system.

#. **For Linux and MacOS only:** Install the prerequisites, using these
   commands. Select the tab for your operating system:

   .. tab-set::

       .. tab-item:: Ubuntu or Debian systems

          .. code-block:: bash

              sudo apt install curl xz-utils jq tar

       .. tab-item:: PhotonOS

          .. code-block:: bash

              sudo tdnf install curl xz jq tar

       .. tab-item:: RedHat systems

          .. code-block:: bash

              sudo dnf install curl xz jq tar

              # If dnf is unavailable and the above fails:
              sudo yum install curl xz jq tar

       .. tab-item:: SUSE

          .. code-block:: bash

              sudo zypper install curl xz jq tar

       .. tab-item:: MacOS

          .. code-block:: bash

              brew install curl xz jq


#. Download and run the quickstart script:

   .. tab-set::

       .. tab-item:: Linux

          .. parsed-literal::

              curl -o quick.sh -L |quickstart-script-path|
              bash ./quick.sh

       .. tab-item:: MacOS

          .. parsed-literal::

              curl -o quick.sh -L |quickstart-script-path|
              bash ./quick.sh

       .. tab-item:: Windows

          .. parsed-literal::

              Set-ExecutionPolicy RemoteSigned -Scope Process -Force
              [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]'Tls12'
              Invoke-WebRequest -Uri |quickstart-script-path-windows| -OutFile .\quick.ps1
              .\quick.ps1

          .. Note::
              Some commands can only run from an elevated prompted, meaning
              you will need to run them as an Administrator.

   This script downloads and extracts Salt. You'll see output similar to the
   following (based on your operating system):

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. parsed-literal::
             :class: no-copybutton

              *  INFO: Downloading Salt
              *  INFO: Extracting Salt
              *  INFO: Get started with Salt by running the following commands
              *  INFO: Add Salt to current path
              *  INFO:   export PATH=/home/${USER}/salt:$PATH
              *  INFO: Use the provided Saltfile
              *  INFO:   export SALT_SALTFILE=/home/${USER}/salt/Saltfile
              *  INFO: Create Salt states in /home/${USER}/salt/srv/salt

       .. tab-item:: Windows

          .. parsed-literal::
             :class: no-copybutton

              Download Salt
              Extracting Salt
              Unzipping '.\salt.zip' to '.'
              Using Expand-Archive to unzip
              Finished unzipping '.\salt.zip' to '.'
              Adding C:\Temp\salt to PATH

#. **For Linux and MacOS only:** You need the last two lines from the output
   of the previous command. This output is specific to your operating system
   and you will use it for the this step.

   Using that output, copy the last two lines from the script output to update
   ``PATH`` and set the included ``SALT_SALTFILE`` for your system. For example:

   .. code-block:: bash

       export PATH=/home/${USER}/salt:$PATH
       export SALT_SALTFILE=/home/${USER}/salt/Saltfile

   These commands allow Salt to run from those directories.

#. Now that Salt is installed, try running your first Salt command:

   .. code-block:: bash

       salt-call grains.items


   This command may take a moment to run, depending on your processor speed.
   This command gets all the *grain* information for the machine you ran the
   command on, which is your local machine in this case.

   .. Tip::
       *Grains* are the basic information about an operating system. It collects
       and displays a wide variety of information, such as your operating
       system, domain name, IP address, kernel, OS type, memory, and many other
       system properties. You can also create your own custom grain data so that
       you can target nodes based on your own criteria.

   The following is an example of some of the grain output:

   .. parsed-literal::
      :class: no-copybutton

       local:
       ----------
       cpu_model:
           11th Gen Intel Core i7-11850H @ 2.50GHz
       cpuarch:
           x86_64
       num_cpus:
           16
       num_gpus:
           2
       os:
           Ubuntu
       os_family:
           Debian
       osarch:
           amd64
       oscodename:
           jammy
       osfinger:
           Ubuntu-22.04
       osfullname:
           Ubuntu
       osmajorrelease:
           22
       osrelease:
           22.04
       osrelease_info:
           - 22
           - 4
       pythonversion:
           - 3
           - 10
           - 12
           - final
           - 0
       saltversion:
           3006.2
       saltversioninfo:
           - 3006
           - 2

#. Try running a few more commands to get information about your system:

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Command
        - Example output

      * - ``salt-call test.version``
        - ``3006.1``

      * - ``salt-call grains.get username``
        - ``root``

      * - ``salt-call grains.get osrelease``
        - ``5.0``

      * - ``salt-call grains.get productname``
        - ``VMware7,1``

      * - ``salt-call grains.get num_cpus``
        - ``1``

      * - ``salt-call grains.get num_gpus``
        - ``0``

      * - ``salt-call grains.get oscodename``
        - ``Photon``

In this step you used Salt from the command line to get basic information about
your system. As you can see, you can use Salt to monitor and quickly get system
data. But that's only a tiny fraction of what Salt can do. In the next tutorial
step, you'll see how Salt can connect nodes together to create a sophisticated
job and communication system.


Install Salt on your infrastructure
===================================
While it's definitely interesting to see how Salt can quickly get detailed
information from one node, the real power of Salt comes from connecting
it to many nodes.

In the classic Salt infrastructure, a node running the ``salt-master`` agent can
rapidly issue commands to many nodes at the same time as long as those nodes
are running the ``salt-minion`` agent.

In this step, you will use the quickstart script again to install the Salt
master and minion agents on your local machine. Then, you will experiment with a
few commands to see how the master and minions interact.

#. Run the quickstart script again with an additional flag that installs the
   master and minion agents:

   .. code-block:: bash

       bash ./quick.sh -f

   This script downloads and extracts Salt. You'll see output similar to the
   following:

   .. parsed-literal::
      :class: no-copybutton

         *  INFO: A salt directory already exists here, not extracting.
         *  INFO: Get started with Salt by running the following commands
         *  INFO: Add Salt to current path
         *  INFO:   export PATH=/home/${USER}/salt:$PATH
         *  INFO: Use the provided Saltfile
         *  INFO:   export SALT_SALTFILE=/home/${USER}/salt/Saltfile
         *  INFO: Create Salt states in /home/${USER}/salt/srv/salt
         *  INFO: Starting salt-master
         *  INFO: Starting salt-minion
         *  INFO: Run salt-key -L to see pending minion keys
         *  INFO: Run salt-key -a minion to accept the pending minion key

#. With the ``salt-master`` agent and ``salt-minion`` agent installed and
   running, the master and minion need to authenticate with each other using
   Salt keys. Run the following command to list the Salt keys:

   .. code-block:: bash

       salt-key -L

   .. Note::
       Salt keys allow the minion and master to authenticate and communicate
       with each other. See :ref:`accept-keys` for more information.

   After running this command, you'll see output similar to the following:

   .. code-block:: bash
      :class: no-copybutton

       Accepted Keys:
       minion
       Denied Keys:
       Unaccepted Keys:
       Rejected Keys:

#. Accept the minion key by running this command:

   .. code-block:: bash

       salt-key -a minion

#. When prompted, type ``y`` to accept the key and continue.

   .. parsed-literal::

       The following keys are going to be accepted:
       Unaccepted Keys:
       minion
       Proceed? [n/Y] y
       Key for minion minion accepted.

#. Now that the master and minion can communicate with each other, try running
   this command:

   .. code-block:: bash

       salt minion test.version


   .. Tip::
       This command is targeting the minion using its minion ID, which is
       ``minion`` in this case. You can target minions using other methods, such
       as targeting by grain data. For example, you could target all the minions
       with a particular operating system. See
       `Targeting minions <https://docs.saltproject.io/en/latest/topics/targeting/index.html>`_
       for more options.

   The minion returns information about which version of Salt it is running:

   .. code-block:: bash

       minion:
           3006.1

#. Try running a few more commands to get information about your system:

   .. list-table::
      :widths: 40 60
      :header-rows: 1
      :class: extra-padding

      * - Command
        - Description

      * - ``salt \* test.ping``
        - Lists each connected minion and returns a ``True`` value if the minion
          is enabled

      * - ``salt \* disk.usage``
        - List the disks for each minion and information about their current
          disk capacity

      * - ``salt \* pkg.list_pkgs``
        - List the current packages installed on all minions along with the
          package version number

      * - ``salt \* pkg.version [package-name]``
        - List the versions of a certain package for all connected minions

      * - ``salt \* grains.get os_family``
        - List the OS family for all connected minions

      * - ``salt \* service.get_all``
        - List the installed services on all connected minions

      * - ``salt \* service.get_enabled``
        - List the installed and enabled services on all connected minions


Congratulations! You've tried Salt and had a taste for some of its potential!


Next steps
==========

Consider exploring Salt deeper by looking at some of these resources and
features:

.. list-table::
   :widths: 20 80
   :header-rows: 1
   :class: extra-padding

   * - Resource
     - Description

   * - `Salt user guide <https://docs.saltproject.io/salt/user-guide/en/latest/topics/overview.html>`_
     - Read the instruction manual for the Salt Foundations course to get an
       introduction to key Salt concepts.

   * - :ref:`overview`
     - Learn how to install Salt for use in production in the Salt Install Guide.

   * - `All Salt modules <https://docs.saltproject.io/en/latest/py-modindex.html>`_
     - Browse the list of modules to see the types of jobs Salt can do. Some
       popular ones are: `file (remote execution module) <https://docs.saltproject.io/en/latest/ref/modules/all/salt.modules.file.html#module-salt.modules.file>`_,
       `file (state module) <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.file.html#module-salt.states.file>`_, and
       `pkg <https://docs.saltproject.io/en/latest/ref/modules/all/salt.modules.pkg.html#module-salt.modules.pkg>`_.

   * - `All Salt modules <https://docs.saltproject.io/en/latest/py-modindex.html>`_
     - Browse the list of modules to see the types of jobs Salt can do.

   * - `Salt analytics <https://saltproject.io/blog/new-salt-extension-salt-analytics/>`_
     - This Salt extension allows users to run data processing pipelines
       alongside Salt.

   * - `Salt describe <https://saltproject.io/blog/new-salt-extension-salt-describe/>`_
     - This Salt extension creates templates for Salt by fetching the settings
       of remote salt minions.

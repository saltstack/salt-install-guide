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
In this exercise:

- You will install the quickstart version of Salt, which is a lightweight
  version of Salt designed to show you it7s key features.
- Then, you will try a few commands to demonstrate howSalt can quickly retrieve
  helpful information about your system.

To complete the exercise:

#. **For Linux and MacOS only:** Install the prerequisites, using these
   commands. Select the tab for your operating system:

   .. tab-set::

       .. tab-item:: Ubuntu or Debian systems

          .. code-block:: bash

              sudo apt install curl xz-utils jq tar

       .. tab-item:: PhotonOS

          .. code-block:: bash

              sudo tdnf install curl xz jq tar coreutils gawk

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
              Invoke-WebRequest -Uri |quickstart-script-path-windows| -OutFile .\\quick.ps1
              .\\quick.ps1

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

              *  INFO: Downloading Salt
              *  INFO: Extracting Salt
              *  INFO: Adding Salt to current path
              *  INFO:   C:\\Users\\Administrator\\Desktop\\salt
              *  INFO: Setting the SALT_SALTFILE environment variable
              *  INFO:   C:\\Users\\Administrator\\Desktop\\salt\\Saltfile
              *  INFO: Create Salt states in C:\\Users\\Administrator\\Desktop\\salt\\srv\\salt

   .. Note::
      Copy the last line of the script output which tells you where to create
      your state files. You will need this directory at various points in the
      tutorial.

#. **For Linux and MacOS only:** You need the two export lines from the output
   of the previous command. This output is specific to your operating system and
   you will use it for this step.

   Using that output, copy the two export lines from the script output to update
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

In this exercise you used Salt from the command line to get basic information
about your system. As you can see, you can use Salt to monitor and quickly get
system data. But that's only a tiny fraction of what Salt can do. In the next
tutorial exercise, you'll see how Salt can connect nodes together to create a
sophisticated job and communication system.


Install Salt on your infrastructure (Linux only)
================================================
While it's definitely interesting to see how Salt can quickly get detailed
information from one node, the real power of Salt comes from connecting
it to many nodes.

.. Note::
    As of this writing, this tutorial exercise only works on Linux-based
    operating systems. However, the other tutorial exercises work for all
    supported operating systems. To continue the tutorial, skip to
    `Write and test your first Salt state`_.

In the classic Salt infrastructure, a node running the ``salt-master`` agent can
rapidly issue commands to many nodes at the same time as long as those nodes
are running the `salt-minion` agent.

In this exercise:

- You will use the quickstart script again to install the Salt master and minion
  agents on your local machine.
- Then, you will experiment with a few commands to see how the master and
  minions interact.

To complete the exercise:

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

In this exercise, you saw how Salt could be used for *remote execution*, which is
when you connect remotely to your nodes (minions) to execute commands and get
data. In the next exercise, you will learn how to manage nodes at scale using
the Salt state system.


Write and test your first Salt state
====================================
In the previous exercise, you learned about Salt's *remote execution* system,
which can execute ad-hoc commands to multiple nodes (minions) from the command
line. Salt has an additional method of managing nodes through the
*state system.* States are files written in Jinja or YAML that contain a set of
declarative statements that keep the targeted nodes (minions) into a desired
"state."

If it is helpful, you can think of states as a kind of a policy that can be
applied to new or existing nodes. Salt checks to see if the targeted node is in
the desired state, such as whether it has the right applications installed
and/or whether it has the correct configuration settings. If the node is not in
the desired *state*—if it is not in compliant with policy—Salt changes the node
to put it into the desired state. For example, it installs the required
application or it applies the correct configuration settings.

In this exercise:

- You will learn how to create a basic Salt state file and test that it is
  working. This state file will create a small text file on your machine.
- After ensuring it is working, you will edit the file to add additional content
  to simulate an unauthorized change to the file.
- Then, you will use Salt to restore the text file back to its desired,
  compliant state with the original content of the text file.

To complete the exercise:

#. Begin the tutorial by confirming that your system currently does not have the
   ``managed-file.txt`` in your salt directory path. Run this command:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              cat /tmp/managed-file.txt

          If the file does not exist, you will see output similar to this:

          .. code-block:: bash

              cat: /tmp/managed-file.txt: No such file or directory

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              Get-Content C:\Windows\temp\managed-file.txt

          If the file does not exist, you will see output similar to this:

          .. code-block:: powershell

              Get-Content : Cannot find path 'C:\Windows\temp\managed-file.txt' because it does not exist.


#. Create a new state file called ``example-state-file.sls`` in the state tree
   directory that the Salt quickstart script created for state files.

   .. Note::
       In the second step of the first tutorial exercise,
       `Install Salt with the quickstart script`_, the quickstart listed the
       directory that you need to use for state files. If you didn't copy that
       directory down at the time, scroll back in your history to get that
       directory now. You need that directory path for this exercise.

       The directory was listed in the output as:
       ``Create Salt states in`` and then lists the directory path.

#. Open the new ``example-state-file.sls`` file and copy this content to it:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: yaml
             :caption: example-state-file.sls

             add_example_file:
               file.managed:
                 - name: /tmp/managed-file.txt
                 - makedirs: True
                 - contents: Yay!

       .. tab-item:: Windows (Powershell)

          .. code-block:: yaml
             :caption: example-state-file.sls

             add_example_file:
               file.managed:
                 - name: c:\Windows\temp\managed-file.txt
                 - makedirs: True
                 - contents: Yay!



   .. Admonition:: What does this Salt state file mean?

      By default, the `file.managed <https://docs.saltproject.io/en/latest/ref/states/all/salt.states.file.html#salt.states.file.managed>`_
      function of the file state module stores a file on the Salt master. When
      this state is applied to a minion, Salt checks to see if the file is
      present and if the content matches the version of the file stored on the
      Salt master. If the file is not present, Salt creates the file on the
      minion. If the file is present but does not match, Salt updates the
      contents of the file to match.

      The ``file.managed`` function is a popular module with many Salt users
      because it is a great way to quickly add and modify configuration files on
      the nodes you manage with Salt.

      In this state file:

      - The part that says ``add_example_file`` is the identifier. The name of
        the identifier is arbitrary (user-defined) and you can choose any name
        for the identifier. As a best practice, give it an identifier name that
        explains the task or goal this state declaration accomplishes.
      - ``file.managed`` is the Salt state module and function you are invoking.
        The rest of the indented sections are the arguments for the module.
      - The ``name`` argument lists the directory path and name for the file.
      - The ``makedirs`` argument creates the directory for the file if the
        directory isn't present.
      - The ``contents`` argument adds the text ``Yay!`` to the file.

#. Run this command to execute the state file:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              salt-call state.apply example-state-file

          When you run this command, you should see output similar to this:

          .. code-block:: bash

               local:
               ----------
                        ID: add_example_file
                  Function: file.managed
                      Name: /tmp/managed-file.txt
                    Result: True
                   Comment: File /tmp/managed-file.txt updated
                   Started: 02:09:01.040086
                  Duration: 35.883 ms
                   Changes:
                   ----------
                   diff:
                       New file

               Summary for local
               ------------
               Succeeded: 1 (changed=1)
               Failed:    0
               ------------
               Total states run:     1
               Total run time:  35.883 ms

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              salt-call state.apply example-state-file

          When you run this command, you should see output similar to this:

          .. code-block:: powershell

               local:
               ----------
                        ID: add_example_file
                  Function: file.managed
                      Name: C:\Windows\temp\managed-file.txt
                    Result: True
                   Comment: File C:\Windows\temp\managed-file.txt updated
                   Started: 02:09:01.040086
                  Duration: 35.883 ms
                   Changes:
                   ----------
                   diff:
                       New file

               Summary for local
               ------------
               Succeeded: 1 (changed=1)
               Failed:    0
               ------------
               Total states run:     1
               Total run time:  35.883 ms

#. Run this command to confirm that the new state file exists:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              cat /tmp/managed-file.txt

          If the file exists, it will print the contents of the file:

          .. code-block:: bash

              Yay!

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              Get-Content C:\Windows\temp\managed-file.txt

          If the file exists, it will print the contents of the file:

          .. code-block:: powershell

              Yay!

#. Now you will simulate an ad-hoc change to the file contents. Run this command
   to add additional content to the file:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              echo "Extra content" >> /tmp/managed-file.txt

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              Add-Content C:\Windows\temp\managed-file.txt -Value "Extra content"

#. Run this command to confirm that the state file now contains extra content:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              cat /tmp/managed-file.txt

          If the file exists, it will print the contents of the file:

          .. code-block:: bash

              Yay!
              Extra content

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              Get-Content C:\Windows\temp\managed-file.txt

          If the file exists, it will print the contents of the file:

          .. code-block:: powershell

              Yay!
              Extra content

#. Re-apply the state file to restore the ``managed-file`` to its desired
   state:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              salt-call state.apply example-state-file

          When you run this command, you should see output similar to this:

          .. code-block:: bash

               local:
               ----------
                        ID: add_example_file
                  Function: file.managed
                      Name: /tmp/managed-file.txt
                    Result: True
                   Comment: File /tmp/managed-file.txt updated
                   Started: 02:09:01.040086
                  Duration: 35.883 ms
                   Changes:
                   ----------
                   diff:
                       ---
                       +++
                       @@ -1,2 +1 @@
                       yay!
                       -Extra content

               Summary for local
               ------------
               Succeeded: 1 (changed=1)
               Failed:    0
               ------------
               Total states run:     1
               Total run time:  35.883 ms

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              salt-call state.apply example-state-file

          When you run this command, you should see output similar to this:

          .. code-block:: powershell

               local:
               ----------
                        ID: add_example_file
                  Function: file.managed
                      Name: C:\Windows\temp\managed-file.txt
                    Result: True
                   Comment: File C:\Windows\temp\managed-file.txt updated
                   Started: 02:09:01.040086
                  Duration: 35.883 ms
                   Changes:
                   ----------
                   diff:
                       ---
                       +++
                       @@ -1,2 +1 @@
                       yay!
                       -Extra content

               Summary for local
               ------------
               Succeeded: 1 (changed=1)
               Failed:    0
               ------------
               Total states run:     1
               Total run time:  35.883 ms

#. Run this command to confirm that the state file has been restored to its
   original content, its desired state:

   .. tab-set::

       .. tab-item:: Linux and MacOS

          .. code-block:: bash

              cat /salt/managed-file.txt

          If the file has been restored, it will print the contents of the file:

          .. code-block:: bash

              Yay!

       .. tab-item:: Windows (Powershell)

          .. code-block:: powershell

              Get-Content \salt\managed-file.txt

          If the file has been restored, it will print the contents of the file:

          .. code-block:: powershell

              Yay!


As this exercise demonstrates, you can use Salt's state system to ensure your
nodes are always in a desired state. Using the ``file.managed`` state module,
you can prevent configuration drift by ensuring your nodes only have the
configurations content approved by your team.

This exercise implies other powerful configuration management strategies. For
example, rather than storing your state files on the master, you could connect
it to an external Git repository to ensure your configuration files are
accurately version-controlled in an infrastructure-as-code system.

Congratulations! You have completed the tutorial. You tried Salt and now have a
taste for some of its potential!


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

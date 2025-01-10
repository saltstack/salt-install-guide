.. _verify-install:

=====================
Verify a Salt install
=====================

The final step in the Salt installation process is to verify that the
installation was successful by sending a test ping from the Salt master to the
connected Salt minions.

Send a test ping
================
After a successful installation of Salt:

#.  With ``systemctl``, check that the Salt master is running and logs no errors:

    .. code-block:: text

        systemctl status salt-master

    Example response:

    .. code-block:: text

        salt-master.service - The Salt Master Server
            Loaded: loaded (/lib/systemd/system/salt-master.service; enabled; vendor preset: enabled)
            Active: active (running) since Tue 2020-02-04 16:34:55 CST; 17h ago
              Docs: man:salt-master(1)
                    file:///usr/share/doc/salt/html/contents.html
                    https://docs.saltproject.io/en/latest/contents.html
          Main PID: 8727 (salt-master)
             Tasks: 32 (limit: 4915)
            CGroup: /system.slice/salt-master.service
                    ├─8727 /usr/bin/python2 /usr/bin/salt-master
        Feb 04 16:34:55 VM systemd[1]: Starting The Salt Master Server...

#.  Check cluster connection and version:

    .. code-block:: bash

        salt '*' test.version

    Example response:

    .. parsed-literal::

        minion1:
          |minor-one-version|


Next steps
==========
After accepting the Salt minion keys, you can now use Salt!

To learn more about Salt, go the
`Salt user guide <https://docs.saltproject.io/salt/user-guide/en/latest/>`_.

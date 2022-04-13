.. _start-salt-services:

====================================
Start the master and minion services
====================================

After you've installed and configured your Salt masters and minions, you need to
start the minions so that they can:

* Send their keys to the master for acceptance.
* Begin listening to the ``master_minion.pub`` for commands.

You can then start the Salt master and accept the minion keys. See
:ref:`accept-keys` for more information.

.. Note::
    Before you start the Salt master and minions, you must first install the
    ``salt-master`` and ``salt-minion`` services and configure the Salt minion
    to connect to the Salt master. See :ref:`configure-master-minion` for more
    information.


Starting Salt services
======================
Using ``systemctl`` is the main way to start Salt processes. Calling the process
directly will show the active logs in the foreground.


Start with ``systemctl``
------------------------
When starting ``salt-master`` and ``salt-minion``, using ``systemctl`` is
recommended.

.. code-block:: bash

    systemctl start salt-master
    systemctl start salt-minion

``systemctl`` is also useful for preliminary debugging and process start/stop
confirmation:

.. code-block:: bash

    systemctl [start|status|stop] [salt-master|salt-minion]


Starting in the foreground
--------------------------
The ``salt-master`` and ``salt-minion`` daemons can show their logs in the
terminal by calling their processes directly:

.. code-block:: bash

    salt-master
    salt-minion


Next steps
==========
After starting the Salt services, the Salt minion keys need to be accepted by
the Salt master. See :ref:`accept-keys` for more information.

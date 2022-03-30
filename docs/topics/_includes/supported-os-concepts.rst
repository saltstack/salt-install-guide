.. _supported-os-concepts:

Salt runs on and manages many versions of Linux, Windows, Mac OS X and UNIX.
However, Salt's ability to run on a specific operating system depends on whether
that operating system will run the `salt-master` service or the `salt-minion`
service.

Salt uses the master-client model in which a master node issues commands to a
client node and the client runs the command. In the Salt ecosystem, the Salt
master is a node that is running the `salt-master` service. It issues commands
to one or more Salt minions, which are nodes that are running the `salt-minion`
service and that are registered with that particular Salt master.

Some operating systems might be able to run both the `salt-master` service and
the `salt-minion` service, which means nodes running that system can both manage
and be managed by Salt.

Other operating systems may only be able to run the `salt-minion` package and
can only be managed by a Salt master running a different operating system.

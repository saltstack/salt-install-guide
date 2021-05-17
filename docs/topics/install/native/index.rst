.. _native-minions:

==============
Native minions
==============

The install guides for native minions are intended for system administrators
with the general knowledge and experience required in the field.

Native minions vs. proxy minions
================================

Salt can target network-connected devices through `Salt proxy
minions <https://docs.saltstack.com/en/master/topics/proxyminion/index.html>`_.
Proxy |minions| are a Salt feature that enables controlling devices that, for
whatever reason, cannot run the standard |minion-service|. Examples include
network gear that has an API but runs a proprietary OS, devices with limited
CPU or memory, or devices that could run a |minion| but, for security reasons,
will not.

**Salt native minions** are packaged to run directly on specific
devices, removing the need for proxy |minions| running elsewhere on a network.
Native |minions| have several advantages, such as:

-  **Performance boosts:** With native |minions|, Salt doesn’t need to rely on
   constant SSH connections across the network. There is also less burden on the
   servers running multiple proxy |minions|.

-  **Higher availability:** For servers running multiple proxy |minions|, server
   issues can cause connection problems to all proxy |minions| being managed by
   the server. Native |minions| remove this potential point of failure.

-  **Improved scalability:** When adding devices to a network that are supported
   by native |minions|, you aren’t required to deploy proxy |minions| on
   separate infrastructure. This reduces the burden of horizontally or
   vertically scaling infrastructure dedicated to proxy |minions|.


.. Note::
    For an overview of how Salt works, see `Salt system architecture
    <https://docs.saltproject.io/en/master/topics/salt_system_architecture.html>`_.


Install directions per native minion
====================================

.. toctree::
   :maxdepth: 2
   :glob:

   *

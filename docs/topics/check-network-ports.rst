.. _check-network-ports:

========================
Check your network ports
========================

In order for the Salt master to communicate with the Salt minion, the Salt
master needs to allow inbound connections. Check your network ports and firewall
settings to ensure that the master can receive messages through the network.

.. Note::
    Although the standard Salt configuration model is the master/client model,
    minions do not necessarily have to have a master to be managed. See
    :ref:`overview` for more information about alternative installation and
    configuration options.


About Salt network ports
========================
The Salt master-to-minion communication model only requires inbound connections
into the Salt master. Connections are established from the minion and never
from the master.

.. list-table::
  :widths: 10 50 40
  :align: left
  :header-rows: 1

  * - Port
    - Type
    - Description

  * - 4505
    - Event Publisher/Subscriber port (publish jobs/events)
    - Constant inquiring connection

  * - 4506
    - Data payloads and minion returns (file services/return data)
    - Connects only to deliver data


.. image:: ../_static/img/minion-subcription-publication-model.jpg
   :align: left
   :alt: Minion subscription publication

.. _access-old-packages:

===========================
Access old packages of Salt
===========================

The current supported versions of Salt are:

* |supported-release-1|
* |supported-release-2|

See :ref:`salt-version-support-lifecycle` for more information about the support
policy for older versions.

.. Danger::
    Avoid using unsupported versions of Salt. Using an unsupported version means
    you will no longer receive package updates from Salt, including important
    security updates such as CVE releases.

Packages for unsupported versions of Salt are available in the repository
archives. Once a version of Salt enters extended life support, it is moved into
the repository archives and the package URL changes so that it is prepended with
``archive``. For example:

.. list-table::
   :widths: 20 80
   :stub-columns: 1

   * - Previous URL
     - https://repo.saltproject.io/py3/amazon/2/x86_64/3001.repo

   * - Archive URL
     - https://archive.repo.saltproject.io/py3/amazon/2/x86_64/3001.repo

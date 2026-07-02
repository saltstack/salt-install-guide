.. _air-gap-install:

==================================
Install in air-gapped environments
==================================

.. include:: ../_includes/install-method.rst


About air-gapped installations
==============================

To install Salt in an air-gapped environment, you can create a local mirror of
the Salt Project repositories using a sync tool such as ``rclone`` or ``wget``.

Create a local mirror with ``rclone`` (faster)
==============================================

.. note::

      Only sync once per day.

.. important::

      Always pass the ``-c`` / ``--checksum`` flag to ``rclone sync``. Without
      it, ``rclone`` compares files by size and modification time only. The
      Salt package repositories publish updates in which small companion
      files (``*.md5``, ``*.sha1``, ``*.sha256``, ``Release``,
      ``Release.gpg``, ``InRelease``, and the RPM ``repodata/repomd.xml``) can
      keep the same size while their content changes, so a size+mtime
      comparison silently skips them. The stale hash/metadata files then
      cause ``apt`` (and ``yum``/``dnf``) to reject the mirror with
      "unexpected size" / hash-mismatch errors. See
      `issue 69652 <https://github.com/saltstack/salt/issues/69652>`__ for
      the original report.

To set up local mirrors with ``rclone``:

.. tab-set::

      .. tab-item:: Linux (RPM)

         Syncs down the following repo: `saltproject-rpm <https://packages.broadcom.com/artifactory/saltproject-rpm/>`__

         In the ``rclone`` command line, adapt this example:

         .. code-block:: bash

               RCLONE_WEBDAV_URL=https://packages.broadcom.com/artifactory/ RCLONE_WEBDAV_VENDOR=other rclone sync --fast-list --checksum -v :webdav:saltproject-rpm/ ./saltproject-rpm/

      .. tab-item:: Linux (DEB)

         Syncs down the following repo: `saltproject-deb <https://packages.broadcom.com/artifactory/saltproject-deb/>`__

         In the ``rclone`` command line, adapt this example:

         .. code-block:: bash

               RCLONE_WEBDAV_URL=https://packages.broadcom.com/artifactory/ RCLONE_WEBDAV_VENDOR=other rclone sync --fast-list --checksum -v :webdav:saltproject-deb/ ./saltproject-deb/

      .. tab-item:: Generic (Windows, macOS, etc.)

         Syncs down the following repo: `saltproject-generic <https://packages.broadcom.com/artifactory/saltproject-generic/>`__

         In the ``rclone`` command line, adapt this example:

         .. code-block:: bash

               RCLONE_WEBDAV_URL=https://packages.broadcom.com/artifactory/ RCLONE_WEBDAV_VENDOR=other rclone sync --fast-list --checksum -v :webdav:saltproject-generic/ ./saltproject-generic/


Create a local mirror with ``wget`` (slower)
============================================

.. note::

      Only sync once per day.

To set up local mirrors with ``wget``:

.. tab-set::

      .. tab-item:: Linux (RPM)

         Syncs down the following repo: `saltproject-rpm <https://packages.broadcom.com/artifactory/saltproject-rpm/>`__

         In the ``wget`` command line, adapt this example:

         .. code-block:: bash

            wget --mirror -nH --cut-dirs=1 https://packages.broadcom.com/artifactory/saltproject-rpm/

      .. tab-item:: Linux (DEB)

         Syncs down the following repo: `saltproject-deb <https://packages.broadcom.com/artifactory/saltproject-deb/>`__

         In the ``wget`` command line, adapt this example:

         .. code-block:: bash

            wget --mirror -nH --cut-dirs=1 https://packages.broadcom.com/artifactory/saltproject-deb/

      .. tab-item:: Generic (Windows, macOS, etc.)

         Syncs down the following repo: `saltproject-generic <https://packages.broadcom.com/artifactory/saltproject-generic/>`__

         In the ``wget`` command line, adapt this example:

         .. code-block:: bash

            wget --mirror -nH --cut-dirs=1 https://packages.broadcom.com/artifactory/saltproject-generic/

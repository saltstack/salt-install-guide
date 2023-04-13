.. _air-gap-install:

==================================
Install in air-gapped environments
==================================

.. include:: _includes/install-method.rst


About air-gapped installations
==============================
To install Salt in an air-gapped environment, you can create a local mirror of
the Salt Project repository using an s3 API compatible sync tool such as the
`aws-cli` or `rclone`.

Be aware that the Salt Project uses a custom endpoint to make it easier to
switch buckets easily.

Also note that `rclone` may warn about the time being out of sync. You can
safely ignore these warning messages. The warning message is caused because Salt
Project uses CloudFront as a cache instead of using s3 directly. Please sync no
more than once per day.


Create a local mirror with `rclone`
===================================
To set up a local mirror with `rclone`:

#. In the `rclone` command line, adapt this example:

   .. code-block:: bash

      RCLONE_CONFIG_S3_TYPE=s3 RCLONE_CONFIG_S3_PROVIDER=Other RCLONE_CONFIG_S3_ENV_AUTH=false RCLONE_CONFIG_S3_ENDPOINT=https://s3.repo.saltproject.io rclone sync --fast-list --use-server-modtime -v s3:s3/ ./fullrepo/

   .. Note::
       On behalf of the Salt Project, include the
       `--use-server-modtime` flags to help us drastically reduce our costs.

#. (Optional): If you can't use the `--use-server-modtime` flag because your
   version of `rclone`` is too old, you can use the `-c flag` instead:

   .. code-block:: bash

       RCLONE_CONFIG_S3_TYPE=s3 RCLONE_CONFIG_S3_PROVIDER=Other RCLONE_CONFIG_S3_ENV_AUTH=false RCLONE_CONFIG_S3_ENDPOINT=https://s3.repo.saltproject.io rclone sync --fast-list -c -v s3:s3/ ./fullrepo/


   .. Tip::
       Only sync once per day.


Create a local mirror with `aws-cli`
====================================
To set up a local mirror with `aws-cli`:

#. In the `aws-cli` command line, adapt this example:

   .. code-block:: bash

      aws --no-sign-request --endpoint-url https://s3.repo.saltproject.io s3 sync --delete --exact-timestamps s3://s3/ ./fullrepo/

#. To sync the local mirror, use `https://s3.archive.repo.saltproject.io` as the
   endpoint URL.

   .. Tip::
       Only sync once per day.

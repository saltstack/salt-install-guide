.. Note::

   When you install a onedir version of Salt (3006 and later), Salt installs its
   own local version of Python and the dependencies needed for the core
   functionality of Salt.

   After installing a onedir verison of Salt, your system has both a global
   version of Python at the system level and a local version of Python used by
   Salt. This architecture change means that the Salt onedir paths for Python
   are different and you need to change how you install third-party Python
   dependencies that you use with Salt, including your state files. See
   :ref:`install-dependencies` for more information.

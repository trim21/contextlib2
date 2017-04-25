Release History
---------------

0.5.5 (2017-04-25)
^^^^^^^^^^^^^^^^^^

* Issue `#13 <https://github.com/jazzband/contextlib2/issues/13>`__:
  ``setup.py`` now falls back to plain ``distutils`` if ``setuptools`` is not
  available (patch by Allan Harwood)

* Updates to the default compatibility testing matrix:
  * Added: PyPy3, CPython 3.6 (maintenance), CPython 3.7 (development)
  * Dropped: CPython 3.3

0.5.4 (2016-07-31)
^^^^^^^^^^^^^^^^^^

* Thanks to the welcome efforts of Jannis Leidel, contextlib2 is now a
  [Jazzband](https://jazzband.co/) project! This means that I (Nick Coghlan)
  am no longer a single point of failure for backports of future contextlib
  updates to earlier Python versions.

* Issue `#7 <https://github.com/jazzband/contextlib2/issues/7>`__: Backported
  fix for CPython issue `#27122 <http://bugs.python.org/issue27122>`__,
  preventing a potential infinite loop on Python 3.5 when handling
  ``RuntimeError`` (CPython updates by Gregory P. Smith & Serhiy Storchaka)


0.5.3 (2016-05-02)
^^^^^^^^^^^^^^^^^^

* ``ExitStack`` now correctly handles context managers implemented as old-style
  classes in Python 2.x (such as ``codecs.StreamReader`` and
  ``codecs.StreamWriter``)

* ``setup.py`` has been migrated to setuptools and configured to emit a
  universal wheel file by default

0.5.2 (2016-05-02)
^^^^^^^^^^^^^^^^^^

* development migrated from BitBucket to GitHub

* ``redirect_stream``, ``redirect_stdout``, ``redirect_stderr`` and ``suppress``
  now explicitly inherit from ``object``, ensuring compatibility with
  ``ExitStack`` when run under Python 2.x (patch contributed by Devin
  Jeanpierre).

* ``MANIFEST.in`` is now included in the published sdist, ensuring the archive
  can be precisely recreated even without access to the original source repo
  (patch contributed by Guy Rozendorn)


0.5.1 (2016-01-13)
^^^^^^^^^^^^^^^^^^

* Python 2.6 compatilibity restored (patch contributed by Armin Ronacher)

* README converted back to reStructured Text formatting


0.5.0 (2016-01-12)
^^^^^^^^^^^^^^^^^^

* Updated to include all features from the Python 3.4 and 3.5 releases of
  contextlib (also includes some ``ExitStack`` enhancements made following
  the integration into the standard library for Python 3.3)

* The legacy ``ContextStack`` and ``ContextDecorator.refresh_cm`` APIs are
  no longer documented and emit ``DeprecationWarning`` when used

* Python 2.6, 3.2 and 3.3 have been dropped from compatibility testing

* tox is now supported for local version compatibility testing (patch by
  Marc Abramowitz)


0.4.0 (2012-05-05)
^^^^^^^^^^^^^^^^^^

* (BitBucket) Issue #8: Replace ContextStack with ExitStack (old ContextStack
  API retained for backwards compatibility)

* Fall back to unittest2 if unittest is missing required functionality


0.3.1 (2012-01-17)
^^^^^^^^^^^^^^^^^^

* (BitBucket) Issue #7: Add MANIFEST.in so PyPI package contains all relevant
  files (patch contributed by Doug Latornell)


0.3 (2012-01-04)
^^^^^^^^^^^^^^^^

* (BitBucket) Issue #5: ContextStack.register no longer pointlessly returns the
  wrapped function
* (BitBucket) Issue #2: Add examples and recipes section to docs
* (BitBucket) Issue #3: ContextStack.register_exit() now accepts objects with
  __exit__ attributes in addition to accepting exit callbacks directly
* (BitBucket) Issue #1: Add ContextStack.preserve() to move all registered
  callbacks to a new ContextStack object
* Wrapped callbacks now expose __wrapped__ (for direct callbacks) or __self__
  (for context manager methods) attributes to aid in introspection
* Moved version number to a VERSION.txt file (read by both docs and setup.py)
* Added NEWS.rst (and incorporated into documentation)


0.2 (2011-12-15)
^^^^^^^^^^^^^^^^

* Renamed CleanupManager to ContextStack (hopefully before anyone started
  using the module for anything, since I didn't alias the old name at all)


0.1 (2011-12-13)
^^^^^^^^^^^^^^^^

* Initial release as a backport module
* Added CleanupManager (based on a `Python feature request`_)
* Added ContextDecorator.refresh_cm() (based on a `Python tracker issue`_)
  
.. _Python feature request: http://bugs.python.org/issue13585
.. _Python tracker issue: http://bugs.python.org/issue11647

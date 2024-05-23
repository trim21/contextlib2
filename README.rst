.. image:: https://jazzband.co/static/img/badge.svg
   :target: https://jazzband.co/
   :alt: Jazzband

.. image:: https://github.com/jazzband/contextlib2/workflows/Test/badge.svg
   :target: https://github.com/jazzband/contextlib2/actions
   :alt: Tests

.. image:: https://codecov.io/gh/jazzband/contextlib2/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jazzband/contextlib2
   :alt: Coverage

.. image:: https://readthedocs.org/projects/contextlib2/badge/?version=latest
   :target: https://contextlib2.readthedocs.org/
   :alt: Latest Docs

contextlib2 is a backport of the `standard library's contextlib
module <https://docs.python.org/3/library/contextlib.html>`_ to
earlier Python versions.

It also sometimes serves as a real world proving ground for possible future
enhancements to the standard library version.

Licensing
---------

As a backport of Python standard library software, the implementation, test
suite and other supporting files for this project are distributed under the
Python Software License used for the CPython reference implementation.

The one exception is the included type hints file, which comes from the
``typeshed`` project, and is hence distributed under the Apache License 2.0.

Development
-----------

``contextlib2`` has no runtime dependencies, but requires ``setuptools`` and
``wheel`` at build time to generate universal wheel archives.

Local testing is a matter of running::

    python3 -m unittest discover -t . -s test

You can test against multiple versions of Python with
`tox <https://tox.testrun.org/>`_::

    pip install tox
    tox

Versions currently tested in both tox and GitHub Actions are:

* CPython 3.8
* CPython 3.9
* CPython 3.10
* CPython 3.11
* CPython 3.12
* PyPy3 (specifically 3.10 in GitHub Actions)

Updating to a new stdlib reference version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of Python 3.12.3, 4 files needed to be copied from the CPython reference
implementation to contextlib2:

* ``Doc/library/contextlib.rst`` -> ``docs/contextlib2.rst``
* ``Lib/contextlib.py`` -> ``contextlib2/__init__.py``
* ``Lib/test/test_contextlib.py`` -> ``test/test_contextlib.py``
* ``Lib/test/test_contextlib_async.py`` -> ``test/test_contextlib_async.py``

The corresponding version of ``contextlib2/__init__.pyi`` also needs to be
retrieved from the ``typeshed`` project::

    wget https://raw.githubusercontent.com/python/typeshed/master/stdlib/contextlib.pyi

The following patch files are saved in the ``dev`` directory:

* changes to ``contextlib2/__init__.py`` to get it to run on the older
  versions (and to add back in the deprecated APIs that never graduated to
  the standard library version)
* changes to ``test/test_contextlib.py`` and ``test/test_contextlib_async.py``
  to get them to run on the older versions
* changes to ``contextlib2/__init__.pyi`` to make the Python version
  guards unconditional (since the ``contextlib2`` API is the same on all
  supported versions)
* changes to ``docs/contextlib2.rst`` to use ``contextlib2`` version
  numbers in the version added/changed notes and to integrate the module
  documentation with the rest of the project documentation

When the upstream changes between releases are minor, these patch files may be
used directly to reapply the ``contextlib2`` specific changes after syncing a
new version. Even when the patches do not apply cleanly, they're still a useful
guide as to the changes that are needed to restore compatibility with older
Python versions and make any other ``contextlib2`` specific updates.

The test directory is laid out so that the test suite's imports from
``test.support`` work the same way as they do in the main CPython test suite.
These files are selective copies rather than complete ones as the ``contextlib``
tests only need a tiny fraction of the features available in the real
``test.support`` module.

The ``dev/sync_from_cpython.sh`` and ``dev/save_diff_snapshot.sh`` scripts
automate some of the steps in the sync process.

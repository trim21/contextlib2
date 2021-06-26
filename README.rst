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

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

Development
-----------

contextlib2 has no runtime dependencies, but requires ``unittest2`` for testing
on Python 2.x, as well as ``setuptools`` and ``wheel`` to generate universal
wheel archives.

Local testing is a matter of running::

    python3 -m unittest discover -t . -s test

You can test against multiple versions of Python with
`tox <https://tox.testrun.org/>`_::

    pip install tox
    tox

Versions currently tested in both tox and GitHub Actions are:

* CPython 3.6
* CPython 3.7
* CPython 3.8
* CPython 3.9
* CPython 3.10
* PyPy3

Updating to a new stdlib reference version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of Python 3.10, 3 files needed to be copied from the CPython reference
implementation to contextlib2:

* ``Lib/contextlib.py`` -> ``contextlib2.py``
* ``Lib/test/test_contextlib.py`` -> ``test/test_contextlib.py``
* ``Lib/test/test_contextlib_async.py`` -> ``test/test_contextlib_async.py``

For the 3.10 sync, the only changes needed to the test files were to import from
``contextlib2`` rather than ``contextlib``. The test directory is laid out so
that the test suite's imports from ``test.support`` work the same way they do in
the main CPython test suite.

The changes made to the ``contextlib2.py`` file to get it to run on the older
versions (and to add back in the deprecated APIs that never graduated to the
standard library version) are saved as a patch file in the ``dev`` directory.

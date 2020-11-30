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
module <https://docs.python.org/3.5/library/contextlib.html>`_ to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

Development
-----------

contextlib2 has no runtime dependencies, but requires ``unittest2`` for testing
on Python 2.x, as well as ``setuptools`` and ``wheel`` to generate universal
wheel archives.

Local testing is just a matter of running ``python test_contextlib2.py``.

You can test against multiple versions of Python with
`tox <https://tox.testrun.org/>`_::

    pip install tox
    tox

Versions currently tested in both tox and GitHub Actions are:

* CPython 2.7
* CPython 3.5
* CPython 3.6
* CPython 3.7
* CPython 3.8
* PyPy
* PyPy3

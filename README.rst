.. image:: https://readthedocs.org/projects/contextlib2/badge/?version=latest
    :target: https://contextlib2.readthedocs.org/
    :alt: Latest Docs

.. todo: set up Travis CI
.. todo: set up Coveralls

contextlib2 is a backport of the `standard library's contextlib
module <https://docs.python.org/3.5/library/contextlib.html>`_ to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

Development
-----------

contextlib2 currently has no dependencies.

Local testing is currently just a matter of running ``python test_contextlib2.py``.

You can test against multiple versions of Python with `tox <http://tox.testrun.org/>`_::

    pip install tox
    tox

Versions currently tested in tox are:

* CPython 2.7
* CPython 3.4
* CPython 3.5
* PyPy
* PyPy3

To install all the relevant runtimes on Fedora 23::

    sudo dnf install python python3 pypy pypy3
    sudo dnf copr enable -y mstuchli/Python3.5
    sudo dnf install python35-python3

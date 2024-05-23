.. contextlib2 documentation master file, created by
   sphinx-quickstart on Tue Dec 13 20:29:56 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

contextlib2 --- Updated utilities for context management
========================================================

.. module:: contextlib2
   :synopsis: Backports and future enhancements for the contextlib module

This module provides backports of features in the latest version of the
standard library's :mod:`contextlib` module to earlier Python versions. It
also serves as a real world proving ground for potential future enhancements
to that module.

Like :mod:`contextlib`, this module provides utilities for common tasks
involving the ``with`` and ``async with`` statements.


Additions Relative to the Standard Library
------------------------------------------

This module is primarily a backport of the Python 3.12.3 version of
:mod:`contextlib` to earlier releases. (Note: as of the start of the Python 3.13
beta release cycle, there have been no subsequent changes to ``contextlib``)

The module makes use of positional-only argument syntax in several call
signatures, so the oldest supported Python version is Python 3.8.

This module may also be used as a proving ground for new features not yet part
of the standard library. There are currently no such features in the module.

Finally, this module contains some deprecated APIs which never graduated to
standard library inclusion. These interfaces are no longer documented, but may
still be present in the code (emitting ``DeprecationWarning`` if used).


Using the Module
====================

.. toctree::
   contextlib2.rst

Obtaining the Module
====================

This module can be installed directly from the `Python Package Index`_ with
pip_::

    pip install contextlib2

Alternatively, you can download and unpack it manually from the `contextlib2
PyPI page`_.

There are no operating system or distribution specific versions of this
module - it is a pure Python module that should work on all platforms.

Supported Python versions are currently 3.8+.

.. _Python Package Index: http://pypi.python.org
.. _pip: http://www.pip-installer.org
.. _contextlib2 pypi page: http://pypi.python.org/pypi/contextlib2


Development and Support
-----------------------

contextlib2 is developed and maintained on GitHub_. Problems and suggested
improvements can be posted to the `issue tracker`_.

.. _GitHub: https://github.com/jazzband/contextlib2
.. _issue tracker: https://github.com/jazzband/contextlib2/issues


.. include:: ../NEWS.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

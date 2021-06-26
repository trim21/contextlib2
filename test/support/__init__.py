"""Enough of the test.support APIs to run the contextlib test suite"""
import sys
import unittest

requires_docstrings = unittest.skipIf(sys.flags.optimize >= 2,
                                      "Test requires docstrings")

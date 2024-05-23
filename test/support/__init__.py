"""Enough of the test.support APIs to run the contextlib test suite"""
import sys
import unittest

# Extra contextlib2 helpers checking CPython version-dependent details
_py_ver = sys.version_info

cl2_gens_have_gi_suspended = (_py_ver >= (3, 11))
cl2_async_gens_have_ag_suspended = (_py_ver >= (3, 12))

cl2_have_exception_groups = (_py_ver >= (3, 11))
cl2_requires_exception_groups = unittest.skipIf(not cl2_have_exception_groups,
                                                "Test requires exception groups")

cl2_check_traceback_details = (_py_ver >= (3, 10))

# CM protocol checking switched to TypeError in Python 3.11
cl2_cm_api_exc_type = TypeError if (_py_ver >= (3, 11)) else AttributeError
cl2_cm_api_exc_text_legacy = {
    "": "has no attribute",
    "__enter__": "__enter__",
    "__exit__": "__exit__",
}
if cl2_cm_api_exc_type is AttributeError:
    cl2_cm_api_exc_text_sync = {
        "": "has no attribute",
        "__enter__": "__enter__",
        "__exit__": "__exit__",
    }
    cl2_cm_api_exc_text_async = cl2_cm_api_exc_text_sync
else:
    cl2_cm_api_exc_text_sync = {
        "": "the context manager",
        "__enter__": "the context manager",
        "__exit__": "the context manager.*__exit__",
    }
    cl2_cm_api_exc_text_async = {
        "": "asynchronous context manager",
        "__enter__": "asynchronous context manager",
        "__exit__": "asynchronous context manager.*__exit__",
    }

def cl2_cm_api_exc_info_sync(check_context="", /):
    return cl2_cm_api_exc_type, cl2_cm_api_exc_text_sync[check_context]

def cl2_cm_api_exc_info_async(check_context="", /):
    return cl2_cm_api_exc_type, cl2_cm_api_exc_text_async[check_context]

# Some tests check docstring details
requires_docstrings = unittest.skipIf(sys.flags.optimize >= 2,
                                      "Test requires docstrings")

# Some tests check CPython implementation details
def _parse_guards(guards):
    # Returns a tuple ({platform_name: run_me}, default_value)
    if not guards:
        return ({'cpython': True}, False)
    is_true = list(guards.values())[0]
    assert list(guards.values()) == [is_true] * len(guards)   # all True or all False
    return (guards, not is_true)

# Use the following check to guard CPython's implementation-specific tests --
# or to run them only on the implementation(s) guarded by the arguments.
def check_impl_detail(**guards):
    """This function returns True or False depending on the host platform.
       Examples:
          if check_impl_detail():               # only on CPython (default)
          if check_impl_detail(jython=True):    # only on Jython
          if check_impl_detail(cpython=False):  # everywhere except on CPython
    """
    guards, default = _parse_guards(guards)
    return guards.get(sys.implementation.name, default)

# Early reference release tests force gc collection
def gc_collect():
    """Force as many objects as possible to be collected.

    In non-CPython implementations of Python, this is needed because timely
    deallocation is not guaranteed by the garbage collector.  (Even in CPython
    this can be the case in case of reference cycles.)  This means that __del__
    methods may be called later than expected and weakrefs may remain alive for
    longer than expected.  This function tries its best to force all garbage
    objects to disappear.
    """
    import gc
    gc.collect()
    gc.collect()
    gc.collect()

# test_contextlib_async includes some socket-based tests
# Emscripten's socket emulation and WASI sockets have limitations.
is_emscripten = sys.platform == "emscripten"
is_wasi = sys.platform == "wasi"
has_socket_support = not is_emscripten and not is_wasi

def requires_working_socket(*, module=False):
    """Skip tests or modules that require working sockets

    Can be used as a function/class decorator or to skip an entire module.
    """
    msg = "requires socket support"
    if module:
        if not has_socket_support:
            raise unittest.SkipTest(msg)
    else:
        return unittest.skipUnless(has_socket_support, msg)

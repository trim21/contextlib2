#!/bin/sh

git_root="$(git rev-parse --show-toplevel)"

cpython_dir="${1:-$git_root/../cpython}"

diff_prefix="py3_12" # Update based on the version being synced

function diff_file()
{
    diff -ud "$2" "$git_root/$3" > "$git_root/dev/${diff_prefix}_$1.patch"
}

diff_file rst_to_contextlib2 \
  "$cpython_dir/Doc/library/contextlib.rst"         "docs/contextlib2.rst"

diff_file py_to_contextlib2 \
  "$cpython_dir/Lib/contextlib.py"                  "contextlib2/__init__.py"

diff_file pyi_to_contextlib2 \
  "$git_root/dev/typeshed_contextlib.pyi"           "contextlib2/__init__.pyi"

diff_file test_to_contextlib2 \
  "$cpython_dir/Lib/test/test_contextlib.py"        "test/test_contextlib.py"

diff_file test_async_to_contextlib2 \
  "$cpython_dir/Lib/test/test_contextlib_async.py"  "test/test_contextlib_async.py"

#!/bin/sh

git_root="$(git rev-parse --show-toplevel)"

cpython_dir="${1:-$git_root/../cpython}" # Folder with relevant CPython version

function sync_file()
{
    cp -fv "$cpython_dir/$1" "$git_root/$2"
}

sync_file "Doc/library/contextlib.rst"         "docs/contextlib2.rst"
sync_file "Lib/contextlib.py"                  "contextlib2/__init__.py"
sync_file "Lib/test/test_contextlib.py"        "test/test_contextlib.py"
sync_file "Lib/test/test_contextlib_async.py"  "test/test_contextlib_async.py"

echo
echo "Note: Update the 'contextlib2/__init__.pyi' stub as described in the file"
echo

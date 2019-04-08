#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='contextlib2',
    version=open('VERSION.txt').read().strip(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    py_modules=['contextlib2'],
    license='PSF License',
    description='Backports and enhancements for the contextlib module',
    long_description=open('README.rst').read(),
    author='Nick Coghlan',
    author_email='ncoghlan@gmail.com',
    url='http://contextlib2.readthedocs.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Python Software Foundation License',
        # These are the Python versions tested, it may work on others
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

)

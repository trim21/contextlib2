#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='contextlib2',
    version=open('VERSION.txt').read().strip(),
    python_requires='>=3.6',
    packages=['contextlib2'],
    include_package_data=True,
    license='PSF License',
    description='Backports and enhancements for the contextlib module',
    long_description=open('README.rst').read(),
    author='Alyssa Coghlan',
    author_email='ncoghlan@gmail.com',
    url='http://contextlib2.readthedocs.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: Python Software Foundation License',
        # These are the Python versions tested, it may work on others
        # It definitely won't work on versions without native async support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

)

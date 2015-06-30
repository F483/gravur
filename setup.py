#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import os
from setuptools import setup, find_packages


THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)


VERSION = open("version.txt").readline().strip()
DOWNLOAD_BASEURL = "https://pypi.python.org/packages/source/a/gravur/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "gravur-%s.tar.gz" % VERSION


setup(
    name='gravur',
    version=VERSION,
    description=('Secure censorship resistant bitcoin messaging application.'),
    long_description=open("README.rst").read(),
    keywords=(""),  # TODO keywords
    url='https://github.com/F483/gravur/',
    author='Fabian Barkhau',
    author_email='fabian.barkhau@gmail.com',
    license='MIT',
    packages=find_packages(),
    download_url = DOWNLOAD_URL,
    test_suite="tests",
    install_requires=[
        'btctxstore == 2.2.0'
    ],
    tests_require=[
        'coverage',
        'coveralls',
        'ipython',
        'pudb'  # import pudb; pu.db # set break point
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # TODO "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        # TODO "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

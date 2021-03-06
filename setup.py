# coding=utf-8

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup (
    name = 'krakenio3',
    version = '0.1.1',
    description = 'Kraken.io API Client',
    long_description = 'Python 3 client for Kraken.io.',
    url = 'https://github.com/TomAnthony/kraken-python',
    author = 'Nekkra UG',
    author_email = 'support@kraken.io',
    license = 'MIT',
    keywords = 'kraken kraken.io image optimizer optimiser resizer',

    packages = [
        'krakenio'
    ],

    install_requires = [
        'requests'
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
setup

@File           : setup.py
@Time           : 2020/3/16 19:33
@Author         : hywell
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : dictfire
@description    : Chinese/English Translation
@homepage:  https://github.com/HeywoodKing/dictfire.git
@license:   MIT, see LICENSE for more details.
@copyright: Copyright (c) 2020 hywell. All rights reserved
"""

import codecs
from dictfire.dictfire import DictFire
import setuptools.command.test


# -*- Long Description -*-

def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.rst file'


setuptools.setup(
    name=DictFire.__name__,
    version=DictFire.__version__,
    description=DictFire.__description__,
    long_description=long_description(),
    long_description_content_type="text/markdown",
    keywords=DictFire.__keywords__,
    author=DictFire.__author__,
    author_email=DictFire.__contact__,
    url=DictFire.__url__,
    license=DictFire.__license__,
    platforms=['any'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Terminals',
        "Topic :: System :: Distributed Computing",

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        '': ['*.py']
    },
    entry_points={
        'console_scripts': [
            'dict = dict:main',
        ],
    },
)

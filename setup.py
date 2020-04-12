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
from __future__ import with_statement
from __future__ import print_function
import io
import os
import sys
import codecs
# import setuptools.command.test
from shutil import rmtree


try:
    from setuptools import find_packages, setup, Command
except ImportError:
    from distutils.core import setup, find_packages, Command

if sys.version_info < (3, 0):
    sys.exit('Python 3.0 or greater is required.')

NAME = 'dictfire'
VERSION = ''
DESCRIPTION = """命令行下[中英，中俄，中日，中韩，中法，中德，中西]文互翻译工具（Command line translation tool for Chinese English,Chinese French, Chinese Japanese, Chinese Korean, Chinese German），翻译服务基于有道翻译。"""
KEYWORDS = """Translation English2Chinese, Chinese2English, Chinese2French, French2Chinese, Chinese2Japanese,
Japanese2Chinese, Chinese2Korean, Korean2Chinese, Chinese2German, German2Chinese） Command-line"""
AUTHOR = 'hywell'
EMAIL = 'opencoding@hotmail.com'
URL = 'https://github.com/HeywoodKing/dictfire'
LICENSE = 'MIT'
REQUIRES_PYTHON = '>=3.0.0'

# What packages are required for this module to be executed?
REQUIRED = [
    "requests", "fake-useragent"
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

here = os.path.abspath(os.path.dirname(__file__))


# -*- Long Description -*-
# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
# def long_description():
#     try:
#         with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
#             content = '\n' + f.read()
#     except FileNotFoundError as ex:
#         print(ex)
#         content = DESCRIPTION
#
#     print(content)
#     return content


# def long_description():
#     try:
#         content = codecs.open('README.md', 'r', 'utf-8').read()
#         # print('*' * 100)
#         # print(content)
#         # print('*' * 100)
#     except IOError as ex:
#         print(ex)
#         content = DESCRIPTION
#
#     return content


# def long_description():
#     try:
#         with open("README.md", "r") as fh:
#             content = fh.read()
#     except IOError as ex:
#         print(ex)
#         content = DESCRIPTION
#
#     return content


def long_description():
    try:
        readme = os.path.join(here, 'README.md')
        if os.path.isfile(readme):
            try:
                import pypandoc
                # from pypandoc.pandoc_download import download_pandoc
                # pypandoc.download_pandoc()

                # file_path, tmp_file_name = os.path.split(readme)
                # short_name, extension = os.path.splitext(tmp_file_name)

                file_name = os.path.basename(readme).split('.')[0]
                rst_file = '{}.rst'.format(file_name)
                rst_path = os.path.join(here, rst_file)
                if os.path.exists(rst_path):
                    os.remove(rst_path)
                pypandoc.convert_file(readme, 'rst', 'md', outputfile=rst_file)
                # content = pypandoc.convert_file(readme, 'rst', 'md')
                with io.open(rst_path, encoding='utf-8') as f:
                    content = '\n' + f.read()
            except Exception as ex:
                print(ex)
                content = DESCRIPTION
        else:
            content = DESCRIPTION
    except IOError as ex:
        print(ex)
        content = DESCRIPTION

    return content


# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError as ex:
            print(ex)

        try:
            self.status('Building Source and Wheel (universal) distribution…')
            # os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
            # os.system('{0} setup.py build sdist bdist_egg bdist_wheel --universal'.format(sys.executable))
            os.system('{0} setup.py build bdist bdist_egg bdist_wheel --universal'.format(sys.executable))

            self.status('Uploading the package to PyPI via Twine…')
            os.system('twine upload dist/*')

            self.status('Pushing git tags…')
            os.system('git tag v{0}'.format(about['__version__']))
            os.system('git push --tags')
        except Exception as ex:
            print(ex)

        sys.exit()


class UploadTestCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError as ex:
            print(ex)

        try:
            self.status('Building Source and Wheel (universal) distribution…')
            os.system('{0} setup.py build bdist bdist_egg bdist_wheel --universal'.format(sys.executable))

            self.status('Uploading the package to PyPI via Twine…')
            os.system('twine upload --repository-url https://test.pypi.org/legacy/ dist/*')

        except Exception as ex:
            print(ex)

        sys.exit()


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    zip_safe=True,
    url=URL,
    download_url=URL,
    keywords=KEYWORDS,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    # 填写你的模块py文件，就是要打包的python文件列表
    # py_modules=['mypackage'],
    license=LICENSE,
    platforms=['any'],
    install_requires=REQUIRED,  # 依赖库
    extras_require=EXTRAS,
    include_package_data=True,
    package_data={
        '': ['*.py', '*.json']
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
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
        # that you indicate whether you support Python 3 and high.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    entry_points={
        'console_scripts': [
            'dict = dictfire:main',
        ],
        # 'distutils.commands': [' my_command=my.command.module.Class'],
    },
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
        'uploadtest': UploadTestCommand,
    },
)

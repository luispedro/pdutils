# -*- coding: utf-8 -*-
# Copyright (C) 2015, Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from __future__ import division
try:
    import setuptools
except:
    print('''
setuptools not found.

On linux, the package is often called python-setuptools''')
    from sys import exit
    exit(1)
import os


exec(compile(open('pdutils/pdutils_version.py').read(),
             'pdutils/pdutils_version.py', 'exec'))

try:
    long_description = open('README.rst', encoding='utf-8').read()
except:
    long_description = open('README.rst').read()


packages = setuptools.find_packages()

install_requires = open('requirements.txt').read()
tests_require = open('tests-requirements.txt').read()


classifiers = [
'Intended Audience :: Developers',
'Intended Audience :: Science/Research',
'Topic :: Software Development :: Libraries',
'Programming Language :: Python',
'Operating System :: OS Independent',
'License :: OSI Approved :: MIT License',
]

setuptools.setup(name = 'pdutils',
      version = __version__,
      description = 'Pandas Utilities',
      long_description = long_description,
      author = 'Luis Pedro Coelho',
      author_email = 'luis@luispedro.org',
      license = 'MIT',
      platforms = ['Any'],
      classifiers = classifiers,
      packages = packages,
      test_suite = 'nose.collector',
      install_requires = install_requires,
      tests_require = tests_require
      )


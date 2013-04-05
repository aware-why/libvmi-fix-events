#!/usr/bin/env python
"""
PyVMI is a python language wrapper for the LibVMI Library. The LibVMI Library
is an introspection library that simplifies access to memory in a target
virtual machine or in a file containing a dump of a system's physical memory.

Author: Bryan D. Payne (bdpayne@acm.org)

Copyright 2013 Bryan D. Payne

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from setuptools import setup

__about__ = {}

with open('pyvmi/__about__.py') as fp:
    exec(fp.read(), None, __about__)


try:
    import pyvmi.interface
except ImportError:
    # installing - there is no cffi yet
    ext_modules = []
else:
    # building bdist - cffi is here!
    ext_modules = [pyvmi.interface.ffi.verifier.get_extension()]


setup(
    name=__about__['__title__'],
    version=__about__['__version__'],

    description=__about__['__summary__'],
    long_description=open('README').read(),
    url=__about__['__uri__'],
    license=open('LICENSE').read(),

    author=__about__['__author__'],
    author_email=__about__['__email__'],

    install_requires=[
        'cffi',
    ],
    extras_require={
        'tests': [
            'pep8',
            'pylint',
            'pytest',
        ],
    },
    tests_require=[
        'pytest',
    ],

    packages=[
        'pyvmi',
    ],

    package_data={
        'pyvmi': [
            'interface.h'
        ]
    },

    ext_package='pyvmi',
    ext_modules=ext_modules,

    zip_safe=False,
)

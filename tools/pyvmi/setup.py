#!/usr/bin/env python
from setuptools import setup

__about__ = {}

with open("pyvmi/__about__.py") as fp:
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
    name=__about__["__title__"],
    version=__about__["__version__"],

    description=__about__["__summary__"],
    long_description=open("README").read(),
    url=__about__["__uri__"],
    license=open('COPYING.LESSER').read(),

    author=__about__["__author__"],
    author_email=__about__["__email__"],

    install_requires=[
        "cffi",
    ],
    extras_require={
        "tests": [
            "pep8",
            "pylint",
            "pytest",
        ],
    },
    tests_require=[
        "pytest",
    ],

    packages=[
        "pyvmi",
    ],

    ext_package="pyvmi",
    ext_modules=ext_modules,

    zip_safe=False,
)

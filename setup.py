#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from distutils.spawn import spawn
from distutils.command import build

import versioneer

class build_doc(build.build):
    description = "build documentation"

    def run(self):
        spawn(['make', '-C', 'docs', 'html'])

packages = [
    'pycudalib',
    'pycudalib.blas',
    'pycudalib.fft',
    'pycudalib.rand',
    'pycudalib.sparse',
    'pycudalib.sorting',
    'pycudalib.utils',
    'pycudalib.tests',
]

cmdclass = versioneer.get_cmdclass()
cmdclass['build_doc'] = build_doc

if __name__ == '__main__':
    setup(
        name='pycudalib',
        description='Pycudalib - python bindings for NVIDIA CUDA libraries',
        author='Continuum Analytics, Inc.',
        author_email='support@continuum.io',
        url='http://continuum.io',
        packages=packages,
        license='BSD',
        version=versioneer.get_version(),
        cmdclass=cmdclass,
    )

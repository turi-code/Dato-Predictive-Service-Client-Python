#!/usr/bin/env python

"""
Copyright 2015 Dato, Inc.

Licensed under the 3-Clause BSD License.
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://github.com/dato-code/Dato-Predictive-Service-Client-Python/raw/master/LICENSE

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import sys
import glob
import subprocess
from setuptools import setup, find_packages

PACKAGE_NAME="dato-predictive-service-client"
VERSION="1.0.0"

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

if __name__ == '__main__':
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        author='Dato, Inc.',
        author_email='support@dato.com',
        packages=find_packages(),
        url='https://github.com/dato-code/Dato-Predictive-Service-Client-Python',
        license='LICENSE',
        description='Dato Predictive Service Client makes it easy to make REST API calls to Dato Predictive Services',
        long_description=long_description,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Financial and Insurance Industry",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Other Audience",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Natural Language :: English",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Operating System :: POSIX :: BSD",
            "Operating System :: Unix",
            "Programming Language :: Python :: 2.7",
            "Topic :: Scientific/Engineering",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
            "Topic :: Scientific/Engineering :: Information Analysis",
        ],
        install_requires=[
            "requests == 2.3.0",
        ],
    )

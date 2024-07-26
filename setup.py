#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2023 Mindbaz
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os;

from setuptools import setup;
from sms.counter import __version__;

with open ( os.path.join ( os.path.dirname ( os.path.abspath ( __file__ ) ), 'README.md' ) , 'r', encoding='utf-8' ) as fh:
    long_description = fh.read ();

setup (
    name = 'sms-counter',
    version = __version__,
    description = 'SMS Character Counter',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Sweego-io/python-sms-counter',
    author = 'Valentin Henon',
    author_email = 'vhenon@mindbaz.com',
    python_requires = '>=3.9',
    license = 'MIT',
    packages = [
        'sms.counter'
    ],
    install_requires = [
        'pydantic'
    ],
    tests_require = [
        'nose',
        'coverage'
    ],
    test_suite = 'tests',
    zip_safe = False,
    classifiers = [
        "Programming Language :: Python :: 3.9"
    ],
);

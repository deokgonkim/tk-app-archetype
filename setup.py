#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Build and setup tool
"""

import os
import sys

sys.path.insert(0, os.path.join('src'))

from distutils.core import setup

# replace with module name
import tkapp.tkapp

# TODO need to automatify locale files.

setup(name='TkApp',
      version=tkapp.__version__,
      description='Tk App Program',
      author='Author',
      author_email='author@email',
      package_dir={'': 'src'},
      packages=['tkapp'],
      data_files=[(os.path.join('share', 'locale',' ko', 'LC_MESSAGES'),
                   os.path.join('locale', 'ko', 'LC_MESSAGES', 'tkapp.mo'))],
      scripts=['post_install.py'])

# usage
# To create windows installation executable.
# setup.py bdist_wininst

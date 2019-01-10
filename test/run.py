#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.join('..', 'src'))

import gettext

from tkapp.tkapp import main

# original locale setup is done at tkapp's __init__.py
# this will override locale directory
gettext.install('tkapp', localedir='../locale', unicode=True)

main()

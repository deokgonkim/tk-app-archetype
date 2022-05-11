# -*- coding: utf-8 -*-

__version__ = '0.1'


import locale
import os
import sys
import gettext


if sys.platform.startswith('win'):
    if os.getenv('LANG') is None:
        lang, enc = locale.getdefaultlocale()
        os.environ['LANG'] = lang

# python2
# gettext.install(__name__, unicode=True)
# python3
gettext.install(__name__)

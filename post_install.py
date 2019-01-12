# -*- coding: cp949 -*-

MODULE_NAME='tkapp.tkapp'
DISPLAY_NAME='tkapp'
DISPLAY_NAME2='Tk App'

import sys

import logging
from logging.handlers import RotatingFileHandler

import os
from os.path import dirname, join, expanduser

import time

formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('post_install')
handler = RotatingFileHandler(os.path.join(os.environ['TEMP'], 'log.txt'),
                              mode='a',
                              maxBytes=50*1024*1024,
                              backupCount=0)
handler.setFormatter(formatter)
logger.addHandler(handler)
sys.stdout = handler.stream

logger.error('Post Install Started')

pyw_executable = 'C:\\Python27\\pythonw.exe'
script_file = '-m %s' % MODULE_NAME
shortcut_file_name = '%s.lnk' % DISPLAY_NAME
shortcut_path = os.path.join(get_special_folder_path('CSIDL_DESKTOPDIRECTORY',
                             shortcut_file_name)

try:
    #help(create_shortcut)
    create_shortcut(pyw_executable,
                    DISPLAY_NAME2,
                    shortcut_path,
                    script_file)
except Exception, e:
    logger.error(e, exc_info=True)

logger.error('Post Install Ended')

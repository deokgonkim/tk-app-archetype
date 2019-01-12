# -*- coding: utf-8 -*-

import inspect
import logging
import os
import sys


def setup_path():
    sys.path.insert(0, os.path.join('..', 'src'))


def setup_logging():
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('test')
    handler = logging.FileHandler('test.log', mode='w')
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False


def test_log(message, level=logging.INFO, *args, **kwargs):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    #print('caller name:', calframe[1][3])

    logger = logging.getLogger('test')
    message = '%s - %s' % (calframe[1][3], message)
    logger.log(level, message, *args, **kwargs)


if __name__ != '__main__':
    import __builtin__
    setup_path()
    setup_logging()
    __builtin__.__dict__['log'] = test_log
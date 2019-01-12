#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test preferences
"""

import unittest

import setup_test

from tkapp.preferences import Preferences


class TestPreferences(unittest.TestCase):

    def test_get_config1(self):
        p = self._get_preferences()
        config1 = p.get_config('config1')
        self.assertIsNotNone(config1)
        log('config1 %s' % config1)

    def _get_preferences(self):
        p = Preferences()
        self.assertIsNotNone(p)
        return p


def test_1():
    print('test1')


if __name__ == '__main__':
    unittest.main()

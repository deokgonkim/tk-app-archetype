# -*- coding: utf-8 -*-
"""
Provides preferences services
"""

from ConfigParser import ConfigParser
import codecs
import logging
import os
import sys

import Tkinter as tk

from . import __name__ as app_name


DATA_PATH='.%s' % app_name
FILE_NAME='%s.ini' % app_name


class Preferences(object):
    """The class that provides preferences service
    """

    def __init__(self):
        # Set encoding for config file
        if sys.platform.startswith('win32'):
            # On windows platform, use 'cp949'
            self.encoding = 'cp949'
        else:
            # On others, use 'utf-8'
            self.encoding = 'utf-8'

    def get_config(self, name, section='DEFAULT'):
        """Returns config value for `name` in `section`
        """
        config = self._get_config()
        return config.get(section, name)

    def set_config(self, name, section='DEFAULT', value=''):
        """Set config `value` for `name` in `section`"""
        config = self._get_config()
        if not config.has_section(section):
            config.add_section(section)
        config.set(section, name, value)
        self._write_config(config)

    def default_config(self):
        """Returns default config elements
        ex. return [
            ( 'SECTION_NAME', 'CONFIG_NAME', 'DEFAULT_VALUE' ),
            ( 'SECTION_NAME', 'CONFIG_NAME', 'DEFAULT_VALUE' )
        ]
        """
        return [
            ( 'DEFAULT', 'config1', '1'),
            ( 'DEFAULT', 'config2', 'some config')
        ]

    def set_default_config(self, fp):
        """Write default configuration to config file"""
        config = ConfigParser()
        for section, option, value in self.default_config():
            if not config.has_section(section):
                if section != 'DEFAULT':
                    config.add_section(section)
            config.set(section, option, value)

        with fp as f:
            config.write(f)

    def _write_config(self, config):
        """Write config file"""
        with self._get_config_file('w') as f:
            config.write(f)

    def _get_config(self):
        """returns ConfigParser object
        Usage.
        config = self._get_config()
        value = config['SECTION_NAME']['NAME']
        """
        config = ConfigParser()
        config_file = self._get_config_path()
        with self._get_config_file('r') as f:
            config.readfp(f)
        if len(config.sections()) < 1:
            logging.info('Config file is empty - %s' % config_file)
            logging.info('Setting default config')
            self.set_default_config(self._get_config_file('w'))
        return config

    def _get_config_file(self, mode=None):
        """Returns file handler of config file.
        If config file doesn't exists, then create new one.
        """
        path = self._get_config_path()
        if not os.path.isdir(path):
            logging.info("Data directory doesn't exists, creating one")
            os.mkdir(path)
        if not os.path.isfile(os.path.join(path, FILE_NAME)):
            logging.info("Config file doesn't exists, creating file")
            self.set_default_config(codecs.open(os.path.join(path, FILE_NAME), 'w', encoding=self.encoding))

        return codecs.open(os.path.join(path, FILE_NAME), 'r' if mode is None else mode, encoding=self.encoding)

    def _get_config_path(self):
        """Returns configuration file path
        configuration file is located at ~/$STORE
        On windows, it is defaulting to C:\\Users\\username\\.appname
        """
        if 'HOME' in os.environ.keys():
            return os.path.join(os.environ['HOME'], DATA_PATH)
        if 'USERPROFILE' in os.environ.keys():
            return os.path.join(os.environ['USERPROFILE'], DATA_PATH)


class PreferencesController(object):
    """Shows Preferences window"""

    def __init__(self, parent):
        self.parent = parent
        self.window = None

    def show(self, event=None):
        self.window = self._create_window()

    def clicked_ok(self, event=None):
        self.save_preferences()
        self.window.destroy()

    def save_preferences(self):
        print('Saving preferences')

    def _create_window(self):
        self.window = w = tk.Toplevel(self.parent)
        w.transient(self.parent)
        w.lbl = tk.Label(w, text=_('Preferences'))
        w.lbl.pack(expand='yes', fill='both')
        w.btn = tk.Button(w, text=_('Ok'))
        w.btn.configure(command=self.clicked_ok)
        w.btn.pack(expand='yes', fill='both')

        return w

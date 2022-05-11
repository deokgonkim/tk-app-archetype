# -*- coding: utf-8 -*-
"""
The main module of tkapp.
"""

# python2
#import Tkinter as tk
# python3
import tkinter as tk
# python2
#import tkMessageBox
from tkinter import messagebox

from .preferences import PreferencesController


class RootWindow(tk.Tk):
    """
    The main class of tkapp
    """

    def __init__(self):
        tk.Tk.__init__(self)

        self.preference = PreferencesController(self)

        self.title(_('tkapp'))

        self.menu = tk.Menu(self)

        self.menu_file = tk.Menu(self)
        self.menu_file.add_command(label=_('Quit'), command=self.terminate, underline=0)

        self.menu_option = tk.Menu(self)
        self.menu_option.add_command(label=_('Preferences'), command=self.preference.show)

        self.menu.add_cascade(label=_('File'), menu=self.menu_file)
        self.menu.add_cascade(label=_('Option'), menu=self.menu_option)

        self.config(menu=self.menu)

        self.btn1 = tk.Button(self, text=_('Button1'))
        self.btn1.config(command=self.btn1_clicked)
        self.btn1.pack()

        self._event_binding()

    def terminate(self, event=None):
        self.destroy()

    def btn1_clicked(self):
        messagebox.showinfo(_('Button1 clicked'), _('Button1 clicked'))

    def _event_binding(self):
        self.protocol('WM_DELETE_WINDOW', self.terminate)

        self.bind('<Control-q>', self.terminate)
        self.bind('<Control-Q>', self.terminate)


def main():
    app = RootWindow()
    app.mainloop()


if __name__ == '__main__':
    main()

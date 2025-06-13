"""Provide a class for the nv_themes settings window.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from tkinter import ttk

from nvlib.gui.widgets.label_combo import LabelCombo
from nvlib.gui.widgets.modal_dialog import ModalDialog
from nvthemes.nvthemes_locale import _
import tkinter as tk


class ThemesDialog(ModalDialog):

    def __init__(self, view, prefs, extraThemes, **kw):
        super().__init__(view, **kw)

        self._ui = view
        self._prefs = prefs
        self._extraThemes = extraThemes
        self.title(_('Theme Changer'))
        window = ttk.Frame(self)
        window.pack(fill='both')

        # Combobox for theme setting.
        theme = self._ui.guiStyle.theme_use()
        themeList = list(self._ui.guiStyle.theme_names())
        themeList.sort()
        self._theme = tk.StringVar(value=theme)
        self._theme.trace('w', self._change_theme)
        themeCombobox = LabelCombo(
            window,
            text=_('GUI Theme'),
            textvariable=self._theme,
            values=themeList,
            lblWidth=20,
        )
        themeCombobox.pack(padx=5, pady=5)

        # "Close" button.
        ttk.Button(
            window, text=_('Close'),
            command=self.destroy,
        ).pack(side='right', padx=5, pady=5)

    def _change_theme(self, *args, **kwargs):
        theme = self._theme.get()
        self._prefs['gui_theme'] = theme
        if self._extraThemes:
            self._ui.guiStyle.set_theme(self._prefs['gui_theme'])
        else:
            self._ui.guiStyle.theme_use(self._prefs['gui_theme'])


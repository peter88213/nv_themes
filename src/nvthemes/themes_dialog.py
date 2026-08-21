"""Provide a class for the nv_themes settings window.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from tkinter import ttk

from nvlib.gui.widgets.modal_dialog import ModalDialog
from nvthemes.nvthemes_locale import _
import tkinter as tk


class ThemesDialog(ModalDialog):

    def __init__(self, view, prefs, extraThemes, **kw):
        super().__init__(view, **kw)

        self.title(_('Theme Changer'))
        # Combobox for theme setting.

        def change_theme(event):
            theme = themeVar.get()
            prefs['gui_theme'] = theme
            try:
                if extraThemes:
                    view.guiStyle.set_theme(prefs['gui_theme'])
                else:
                    view.guiStyle.theme_use(prefs['gui_theme'])
            except:
                pass

        themeFrame = ttk.Frame(self)
        themeFrame.pack(fill='x', expand=True, pady=2)
        ttk.Label(
            themeFrame,
            text=_('GUI Theme'),
            anchor='w',
            width=20,
        ).pack(
            side='left',
            padx=5,
        )

        theme = view.guiStyle.theme_use()
        themeList = list(view.guiStyle.theme_names())
        themeList.sort()
        themeVar = tk.StringVar(value=theme)
        themeCombobox = ttk.Combobox(
            themeFrame,
            textvariable=themeVar,
            values=themeList,
        )
        themeCombobox.pack(padx=5, pady=5)
        themeCombobox.bind('<<ComboboxSelected>>', change_theme)

        footer = tk.Frame(self)
        footer.pack(fill='both')

        # "Close" button.
        ttk.Button(
            footer,
            text=_('Close'),
            command=self.destroy,
        ).pack(side='right', padx=5, pady=5)


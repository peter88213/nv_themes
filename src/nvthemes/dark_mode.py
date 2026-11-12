"""Provide a class for the nv_themes dark mode color settings.

Copyright (c) 2026 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from tkinter import messagebox

from nvlib.gui.default_colors import DEFAULT_COLORS
from nvlib.gui.dark_mode_colors import DARK_MODE_COLORS
from nvthemes.nvthemes_locale import _


class DarkMode:

    @classmethod
    def set_colors(cls, prefs):
        """Set colors for a dark mode."""
        colorsChanged = False
        for color in DARK_MODE_COLORS:
            if prefs.get(
                color,
                DARK_MODE_COLORS[color]
            ) != DARK_MODE_COLORS[color]:
                prefs[color] = DARK_MODE_COLORS[color]
                colorsChanged = True
        if colorsChanged:
            cls._show_message(_('Dark mode selected'))

    @classmethod
    def reset_colors(cls, prefs):
        """Reset colors to defaults"""
        colorsChanged = False
        for color in DARK_MODE_COLORS:
            if prefs.get(
                color,
                DEFAULT_COLORS[color]
            ) != DEFAULT_COLORS[color]:
                prefs[color] = DEFAULT_COLORS[color]
                colorsChanged = True
        if colorsChanged:
            cls._show_message(_('Bright mode selected'))

    @classmethod
    def _show_message(cls, detail):
        messagebox.showinfo(
            title=_('Theme changed'),
            message=_('Please restart novelibre now to apply changed colors'),
            detail=detail,
        )

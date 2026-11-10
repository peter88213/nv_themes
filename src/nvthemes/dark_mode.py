"""Provide a class for the nv_themes dark mode color settings.

Copyright (c) 2026 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from tkinter import messagebox

from nvlib.gui.default_colors import DEFAULT_COLORS
from nvthemes.nvthemes_locale import _


class DarkMode:

    COLORS = dict(
        color_1st_edit='#eead0e',  # DarkGoldenrod2
        color_2nd_edit='#cd950c',  # DarkGoldenrod3
        color_before_schedule='#2e8b57',  # sea green
        color_behind_schedule='#ff6347',  # tomato
        color_chapter='#7fff00',  # chartreuse
        color_comment_tag='#8b7e66',  # wheat4
        color_done='#8b6508',  # DarkGoldenrod4
        color_draft='#ffffff',  # white
        color_highlight='#2f4f4f',  # dark slate gray
        color_inactive_bg='#394341',
        color_locked_bg='#696969',  # dim gray
        color_locked_fg='#d3d3d3',  # light gray
        color_modified_bg='#ffc125',  # goldenrod1
        color_modified_fg='#b03060',  # maroon
        color_notes_bg='#8b7e66',  # wheat4
        color_notes_fg='#ffffff',  # white
        color_on_schedule='#ffffff',  # white
        color_outline='#ee7ae9',  # orchid2
        color_separator='#000000',  # black
        color_stage='#ff6347',  # tomato
        color_status_error_bg='#ff0000',  # red
        color_status_error_fg='#ffffff',  # white
        color_status_notification_bg='#ffff00',  # yellow
        color_status_notification_fg='#000000',  # black
        color_status_success_bg='#008b00',  # green4
        color_status_success_fg='#ffffff',  # white
        color_text_bg='#424242',
        color_text_fg='#d3d3d3',  # light gray
        color_unused='#808080',
        color_xml_tag='#6495ed',  # cornflower blue
    )

    @classmethod
    def set_colors(cls, prefs):
        """Set colors for a dark mode."""
        colorsChanged = False
        for color in cls.COLORS:
            if prefs.get(
                color,
                cls.COLORS[color]
            ) != cls.COLORS[color]:
                prefs[color] = cls.COLORS[color]
                colorsChanged = True
        if colorsChanged:
            cls._show_message(_('Dark mode selected'))

    @classmethod
    def reset_colors(cls, prefs):
        """Reset colors to defaults"""
        colorsChanged = False
        for color in cls.COLORS:
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

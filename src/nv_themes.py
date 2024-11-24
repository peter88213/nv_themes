"""A 'Theme Changer' plugin for novelibre.

Version @release

Adds a 'Theme Changer' entry to the 'Tools' menu to open a window
with a combobox that lists all available themes. 
The selected theme will be persistently applied.  

To have a wider choice, you may want to install the ttkthemes package:

pip install ttkthemes

Requires Python 3.6+
Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from nvlib.controller.plugin.plugin_base import PluginBase
from nvthemeslib.nvthemes_globals import _
from nvthemeslib.themes_window import ThemesWindow

try:
    from ttkthemes import ThemedStyle
    extraThemes = True
except ModuleNotFoundError:
    extraThemes = False


class Plugin(PluginBase):
    """A 'Theme Changer' plugin class."""
    VERSION = '@release'
    API_VERSION = '5.0'
    DESCRIPTION = 'Allows changing between available themes'
    URL = 'https://github.com/peter88213/nv_themes'

    def install(self, model, view, controller):
        """Add a submenu to the 'Tools' menu.
        
        Positional arguments:
            model -- reference to the main model instance of the application.
            view -- reference to the main view instance of the application.
            controller -- reference to the main controller instance of the application.

        Optional arguments:
            prefs -- deprecated. Please use controller.get_preferences() instead.
        
        Extends the superclass method.
        """
        super().install(model, view, controller)
        prefs = controller.get_preferences()
        if extraThemes:
            view.guiStyle = ThemedStyle(view.root)
        if not prefs.get('gui_theme', ''):
            prefs['gui_theme'] = view.guiStyle.theme_use()

        if not prefs['gui_theme'] in view.guiStyle.theme_names():
            prefs['gui_theme'] = view.guiStyle.theme_use()
        if extraThemes:
            view.guiStyle.set_theme(prefs['gui_theme'])
        else:
            view.guiStyle.theme_use(prefs['gui_theme'])

        # Create a submenu
        view.viewMenu.insert_command(
            _('Options'),
            label=_('Change theme'),
            command=lambda: ThemesWindow(view, prefs, extraThemes)
            )
        view.viewMenu.insert_separator(_('Options'))


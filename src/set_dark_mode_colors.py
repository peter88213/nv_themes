#!/usr/bin/python3
"""Set dark mode colors for novelibre. 

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from configparser import ConfigParser
from pathlib import Path

COLORS = dict(
    color_1st_edit='DarkGoldenrod2',
    color_2nd_edit='DarkGoldenrod3',
    color_arc='plum',
    color_before_schedule='sea green',
    color_behind_schedule='tomato',
    color_chapter='chartreuse',
    color_comment_tag='wheat4',
    color_done='DarkGoldenrod4',
    color_draft='white',
    color_locked_bg='dim gray',
    color_locked_fg='light gray',
    color_major='SteelBlue1',
    color_minor='SteelBlue',
    color_modified_bg='goldenrod1',
    color_modified_fg='maroon',
    color_notes_bg='wheat4',
    color_notes_fg='white',
    color_on_schedule='white',
    color_outline='orchid2',
    color_stage='tomato',
    color_text_bg='#33393b',
    color_text_fg='light grey',
    color_unused='gray',
)

print(f'Setting up the dark mode colors. Please make sure novelibre is not running.')
homePath = str(Path.home()).replace('\\', '/')
applicationDir = f'{homePath}/.novx'
iniFile = f'{applicationDir}/config/novx.ini'
config = ConfigParser()
config.read(iniFile, encoding='utf-8')
for color in COLORS:
    config['SETTINGS'][color] = COLORS[color]
with open(iniFile, 'w', encoding='utf-8') as f:
    config.write(f)
print('Dark mode colors successfully set.')


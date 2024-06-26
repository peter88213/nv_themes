"""Build a nv_themes plugin.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib project (see https://github.com/peter88213/novxlib)
must be located on the same directory level as the nv_themes project. 

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../novxlib/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}nv_themes.py'
TARGET_FILE = f'{BUILD}nv_themes.py'

os.makedirs(BUILD, exist_ok=True)


def main():
    os.makedirs(BUILD, exist_ok=True)
    inliner.run(SOURCE_FILE, TARGET_FILE, 'nvthemeslib', '../../nv_themes/src/')
    inliner.run(TARGET_FILE, TARGET_FILE, 'nvlib', '../../novelibre/src/')
    print('Done.')


if __name__ == '__main__':
    main()

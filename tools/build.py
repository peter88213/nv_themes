"""Build the nv_themes novelibre plugin package.
        
Note: VERSION must be updated manually before starting this script.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_themes
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')
from package_builder import PackageBuilder

VERSION = '5.0.4'


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_themes'
    LOCAL_LIB = 'nvthemes'
    GERMAN_TRANSLATION = True

    def __init__(self, version):
        super().__init__(version)
        self.distFiles.append(
            (f'{self.sourceDir}set_dark_mode_colors.py', self.buildDir)
        )
        self.distFiles.append(
            (f'{self.sourceDir}restore_default_colors.py', self.buildDir)
        )


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()

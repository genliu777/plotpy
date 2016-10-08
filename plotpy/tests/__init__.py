# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""
plotpy test package
===================
"""

def run():
    """Run plotpy test launcher"""
    import plotpy.config # Loading icons
    from plotpy.guitest import run_testlauncher
    run_testlauncher(plotpy)

if __name__ == '__main__':
    run()
    
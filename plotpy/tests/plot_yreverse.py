# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""Reverse y-axis test for curve plotting"""

SHOW = False # Do not show test in GUI-based test launcher

from plotpy.plot import CurveDialog
from plotpy.builder import make

def test():
    """Test"""
    # -- Create QApplication
    import plotpy
    _app = plotpy.qapplication()
    # --
    import numpy as np
    x = np.linspace(-10, 10, 200)
    y = x*np.exp(-x)
    item = make.curve(x, y, color="b")
    
    win = CurveDialog()
    plot = win.get_plot()
    plot.add_item(item)
    plot.set_axis_direction("left", True)
    plot.set_axis_direction("bottom", True)
    win.show()
    win.exec_()

if __name__ == "__main__":
    test()

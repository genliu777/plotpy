# -*- coding: utf-8 -*-
#
# Copyright © 2009-2011 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""
guiqwt.transitional
-------------------

The purpose of this transitional package is to regroup all the references to 
the ``PyQwt`` library.

No other ``guiqwt`` module should import ``PyQwt`` or use any of its 
interfaces directly.
"""

from __future__ import print_function
import sys

print("Using experimental 'pure Python' qwt API", file=sys.stderr)
from qwt import (QwtPlot, QwtSymbol, QwtLinearScaleEngine, QwtLogScaleEngine,
                 QwtText, QwtPlotCanvas, QwtLinearColorMap, QwtDoubleInterval,
                 toQImage, QwtPlotGrid, QwtPlotItem, QwtScaleMap, QwtPlotCurve,
                 QwtPlotMarker, QwtPlotRenderer, QwtLog10ScaleEngine,
                 QwtPlotPrintFilter)

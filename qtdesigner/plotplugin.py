# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""
plotplugin
==========

A plotpy plot widget plugin for Qt Designer
"""

from plotpy.qtdesigner import create_qtdesigner_plugin
Plugin = create_qtdesigner_plugin("plotpy", "plotpy.plot", "CurveWidget",
                                  icon="curve.png")

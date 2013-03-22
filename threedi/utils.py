# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import os

from threedi import config


def get_netcdf_path(layer):
    """ Return path to netcdf from layer. """
    names = os.listdir(os.path.join(config.DATA_DIR, layer))
    # Look for netcdf
    for name in names:
        if os.path.splitext(name)[1].lower() == '.nc':
            return os.path.join(config.DATA_DIR, layer, name)


def get_bathymetry_path(layer):
    """
    Return path to bathymetry from layer.

    Prefers geotiff above aaigrid.
    """
    names = os.listdir(os.path.join(config.DATA_DIR, layer))
    # Look for geotiff
    for name in names:
        if os.path.splitext(name)[1].lower() in ('.tif', '.tiff'):
            return os.path.join(config.DATA_DIR, layer, name)
    for name in names:
    # Look for aaigrid
        if os.path.splitext(name)[1].lower() in ('.asc'):
            return os.path.join(config.DATA_DIR, layer, name)


def get_pyramid_path(layer):
    """ Return pyramid path. """
    return os.path.join(config.CACHE_DIR, layer, 'pyramid')


def get_monolith_path(layer):
    """ Return monolith path. """
    return os.path.join(config.CACHE_DIR, layer, 'monolith')

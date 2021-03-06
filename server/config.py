# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import os

# Register your backends here
BLUEPRINTS = [
    'threedi_wms.threedi',
    'threedi_wms.rasterinfo',
]

# Directories
BUILDOUT_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..',
)
CACHE_DIR = os.path.join(BUILDOUT_DIR, 'var', 'cache')
CELERY_DIR = os.path.join(BUILDOUT_DIR, 'var', 'celery')
DATA_DIR = os.path.join(BUILDOUT_DIR, 'var', 'data')
LOG_DIR = os.path.join(BUILDOUT_DIR, 'var', 'log')

# Celery
CELERY_DB = os.path.join(CELERY_DIR, 'celerydb.sqlite')

# Import local settings
try:
    from threedi_server.localconfig import *
except ImportError:
    pass

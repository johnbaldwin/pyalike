# -*- coding: utf-8 -*-

"""
Pyalike Directory and File comparison library

Example:
   >>> import pyalike
   >>> somewhere = pyalike.make_digest('/path/to/somewhere')
   >>> elsewhere = pyalike.make_digest('/path/to/elsewhere')
   >>> diff = pyalike.diff(somewhere,elsewhere)
   >>> # add snippet of diff.dump


"""

__title__ = 'pyalike'
__version__ = '0.0.1'
__author__ = 'John Baldwin'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 John Baldwin'



FSO_FILE = 0
FSO_DIR = 1
FSO_LINK = 2


from .core import make_digest, diff
from .db import DB


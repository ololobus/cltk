"""The Classical Language Toolkit (CLTK) offers natural language
processing support for Classical languages. See the webpage for
more information and documentation: http://cltk.org
"""

import sys
from pkg_resources import get_distribution

if sys.version_info[0] != 3:
    raise ImportError('Python Version 3 or above is required for cltk.')

__author__ = 'Kyle P. Johnson et al.'

__copyright__ = 'Copyright (c) 2016 Kyle P. Johnson. Distributed and Licensed under the MIT License.'  # pylint: disable=line-too-long

__description__ = __doc__

with open('LICENSE') as file_open:
    __license__ = file_open.read()

__url__ = 'http://cltk.org'

__version__ = get_distribution('cltk').version  # pylint: disable=no-member

# rm these namespaces from memory, or these show up in dir(cltk)
del file_open
del get_distribution
del sys

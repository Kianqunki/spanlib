#################################################################################
# File: __init__.py
#
# This file is part of the SpanLib library.
# Copyright (C) 2006-2013  Stephane Raynaud, Charles Doutriaux
# Contact: stephane dot raynaud at gmail dot com
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#################################################################################
from .analyzer import *
from .filler import *
from .util import *
import spanlib.analyzer
del docs
__version__ = "2.3.0"

__all__ = ['Data', 'Dataset', 'Analyzer', 'SVDModel', 'RedNoise', 'Filler',
    'freqfilter', 'SpanlibError', 'phase_composites']

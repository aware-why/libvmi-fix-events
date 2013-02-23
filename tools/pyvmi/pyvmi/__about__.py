# pylint: disable=C0301
"""
PyVMI is a python wrapper around the LibVMI Library, with some added niceties
to make it more suitable for python programmers.  For more information on
LibVMI and PyVMI, see http://www.libvmi.com.

Author: Bryan D. Payne (bdpayne@acm.org)

This file is part of PyVMI.

LibVMI is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

LibVMI is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
License for more details.

You should have received a copy of the GNU Lesser General Public License
along with LibVMI.  If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__copyright__",
]

__title__ = "pyvmi"
__summary__ = "Python binding to LibVMI"
__uri__ = "http://www.libvmi.com"

__version__ = "0.9.0"

__author__ = "Bryan D. Payne"
__email__ = "bdpayne@acm.org"

__copyright__ = "Copyright 2012 Bryan Payne"

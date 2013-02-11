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

__title__ = 'pyvmi'
__version__ = '0.10.0'
__author__ = 'Bryan D. Payne'
__license__ = 'LGPL 3.0'
__copyright__ = 'Copyright 2013 Bryan Payne'

from .core import vmi_init

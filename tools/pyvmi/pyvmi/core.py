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

"""
For reference:
    http://docs.python.org/2/reference/datamodel.html
"""
class vmi_init(object):
    def __init__(self, name):
        # call init from capi, save vmi object as class var self.vmi
        pass

    def __del__(self):
        pass

    def __enter__(self):
        return self.vmi

    def __exit__(self, type, value traceback):
        pass

    def __str__(self):
        pass

    def __getitem__(self, key):
        pass

    def _addrlen(self):
        #return 4 for 32-bit systems, 8 for 64-bit systems

    def read(self, pa=None, va=None, ksym=None,
             size=self._addrlen, string=False):
        pass

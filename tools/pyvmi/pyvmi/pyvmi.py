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

import struct
from .libvmi import Libvmi, C


class Pyvmi(object):
    offset_names = {
            'Linux': {
                'tasks_offset': 'linux_tasks',
                'mm_offset': 'linux_mm',
                'pid_offset': 'linux_pid',
                'name_offset': 'linux_name',
                'pgd_offset': 'linux_pgd',
                },
            'Windows': {
                'tasks_offset': 'win_tasks',
                'pdbase_offset': 'win_pdbase',
                'pid_offset': 'win_pid',
                'name_offset': 'win_pname',
                },
            }

    def __init__(self, name):
        self.vmi = Libvmi().init(C.VMI_AUTO | C.VMI_INIT_COMPLETE, name)

    def __del__(self):
        self.vmi.destroy()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.vmi.destroy()

    def __str__(self):
        pass

    def _get_offset_ref(self, os, key):
        try:
            return self.offset_names[os][key]
        except KeyError:
            return None

    def __getitem__(self, key):
        # Set the os type value
        os = self.vmi.get_ostype()
        if (os == C.VMI_OS_LINUX or os == 'VMI_OS_LINUX'):
            os = 'Linux'
        elif (os == C.VMI_OS_WINDOWS or os == 'VMI_OS_WINDOWS'):
            os = 'Windows'
        else:
            os = 'Unknown'

        # Return os type, if requested
        if key == 'ostype':
            return os

        # Return offset, if requested
        offset_ref = self._get_offset_ref(os, key)
        if offset_ref:
            return self.vmi.get_offset(offset_ref)

        raise KeyError

    def _addrlen(self):
        """return 4 for 32-bit systems, 8 for 64-bit systems"""
        mode = self.vmi.get_page_mode()
        if (mode == C.VMI_PM_IA32E or mode == 'VMI_PM_IA32E'):
            return 8
        else:
            return 4

    def translate(self, ksym=None, va=None, pid=0):
        if ksym:
            return self.vmi.translate_ksym2v(ksym)
        elif va:
            return self.vmi.translate_uv2p(va, pid)

    def read(self, pa=None, va=None, ksym=None, pid=0, size=None, string=False):
        if not size:
            size = self._addrlen()

        if pa:
            if string:
                buf = self.vmi.read_str_pa(pa)
            else:
                buf = self.vmi.read_pa(pa, size)
        elif va:
            if string:
                buf = self.vmi.read_str_va(va, pid)
            else:
                buf = self.vmi.read_va(va, pid, size)
        elif ksym:
            if string:
                buf = self.vmi.read_str_ksym(ksym)
            else:
                buf = self.vmi.read_ksym(ksym, size)

        if string:
            return buf
        elif size == 1:
            return struct.unpack('B', buf)[0]
        elif size == 2:
            return struct.unpack('H', buf)[0]
        elif size == 4:
            return struct.unpack('I', buf)[0]
        elif size == 8:
            return struct.unpack('Q', buf)[0]
        else:
            return struct.unpack('s#', buf)[0]

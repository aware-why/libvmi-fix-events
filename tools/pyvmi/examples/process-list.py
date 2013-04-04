#!/usr/bin/env python
"""
The LibVMI Library is an introspection library that simplifies access to
memory in a target virtual machine or in a file containing a dump of
a system's physical memory.  LibVMI is based on the XenAccess Library.

Copyright 2011 Sandia Corporation. Under the terms of Contract
DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government
retains certain rights in this software.

Author: Bryan D. Payne (bdpayne@acm.org)

This file is part of LibVMI.

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
import pyvmi
import sys


def get_processes(vmi):
    if vmi['ostype'] == 'Linux':
        current_process = vmi.translate(ksym='init_task')
    elif vmi['ostype'] == 'Windows':
        current_process = vmi.read(ksym='PsInitialSystemProcess')

    list_head = current_process + vmi['tasks_offset']
    next_list_entry = vmi.read(va=list_head)

    while (next_list_entry != list_head):
        yield(current_process)
        current_process = next_list_entry - vmi['tasks_offset']
        next_list_entry = vmi.read(va=next_list_entry)


def get_pid_and_proc(vmi):
    process_structs = get_processes(vmi)
    for struct in process_structs:
        procname = vmi.read(va=struct + vmi['name_offset'], string=True)
        pid = vmi.read(va=struct + vmi['pid_offset'], size=4)
        if (pid < 1<<16):
            yield pid, procname


def main(argv):
    with pyvmi.init(argv[1]) as vmi:
        for pid, procname in get_pid_and_proc(vmi):
            print "[%5d] %s" % (pid, procname)


if __name__ == "__main__":
    main(sys.argv)

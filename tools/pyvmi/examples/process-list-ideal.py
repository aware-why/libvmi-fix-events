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


"""
def get_processes(vmi):
    tasks_offset = vmi.get_offset("win_tasks")
    name_offset = vmi.get_offset("win_pname") - tasks_offset
    pid_offset = vmi.get_offset("win_pid") - tasks_offset

    list_head = vmi.read_addr_ksym("PsInitialSystemProcess")
    next_process = vmi.read_addr_va(list_head + tasks_offset, 0)
    list_head = next_process

    while True:
        procname = vmi.read_str_va(next_process + name_offset, 0)
        pid = vmi.read_32_va(next_process + pid_offset, 0)
        next_process = vmi.read_addr_va(next_process, 0)

        if (pid < 1<<16):
            yield pid, procname
        if (list_head == next_process):
            break
"""


## work in progress below
def get_processes(vmi, head_sym):
    list_head = vmi.read(ksym=head_sym)
    next_process = vmi.read(va=list_head + vmi['list_offset'])

    while list_head != next_process:
        yield (next_process - vmi['list_offset'])
        next_process = vmi.read(va=next_process)


def get_pid_and_proc(vmi):
    if vmi['ostype'] == 'Windows':
        head_sym = 'PsInitialSystemProcess'
    elif vmi['ostype'] == 'Linux':
        head_sym = 'init_task'
    else:
        print 'Invalid or missing OS type.'
        return

    process_structs = get_processes(vmi, head_sym)
    for struct in process_structs:
        procname = vmi.read(va=struct + vmi['name_offset'], string=True)
        pid = vmi.read(va=struct + vmi['pid_offset'], size=4)
        yield pid, procname


def main(argv):
    with vmi_init(argv[1]) as vmi:
        for pid, procname in get_pid_and_proc(vmi):
            print "[%5d] %s" % (pid, procname)


if __name__ == "__main__":
    main(sys.argv)

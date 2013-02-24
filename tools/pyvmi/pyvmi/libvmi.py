"""
CFFI interface to LibVMI
"""
from .interface import ffi, lib
from .exceptions import LibvmiError


# Define functions local to this module for easier calling
class Libvmi(object):
    def __init__(self, name, flags):
        self.vmi = ffi.new('vmi_instance_t *')
        if not lib.vmi_init(self.vmi, lib.VMI_AUTO | lib.VMI_INIT_COMPLETE, name):
            raise LibvmiError()

    def get_offset(self, name):
        return lib.vmi_get_offset(self.vmi[0], name)

    def read_addr_ksym(self, sym):
        value = ffi.new('addr_t *')
        if not lib.vmi_read_addr_ksym(self.vmi[0], sym, value):
            raise LibvmiError()
        return value[0]

    def read_addr_va(self, va, pid):
        value = ffi.new('addr_t *')
        if not lib.vmi_read_addr_va(self.vmi[0], va, pid, value):
            raise LibvmiError()
        return value[0]

    def read_32_va(self, va, pid):
        value = ffi.new('uint32_t *')
        if not lib.vmi_read_32_va(self.vmi[0], va, pid, value):
            raise LibvmiError()
        return value[0]

    def read_str_va(self, va, pid):
        value = lib.vmi_read_str_va(self.vmi[0], va, pid)
        return ffi.string(value)

"""
Low-level LibVMI access from Python
"""
from .interface import ffi, lib
from .exceptions import LibvmiError


# Define functions local to this module for easier calling
class Libvmi(object):
    def __init__(self, name, flags):
        pass

    #
    # Init and destruct
    #
    def init(self, flags, name):
        self.vmi = ffi.new('vmi_instance_t *')
        if not lib.vmi_init(self.vmi, lib.VMI_AUTO | lib.VMI_INIT_COMPLETE, name):
            raise LibvmiError()

    def init_custom(self, flags, config):
        pass

    def init_complete(self, config):
        pass

    def init_complete_custom(self, config):
        pass

    def destroy(self):
        pass

    #
    # Memory translation
    #
    def translate_kv2p(self, vaddr):
        pass

    def translate_uv2p(self, vaddr, pid):
        pass

    def translate_ksym2v(self, symbol):
        pass

    def pid_to_dtb(self, pid):
        pass

    def pagetable_lookup(self, dtb, vaddr):
        pass

    #
    # Memory read
    #
    def read_ksym(self, sym, count):
        pass

    def read_va(self, vaddr, pid, count):
        pass

    def read_pa(self, paddr, count):
        pass

    def read_8_ksym(self, sym):
        pass

    def read_16_ksym(self, sym):
        pass

    def read_32_ksym(self, sym):
        pass

    def read_64_ksym(self, sym):
        pass

    def read_addr_ksym(self, sym):
        value = ffi.new('addr_t *')
        if not lib.vmi_read_addr_ksym(self.vmi[0], sym, value):
            raise LibvmiError()
        return value[0]

    def read_str_ksym(self, sym):
        pass

    def read_8_va(self, vaddr, pid):
        pass

    def read_16_va(self, vaddr, pid):
        pass

    def read_32_va(self, vaddr, pid):
        value = ffi.new('uint32_t *')
        if not lib.vmi_read_32_va(self.vmi[0], vaddr, pid, value):
            raise LibvmiError()
        return value[0]

    def read_64_va(self, vaddr, pid):
        pass

    def read_addr_va(self, vaddr, pid):
        value = ffi.new('addr_t *')
        if not lib.vmi_read_addr_va(self.vmi[0], vaddr, pid, value):
            raise LibvmiError()
        return value[0]

    def read_str_va(self, vaddr, pid):
        value = lib.vmi_read_str_va(self.vmi[0], vaddr, pid)
        return ffi.string(value)

    def read_unicode_str_va(self, vaddr, pid):
        pass

    def free_unicode_str(self, p_us):
        pass

    def read_8_pa(self, paddr):
        pass

    def read_16_pa(self, paddr):
        pass

    def read_32_pa(self, paddr):
        pass

    def read_64_pa(self, paddr):
        pass

    def read_addr_pa(self, paddr):
        pass

    def read_str_pa(self, paddr):
        pass

    #
    # Memory write
    #

    #
    # Others
    #
    def get_offset(self, name):
        return lib.vmi_get_offset(self.vmi[0], name)


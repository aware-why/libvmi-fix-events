"""
CFFI interface to LibVMI
"""
import functools
import os

from cffi import FFI, VerificationError


INTERFACE_H = os.path.dirname(os.path.abspath(__file__)) + '/interface.h'
__all__ = ["ffi", "lib"]


# Setup CFFI with LibVMI
ffi = FFI()

ffi.cdef(open(INTERFACE_H, 'r').read())
lib = ffi.verify('#include <libvmi/libvmi.h>', libraries=['vmi'])


# Convert return values from LibVMI
#  :VMI_SUCCESS --> True
#  :VMI_FAILURE --> False
def wrap_libvmi_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return (ret == lib.VMI_SUCCESS or  # cffi >= 0.6
                ret == 'VMI_SUCCESS')      # cffi <= 0.5
    return wrapper


# wrap functions that return status_t
lib.vmi_init = wrap_libvmi_func(lib.vmi_init)
lib.vmi_init_custom = wrap_libvmi_func(lib.vmi_init_custom)
lib.vmi_init_complete = wrap_libvmi_func(lib.vmi_init_complete)
lib.vmi_init_complete_custom = wrap_libvmi_func(lib.vmi_init_complete_custom)
lib.vmi_destroy = wrap_libvmi_func(lib.vmi_destroy)

lib.vmi_read_8_ksym = wrap_libvmi_func(lib.vmi_read_8_ksym)
lib.vmi_read_16_ksym = wrap_libvmi_func(lib.vmi_read_16_ksym)
lib.vmi_read_32_ksym = wrap_libvmi_func(lib.vmi_read_32_ksym)
lib.vmi_read_64_ksym = wrap_libvmi_func(lib.vmi_read_64_ksym)
lib.vmi_read_addr_ksym = wrap_libvmi_func(lib.vmi_read_addr_ksym)

lib.vmi_read_8_va = wrap_libvmi_func(lib.vmi_read_8_va)
lib.vmi_read_16_va = wrap_libvmi_func(lib.vmi_read_16_va)
lib.vmi_read_32_va = wrap_libvmi_func(lib.vmi_read_32_va)
lib.vmi_read_64_va = wrap_libvmi_func(lib.vmi_read_64_va)
lib.vmi_read_addr_va = wrap_libvmi_func(lib.vmi_read_addr_va)
lib.vmi_convert_str_encoding = wrap_libvmi_func(lib.vmi_convert_str_encoding)

lib.vmi_read_8_pa = wrap_libvmi_func(lib.vmi_read_8_pa)
lib.vmi_read_16_pa = wrap_libvmi_func(lib.vmi_read_16_pa)
lib.vmi_read_32_pa = wrap_libvmi_func(lib.vmi_read_32_pa)
lib.vmi_read_64_pa = wrap_libvmi_func(lib.vmi_read_64_pa)
lib.vmi_read_addr_pa = wrap_libvmi_func(lib.vmi_read_addr_pa)

lib.vmi_write_8_ksym = wrap_libvmi_func(lib.vmi_write_8_ksym)
lib.vmi_write_16_ksym = wrap_libvmi_func(lib.vmi_write_16_ksym)
lib.vmi_write_32_ksym = wrap_libvmi_func(lib.vmi_write_32_ksym)
lib.vmi_write_64_ksym = wrap_libvmi_func(lib.vmi_write_64_ksym)

lib.vmi_write_8_va = wrap_libvmi_func(lib.vmi_write_8_va)
lib.vmi_write_16_va = wrap_libvmi_func(lib.vmi_write_16_va)
lib.vmi_write_32_va = wrap_libvmi_func(lib.vmi_write_32_va)
lib.vmi_write_64_va = wrap_libvmi_func(lib.vmi_write_64_va)

lib.vmi_write_8_pa = wrap_libvmi_func(lib.vmi_write_8_pa)
lib.vmi_write_16_pa = wrap_libvmi_func(lib.vmi_write_16_pa)
lib.vmi_write_32_pa = wrap_libvmi_func(lib.vmi_write_32_pa)
lib.vmi_write_64_pa = wrap_libvmi_func(lib.vmi_write_64_pa)

lib.vmi_get_vcpureg = wrap_libvmi_func(lib.vmi_get_vcpureg)
lib.vmi_pause_vm = wrap_libvmi_func(lib.vmi_pause_vm)
lib.vmi_resume_vm = wrap_libvmi_func(lib.vmi_resume_vm)

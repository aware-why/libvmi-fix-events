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

lib.vmi_init = wrap_libvmi_func(lib.vmi_init)

lib.vmi_read_addr_ksym = wrap_libvmi_func(lib.vmi_read_addr_ksym)
lib.vmi_read_addr_va = wrap_libvmi_func(lib.vmi_read_addr_va)
lib.vmi_read_32_va = wrap_libvmi_func(lib.vmi_read_32_va)

"""
CFFI interface to LibVMI
"""
import functools

from cffi import FFI, VerificationError


__all__ = ["ffi", "lib"]


# Setup CFFI with LibVMI
ffi = FFI()

ffi.cdef(
    # pylint: disable=C0301

    """
        typedef ... *vmi_instance_t;
        typedef enum status {
            VMI_SUCCESS,
            VMI_FAILURE
        } status_t;
        typedef uint64_t addr_t;

        #define VMI_AUTO ...
        #define VMI_INIT_COMPLETE ...

        status_t vmi_init(vmi_instance_t *vmi, uint32_t flags, char *name);
        status_t vmi_destroy(vmi_instance_t vmi);

        status_t vmi_read_addr_ksym(vmi_instance_t vmi, char *sym, addr_t *value);
        status_t vmi_read_addr_va(vmi_instance_t vmi, addr_t vaddr, int pid, addr_t *value);
        status_t vmi_read_32_va(vmi_instance_t vmi, addr_t vaddr, int pid, uint32_t * value);
        char *vmi_read_str_va(vmi_instance_t vmi, addr_t vaddr, int pid);

        unsigned long vmi_get_offset(vmi_instance_t vmi, char *offset_name);
    """
)

lib = ffi.verify(
    # pylint: disable=C0301

    """
        #include <libvmi/libvmi.h>
    """,

    libraries=['vmi']
)


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

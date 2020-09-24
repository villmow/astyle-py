from ctypes import cdll, c_char, addressof
from ctypes import c_char_p, CFUNCTYPE, c_int, c_char, addressof, c_ulong
import pathlib as pl
import os



def get_project_root() -> pl.Path:
    """Returns project root folder."""
    return pl.Path(__file__).parent.parent



###############################

# global memory allocation returned to artistic style
# must be global for CPython, not a function attribute
# did not try a class attribute but it may not work for CPython
ALLOCATED = c_char_p

def initialize_library():
    """ Set the file path and load the shared object (DLL).
        Return the handle to the shared object (DLL).
    """
    # return the handle to the shared object
    if os.name == "nt":
        pass
        # libc = load_windows_dll()
    else:
        libc = load_linux_so()
    return libc


def load_linux_so():
    """ Load the shared object for Linux platforms.
        The shared object must be in the same folder as this python script.
    """
    shared_name = get_project_root() / "build/libastyle.so"

    shared = str(pl.Path(shared_name).absolute())
    # file_ = {f for f in pl.Path().iterdir() if f.name == shared_name}

    try:
        libc = cdll.LoadLibrary(shared)
    except OSError as err:
        # "cannot open shared object file: No such file or directory"
        print(err)
        raise FileNotFoundError("Cannot find " + shared)
    return libc


# def load_windows_dll():
#     """ Load the dll for Windows platforms.
#         The shared object must be in the same folder as this python script.
#         An exception is handled if the dll bits do not match the Python
#         executable bits (32 vs 64).
#     """
#     dll_name = get_library_name()
#     dll = os.getcwd() + os.path.sep + dll_name
#     if __is_iron_python__:
#         try:
#             libc = windll.LoadLibrary(dll)
#         # exception for IronPython
#         except OSError as err:
#             print("Cannot load library", dll)
#             error("Library is not available or you may be mixing 32 and 64 bit code")
#         # exception for IronPython
#         # this sometimes occurs with IronPython during debug
#         # rerunning will probably fix
#         except TypeError as err:
#             error("TypeError - rerunning will probably fix")
#     else:
#         try:
#             libc = windll.LoadLibrary(dll)
#         # exception for CPython
#         except WindowsError as err:
#             # print(err)
#             if err.winerror == 126:     # "The specified module could not be found"
#                 error("Cannot load library " + dll)
#             elif err.winerror == 193:   # "%1 is not a valid Win32 application"
#                 print("Cannot load library " + dll)
#                 error("You may be mixing 32 and 64 bit code")
#             else:
#                 error(err.strerror)
#     return libc


# -----------------------------------------------------------------------------
# AStyle Error Handler Callback

def error_handler(num, err):
    """ AStyle callback error handler.
        The return error string (err) is always byte type.
        It is converted to unicode for Python 3.
    """
    print("Error in input {}".format(num))
    err = err.decode()
    raise Exception(err)

# global to create the error handler callback function
ERROR_HANDLER_CALLBACK = CFUNCTYPE(None, c_int, c_char_p) if os.name != "nt" else WINFUNCTYPE(None, c_int, c_char_p)
ERROR_HANDLER = ERROR_HANDLER_CALLBACK(error_handler)

# -----------------------------------------------------------------------------

# AStyle Memory Allocation Callback

# global memory allocation returned to artistic style
# must be global for CPython, not a function attribute
# did not try a class attribute but it may not work for CPython
ALLOCATED = c_char_p

def memory_allocation(size):
    """ AStyle callback memory allocation.
        The size to allocate is always byte type.
        The allocated memory MUST BE FREED by the calling function.
    """
    global ALLOCATED
    # ctypes for CPython ARE mutable and can be used for input
    # using create_string_buffer() in CPython results in a
    # "TypeError: string or integer address expected instead of c_char_Array"
    # CPython must use c_char_Array object
    arr_type = c_char * size    # create a c_char array
    ALLOCATED = arr_type()      # create an array object
    return addressof(ALLOCATED)

MEMORY_ALLOCATION_CALLBACK = CFUNCTYPE(c_char_p, c_ulong) if os.name != "nt" else WINFUNCTYPE(c_char_p, c_ulong)
MEMORY_ALLOCATION = MEMORY_ALLOCATION_CALLBACK(memory_allocation)

###################################################################

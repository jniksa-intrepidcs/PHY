# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class CANOptions(ctypes.Structure):
    _fields_ = [
        ('iNetworkID', ctypes.c_int32),
    ]



class tag_options_open_neo_ex(ctypes.Union):
    _fields_ = [
        ('CANOptions', CANOptions),
        ('Reserved', ctypes.c_uint32 * 16),
    ]


tagOptionsOpenNeoEx = tag_options_open_neo_ex
OptionsOpenNeoEx = tag_options_open_neo_ex
POptionsOpenNeoEx = tag_options_open_neo_ex


import ctypes
from visatype import *

#load tktds1k2k DLL into memory
tkDLL = ctypes.cdll.LoadLibrary(r'C:\Program Files\IVI Foundation\IVI\Bin\tktds1k2k_64.dll')

session = ViSession()

resourceName = ctypes.create_string_buffer('1001C'.encode('windows-1251'))
optionString = ctypes.create_string_buffer('Simulate-1, RangeCheck = 1, QueryInstrStatus-0, Cache-1'.encode('windows-1251'))

tkDLL.tktds1k2k_InitWithOptions(resourceName, VI_TRUE, VI_TRUE, optionString, ctypes.pointer(session))

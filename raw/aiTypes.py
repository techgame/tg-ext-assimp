#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiMatrix3x3 import *
from aiMatrix4x4 import *
from aiVector3D import *
from aiVector2D import *
from aiQuaternion import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiTypes.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiPlane(Structure):
    _fields_ = [
        ("a", c_float),
        ("b", c_float),
        ("c", c_float),
        ("d", c_float),
        ]

#~ line: 133, skipped: 18 ~~~~~~

class aiRay(Structure):
    _fields_ = [
        ("pos", aiVector3D),
        ("dir", aiVector3D),
        ]

#~ line: 151, skipped: 18 ~~~~~~

class aiColor3D(Structure):
    _fields_ = [
        ("r", c_float),
        ("g", c_float),
        ("b", c_float),
        ]

#~ line: 215, skipped: 64 ~~~~~~

class aiColor4D(Structure):
    _fields_ = [
        ("r", c_float),
        ("g", c_float),
        ("b", c_float),
        ("a", c_float),
        ]

#~ line: 280, skipped: 65 ~~~~~~

class aiString(Structure):
    _fields_ = [
        ("length", size_t),
        ("data", (8192*c_char)),
        ]

#~ line: 394, skipped: 114 ~~~~~~

class aiReturn(c_int):
    '''enum aiReturn''' 
    aiReturn_SUCCESS = 0
    aiReturn_FAILURE = -1
    aiReturn_OUTOFMEMORY = -3
    _AI_ENFORCE_ENUM_SIZE = 2147483647
    lookup = {
        0: "aiReturn_SUCCESS",
        -1: "aiReturn_FAILURE",
        -3: "aiReturn_OUTOFMEMORY",
        2147483647: "_AI_ENFORCE_ENUM_SIZE",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 422, skipped: 28 ~~~~~~

class aiOrigin(c_int):
    '''enum aiOrigin''' 
    aiOrigin_SET = 0
    aiOrigin_CUR = 1
    aiOrigin_END = 2
    _AI_ORIGIN_ENFORCE_ENUM_SIZE = 2147483647
    lookup = {
        0: "aiOrigin_SET",
        1: "aiOrigin_CUR",
        2: "aiOrigin_END",
        2147483647: "_AI_ORIGIN_ENFORCE_ENUM_SIZE",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 445, skipped: 23 ~~~~~~

class aiDefaultLogStream(c_int):
    '''enum aiDefaultLogStream''' 
    aiDefaultLogStream_FILE = 1
    aiDefaultLogStream_STDOUT = 2
    aiDefaultLogStream_STDERR = 4
    aiDefaultLogStream_DEBUGGER = 8
    _AI_DLS_ENFORCE_ENUM_SIZE = 2147483647
    lookup = {
        1: "aiDefaultLogStream_FILE",
        2: "aiDefaultLogStream_STDOUT",
        4: "aiDefaultLogStream_STDERR",
        8: "aiDefaultLogStream_DEBUGGER",
        2147483647: "_AI_DLS_ENFORCE_ENUM_SIZE",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 479, skipped: 34 ~~~~~~

class aiMemoryInfo(Structure):
    _fields_ = [
        ("textures", c_uint),
        ("materials", c_uint),
        ("meshes", c_uint),
        ("nodes", c_uint),
        ("animations", c_uint),
        ("cameras", c_uint),
        ("lights", c_uint),
        ("total", c_uint),
        ]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiTypes.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


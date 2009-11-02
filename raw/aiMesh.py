#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTypes import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiMesh.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiFace(Structure):
    _fields_ = [
        ("mNumIndices", c_uint),
        ("mIndices", POINTER(c_uint)),
        ]

#~ line: 147, skipped: 69 ~~~~~~

class aiVertexWeight(Structure):
    _fields_ = [
        ("mVertexId", c_uint),
        ("mWeight", c_float),
        ]

#~ line: 179, skipped: 32 ~~~~~~

class aiBone(Structure):
    _fields_ = [
        ("mName", aiString),
        ("mNumWeights", c_uint),
        ("mWeights", POINTER(aiVertexWeight)),
        ("mOffsetMatrix", aiMatrix4x4),
        ]

#~ line: 261, skipped: 82 ~~~~~~

class aiPrimitiveType(c_int):
    '''enum aiPrimitiveType''' 
    aiPrimitiveType_POINT = 1
    aiPrimitiveType_LINE = 2
    aiPrimitiveType_TRIANGLE = 4
    aiPrimitiveType_POLYGON = 8
    _aiPrimitiveType_Force32Bit = -1610612737
    lookup = {
        1: "aiPrimitiveType_POINT",
        2: "aiPrimitiveType_LINE",
        4: "aiPrimitiveType_TRIANGLE",
        8: "aiPrimitiveType_POLYGON",
        -1610612737: "_aiPrimitiveType_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 323, skipped: 62 ~~~~~~

class aiMesh(Structure):
    _fields_ = [
        ("mPrimitiveTypes", c_uint),
        ("mNumVertices", c_uint),
        ("mNumFaces", c_uint),
        ("mVertices", POINTER(aiVector3D)),
        ("mNormals", POINTER(aiVector3D)),
        ("mTangents", POINTER(aiVector3D)),
        ("mBitangents", POINTER(aiVector3D)),
        ("mColors", (128*POINTER(aiColor4D))),
        ("mTextureCoords", (128*POINTER(aiVector3D))),
        ("mNumUVComponents", (128*c_uint)),
        ("mFaces", POINTER(aiFace)),
        ("mNumBones", c_uint),
        ("mBones", POINTER(POINTER(aiBone))),
        ("mMaterialIndex", c_uint),
        ]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiMesh.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


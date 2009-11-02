#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTexture import *
from aiMesh import *
from aiLight import *
from aiCamera import *
from aiMaterial import *
from aiAnim import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiScene.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiNode(Structure):
    pass
aiNode._fields_ = [
        ("mName", aiString),
        ("mTransformation", aiMatrix4x4),
        ("mParent", POINTER(aiNode)),
        ("mNumChildren", c_uint),
        ("mChildren", POINTER(POINTER(aiNode))),
        ("mNumMeshes", c_uint),
        ("mMeshes", POINTER(c_uint)),
        ]

#~ line: 228, skipped: 158 ~~~~~~

class aiScene(Structure):
    _fields_ = [
        ("mFlags", c_uint),
        ("mRootNode", POINTER(aiNode)),
        ("mNumMeshes", c_uint),
        ("mMeshes", POINTER(POINTER(aiMesh))),
        ("mNumMaterials", c_uint),
        ("mMaterials", POINTER(POINTER(aiMaterial))),
        ("mNumAnimations", c_uint),
        ("mAnimations", POINTER(POINTER(aiAnimation))),
        ("mNumTextures", c_uint),
        ("mTextures", POINTER(POINTER(aiTexture))),
        ("mNumLights", c_uint),
        ("mLights", POINTER(POINTER(aiLight))),
        ("mNumCameras", c_uint),
        ("mCameras", POINTER(POINTER(aiCamera))),
        ]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiScene.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


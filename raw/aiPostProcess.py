#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiPostProcess.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiPostProcessSteps(c_int):
    '''enum aiPostProcessSteps''' 
    aiProcess_CalcTangentSpace = 1
    aiProcess_JoinIdenticalVertices = 2
    aiProcess_MakeLeftHanded = 4
    aiProcess_Triangulate = 8
    aiProcess_RemoveComponent = 16
    aiProcess_GenNormals = 32
    aiProcess_GenSmoothNormals = 64
    aiProcess_SplitLargeMeshes = 128
    aiProcess_PreTransformVertices = 256
    aiProcess_LimitBoneWeights = 512
    aiProcess_ValidateDataStructure = 1024
    aiProcess_ImproveCacheLocality = 2048
    aiProcess_RemoveRedundantMaterials = 4096
    aiProcess_FixInfacingNormals = 8192
    aiProcess_SortByPType = 32768
    aiProcess_FindDegenerates = 65536
    aiProcess_FindInvalidData = 131072
    aiProcess_GenUVCoords = 262144
    aiProcess_TransformUVCoords = 524288
    aiProcess_FindInstances = 1048576
    aiProcess_OptimizeMeshes = 2097152
    aiProcess_OptimizeGraph = 4194304
    aiProcess_FlipUVs = 8388608
    aiProcess_FlipWindingOrder = 16777216
    lookup = {
        1: "aiProcess_CalcTangentSpace",
        2: "aiProcess_JoinIdenticalVertices",
        4: "aiProcess_MakeLeftHanded",
        8: "aiProcess_Triangulate",
        16: "aiProcess_RemoveComponent",
        32: "aiProcess_GenNormals",
        64: "aiProcess_GenSmoothNormals",
        128: "aiProcess_SplitLargeMeshes",
        256: "aiProcess_PreTransformVertices",
        512: "aiProcess_LimitBoneWeights",
        1024: "aiProcess_ValidateDataStructure",
        2048: "aiProcess_ImproveCacheLocality",
        4096: "aiProcess_RemoveRedundantMaterials",
        8192: "aiProcess_FixInfacingNormals",
        32768: "aiProcess_SortByPType",
        65536: "aiProcess_FindDegenerates",
        131072: "aiProcess_FindInvalidData",
        262144: "aiProcess_GenUVCoords",
        524288: "aiProcess_TransformUVCoords",
        1048576: "aiProcess_FindInstances",
        2097152: "aiProcess_OptimizeMeshes",
        4194304: "aiProcess_OptimizeGraph",
        8388608: "aiProcess_FlipUVs",
        16777216: "aiProcess_FlipWindingOrder",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiPostProcess.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


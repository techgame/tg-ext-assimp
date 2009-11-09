#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiPostProcess.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiPostProcessSteps(c_enum):
    '''enum aiPostProcessSteps''' 
    values = dict(
        aiProcess_CalcTangentSpace=1,
        aiProcess_JoinIdenticalVertices=2,
        aiProcess_MakeLeftHanded=4,
        aiProcess_Triangulate=8,
        aiProcess_RemoveComponent=16,
        aiProcess_GenNormals=32,
        aiProcess_GenSmoothNormals=64,
        aiProcess_SplitLargeMeshes=128,
        aiProcess_PreTransformVertices=256,
        aiProcess_LimitBoneWeights=512,
        aiProcess_ValidateDataStructure=1024,
        aiProcess_ImproveCacheLocality=2048,
        aiProcess_RemoveRedundantMaterials=4096,
        aiProcess_FixInfacingNormals=8192,
        aiProcess_SortByPType=32768,
        aiProcess_FindDegenerates=65536,
        aiProcess_FindInvalidData=131072,
        aiProcess_GenUVCoords=262144,
        aiProcess_TransformUVCoords=524288,
        aiProcess_FindInstances=1048576,
        aiProcess_OptimizeMeshes=2097152,
        aiProcess_OptimizeGraph=4194304,
        aiProcess_FlipUVs=8388608,
        aiProcess_FlipWindingOrder=16777216,
        )
aiPostProcessSteps._nsUpdate_(locals())


#~ line: 516, skipped: 454 ~~~~~~

aiProcess_ConvertToLeftHanded = ( aiProcess_MakeLeftHanded | aiProcess_FlipUVs | aiProcess_FlipWindingOrder | 0 )

#~ line: 537, skipped: 21 ~~~~~~

aiProcessPreset_TargetRealtime_Fast = ( aiProcess_CalcTangentSpace | aiProcess_GenNormals | aiProcess_JoinIdenticalVertices | aiProcess_Triangulate | aiProcess_GenUVCoords | aiProcess_SortByPType | 0 )

#~ line: 562, skipped: 25 ~~~~~~

aiProcessPreset_TargetRealtime_Quality = ( aiProcess_CalcTangentSpace | aiProcess_GenSmoothNormals | aiProcess_JoinIdenticalVertices | aiProcess_ImproveCacheLocality | aiProcess_LimitBoneWeights | aiProcess_RemoveRedundantMaterials | aiProcess_SplitLargeMeshes | aiProcess_Triangulate | aiProcess_GenUVCoords | aiProcess_SortByPType | aiProcess_FindDegenerates | aiProcess_FindInvalidData | 0 )

#~ line: 592, skipped: 30 ~~~~~~

aiProcessPreset_TargetRealtime_MaxQuality = ( aiProcessPreset_TargetRealtime_Quality | aiProcess_FindInstances | aiProcess_ValidateDataStructure | aiProcess_OptimizeMeshes | 0 )


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiPostProcess.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


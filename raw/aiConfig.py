#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiConfig.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AI_CONFIG_PP_CT_MAX_SMOOTHING_ANGLE = "PP_CT_MAX_SMOOTHING_ANGLE"

#~ line: 91, skipped: 15 ~~~~~~

AI_CONFIG_PP_GSN_MAX_SMOOTHING_ANGLE = "PP_GSN_MAX_SMOOTHING_ANGLE"

#~ line: 104, skipped: 13 ~~~~~~

AI_CONFIG_IMPORT_MDL_COLORMAP = "IMPORT_MDL_COLORMAP"

#~ line: 126, skipped: 22 ~~~~~~

AI_CONFIG_PP_RRM_EXCLUDE_LIST = "PP_RRM_EXCLUDE_LIST"

#~ line: 141, skipped: 15 ~~~~~~

AI_CONFIG_PP_PTV_KEEP_HIERARCHY = "PP_PTV_KEEP_HIERARCHY"

#~ line: 151, skipped: 10 ~~~~~~

AI_CONFIG_PP_PTV_NORMALIZE = "PP_PTV_NORMALIZE"

#~ line: 164, skipped: 13 ~~~~~~

AI_CONFIG_PP_FD_REMOVE = "PP_FD_REMOVE"

#~ line: 185, skipped: 21 ~~~~~~

AI_CONFIG_PP_OG_EXCLUDE_LIST = "PP_OG_EXCLUDE_LIST"

#~ line: 196, skipped: 11 ~~~~~~

AI_CONFIG_PP_SLM_TRIANGLE_LIMIT = "PP_SLM_TRIANGLE_LIMIT"

#~ line: 212, skipped: 16 ~~~~~~

AI_CONFIG_PP_SLM_VERTEX_LIMIT = "PP_SLM_VERTEX_LIMIT"

#~ line: 226, skipped: 14 ~~~~~~

AI_CONFIG_PP_LBW_MAX_WEIGHTS = "PP_LBW_MAX_WEIGHTS"

#~ line: 251, skipped: 25 ~~~~~~

AI_CONFIG_PP_ICL_PTCACHE_SIZE = "PP_ICL_PTCACHE_SIZE"

#~ line: 259, skipped: 8 ~~~~~~

class aiComponent(c_enum):
    '''enum aiComponent''' 
    values = dict(
        aiComponent_NORMALS=2,
        aiComponent_TANGENTS_AND_BITANGENTS=4,
        aiComponent_COLORS=8,
        aiComponent_TEXCOORDS=16,
        aiComponent_BONEWEIGHTS=32,
        aiComponent_ANIMATIONS=64,
        aiComponent_TEXTURES=128,
        aiComponent_LIGHTS=256,
        aiComponent_CAMERAS=512,
        aiComponent_MESHES=1024,
        aiComponent_MATERIALS=2048,
        _aiComponent_Force32Bit=-1610612737,
        )
aiComponent._nsUpdate_(locals())


#~ line: 329, skipped: 70 ~~~~~~

AI_CONFIG_PP_RVC_FLAGS = "PP_RVC_FLAGS"

#~ line: 341, skipped: 12 ~~~~~~

AI_CONFIG_PP_SBP_REMOVE = "PP_SBP_REMOVE"

#~ line: 353, skipped: 12 ~~~~~~

AI_CONFIG_PP_FID_ANIM_ACCURACY = "PP_FID_ANIM_ACCURACY"

#~ line: 377, skipped: 24 ~~~~~~

AI_CONFIG_PP_TUV_EVALUATE = "PP_TUV_EVALUATE"

#~ line: 389, skipped: 12 ~~~~~~

AI_CONFIG_FAVOUR_SPEED = "FAVOUR_SPEED"

#~ line: 412, skipped: 23 ~~~~~~

AI_CONFIG_IMPORT_GLOBAL_KEYFRAME = "IMPORT_GLOBAL_KEYFRAME"

AI_CONFIG_IMPORT_MD3_KEYFRAME = "IMPORT_MD3_KEYFRAME"
AI_CONFIG_IMPORT_MD2_KEYFRAME = "IMPORT_MD2_KEYFRAME"
AI_CONFIG_IMPORT_MDL_KEYFRAME = "IMPORT_MDL_KEYFRAME"
AI_CONFIG_IMPORT_MDC_KEYFRAME = "IMPORT_MDC_KEYFRAME"
AI_CONFIG_IMPORT_SMD_KEYFRAME = "IMPORT_SMD_KEYFRAME"
AI_CONFIG_IMPORT_UNREAL_KEYFRAME = "IMPORT_UNREAL_KEYFRAME"

#~ line: 428, skipped: 9 ~~~~~~

AI_CONFIG_IMPORT_AC_SEPARATE_BFCULL = "IMPORT_AC_SEPARATE_BFCULL"

#~ line: 437, skipped: 9 ~~~~~~

AI_CONFIG_IMPORT_UNREAL_HANDLE_FLAGS = "UNREAL_HANDLE_FLAGS"

#~ line: 450, skipped: 13 ~~~~~~

AI_CONFIG_IMPORT_TER_MAKE_UVS = "IMPORT_TER_MAKE_UVS"

#~ line: 460, skipped: 10 ~~~~~~

AI_CONFIG_IMPORT_ASE_RECONSTRUCT_NORMALS = "IMPORT_ASE_RECONSTRUCT_NORMALS"

#~ line: 471, skipped: 11 ~~~~~~

AI_CONFIG_IMPORT_MD3_HANDLE_MULTIPART = "IMPORT_MD3_HANDLE_MULTIPART"

#~ line: 483, skipped: 12 ~~~~~~

AI_CONFIG_IMPORT_MD3_SKIN_NAME = "IMPORT_MD3_SKIN_NAME"

#~ line: 501, skipped: 18 ~~~~~~

AI_CONFIG_IMPORT_MD3_SHADER_SRC = "IMPORT_MD3_SHADER_SRC"

#~ line: 515, skipped: 14 ~~~~~~

AI_CONFIG_IMPORT_LWO_ONE_LAYER_ONLY = "IMPORT_LWO_ONE_LAYER_ONLY"

#~ line: 529, skipped: 14 ~~~~~~

AI_CONFIG_IMPORT_MD5_NO_ANIM_AUTOLOAD = "IMPORT_MD5_NO_ANIM_AUTOLOAD"

#~ line: 548, skipped: 19 ~~~~~~

AI_CONFIG_IMPORT_LWS_ANIM_START = "IMPORT_LWS_ANIM_START"

AI_CONFIG_IMPORT_LWS_ANIM_END = "IMPORT_LWS_ANIM_END"

#~ line: 561, skipped: 11 ~~~~~~

AI_CONFIG_IMPORT_IRR_ANIM_FPS = "IMPORT_IRR_ANIM_FPS"

#~ line: 571, skipped: 10 ~~~~~~

AI_CONFIG_IMPORT_OGRE_MATERIAL_FILE = "IMPORT_OGRE_MATERIAL_FILE"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiConfig.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


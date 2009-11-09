#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTypes import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiLight.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiLightSourceType(c_enum):
    '''enum aiLightSourceType''' 
    values = dict(
        aiLightSource_UNDEFINED=0,
        aiLightSource_DIRECTIONAL=1,
        aiLightSource_POINT=2,
        aiLightSource_SPOT=3,
        _aiLightSource_Force32Bit=-1610612737,
        )
aiLightSourceType._nsUpdate_(locals())


#~ line: 99, skipped: 41 ~~~~~~

class aiLight(Structure):
    _fields_ = [
        ("mName", aiString),
        ("mType", aiLightSourceType),
        ("mPosition", aiVector3D),
        ("mDirection", aiVector3D),
        ("mAttenuationConstant", c_float),
        ("mAttenuationLinear", c_float),
        ("mAttenuationQuadratic", c_float),
        ("mColorDiffuse", aiColor3D),
        ("mColorSpecular", aiColor3D),
        ("mColorAmbient", aiColor3D),
        ("mAngleInnerCone", c_float),
        ("mAngleOuterCone", c_float),
        ]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiLight.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


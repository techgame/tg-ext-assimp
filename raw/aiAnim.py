#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTypes import *
from aiQuaternion import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiAnim.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiVectorKey(Structure):
    _fields_ = [
        ("mTime", c_double),
        ("mValue", aiVector3D),
        ]

#~ line: 77, skipped: 18 ~~~~~~

# typedef elem_type
elem_type = aiVector3D

#~ line: 104, skipped: 27 ~~~~~~

class aiQuatKey(Structure):
    _fields_ = [
        ("mTime", c_double),
        ("mValue", aiQuaternion),
        ]

#~ line: 121, skipped: 17 ~~~~~~

# typedef elem_type
elem_type = aiQuaternion

#~ line: 147, skipped: 26 ~~~~~~

class aiAnimBehaviour(c_enum):
    '''enum aiAnimBehaviour''' 
    values = dict(
        aiAnimBehaviour_DEFAULT=0,
        aiAnimBehaviour_CONSTANT=1,
        aiAnimBehaviour_LINEAR=2,
        aiAnimBehaviour_REPEAT=3,
        _aiAnimBehaviour_Force32Bit=-1879048193,
        )
aiAnimBehaviour._nsUpdate_(locals())


#~ line: 186, skipped: 39 ~~~~~~

class aiNodeAnim(Structure):
    _fields_ = [
        ("mNodeName", aiString),
        ("mNumPositionKeys", c_uint),
        ("mPositionKeys", POINTER(aiVectorKey)),
        ("mNumRotationKeys", c_uint),
        ("mRotationKeys", POINTER(aiQuatKey)),
        ("mNumScalingKeys", c_uint),
        ("mScalingKeys", POINTER(aiVectorKey)),
        ("mPreState", aiAnimBehaviour),
        ("mPostState", aiAnimBehaviour),
        ]

#~ line: 261, skipped: 75 ~~~~~~

class aiAnimation(Structure):
    _fields_ = [
        ("mName", aiString),
        ("mDuration", c_double),
        ("mTicksPerSecond", c_double),
        ("mNumChannels", c_uint),
        ("mChannels", POINTER(POINTER(aiNodeAnim))),
        ]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiAnim.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


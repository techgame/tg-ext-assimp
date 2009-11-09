#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTypes import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiMaterial.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiTextureOp(c_enum):
    '''enum aiTextureOp''' 
    values = dict(
        aiTextureOp_Multiply=0,
        aiTextureOp_Add=1,
        aiTextureOp_Subtract=2,
        aiTextureOp_Divide=3,
        aiTextureOp_SmoothAdd=4,
        aiTextureOp_SignedAdd=5,
        _aiTextureOp_Force32Bit=-1610612737,
        )
aiTextureOp._nsUpdate_(locals())


#~ line: 112, skipped: 34 ~~~~~~

class aiTextureMapMode(c_enum):
    '''enum aiTextureMapMode''' 
    values = dict(
        aiTextureMapMode_Wrap=0,
        aiTextureMapMode_Clamp=1,
        aiTextureMapMode_Decal=3,
        aiTextureMapMode_Mirror=2,
        _aiTextureMapMode_Force32Bit=-1610612737,
        )
aiTextureMapMode._nsUpdate_(locals())


#~ line: 150, skipped: 38 ~~~~~~

class aiTextureMapping(c_enum):
    '''enum aiTextureMapping''' 
    values = dict(
        aiTextureMapping_UV=0,
        aiTextureMapping_SPHERE=1,
        aiTextureMapping_CYLINDER=2,
        aiTextureMapping_BOX=3,
        aiTextureMapping_PLANE=4,
        aiTextureMapping_OTHER=5,
        _aiTextureMapping_Force32Bit=-1610612737,
        )
aiTextureMapping._nsUpdate_(locals())


#~ line: 199, skipped: 49 ~~~~~~

class aiTextureType(c_enum):
    '''enum aiTextureType''' 
    values = dict(
        aiTextureType_NONE=0,
        aiTextureType_DIFFUSE=1,
        aiTextureType_SPECULAR=2,
        aiTextureType_AMBIENT=3,
        aiTextureType_EMISSIVE=4,
        aiTextureType_HEIGHT=5,
        aiTextureType_NORMALS=6,
        aiTextureType_SHININESS=7,
        aiTextureType_OPACITY=8,
        aiTextureType_DISPLACEMENT=9,
        aiTextureType_LIGHTMAP=10,
        aiTextureType_REFLECTION=11,
        aiTextureType_UNKNOWN=12,
        _aiTextureType_Force32Bit=-1610612737,
        )
aiTextureType._nsUpdate_(locals())


#~ line: 316, skipped: 117 ~~~~~~

class aiShadingMode(c_enum):
    '''enum aiShadingMode''' 
    values = dict(
        aiShadingMode_Flat=1,
        aiShadingMode_Gouraud=2,
        aiShadingMode_Phong=3,
        aiShadingMode_Blinn=4,
        aiShadingMode_Toon=5,
        aiShadingMode_OrenNayar=6,
        aiShadingMode_Minnaert=7,
        aiShadingMode_CookTorrance=8,
        aiShadingMode_NoShading=9,
        aiShadingMode_Fresnel=10,
        _aiShadingMode_Force32Bit=-1610612737,
        )
aiShadingMode._nsUpdate_(locals())


#~ line: 390, skipped: 74 ~~~~~~

class aiTextureFlags(c_enum):
    '''enum aiTextureFlags''' 
    values = dict(
        aiTextureFlags_Invert=1,
        aiTextureFlags_UseAlpha=2,
        aiTextureFlags_IgnoreAlpha=4,
        _aiTextureFlags_Force32Bit=-1610612737,
        )
aiTextureFlags._nsUpdate_(locals())


#~ line: 439, skipped: 49 ~~~~~~

class aiBlendMode(c_enum):
    '''enum aiBlendMode''' 
    values = dict(
        aiBlendMode_Default=0,
        aiBlendMode_Additive=1,
        _aiBlendMode_Force32Bit=-1610612737,
        )
aiBlendMode._nsUpdate_(locals())


#~ line: 483, skipped: 44 ~~~~~~

class aiUVTransform(Structure):
    _fields_ = [
        ("mTranslation", aiVector2D),
        ("mScaling", aiVector2D),
        ("mRotation", c_float),
        ]

#~ line: 523, skipped: 40 ~~~~~~

class aiPropertyTypeInfo(c_enum):
    '''enum aiPropertyTypeInfo''' 
    values = dict(
        aiPTI_Float=1,
        aiPTI_String=3,
        aiPTI_Integer=4,
        aiPTI_Buffer=5,
        _aiPTI_Force32Bit=-1610612737,
        )
aiPropertyTypeInfo._nsUpdate_(locals())


#~ line: 581, skipped: 58 ~~~~~~

class aiMaterialProperty(Structure):
    _fields_ = [
        ("mKey", aiString),
        ("mSemantic", c_uint),
        ("mIndex", c_uint),
        ("mDataLength", c_uint),
        ("mType", aiPropertyTypeInfo),
        ("mData", c_char_p),
        ]

#~ line: 646, skipped: 65 ~~~~~~

class aiMaterial(Structure):
    _fields_ = [
        ("mProperties", POINTER(POINTER(aiMaterialProperty))),
        ("mNumProperties", c_uint),
        ("mNumAllocated", c_uint),
        ]

#~ line: 1194, skipped: 548 ~~~~~~

@bind(aiReturn, [POINTER(aiMaterial), c_char_p, aiTextureType, c_uint, POINTER(POINTER(aiMaterialProperty))])
def aiGetMaterialProperty(pMat, pKey, type, index, pPropOut, _api_=None): 
    """aiGetMaterialProperty(pMat, pKey, type, index, pPropOut)
    
        pMat : POINTER(aiMaterial)
        pKey : c_char_p
        type : aiTextureType
        index : c_uint
        pPropOut : POINTER(POINTER(aiMaterialProperty))
    """
    return _api_(pMat, pKey, type, index, pPropOut)
    

#~ line: 1228, skipped: 34 ~~~~~~

@bind(aiReturn, [POINTER(aiMaterial), c_char_p, c_uint, c_uint, POINTER(c_float), POINTER(c_uint)])
def aiGetMaterialFloatArray(pMat, pKey, type, index, pOut, pMax, _api_=None): 
    """aiGetMaterialFloatArray(pMat, pKey, type, index, pOut, pMax)
    
        pMat : POINTER(aiMaterial)
        pKey : c_char_p
        type : c_uint
        index : c_uint
        pOut : POINTER(c_float)
        pMax : POINTER(c_uint)
    """
    return _api_(pMat, pKey, type, index, pOut, pMax)
    

#~ line: 1280, skipped: 52 ~~~~~~

@bind(aiReturn, [POINTER(aiMaterial), c_char_p, c_uint, c_uint, POINTER(c_int), POINTER(c_uint)])
def aiGetMaterialIntegerArray(pMat, pKey, type, index, pOut, pMax, _api_=None): 
    """aiGetMaterialIntegerArray(pMat, pKey, type, index, pOut, pMax)
    
        pMat : POINTER(aiMaterial)
        pKey : c_char_p
        type : c_uint
        index : c_uint
        pOut : POINTER(c_int)
        pMax : POINTER(c_uint)
    """
    return _api_(pMat, pKey, type, index, pOut, pMax)
    

#~ line: 1318, skipped: 38 ~~~~~~

@bind(aiReturn, [POINTER(aiMaterial), c_char_p, c_uint, c_uint, POINTER(aiColor4D)])
def aiGetMaterialColor(pMat, pKey, type, index, pOut, _api_=None): 
    """aiGetMaterialColor(pMat, pKey, type, index, pOut)
    
        pMat : POINTER(aiMaterial)
        pKey : c_char_p
        type : c_uint
        index : c_uint
        pOut : POINTER(aiColor4D)
    """
    return _api_(pMat, pKey, type, index, pOut)
    

#~ line: 1330, skipped: 12 ~~~~~~

@bind(aiReturn, [POINTER(aiMaterial), c_char_p, c_uint, c_uint, POINTER(aiString)])
def aiGetMaterialString(pMat, pKey, type, index, pOut, _api_=None): 
    """aiGetMaterialString(pMat, pKey, type, index, pOut)
    
        pMat : POINTER(aiMaterial)
        pKey : c_char_p
        type : c_uint
        index : c_uint
        pOut : POINTER(aiString)
    """
    return _api_(pMat, pKey, type, index, pOut)
    

#~ line: 1340, skipped: 10 ~~~~~~

@bind(c_uint, [POINTER(aiMaterial), aiTextureType])
def aiGetMaterialTextureCount(pMat, type, _api_=None): 
    """aiGetMaterialTextureCount(pMat, type)
    
        pMat : POINTER(aiMaterial)
        type : aiTextureType
    """
    return _api_(pMat, type)
    

#~ line: 1385, skipped: 45 ~~~~~~

@bind(aiReturn, [POINTER(aiMaterial), aiTextureType, c_uint, POINTER(aiString), POINTER(aiTextureMapping), POINTER(c_uint), POINTER(c_float), POINTER(aiTextureOp), POINTER(aiTextureMapMode), POINTER(c_uint)])
def aiGetMaterialTexture(mat, type, index, path, mapping, uvindex, blend, op, mapmode, flags, _api_=None): 
    """aiGetMaterialTexture(mat, type, index, path, mapping, uvindex, blend, op, mapmode, flags)
    
        mat : POINTER(aiMaterial)
        type : aiTextureType
        index : c_uint
        path : POINTER(aiString)
        mapping : POINTER(aiTextureMapping)
        uvindex : POINTER(c_uint)
        blend : POINTER(c_float)
        op : POINTER(aiTextureOp)
        mapmode : POINTER(aiTextureMapMode)
        flags : POINTER(c_uint)
    """
    return _api_(mat, type, index, path, mapping, uvindex, blend, op, mapmode, flags)
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/aiMaterial.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


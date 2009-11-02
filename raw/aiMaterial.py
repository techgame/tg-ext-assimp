#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTypes import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/aiMaterial.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class aiTextureOp(c_int):
    '''enum aiTextureOp''' 
    aiTextureOp_Multiply = 0
    aiTextureOp_Add = 1
    aiTextureOp_Subtract = 2
    aiTextureOp_Divide = 3
    aiTextureOp_SmoothAdd = 4
    aiTextureOp_SignedAdd = 5
    _aiTextureOp_Force32Bit = -1610612737
    lookup = {
        0: "aiTextureOp_Multiply",
        1: "aiTextureOp_Add",
        2: "aiTextureOp_Subtract",
        3: "aiTextureOp_Divide",
        4: "aiTextureOp_SmoothAdd",
        5: "aiTextureOp_SignedAdd",
        -1610612737: "_aiTextureOp_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 112, skipped: 34 ~~~~~~

class aiTextureMapMode(c_int):
    '''enum aiTextureMapMode''' 
    aiTextureMapMode_Wrap = 0
    aiTextureMapMode_Clamp = 1
    aiTextureMapMode_Decal = 3
    aiTextureMapMode_Mirror = 2
    _aiTextureMapMode_Force32Bit = -1610612737
    lookup = {
        0: "aiTextureMapMode_Wrap",
        1: "aiTextureMapMode_Clamp",
        3: "aiTextureMapMode_Decal",
        2: "aiTextureMapMode_Mirror",
        -1610612737: "_aiTextureMapMode_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 150, skipped: 38 ~~~~~~

class aiTextureMapping(c_int):
    '''enum aiTextureMapping''' 
    aiTextureMapping_UV = 0
    aiTextureMapping_SPHERE = 1
    aiTextureMapping_CYLINDER = 2
    aiTextureMapping_BOX = 3
    aiTextureMapping_PLANE = 4
    aiTextureMapping_OTHER = 5
    _aiTextureMapping_Force32Bit = -1610612737
    lookup = {
        0: "aiTextureMapping_UV",
        1: "aiTextureMapping_SPHERE",
        2: "aiTextureMapping_CYLINDER",
        3: "aiTextureMapping_BOX",
        4: "aiTextureMapping_PLANE",
        5: "aiTextureMapping_OTHER",
        -1610612737: "_aiTextureMapping_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 199, skipped: 49 ~~~~~~

class aiTextureType(c_int):
    '''enum aiTextureType''' 
    aiTextureType_NONE = 0
    aiTextureType_DIFFUSE = 1
    aiTextureType_SPECULAR = 2
    aiTextureType_AMBIENT = 3
    aiTextureType_EMISSIVE = 4
    aiTextureType_HEIGHT = 5
    aiTextureType_NORMALS = 6
    aiTextureType_SHININESS = 7
    aiTextureType_OPACITY = 8
    aiTextureType_DISPLACEMENT = 9
    aiTextureType_LIGHTMAP = 10
    aiTextureType_REFLECTION = 11
    aiTextureType_UNKNOWN = 12
    _aiTextureType_Force32Bit = -1610612737
    lookup = {
        0: "aiTextureType_NONE",
        1: "aiTextureType_DIFFUSE",
        2: "aiTextureType_SPECULAR",
        3: "aiTextureType_AMBIENT",
        4: "aiTextureType_EMISSIVE",
        5: "aiTextureType_HEIGHT",
        6: "aiTextureType_NORMALS",
        7: "aiTextureType_SHININESS",
        8: "aiTextureType_OPACITY",
        9: "aiTextureType_DISPLACEMENT",
        10: "aiTextureType_LIGHTMAP",
        11: "aiTextureType_REFLECTION",
        12: "aiTextureType_UNKNOWN",
        -1610612737: "_aiTextureType_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 316, skipped: 117 ~~~~~~

class aiShadingMode(c_int):
    '''enum aiShadingMode''' 
    aiShadingMode_Flat = 1
    aiShadingMode_Gouraud = 2
    aiShadingMode_Phong = 3
    aiShadingMode_Blinn = 4
    aiShadingMode_Toon = 5
    aiShadingMode_OrenNayar = 6
    aiShadingMode_Minnaert = 7
    aiShadingMode_CookTorrance = 8
    aiShadingMode_NoShading = 9
    aiShadingMode_Fresnel = 10
    _aiShadingMode_Force32Bit = -1610612737
    lookup = {
        1: "aiShadingMode_Flat",
        2: "aiShadingMode_Gouraud",
        3: "aiShadingMode_Phong",
        4: "aiShadingMode_Blinn",
        5: "aiShadingMode_Toon",
        6: "aiShadingMode_OrenNayar",
        7: "aiShadingMode_Minnaert",
        8: "aiShadingMode_CookTorrance",
        9: "aiShadingMode_NoShading",
        10: "aiShadingMode_Fresnel",
        -1610612737: "_aiShadingMode_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 390, skipped: 74 ~~~~~~

class aiTextureFlags(c_int):
    '''enum aiTextureFlags''' 
    aiTextureFlags_Invert = 1
    aiTextureFlags_UseAlpha = 2
    aiTextureFlags_IgnoreAlpha = 4
    _aiTextureFlags_Force32Bit = -1610612737
    lookup = {
        1: "aiTextureFlags_Invert",
        2: "aiTextureFlags_UseAlpha",
        4: "aiTextureFlags_IgnoreAlpha",
        -1610612737: "_aiTextureFlags_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 439, skipped: 49 ~~~~~~

class aiBlendMode(c_int):
    '''enum aiBlendMode''' 
    aiBlendMode_Default = 0
    aiBlendMode_Additive = 1
    _aiBlendMode_Force32Bit = -1610612737
    lookup = {
        0: "aiBlendMode_Default",
        1: "aiBlendMode_Additive",
        -1610612737: "_aiBlendMode_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

#~ line: 483, skipped: 44 ~~~~~~

class aiUVTransform(Structure):
    _fields_ = [
        ("mTranslation", aiVector2D),
        ("mScaling", aiVector2D),
        ("mRotation", c_float),
        ]

#~ line: 523, skipped: 40 ~~~~~~

class aiPropertyTypeInfo(c_int):
    '''enum aiPropertyTypeInfo''' 
    aiPTI_Float = 1
    aiPTI_String = 3
    aiPTI_Integer = 4
    aiPTI_Buffer = 5
    _aiPTI_Force32Bit = -1610612737
    lookup = {
        1: "aiPTI_Float",
        3: "aiPTI_String",
        4: "aiPTI_Integer",
        5: "aiPTI_Buffer",
        -1610612737: "_aiPTI_Force32Bit",
        }
    rlookup = dict([(v,k) for k,v in lookup.items()])
    
    def __repr__(self): return str(self)
    def __str__(self): 
        return self.lookup.get(self.value) or str(self.value)
    

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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from _ctypes_assimp import *
from aiTypes import *
from aiConfig import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Code generated from:
#~   "inc/assimp.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

aiScene = c_void_p # Structure with empty _fields_
aiFileIO = c_void_p # Structure with empty _fields_
# typedef aiLogStreamCallback
aiLogStreamCallback = CFUNCTYPE(None, c_char_p, c_char_p)

#~ line: 65, skipped: 10 ~~~~~~

class aiLogStream(Structure):
    _fields_ = [
        ("callback", aiLogStreamCallback),
        ("user", c_char_p),
        ]

#~ line: 74, skipped: 9 ~~~~~~

# typedef aiBool
aiBool = c_int

#~ line: 97, skipped: 23 ~~~~~~

@bind(POINTER(aiScene), [c_char_p, c_uint])
def aiImportFile(pFile, pFlags, _api_=None): 
    """aiImportFile(pFile, pFlags)
    
        pFile : c_char_p
        pFlags : c_uint
    """
    return _api_(pFile, pFlags)
    

#~ line: 122, skipped: 25 ~~~~~~

@bind(POINTER(aiScene), [c_char_p, c_uint, POINTER(aiFileIO)])
def aiImportFileEx(pFile, pFlags, pFS, _api_=None): 
    """aiImportFileEx(pFile, pFlags, pFS)
    
        pFile : c_char_p
        pFlags : c_uint
        pFS : POINTER(aiFileIO)
    """
    return _api_(pFile, pFlags, pFS)
    

#~ line: 157, skipped: 35 ~~~~~~

@bind(POINTER(aiScene), [c_char_p, c_uint, c_uint, c_char_p])
def aiImportFileFromMemory(pBuffer, pLength, pFlags, pHint, _api_=None): 
    """aiImportFileFromMemory(pBuffer, pLength, pFlags, pHint)
    
        pBuffer : c_char_p
        pLength : c_uint
        pFlags : c_uint
        pHint : c_char_p
    """
    return _api_(pBuffer, pLength, pFlags, pHint)
    

#~ line: 176, skipped: 19 ~~~~~~

@bind(POINTER(aiScene), [POINTER(aiScene), c_uint])
def aiApplyPostProcessing(pScene, pFlags, _api_=None): 
    """aiApplyPostProcessing(pScene, pFlags)
    
        pScene : POINTER(aiScene)
        pFlags : c_uint
    """
    return _api_(pScene, pFlags)
    

#~ line: 200, skipped: 24 ~~~~~~

@bind(aiLogStream, [aiDefaultLogStream, c_char_p])
def aiGetPredefinedLogStream(pStreams, file, _api_=None): 
    """aiGetPredefinedLogStream(pStreams, file)
    
        pStreams : aiDefaultLogStream
        file : c_char_p
    """
    return _api_(pStreams, file)
    

#~ line: 213, skipped: 13 ~~~~~~

@bind(None, [POINTER(aiLogStream)])
def aiAttachLogStream(stream, _api_=None): 
    """aiAttachLogStream(stream)
    
        stream : POINTER(aiLogStream)
    """
    return _api_(stream)
    

#~ line: 222, skipped: 9 ~~~~~~

@bind(None, [aiBool])
def aiEnableVerboseLogging(d, _api_=None): 
    """aiEnableVerboseLogging(d)
    
        d : aiBool
    """
    return _api_(d)
    

#~ line: 234, skipped: 12 ~~~~~~

@bind(aiReturn, [POINTER(aiLogStream)])
def aiDetachLogStream(stream, _api_=None): 
    """aiDetachLogStream(stream)
    
        stream : POINTER(aiLogStream)
    """
    return _api_(stream)
    

#~ line: 244, skipped: 10 ~~~~~~

@bind(None, [])
def aiDetachAllLogStreams(_api_=None): 
    """aiDetachAllLogStreams()
    
        
    """
    return _api_()
    

#~ line: 253, skipped: 9 ~~~~~~

@bind(None, [POINTER(aiScene)])
def aiReleaseImport(pScene, _api_=None): 
    """aiReleaseImport(pScene)
    
        pScene : POINTER(aiScene)
    """
    return _api_(pScene)
    

#~ line: 262, skipped: 9 ~~~~~~

@bind(c_char_p, [])
def aiGetErrorString(_api_=None): 
    """aiGetErrorString()
    
        
    """
    return _api_()
    

#~ line: 272, skipped: 10 ~~~~~~

@bind(aiBool, [c_char_p])
def aiIsExtensionSupported(szExtension, _api_=None): 
    """aiIsExtensionSupported(szExtension)
    
        szExtension : c_char_p
    """
    return _api_(szExtension)
    

#~ line: 283, skipped: 11 ~~~~~~

@bind(None, [POINTER(aiString)])
def aiGetExtensionList(szOut, _api_=None): 
    """aiGetExtensionList(szOut)
    
        szOut : POINTER(aiString)
    """
    return _api_(szOut)
    

#~ line: 292, skipped: 9 ~~~~~~

@bind(None, [POINTER(aiScene), POINTER(aiMemoryInfo)])
def aiGetMemoryRequirements(pIn, in_, _api_=None): 
    """aiGetMemoryRequirements(pIn, in_)
    
        pIn : POINTER(aiScene)
        in_ : POINTER(aiMemoryInfo)
    """
    return _api_(pIn, in_)
    

#~ line: 307, skipped: 15 ~~~~~~

@bind(None, [c_char_p, c_int])
def aiSetImportPropertyInteger(szName, value, _api_=None): 
    """aiSetImportPropertyInteger(szName, value)
    
        szName : c_char_p
        value : c_int
    """
    return _api_(szName, value)
    

#~ line: 322, skipped: 15 ~~~~~~

@bind(None, [c_char_p, c_float])
def aiSetImportPropertyFloat(szName, value, _api_=None): 
    """aiSetImportPropertyFloat(szName, value)
    
        szName : c_char_p
        value : c_float
    """
    return _api_(szName, value)
    

#~ line: 337, skipped: 15 ~~~~~~

@bind(None, [c_char_p, POINTER(aiString)])
def aiSetImportPropertyString(szName, st, _api_=None): 
    """aiSetImportPropertyString(szName, st)
    
        szName : c_char_p
        st : POINTER(aiString)
    """
    return _api_(szName, st)
    

#~ line: 347, skipped: 10 ~~~~~~

@bind(None, [POINTER(aiQuaternion), POINTER(aiMatrix3x3)])
def aiCreateQuaternionFromMatrix(quat, mat, _api_=None): 
    """aiCreateQuaternionFromMatrix(quat, mat)
    
        quat : POINTER(aiQuaternion)
        mat : POINTER(aiMatrix3x3)
    """
    return _api_(quat, mat)
    

#~ line: 363, skipped: 16 ~~~~~~

@bind(None, [POINTER(aiMatrix4x4), POINTER(aiVector3D), POINTER(aiQuaternion), POINTER(aiVector3D)])
def aiDecomposeMatrix(mat, scaling, rotation, position, _api_=None): 
    """aiDecomposeMatrix(mat, scaling, rotation, position)
    
        mat : POINTER(aiMatrix4x4)
        scaling : POINTER(aiVector3D)
        rotation : POINTER(aiQuaternion)
        position : POINTER(aiVector3D)
    """
    return _api_(mat, scaling, rotation, position)
    

#~ line: 370, skipped: 7 ~~~~~~

@bind(None, [POINTER(aiMatrix4x4)])
def aiTransposeMatrix4(mat, _api_=None): 
    """aiTransposeMatrix4(mat)
    
        mat : POINTER(aiMatrix4x4)
    """
    return _api_(mat)
    

#~ line: 377, skipped: 7 ~~~~~~

@bind(None, [POINTER(aiMatrix3x3)])
def aiTransposeMatrix3(mat, _api_=None): 
    """aiTransposeMatrix3(mat)
    
        mat : POINTER(aiMatrix3x3)
    """
    return _api_(mat)
    

#~ line: 386, skipped: 9 ~~~~~~

@bind(None, [POINTER(aiVector3D), POINTER(aiMatrix3x3)])
def aiTransformVecByMatrix3(vec, mat, _api_=None): 
    """aiTransformVecByMatrix3(vec, mat)
    
        vec : POINTER(aiVector3D)
        mat : POINTER(aiMatrix3x3)
    """
    return _api_(vec, mat)
    

#~ line: 395, skipped: 9 ~~~~~~

@bind(None, [POINTER(aiVector3D), POINTER(aiMatrix4x4)])
def aiTransformVecByMatrix4(vec, mat, _api_=None): 
    """aiTransformVecByMatrix4(vec, mat)
    
        vec : POINTER(aiVector3D)
        mat : POINTER(aiMatrix4x4)
    """
    return _api_(vec, mat)
    

#~ line: 404, skipped: 9 ~~~~~~

@bind(None, [POINTER(aiMatrix4x4), POINTER(aiMatrix4x4)])
def aiMultiplyMatrix4(dst, src, _api_=None): 
    """aiMultiplyMatrix4(dst, src)
    
        dst : POINTER(aiMatrix4x4)
        src : POINTER(aiMatrix4x4)
    """
    return _api_(dst, src)
    

#~ line: 413, skipped: 9 ~~~~~~

@bind(None, [POINTER(aiMatrix3x3), POINTER(aiMatrix3x3)])
def aiMultiplyMatrix3(dst, src, _api_=None): 
    """aiMultiplyMatrix3(dst, src)
    
        dst : POINTER(aiMatrix3x3)
        src : POINTER(aiMatrix3x3)
    """
    return _api_(dst, src)
    

#~ line: 420, skipped: 7 ~~~~~~

@bind(None, [POINTER(aiMatrix3x3)])
def aiIdentityMatrix3(mat, _api_=None): 
    """aiIdentityMatrix3(mat)
    
        mat : POINTER(aiMatrix3x3)
    """
    return _api_(mat)
    

#~ line: 427, skipped: 7 ~~~~~~

@bind(None, [POINTER(aiMatrix4x4)])
def aiIdentityMatrix4(mat, _api_=None): 
    """aiIdentityMatrix4(mat)
    
        mat : POINTER(aiMatrix4x4)
    """
    return _api_(mat)
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ End of code generated from:
#~   "inc/assimp.h"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


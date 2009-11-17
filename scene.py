#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os, sys
import operator, functools

from .raw import assimp
from .raw.errors import OpenAssestError, OpenAssestApiError
from .raw import aiPostProcess

from .assetBase import AssetBase, byref

from . import node, mesh, material, animation, light, camera

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BasicScene(AssetBase):
    _objFactoryMap = {
        "RootNode": ('single', node.Node),
        "Meshes": ('list', mesh.Mesh),
        "Materials": ('list', material.Material),
        "Animations": ('list', animation.Animation),
        "Textures": ('list', material.ModelTexture),
        "Lights": ('list', light.Light),
        "Cameras": ('list', camera.Camera),
    }

    importFlags = []

    def __init__(self, path=None, flags=None):
        if path is not None:
            self.load(path, flags)

    def __del__(self):
        self.unload()

    def acceptSceneVisitor(self, v, *args, **kw):
        return v.visitScene(self, *args, **kw)

    def load(self, filePath, flags=None):
        filePath = os.path.abspath(filePath)
        if not os.access(filePath, os.R_OK):
            raise IOError("Unable to read file: %r" % (filePath,), filePath)

        # assure we've unload the last one
        self.unload()

        flags = self._reduceFlags(flags)
        ptr = assimp.aiImportFile(filePath, flags)
        if ptr:
            self._as_parameter_ = ptr[0]
            return self._onLoadSuccess(filePath, flags)
        else:
            self._as_parameter_ = None
            return self._onLoadFailure(filePath, flags)

    def _onLoadSuccess(self, filePath, flags):
        self.importFlags = flags

        resourcePath = filePath
        if resourcePath and not os.path.isdir(resourcePath):
            resourcePath = os.path.dirname(resourcePath)

        self.filePath = filePath
        self.resourcePath = resourcePath

        self._loadAssetData()

        return True

    def _onLoadFailure(self, filePath, flags):
        raise OpenAssestApiError("Import failed", filePath)

    def unload(self):
        scene = self._as_parameter_
        if scene is not None:
            assimp.aiReleaseImport(byref(scene))
            self._as_parameter_ = None
            self.__dict__.clear()

    def postProcess(self, flags):
        flags = self._reduceFlags(flags)
        scene = aiApplyPostProcessing(self, flags)
        if not scene:
            raise OpenAssestApiError("Post processing application failed")

    def _reduceFlags(self, flags=None):
        if flags is None:
            flags = self.importFlags

        if isinstance(flags, list):
            flags = functools.reduce(operator.or_, flags, 0)

        return aiPostProcess.aiPostProcessSteps(flags)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def getSceneFlags(self):
        return self._as_parameter_.mFlags
    sceneFlags = property(getSceneFlags)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Scene
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Scene(BasicScene):
    importFlags = [
        aiPostProcess.aiProcess_CalcTangentSpace,
        aiPostProcess.aiProcess_GenSmoothNormals,
        aiPostProcess.aiProcess_JoinIdenticalVertices,
        aiPostProcess.aiProcess_ImproveCacheLocality,
        aiPostProcess.aiProcess_LimitBoneWeights,
        aiPostProcess.aiProcess_RemoveRedundantMaterials,
        aiPostProcess.aiProcess_SplitLargeMeshes,
        aiPostProcess.aiProcess_Triangulate,
        aiPostProcess.aiProcess_GenUVCoords,
        aiPostProcess.aiProcess_SortByPType,
        aiPostProcess.aiProcess_FindDegenerates,
        aiPostProcess.aiProcess_FindInvalidData,
        aiPostProcess.aiProcess_FindInstances,
        aiPostProcess.aiProcess_ValidateDataStructure,
        aiPostProcess.aiProcess_OptimizeMeshes,
        ]


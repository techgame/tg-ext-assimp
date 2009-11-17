##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##~ Copyright (C) 2002-2009  TechGame Networks, LLC.              ##
##~                                                               ##
##~ This library is free software; you can redistribute it        ##
##~ and/or modify it under the terms of the BSD style License as  ##
##~ found in the LICENSE file included with this distribution.    ##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class SceneVisitor(object):
    def visitScene(self, scene):
        self._walkScene(scene)

    def _walkScene(self, scene):
        for lst in [scene.Meshes, scene.Materials, scene.Textures, 
                    scene.Animations, scene.Lights, scene.Cameras]:

            for e in lst:
                e.acceptSceneVisitor(self)

        scene.RootNode.acceptSceneVisitor(self)

    def visitNode(self, node): pass
    def visitMesh(self, mesh): pass
    def visitMaterial(self, material): pass
    def visitModelTexture(self, modelTex): pass
    def visitAnimation(self, animation): pass
    def visitLights(self, light): pass
    def visitCameras(self, camera): pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ScenePrinter(SceneVisitor):
    def __init__(self, item):
        item.acceptSceneVisitor(self)

    def visitScene(self, scene):
        print 'scene:', scene
        self._walkScene(scene)
    def visitNode(self, node):
        print 'node:', node
    def visitMesh(self, mesh):
        print 'mesh:', mesh
    def visitMaterial(self, material):
        print 'material:', material
    def visitModelTexture(self, modelTex):
        print 'modelTex:', modelTex
    def visitAnimation(self, animation):
        print 'animation:', animation
    def visitLights(self, light):
        print 'light:', light
    def visitCameras(self, camera):
        print 'camera:', camera


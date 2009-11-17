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

import weakref
from .assetBase import AssetBase
from . import mesh

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Node(AssetBase):
    _objFactoryMap = {
        "Children": ('list', None), ## Node self-reference
    }

    Parent = None
    Meshes = None

    def acceptSceneVisitor(self, v, *args, **kw):
        return v.visitNode(self, *args, **kw)

    def walkNodes(self):
        stack = [[self]]
        while stack:
            for e in stack.pop():
                yield e
                stack.append(e.Children)

    def walkNodeLevels(self):
        stack = [(0, [self])]
        while stack:
            k, level = stack.pop()
            for e in level:
                e.loadData()
                yield (k,e)
                stack.append((k+1, e.Children))

    def getName(self):
        return str(self._as_parameter_.mName.data)
    name = property(getName)

    def _fixupAssetData(self):
        pxy = weakref.proxy(self)
        for e in self.Children:
            e.Parent = pxy

        s = self._as_parameter_
        if s.mNumMeshes > 0:
            self.Meshes = self._ptrAsArray((s.mNumMeshes,), s.mMeshes, 'I')
        else:
            self.Meshes = None

Node._objFactoryMap["Children"] = ('list', Node)


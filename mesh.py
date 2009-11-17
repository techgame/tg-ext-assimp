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

import numpy
from .assetBase import AssetBase

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Bone(AssetBase):
    _objFactoryMap = {}

    def getName(self):
        return str(self._as_parameter_.mName.data)
    name = property(getName)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Mesh(AssetBase):
    _objFactoryMap = {
        'Bones': ('list', Bone),
    }

    Vertices = Normals = Tangents = Bitangents = Colors = TextureCoords = None

    def acceptSceneVisitor(self, v, *args, **kw):
        return v.visitMesh(self, *args, **kw)

    def getMaterialIndex(self):
        return self._as_parameter_.mMaterialIndex
    materialIdx = materialIndex = property(getMaterialIndex)

    def getPrimTypeMask(self):
        return self._as_parameter_.mPrimitiveTypes
    primTypeMask = property(getPrimTypeMask)

    def _fixupAssetData(self):
        self._loadGeometry()
        self._loadFaces()

    def _loadGeometry(self):
        s = self._as_parameter_
        n = s.mNumVertices

        ptrAsArray = self._ptrAsArray
        self.Vertices = ptrAsArray((n, 3), s.mVertices)
        self.Normals = ptrAsArray((n, 3), s.mNormals)
        self.Tangents = ptrAsArray((n, 3), s.mTangents)
        self.Bitangents = ptrAsArray((n, 3), s.mBitangents)

        cv = [ptrAsArray((n, 4), s.mColors[c]) for c in range(4)]
        cv = [e for e in cv if e.size]
        self.Colors = cv

        tcv = [ptrAsArray((n, 3), s.mTextureCoords[tc]) for tc in range(4)]
        tcv = [e for e in tcv if e.size]
        self.TextureCoords = tcv

    def _loadFaces(self):
        s = self._as_parameter_

        grps = {}
        mask = int(self.primTypeMask)
        for dflag, dim in [(1,1), (2,2), (4,3)]:
            if mask & dflag:
                grps[dim] = FaceGroup(dim)
        if len(grps) == 1:
            grps.values()[0].blockSize = s.mNumFaces

        for fi in xrange(s.mNumFaces):
            f = s.mFaces[fi]
            k = f.mNumIndices

            fg = grps.get(k, None)
            if fg is None:
                grps[k] = fg = FaceGroup(k)

            fg.addFace(f)

        self.faceGroups = dict((fg.dim, fg.result()) for fg in grps.values())


class FaceGroup(object):
    idx = 0
    data = None
    blockSize = 64

    def __init__(self, dim, dtype='H'):
        self.dim = dim
        self.dataList = []
        self.dtype = numpy.dtype(dtype)

    def addFace(self, face):
        idx = self.idx
        d = self.data
        if d is None or d.shape[0] <= idx:
            idx, d = self.newBlock()

        d[idx,:] = [face.mIndices[i] for i in range(face.mNumIndices)]
        self.idx = idx+1

    def addResultBlock(self):
        d = self.data
        if d is not None:
            n = self.idx
            self.data = None
            self.idx = 0

            d.resize((n, self.dim))
            self.dataList.append(d)
            return self.dataList

    def newBlock(self):
        self.addResultBlock()
        self.data = d = numpy.zeros((self.blockSize, self.dim), self.dtype)
        self.idx = 0
        return 0, d

    def result(self):
        dl = self.addResultBlock()
        if len(dl) == 1:
            dl = dl[0]
        elif dl:
            dl = numpy.concatenate(dl, 0)
        else: dl = None
        return dl


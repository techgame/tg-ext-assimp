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

import ctypes
from ctypes import byref, sizeof, string_at
import numpy
from numpy import ndarray

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ptrAsArray(dims, meshData, dtype='f'):
    if not meshData or not dims[0]:
        return ndarray((0,)+dims[1:], dtype)
    print (meshData._type_)
    sz = sizeof(meshData._type_)
    data = string_at(meshData, sz*dims[0])
    return ndarray(dims, dtype, data)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def registerKind(kind, registry):
    def registerFn(fn):
        registry[kind] = fn
        return fn
    return registerFn

class AssetBase(object):
    _as_parameter_ = None

    _objFactoryMap = {} # key: (kind, factory)
    _factoryKindMap = {}

    def __init__(self, ptr=None):
        if ptr:
            self._as_parameter_ = ptr[0]
        else:
            self._as_parameter_ = None

    def __nonzero__(self):
        return bool(self._as_parameter_)

    def _listForKey(self, key):
        s = self._as_parameter_
        num = getattr(s, 'mNum%s'%key)
        arr = getattr(s, 'm%s'%key)
        return [arr[i] for i in range(num)]

    @registerKind('single', _factoryKindMap)
    def _newObjectForKey(self, key, factory):
        e = getattr(self._as_parameter_, 'm%s'%(key,))
        return factory(e)

    @registerKind('list', _factoryKindMap)
    def _newObjectListForKey(self, key, factory):
        try:
            return [factory(e) for e in self._listForKey(key)]
        except:
            print '_newObjectListForKey:', key, factory
            raise

    def _iterLoadAssets(self, factoryMap=None):
        if factoryMap is None:
            factoryMap = self._objFactoryMap

        for key, (kind, factory) in factoryMap.iteritems():
            fnKind = self._factoryKindMap[kind]
            r = fnKind(self, key, factory)
            yield key, r

    _loaded = False
    def loadData(self):
        if not self._loaded:
            self._loadAssetData()
            self._loaded = True

    def _loadAssetData(self):
        for key, r in self._iterLoadAssets():
            setattr(self, key, r)
        self._fixupAssetData()

    def _fixupAssetData(self):
        pass

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def acceptSceneVisitor(self, v, *args, **kw):
        raise NotImplementedError('Subclass Responsibility: %r' % (self,))

    _ptrAsArray = staticmethod(ptrAsArray)


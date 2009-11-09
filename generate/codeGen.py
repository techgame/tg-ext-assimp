#!/usr/bin/env python
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

import os
from TG.gccxml.codeAnalyzer import CodeAnalyzer
from TG.gccxml.xforms.ctypes import AtomFilterVisitor, CCodeGenContext
from TG.gccxml.xforms.ctypes import utils

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

analyzer = CodeAnalyzer(
        inc=['inc',],
        src=['src/genAssImp.c'], 
        baseline=['src/baseline.c'])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class FilterVisitor(AtomFilterVisitor):
    def onFunction(self, item):
        if not item.extern: return
        if item.hasEllipsis():
            return

        if item.name.startswith('ai'):
            if item.name.startswith('aiAssert'):
                return

            self.select(item)

    def onEnumeration(self, item, *args, **kw):
        if item.name.startswith('ai'):
            self.select(item)

    def onUnion(self, item, *args, **kw):
        if item.name.startswith('ai'):
            self.select(item)

    def onStruct(self, item, *args, **kw): 
        if item.name.startswith('ai'):
            self.select(item)

    def onPPDefine(self, item, *args, **kw):
        if item.name.endswith("INC"):
            return

        if item.name.startswith('AI_CONFIG'):
            self.select(item)
        elif item.name.startswith('ai'):
            self.select(item)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Main 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    root = analyzer.loadModel()
    context = CCodeGenContext(root)
    context.atomFilter = FilterVisitor()

    ciFilesByName = dict((os.path.basename(f.name), f) for f in context if f)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # setup imports

    for ciFile in ciFilesByName.itervalues():
        ciFile.importAll('_ctypes_assimp')

    aiConfig = ciFilesByName['aiConfig.h']
    aiTypes = ciFilesByName['aiTypes.h']

    for incFn in ['aiMatrix3x3.h', 'aiMatrix4x4.h', 'aiVector3D.h', 'aiVector2D.h', 'aiQuaternion.h']:
        aiFile = ciFilesByName[incFn]
        aiTypes.importAll(aiFile)

    aiScene = ciFilesByName['aiScene.h']

    for incFn in ['aiTexture.h', 'aiMesh.h', 'aiLight.h', 'aiCamera.h', 'aiMaterial.h', 'aiAnim.h']:
        aiFile = ciFilesByName[incFn]
        aiFile.importAll(aiTypes)
        aiScene.importAll(aiFile)
    ciFilesByName['aiAnim.h'].importAll(ciFilesByName['aiQuaternion.h'])

    assimp = ciFilesByName['assimp.h']
    assimp.importAll(aiTypes, aiConfig, aiScene)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # write output files

    context.outputPath = '../raw/'
    print
    print "Writing out ctypes code:"
    print "========================"
    for ciFile in ciFilesByName.values():
        print 'Writing:', ciFile.filename
        ciFile.writeToFile()
        print 'Done Writing:', ciFile.filename
        print
    print

    utils.includeSupportIn(context.getOutputFilename('_ctypes_support.py'), copySource=True)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__=='__main__':
    main()


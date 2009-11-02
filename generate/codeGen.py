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
            print 'onEnumeration:', item

    def onUnion(self, item, *args, **kw):
        if item.name.startswith('ai'):
            self.select(item)
            print 'onUnion:', item

    def onStruct(self, item, *args, **kw): 
        if item.name.startswith('ai'):
            self.select(item)

    def onClass(self, item, *args, **kw):
        if item.name.startswith('ai'):
            self.select(item)
            print 'onClass:', item

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

    aiTypes = ciFilesByName['aiTypes.h']

    for incFn in ['aiMatrix3x3.h', 'aiMatrix4x4.h', 'aiVector3D.h', 'aiVector2D.h', 'aiQuaternion.h']:
        aiFile = ciFilesByName[incFn]
        aiTypes.importAll(aiFile)

    assimp = ciFilesByName['assimp.h']
    assimp.importAll(aiTypes)

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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Imports 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from . import assimp

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Definitions 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class OpenAssestError(Exception):
    pass

class OpenAssestApiError(OpenAssestError):
    def __init__(self, msg, *args):
        self.aiError = str(assimp.aiGetErrorString())
        msg = '%s: %s' % (msg, self.aiError)
        OpenAssestError.__init__(self, msg, *args)


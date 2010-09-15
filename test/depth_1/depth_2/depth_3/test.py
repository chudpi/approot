import os
import sys
# approot.py may not be in the system path yet, but we still want to be able to test it.
sys.path.append(os.path.abspath('../../../..'))

import approot

'''TODO: write actual unittests'''
print "found .approot at %s" % approot.APPROOT_DIR
print "syspath:"
print '\n'.join(sys.path)

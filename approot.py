import sys
import os

APPROOT_DIR = ''

'''Finds a file named .approot to indicate the disk location of your application's root.
There are two beginning search locations:
1. The location of the executing script,
2. The current executing location (cwd)
Starting at the beginning location, the module traverses the directory tree in the
direction of the root directory, stopping at each level to check for the existence of 
a file named '.approot'; once found, the path is saved in a global variable and the 
search is over.
'''
 
def rootdir():
     ''' what is the root dir on this system'''
     downdir = os.path.abspath('')
     while True:
         updir = os.path.split(downdir)[0]
         if updir == downdir: return updir
         downdir = updir

startdirs = [  os.path.abspath(sys.argv[0]), os.path.abspath('') ]
for updir in startdirs:
    while True:
        if os.path.isfile( os.path.join(updir,'.approot') ) and not os.path.islink( os.path.join(updir,'.approot') ):
            APPROOT_DIR = updir
            break
        updir = os.path.dirname(updir)
        if updir == rootdir(): break #reached root
    if APPROOT_DIR:
        break 

if APPROOT_DIR:
    try:
        fh = open( os.path.join(APPROOT_DIR, '.approot'), 'r' )
#        print code_str
#        code_obj = compile(code_str,'.approot','exec')
        exec(fh)
        fh.close()
    except:
        raise

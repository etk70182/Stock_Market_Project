import os
import sys
import math
import glob

def clip(lo, x, hi):
    return max(lo, min(hi, x))

def getAllFiles( folder, ftype="", m="" ):
    file_filt = ""
    if m != "":
        file_filt = "*" + m
    file_filt = file_filt + "*." + ftype
    files = glob.glob( os.path.join( folder, file_filt ) )
    if len( files ) == 0:
        print( "Could not find any {0:s} files.".format(file_filt) )
        sys.exit(-1)
    return files

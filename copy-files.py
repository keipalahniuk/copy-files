#! python3
from shutil import copy
import os

rootdir = r'D:\path\pathpath\looooooongpath\ROOT FOLDER'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        src = os.path.join(subdir, file)

        if (file[15:18] == 'x'):
            dst = r'D:\path\DESTINATION 1'
            copy(src, dst)

        if (file[15:18] == 'y'):
            dst = r'D:\path\DESTINATION 2'
            copy(src, dst)

        if (file[15:18] == 'z'):
            dst = r'D:\path\DESTINATION 3'
            copy(src, dst)




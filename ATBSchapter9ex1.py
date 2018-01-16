# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:59:22 2018

@author: Justin Clifford Smith
"""

#%% Exercise One - Selective Copy

#Walks through a folder tree and searches for files with a certain file extension. 
#Copy these files from whatever location they are in to a new folder.

import os
import sys
import shutil

copyfolder = input('Select a folder: ')
extension = input(f'Copy all files with what extension to {copyfolder}: ')

try: 
    os.mkdir(os.path.join('.', copyfolder))
except FileExistsError:
    print("Selected folder exists.")
    
if extension[0] != '.':
    print('ERROR: extension must begin with a period.')
    sys.exit()


for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith(extension):
            if os.path.isfile(os.path.join('.', copyfolder, filename)) != True:
                shutil.copy(os.path.join(foldername, filename), \
                            os.path.join('.',copyfolder))
                print(f"Copying {os.path.join(foldername,filename)} " 
                                 f"to {os.path.join('.', copyfolder)}")
            

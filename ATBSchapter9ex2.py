# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:00:23 2018

@author: Justin Clifford Smith
"""

#%% Exercise Two - Deleting Unneeded Files

#Walk through a folder tree and searches for files or folders over 50 MB
#(Remember, to get a file’s size, you can use os.path.getsize() from the os module.) 
#Print the files with their absolute path to the screen.

import os

for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        size = os.path.getsize(os.path.join(foldername, filename))
        if size > 50000: #50 MB
            print(f"{os.path.abspath(os.path.join(foldername, filename))}"
                       "is {size/1000} MB.")
    
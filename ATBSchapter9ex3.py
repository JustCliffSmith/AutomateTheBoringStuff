# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:00:48 2018

@author: Justin Clifford Smith
"""

#%% Exercise Three - Filling In The Gaps

#Finds all files with a given prefix, such as spam001.txt, spam002.txt, etc. 
#in a single folder and locates any gaps in the numbering. 
#Have the program rename all the later files to close this gap.

import os
import shutil
import re

'''
choice = input('Open or close a numbering gap? (open, close) ')
if choice != 'open' or choice != 'close':
    print('You entered an invalid choice. Goodbye.')
    sys.exit()
'''
choice = 'close'
#choice = 'open'

if choice == 'close':
    prefix = input('Input prefix that has a numbering gap: ')

    regex = re.compile(rf'^({prefix})(\d)+\.(\w)')

    count = 1
    for files in os.listdir('.'):
        root, ext = os.path.splitext(files)
        mo = regex.search(files)
        if mo != None and mo[1] == prefix:
            shutil.move('./' + files, './' + prefix + str(count).zfill(4) +ext)
            print(f"{'./' + files} -> "
                  f"{'./' + prefix + str(count).zfill(4) + ext}")
            count += 1

'''
My attempt below at trying to figure out how to open up a gap. The idea I
struggle with is figuring out how to do it without overwriting files.


def file_increment(prefix, count, ext):
    if os.path.isfile('./' + prefix + str(count+1).zfill(4) + ext):
        count += 1
        file_increment(prefix, count, ext)
    #shutil.move({'./' + prefix + str(count).zfill(4) + ext},\
                #{'./' + prefix + str(count+1).zfill(4) + ext})
    print(f"{'./' + prefix + str(count).zfill(4) + ext} -> "
          f"{'./' + prefix + str(count+1).zfill(4) + ext}")

if choice == 'open':
    prefix = input('Input prefix that you want a numbering gap: ')
    gap = input('Input the value you want missing: ')

    regex = re.compile(rf'^({prefix})(\d)+\.(\w)')

    count = int(gap) + 1
    for files in os.listdir('.'):
        root, ext = os.path.splitext(files)
        mo = regex.search(files)
        if mo != None and mo[1] == prefix:
            if int(mo[2]) < count:
                print(f'{mo[2]}, {count}')
            else:
                #shutil.move('./' + files, './' + prefix + str(count).zfill(4) + ext))
                file_increment(prefix, count ,ext)
                count += 1
'''            
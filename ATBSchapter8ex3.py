# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:53:17 2018

@author: Justin Clifford Smith
"""

#%% Exercise Three - Regex Search

#Opens all .txt files in folder and searches for any line that matches a regex.

import re
import os

inputregex = input("Input your regex: ")

regex = re.compile(r'{}'.format(inputregex))

for file in os.listdir('.'):
    if file.endswith('.txt'):
        with open(file) as file:
#            for line in file:
#                search = regex.search(line)
#                if search != None:
#                    print(line)
            [print(line) for line in file if regex.search(line) != None]
#Yay, first time recognziing a good spot for list comprehension on my own!
#Also this book doesn't teach them.
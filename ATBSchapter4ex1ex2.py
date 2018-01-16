# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:20:54 2017

author: Justin Clifford Smith
"""

#%% First Exercise - Comma Code
# Take a list of words and output the list comma seperated with and 
# before the final

def commacode(foo):
    combined_string = ''
    for i in range(len(foo)-1):
        combined_string += foo[i]
        combined_string += ', '
    combined_string += 'and ' + foo[-1]
    return combined_string

assert commacode(['apples', 'bananas', 'tofu', 'cats']) ==\
     'apples, bananas, tofu, and cats'

print(commacode(['apples', 'bananas', 'tofu', 'cats', 'horses', 'mules']))

#%% Second Exercise - Character Picture Grid
# Rotate the grid such that it is a vertical heart.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for xcoord in range(len(grid[0])):
    for ycoord in range(len(grid)):
#        print('{},{} '.format(xcoord, ycoord),end='')
        print('{}'.format(grid[ycoord][xcoord]), end='')
    print('')
        

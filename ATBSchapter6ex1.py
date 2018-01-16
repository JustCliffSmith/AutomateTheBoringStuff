# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:33:53 2017

author: Justin Clifford Smith
"""

#%% Exercise One - Table Printer
# Take a list of strings and print a nice table

#this is oriented differently from what was asked
def print_table(table):
    colWidths = [0]*len(table[0])
    for row in table:
        for index, colvalue in enumerate(row):
            if len(colvalue) > colWidths[index]:
                colWidths[index] = len(colvalue)
        
    for row in table:
        for index, colvalue in enumerate(row):
            print(colvalue.rjust(colWidths[index]), end='')    
        print('\n',end='')

# this is what the exercise asked for
def print_table2(table):
    colWidths = [0]*len(table)
    for colindex, col in enumerate(table):
        for colvalue in col:
            if len(colvalue) > colWidths[colindex]:
                colWidths[colindex] = len(colvalue)
    
    for rowindex in range(len(table[0])):
#        for colindex, col in enumerate(table):
#            print(col[rowindex].rjust(colWidths[colindex]), end=' ')
        for col in table:
            print(col[rowindex].rjust(max(colWidths)), end='')
        print('\n',end='')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
print('\n')
print_table2(tableData)
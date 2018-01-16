# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:53:17 2018

@author: Justin Clifford Smith
"""

#%% Exercise Two - Mad Libs

#Mad Libs program that reads in a text file and prompts users for replacements 
#for each instance of the words ADJECTIVE, NOUN, ADVERB, or VERB.

import sys

replace = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

with open(sys.argv[1]) as madlib:
    with open('madlibs_update.txt', 'w') as out:
        for sentence in madlib.read().split('.'):
            if sentence != '':
                for word in sentence.split():
                    if word in replace:
                        if word != 'ADJECTIVE':
                            word = input('Enter a {}: '.format(word.lower()))
                        else:
                            word = input('Enter an {}: '.format(word.lower()))
                    out.write(' {}'.format(word))
                out.write('.')
        print("Mad libs written to madlibs_update.txt")

#This works.... but I feel like it can be written more simply using regex. 
#It currently is overengineered to work only with sentences that end in .

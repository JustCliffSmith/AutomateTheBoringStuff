# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:20:37 2018

@author: Justin Clifford Smith
"""

#Debug the following code

'''
This is the original code

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        
'''

#This is my debugged code along with notes of changes

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1: #the numeric toss wasn't translated to the language of our input
    toss = 'heads'
else:
    toss = 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    #not a bug, but this input should be changed to be as robust as above
    guess = input() #guess was mispelled
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        
#ATBS uses IDLE, however I am using Spyder. The debugger was helpful for
#noticing the misspelled variable!
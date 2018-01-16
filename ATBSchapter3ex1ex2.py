# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:22:50 2017

author: Justin Clifford Smith
"""

#%% First and Second Exercise - The Collatz Sequence and Input Validation
# Ex1) Implement the collatz sequence, Ex2) add input validation.

import sys

def collatz(number):
    if number % 2 == 0:
        print(number/2)
        return number/2
    if number % 2 ==1:
        print(3*number + 1)
        return 3*number + 1
     
print("Input an int: ")
try:
    num = int(input())
except ValueError:
    sys.exit("Not an int!")

if num <= 0:    
    sys.exit("Oh yeah, needs to be positive too.")    
    
while True:
    num = collatz(num)
    if num == 1:
        break

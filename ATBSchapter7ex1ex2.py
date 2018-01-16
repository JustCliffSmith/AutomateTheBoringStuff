# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:39:15 2017

author: Justin Clifford Smith
"""

#%% Exercise One - Strong Password Detection
# Detect a strong password

import re

goodpwd = 'Thisstrong90' #order doesn't matter in my regex. This is sufficient.
badpwd1 = 'thisstrong90'#no caps
badpwd2 = 'THISSTRONG90' #no lower
badpwd3 = 'Thisstrong' #no number
badpwd4 = 'This' #too short

capreg = re.compile(r'[A-Z]+')#contains at least one capital
lowreg = re.compile(r'[a-z]+')#contains at least one lower
numreg = re.compile(r'\d+')#contains at least one digit
lenreg = re.compile(r'(\S){8,}')#has at least 8 non-whitespace characters

def checkpwd(pwd):
    mocap = capreg.search(str(pwd))
    molow = lowreg.search(str(pwd))
    monum = numreg.search(str(pwd))
    molen = lenreg.search(str(pwd))
    if mocap and molow and monum and molen != None:
        print('Strong!')
    else:
        print('Too weak!') #possible improvement: report what fails
        
checkpwd(goodpwd)
checkpwd(badpwd1)
checkpwd(badpwd2)
checkpwd(badpwd3)
checkpwd(badpwd4)


#%% Exercise Two - Regex version of strip()
# Implement strip including removal of non-whitespace

import re


def regex_strip(string, remove=r'\s'):
    remove = str(remove)
    #removal = r'^({})*([^{}]*)({})*$'.format(remove,remove,remove) 
    #the above works unless there is a remove character in the middle
    removal = r'^({})*(.*)'.format(remove)#strips from the front of the string
    stripreg = re.compile(removal)
    mo = stripreg.search(str(string))
    if mo != None:
        mo = stripreg.search(mo.group(2)[::-1])#strip the reversed string
        return mo.group(2)[::-1]#put the string back in the right order
    else:
        return string

teststring1 = '  remove  '
teststring2 = '  remove this  '
teststring3 = 'remove  '
teststring4 = 'aaaremove aaa'

print(regex_strip(teststring1))
print(regex_strip(teststring2))
print(regex_strip(teststring3))
print(regex_strip(teststring4, 'a') )


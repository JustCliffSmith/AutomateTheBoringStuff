# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:53:17 2018

@author: Justin Clifford Smith
"""
#%% Exercise One - Extending the Multiclipboard
# Implement a delete and delete all functionality into the 
# multiclipboard example.

#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe delete <keyword> - Deletes keyword
#        py.exe delete - Deletes all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    try: #didn't ask for this, but why not include it?!
        del mcbShelf[sys.argv[2]]
    except KeyError:
        print("Key doesn't exist.")
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'delete':
        for key in mcbShelf:
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()


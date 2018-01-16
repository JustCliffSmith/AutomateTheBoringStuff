# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:24:07 2017

author: Justin Clifford Smith
"""

#%% Exercise One - Fantasy Game Inventory
# Create a display inventory function


def display_inventory(inventory):
    total = 0
    print('Inventory:')
    for key in inventory:
        print('{} {}'.format(inventory[key], key))
        total += inventory[key]
    print('Total number of items: ' + str(total))
    
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(stuff)

#%% Exercise Two - List to Dictionary Function
# Create a function to add items to the inventory
    
def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)

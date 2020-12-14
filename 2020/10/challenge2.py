# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:44:51 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.readlines()   # Read text from file into variable
    
adapters = sorted([int(elem) for elem in inputs])   # Convert strings in list to integers

combinations = {0:1}    # Create dict for combinations at each index of adapters, at index of 0, number of combinations is 1
for a in adapters:
    combinations[a] = 0     # Create empty key-value pair for adapter
    # Test each condition, add total combinations of the previous adapter
    if a-1 in combinations:
        combinations[a] += combinations[a-1]
    if a-2 in combinations:
        combinations[a] += combinations[a-2]
    if a-3 in combinations:
        combinations[a] += combinations[a-3]

answer = combinations[adapters[-1]] # Get total combinations from highest joltage adapter
print(answer)   # 2644613988352
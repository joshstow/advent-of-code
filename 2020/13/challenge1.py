# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:52:09 2021

@author: Josh Stow
"""

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read text from file into variable
    earliest, ids = f.readlines()

# Cast earliest var to int
earliest = int(earliest)
depart = earliest

# Split string on commas, remove x values from list
ids = [int(elem) for elem in ids.split(',') if elem != 'x']

found = False
while not found:
    # Increment depart timestamp
    depart += 1
    
    for id in ids:
        if depart % id == 0:    # Check if id is factor of depart time
            found = True
            break

# Calculate answer as required
answer = (depart - earliest) * id
print(answer)   # 4722
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:55:08 2021

@author: Josh Stow
"""

# Import dependencies
import re

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read inputs into variable, split on newlines
    data = f.read().split('\n\n')

rules = []
for rule in data[0].split('\n'):
    rules.extend(re.findall('\d+-\d+', rule))   # Extract number ranges from rules

ranges = [tuple(map(int, elem.split('-'))) for elem in rules]   # Construct list of range tuples

nearby_tickets = [list(map(int, elem.split(','))) for elem in data[2].split('\n')[1:]]  # Construct list of ticket field values

error_rate = 0
for ticket in nearby_tickets:
    for val in ticket:
        if not any(min <= val <= max for (min, max) in ranges): # Add value if it exists outside any of the ranges
            error_rate += val
            
print(error_rate)   # 24110
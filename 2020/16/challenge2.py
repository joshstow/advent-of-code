# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:10:01 2021

@author: Josh Stow
"""

# Import dependencies
import re

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read inputs into variable, split on newlines
    data = f.read().split('\n\n')

ranges = []
for line in data[0].split('\n'):
    ranges.extend(re.findall(r'\d+-\d+', line))   # Extract number ranges

ranges = [tuple(map(int, elem.split('-'))) for elem in ranges]   # Construct list of range tuples
ranges = [range(elem[0], elem[1]+1) for elem in ranges]     # Convert ranges into range objects

field_names = re.findall(r'([a-z ]+):', data[0])    # Get field names from data
field_rules = list(zip(field_names, [(x,y) for x,y in zip(ranges[0::2], ranges[1::2])]))    # Combine field names with respective ranges

nearby_tickets = [list(map(int, elem.split(','))) for elem in data[2].split('\n')[1:]]  # Construct list of ticket field values

# Filter out invalid tickets
valid_tickets = []
for ticket in nearby_tickets:
    valid = True
    for val in ticket:
        if not any(val in range for range in ranges):
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)
        
field_values = [[elem[i] for elem in valid_tickets] for i in range(len(valid_tickets[0]))]    # Rotate list to isolate values for each field to sublists

my_tickets = list(map(int, data[1].split('\n')[1].split(',')))  # Isolate my ticket values

# Build list of valid rules for each field
valids = {}
for i in range(len(field_values)):
    valids[i] = []
    for rule in field_rules:
        if all(val in rule[1][0] or val in rule[1][1] for val in field_values[i]):
            valids[i].append(rule[0])   # Append valid rules to end of array with column number key

# Sequentially remove rules from all list when a key contains solely said rule
my_tickets_dict = {}
for _ in range(len(field_values)-1):
    rule = ''
    for j in range(len(field_values)):
        if len(valids[j]) == 1:
            rule = valids[j][0]
            my_tickets_dict[rule] = my_tickets[j]
            for k in range(len(field_values)):
                if rule in valids[k] and len(valids[k]) != 1:
                    valids[k].remove(rule)

answer = 1
for field in my_tickets_dict.keys():
    # Multiply values of fields which contain departure
    if 'departure' in field:
        answer *= my_tickets_dict[field]

print(answer)   # 6766503490793

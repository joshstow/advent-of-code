# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:11:30 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable

inputs = inputs.split('\n\n')     # Split string on each new line char
inputs = [input.split('\n') for input in inputs]   # Remove newline chars from each item

# Convert strings in list to sets
a = []
for item in inputs:
    b = []
    for string in item:
        b.append(set(string))
    a.append(b)

commons = []
for item in a:
    commons.append(len(item[0].intersection(*item))) # Append number of common chars in group to list

answer = sum(commons)   # Calculate total number of chars shared for each group
print(answer)   # 3050
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:00:36 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.readlines()   # Read text from file into variable
    
adapters = [int(elem) for elem in inputs]   # Convert strings in list to integers
adapters.append(max(adapters)+3)    # Append built-in joltage adapter

# Declare iterator variables
rating = 0  # Start with outlet rating
one_jolt = 0
three_jolt = 0
while True:
    # Test each condition
    if (rating+1) in adapters:
        rating += 1
        one_jolt += 1
        continue
    if (rating+2) in adapters:
        rating += 2
        continue
    if (rating+3) in adapters:
        rating += 3
        three_jolt += 1
        continue
    break

answer = one_jolt*three_jolt    # Multiply number of difference of 3's by number of difference of 1's as required
print(answer)   # 2574
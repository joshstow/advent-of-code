# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:43:58 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable

inputs = inputs.split('\n\n')     # Split string on each new line char
inputs = [input.replace('\n','') for input in inputs]   # Remove newline chars from each item

# Get number of unique characters in each item of list
answer = 0
for item in inputs:
    answer += len(set(item))
    
print(answer)   # 6416
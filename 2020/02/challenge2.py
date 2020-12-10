# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:38:06 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n')     # Split string on each new line char

passwords = []
for item in inputs:
    positions, char, password = item.split()    # Split string on each space char
    char = char[0]  # Remove ':' char
    pos1, pos2 = positions.split('-')     # Split string on '-' char
    passwords.append({'password': password, 'char': char, 'pos1': int(pos1), 'pos2': int(pos2)})    # Create new dict for each line in inputs

answer = 0
for item in passwords:
    try:
        char1 = item['password'][item['pos1']-1]    # Find char in password at specified position
    except: char1 = None    # Handle error if index out of range
    try:
        char2 = item['password'][item['pos2']-1]    # Find char in password at specified position
    except: char2 = None    # Handle error if index out of range
    if char1 == item['char'] and not char2 == item['char']:    # Evaluate
        answer += 1
    if char2 == item['char'] and not char1 == item['char']:    # Evaluate
        answer += 1

print(answer) # 502
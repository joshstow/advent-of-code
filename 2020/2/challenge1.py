# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:20:41 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n')     # Split string on each new line char

passwords = []
for item in inputs:
    range, char, password = item.split()    # Split string on each space char
    char = char[0]  # Remove ':' char
    min, max = range.split('-')     # Split string on '-' char
    passwords.append({'password': password, 'char': char, 'min': int(min), 'max': int(max)})    # Create new dict for each line in inputs

answer = 0
for item in passwords:
    chars_in_str = item['password'].count(item['char'])     # Count number of desired char in password
    if chars_in_str >= item['min'] and chars_in_str <= item['max']:     # Evaluate
        answer += 1
        
print(answer)   # 548
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:17:42 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n')     # Split string into list on each newline char
instructions = [(item.split()[0],int(item.split()[1])) for item in inputs] # Create list with tuple for each operator and operand pair

# Declare iterators
visited = []
accumulator = 0
pointer = 0
while True:
    # Break loop if instruction has already been visited
    if pointer not in visited:
        visited.append(pointer) # Add instruction index to visited list
        if instructions[pointer][0] == 'acc':
            # Add operand to accumulator var and increment pointer by 1
            accumulator += instructions[pointer][1]
            pointer += 1
        if instructions[pointer][0] == 'jmp':
            # Increment pointer by operand
            pointer += instructions[pointer][1]
        if instructions[pointer][0] == 'nop':
            # Increment pointer by 1
            pointer += 1
    else:
        break

answer = accumulator
print(answer)   # 1930
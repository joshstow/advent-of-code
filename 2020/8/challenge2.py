# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:27:24 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n')     # Split string into list on each newline char
instructions = [(item.split()[0],int(item.split()[1])) for item in inputs] # Create list with tuple for each operator and operand pair

def run_instructions(instructions):
    # Declare iterators
    visited = []
    accumulator = 0
    pointer = 0
    while True:
        # Break loop if instruction has already been visited
        if pointer not in visited:
            visited.append(pointer) # Add instruction index to visited list
            # If index out of range, program finished
            try:
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
            except:
                return accumulator
        else:
            return None
    return None

# Declare iterators
answer = None
index = 0
for line in instructions:
    temp = [(item.split()[0],int(item.split()[1])) for item in inputs] # Create new version of list on each iteration
    # Convert operator to nop if jmp
    if line[0] == 'jmp':
        temp[index] = ('nop', temp[index][1])
        answer = run_instructions(temp)     # Call function to run through instructions
    # Convert operator to jmp if nop
    if line[0] == 'nop':
        temp[index] = ('jmp', temp[index][1])
        answer = run_instructions(temp)     # Call function to run through instructions
    # Break loop if accumulator value returned
    if answer != None:
        break
    index += 1

print(answer)   # 1688
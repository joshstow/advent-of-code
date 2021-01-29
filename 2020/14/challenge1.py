# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:06:15 2021

@author: Josh Stow
"""

# Import dependencies
import re

def bitmask(val, mask):
    """
    Apply bitmask to value, return decimal conversion from binary.
    
    Args:
        val::str
        mask::str
        
    Returns:
        result::int
        
    """
    result = ''
    
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += val[i]
        else:
            result += mask[i]
    
    return int('0b'+result, 2)
    
with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read instructions from file into list of tuples
    instructions = [(int(re.findall(r'\d+', line[0])[0]),bin(int(line[1]))[2:].zfill(36)) if line[0] != 'mask' else (line[0],line[1].strip()) for line in [line.split(' = ') for line in f.readlines()]]
    
memory = {}
mask = ''
for instruc in instructions:
    # Set mask var to new bitmask
    if instruc[0] == 'mask':
        mask = instruc[1]
        continue
    # Write value of masked binary to memory location in dict
    memory[instruc[0]] = bitmask(instruc[1], mask)
    
answer = sum(memory.values())   # Sum all values of dictionary as required
print(answer)   # 8566770985168
    
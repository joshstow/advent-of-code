# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:09:36 2021

@author: Josh Stow
"""

# Import dependencies
import re

def bitmask(val, mask):
    """
    Apply bitmask to value, return masked address.
    
    Args:
        val::str
        mask::str
        
    Returns:
        result::str
        
    """
    result = ''
    
    for i in range(len(mask)):
        if mask[i] != '0':
            result += mask[i]
        else:
            result += val[i]
    
    return result

def calc_addresses(masked):
    """
    Recursively calculate all possible combinations of addresses.
    
    Args:
        masked::str
        
    Returns:
        masked::str
        addresses::str
        
    """
    addresses = ''
    
    if 'X' not in masked:
        return masked
    
    xloc = masked.index('X')
    masked_0 = masked[:xloc]+'0'+masked[xloc+1:]
    masked_1 = masked[:xloc]+'1'+masked[xloc+1:]
    
    addresses += calc_addresses(masked_0)+','
    addresses += calc_addresses(masked_1)
    
    return addresses
    
with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read instructions from file into list of tuples
    instructions = [(bin(int(re.findall(r'\d+', line[0])[0]))[2:].zfill(36),int(line[1])) if line[0] != 'mask' else (line[0],line[1].strip()) for line in [line.split(' = ') for line in f.readlines()]]
    
memory = {}
mask = ''
for instruc in instructions:
    # Set mask var to new bitmask
    if instruc[0] == 'mask':
        mask = instruc[1]
        continue
    
    masked = bitmask(instruc[0], mask)  # Calculate masked string
    addresses = calc_addresses(masked).split(',')   # Find all possible addresses and split into list
    
    # Write values for each address to memory
    for address in addresses:
        memory[address] = instruc[1]
    
answer = sum(memory.values())   # Sum all values of dictionary as required
print(answer)   # 4832039794082

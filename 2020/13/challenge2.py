# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:57:08 2021

@author: Josh Stow
"""

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read text from file into variable
    earliest, ids = f.readlines()

# Split string on commas, enumerate, and remove x values from resultant list
ids = [(elem[0], int(elem[1])) for elem in list(enumerate(ids.split(','))) if elem[1] != 'x']

# Calculate Chinese Remainder Theorem modulus calculation
crt_mods = {bus: -i % bus for i, bus in ids}
# Sort list of (id - index) % id and invert
vals = list(reversed(sorted(crt_mods)))
# Get id of highest (id -index) % index value in dict
answer = crt_mods[vals[0]]
# Set r to highest (id - index) % id value
r = vals[0]

for x in vals[1:]:
    # Repeat until CRT value is found
    while (answer % x) != crt_mods[x]:
        answer += r
    # Multipy to find full product
    r *= x
    
print(answer)  # 825305207525452


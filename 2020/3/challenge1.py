# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:40:59 2020

@author: joshstow
"""

import collections

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n')     # Split string on each new line char
Coord = collections.namedtuple('Coord', 'x y')  # Create namedtuple type
vector = Coord(x=3,y=1)     # Write angle as vector

# Calculate number each element should be multiplied by
mul = int(((len(inputs)/vector.y)*vector.x)//len(inputs[0]))
if ((len(inputs)/vector.y)*vector.x)%len(inputs[0]) != 0:
    mul += 1
    
l = [line*mul for line in inputs]   # Extend items in list by factor of multiplier

# Declare increment variables
y = 0
x = 0
answer = 0
while True:     # Loop through entire list
    try:
        if l[y][x] == '#':  # Evaluate if tree encountered
            answer += 1
        # Move "pointer"
        y += vector.y
        x += vector.x
    except:
        break
    
print(answer)   # 187
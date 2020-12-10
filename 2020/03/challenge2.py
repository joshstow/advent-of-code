# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:54:07 2020

@author: joshstow
"""

import collections

def getTrees(inputs, x, y):
    vector = Coord(x=x,y=y)     # Write angle as vector
    l = extendList(inputs, vector)  # Call function to extend list
    # Declare increment variables
    y = 0
    x = 0
    sum = 0
    while True:     # Loop through entire list
        try:
            if l[y][x] == '#':  # Evaluate if tree encountered
                sum += 1
            # Move "pointer"
            y += vector.y
            x += vector.x
        except:
            break
    return sum

def extendList(inputs, vector):
    # Calculate number each element should be multiplied by
    mul = int(((len(inputs)/vector.y)*vector.x)//len(inputs[0]))
    if ((len(inputs)/vector.y)*vector.x)%len(inputs[0]) != 0:
        mul += 1
    return [line*mul for line in inputs]   # Extend items in list by factor of multiplier

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable

inputs = inputs.split('\n')     # Split string on each new line char
Coord = collections.namedtuple('Coord', 'x y')  # Create namedtuple type

# Call functions to get number of trees for each condition
a = getTrees(inputs, 1, 1)
b = getTrees(inputs, 3, 1)
c = getTrees(inputs, 5, 1)
d = getTrees(inputs, 7, 1)
e = getTrees(inputs, 1, 2)
answer = a*b*c*d*e  # Multiply as per instructions

print(answer)   # 4723283400

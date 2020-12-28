# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:10:56 2020

@author: Josh Stow
"""

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read text from file into variable, split on new line, convert each string to tuple pair of instruction and integer
    instructions = [(item[0], int(item[1:])) for item in f.read().split('\n')]

# Declare location variables
x = 0
y = 0
# Starting direction and bearing
direction = 'E'
bearing = 90
for instruc, val in instructions:
    # If Forward, change instruction to current direction
    if instruc == 'F':
        instruc = direction
    # Move ship in required direction
    if instruc == 'N':    # Add num to y if North
        y += val
    if instruc == 'S':    # Subtract num from y if South
        y -= val
    if instruc == 'E':    # Add num to x if East
        x += val
    if instruc == 'W':    # Subtract num from x if West
        x -= val
    # Change bearing by specified amount
    if instruc == 'R':
        bearing += val
    if instruc == 'L':
        bearing -= val
    # Keep bearing value between 0 and 360
    bearing = bearing % 360
    # Change direction accordingly
    if bearing == 0:
        direction = 'N'
    if bearing == 90:
        direction = 'E'
    if bearing == 180:
        direction = 'S'
    if bearing == 270:
        direction = 'W'
        
answer = abs(x)+abs(y)    # Calculate Manhattan distance as required
print(answer)   # 2297
        

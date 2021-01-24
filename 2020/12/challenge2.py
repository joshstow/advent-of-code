# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:00:44 2020

@author: Josh Stow
"""

# Import dependencies
import math

def rotateAboutPoint(ox, oy, px, py, val):
    """
    Return point rotated about origin by given value.
    
    Args:
        ox::int
        oy::int
        px::int
        py::int
        val::int

    Returns:
        x::int
        y::int

    """
    angle = math.radians(val)   # Convert degrees to radians for trig calcs
    
    # Declare constants
    c = math.cos(angle)
    s = math.sin(angle)
    
    # Calculate x and y points after rotation with trig
    x = round(ox + c * (px - ox) - s * (py - oy))
    y = round(oy + s * (px - ox) + c * (py - oy))

    return x, y

def moveToWaypoint(ship_x, ship_y, wp_x, wp_y, val):
    """
    Move ship to waypoint a given number of times.
    
    Args:
        ship_x::int
        ship_y::int
        wp_x::int
        wp_y::int
        val::int
        
    Returns:
        ship_x::int
        ship_y::int
        wp_x::int
        wp_y::int
        
    """
    # Calculate difference between waypoint and ship positions
    dx = wp_x - ship_x
    dy = wp_y - ship_y
    
    # Move coords given number of times
    for _ in range(val):
        ship_x += dx
        wp_x += dx
        ship_y += dy
        wp_y += dy
        
    return ship_x, ship_y, wp_x, wp_y

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read text from file into variable, split on new line, convert each string to tuple pair of instruction and integer
    instructions = [(item[0], int(item[1:])) for item in f.read().split('\n')]

# Declare ship axis variables
ship_x = 0
ship_y = 0

# Declare waypoint axis variables
wp_x = 10
wp_y = 1

for instruc, val in instructions:
    # Move ship in required direction
    if instruc == 'N':    # Add val to wp_y if North
        wp_y += val
        continue
    if instruc == 'S':    # Subtract val from wp_y if South
        wp_y -= val
        continue
    if instruc == 'E':    # Add val to wp_x if East
        wp_x += val
        continue
    if instruc == 'W':    # Subtract val from wp_x if West
        wp_x -= val
        continue
    if instruc == 'L':
        wp_x, wp_y = rotateAboutPoint(ship_x, ship_y, wp_x, wp_y, val)  # Calculate point after rotation anti-clockwise
        continue
    if instruc == 'R':
        wp_x, wp_y = rotateAboutPoint(ship_x, ship_y, wp_x, wp_y, -val) # Calculate point after rotation clockwise
        continue
    if instruc == 'F':
        ship_x, ship_y, wp_x, wp_y = moveToWaypoint(ship_x, ship_y, wp_x, wp_y, val)    # Move ship to waypoint
        continue
        
answer = abs(ship_x)+abs(ship_y)    # Calculate Manhattan distance as required
print(answer)   # 89984
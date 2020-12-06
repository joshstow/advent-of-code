# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:16:48 2020

@author: joshstow
"""

def findSeat(boarding_pass_tup, rows, cols):
    for char in boarding_pass_tup[0]:
        if char == 'F':
            rows = splitList(rows)[0]   # Keep first half of list
        else:
            rows = splitList(rows)[1]   # Keep second half of list
    for char in boarding_pass_tup[1]:
        if char == 'L':
            cols = splitList(cols)[0]   # Keep first half of list
        else:
            cols = splitList(cols)[1]   # Keep second half of list
    return (rows.pop(), cols.pop()) # Take remaining values and remove from list

def splitList(list):
    return (list[:len(list)//2], list[len(list)//2:])   # Return tuple of each half of list

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable

inputs = inputs.split('\n')     # Split string on each new line char

# Create new list with tuples of column and row values
l = []
for item in inputs:
    l.append((item[:7],item[-3:]))

# Create strings of all rows and columns
total_rows = [row for row in range(128)]
total_cols = [col for col in range(8)]

# Create new list for seat IDs
ids = []
for item in l:
    a = findSeat(item, total_rows, total_cols)
    ids.append((a[0]*8)+a[1])   # Calculate ID and append to list
    
ids.sort()  # Sort list in numerical order
ids = ids[8:-8]     # Remove first and last rows from list

# Find missing item in list
i = ids[0]
for item in ids:
    if item != i:
        answer = i
        break
    i += 1

print(answer)   # 565
    
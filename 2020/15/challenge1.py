# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:30:08 2021

@author: Josh Stow
"""

# Puzzle inputs
inputs = [2,1,10,11,0,6]

visited = {}

# Populate visited dictionary with starting numbers
for i in range(len(inputs)):
    visited[inputs[i]] = [i]
    prev = inputs[i]

i = len(visited)    # Set index to next value after input list
while i < 2020:
    # Number is new
    if len(visited[prev]) == 1:
        visited[0].append(i)
        prev = 0
        i += 1
        continue
    # Number already been encountered
    diff = visited[prev][-1] - visited[prev][-2]    # Subtract prev index from last seen index
    if diff not in visited:
        visited[diff] = [i]
    else:
        visited[diff].append(i)
    prev = diff
    i += 1
    
print(prev) # 232
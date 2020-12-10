# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:33:46 2020

@author: joshstow
"""

import re

# Create graph data structure class
class Graph():
    def __init__(self, dict, edges):
        self.edges = edges
        self.dict = dict
        # Create dictionary of each nodes parents
        for parent, child in self.edges:
            self.dict[child].append(parent)
           
    def traverse(self, colour):
        parents = set(self.dict[colour])    # Remove dupes with set
        for parent_colour in self.dict[colour]:
            parents |= self.traverse(parent_colour)     # Union parent set with recursively called sets
        return parents

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.readlines()   # Read lines from text file into variable

# Create keys in dictionary for all possible colours, create list of edge tuples for each parent/child pair
dict = {}
edges = []
for line in inputs:
    parent = re.match(r'(\w+\s\w+)\sbags', line).group(1)   # Match first bag colour in string
    children = re.findall(r'(\w+\s\w+)\sbag', line)[1:]     # Match remaining bag colours in string
    dict[parent] = []   # Add key for parent colour with value of empty list to dictionary
    if children[0] == 'no other':   # Skip iteration if bag contains nothing
        continue
    for child in children:
        edges.append((parent,child))    # Append tuple to list


graph = Graph(dict, edges)  # Construct graph of parents
answer = len(graph.traverse('shiny gold'))  # Calculate length of set returned by function
print(answer)   # 278

    


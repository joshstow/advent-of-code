# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:22:48 2020

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
            self.dict[parent].append(child)
           
    def traverse(self, colour):
        # Sum the product of the number of each child bag and the number of parent bags recursively
        return sum(int(num)+int(num)*self.traverse(child_colour) for num, child_colour in self.dict[colour])
        

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.readlines()   # Read lines from text file into variable

# Create keys in dictionary for all possible colours, create list of edge tuples for each parent/child pair
dict = {}
edges = []
for line in inputs:
    parent = re.match(r'(\w+\s\w+)\sbags', line).group(1)   # Match first bag colour in string
    children = re.findall(r'(\d)?\s?(\w+\s\w+)\sbag', line)[1:]     # Match remaining bag colours and respective numbers in string
    dict[parent] = []   # Add key for parent colour with value of empty list to dictionary
    if children[0][1] == 'no other':   # Skip iteration if bag contains nothing
        continue
    for child in children:
        edges.append((parent,child))    # Append tuple to list



graph = Graph(dict, edges)  # Construct graph of children
answer = graph.traverse('shiny gold') # Calculate number of bags contained in given colour bag
print(answer)   # 45157
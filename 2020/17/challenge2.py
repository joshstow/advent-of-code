# -*- coding: utf8 -*-
"""
Created on Mon Feb 22 13:05:31 2021

@author: Josh Stow
"""

def populateInitialNodes(data):
    alive_nodes = set()

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                alive_nodes.add((y,x,0,0))

    return alive_nodes

def runCycles(alive_nodes, iterations):
    for idx in range(iterations):

        offset = idx + 1    # Expand view area by 1 in each direction
        new_alive_nodes = set()
        # Account for original grid size in each range
        for y in range(-offset, offset+8):
            for x in range(-offset, offset+8): 
                for z in range(-offset, offset+1):
                    for w in range(-offset, offset+1):

                        adj = 0
                        for i in range(-1,2):
                            for j in range(-1,2):
                                for k in range(-1,2):
                                    for l in range(-1,2):
                                        # Increment adjacent counter if an alive node surrounds current node
                                        if not(i == 0 and j == 0 and k == 0 and l == 0):
                                            if (y+i, x+j, z+k, w+l) in alive_nodes:
                                                adj += 1

                        # If node is alive and either exactly 2 or 3 adj nodes are alive, node remains active
                        if (y,x,z,w) in alive_nodes and (adj == 2 or adj == 3):
                            new_alive_nodes.add((y,x,z,w)) 
                        
                        # If node is not alive and exactly 3 adj nodes are alive, node becomes alive
                        if (y,x,z,w) not in alive_nodes and adj == 3:
                            new_alive_nodes.add((y,x,z,w))

        alive_nodes = new_alive_nodes

    return alive_nodes

with open('inputs.txt', 'r') as f:  # Open file of puzzle inputs
    # Read lines into variable
    data = f.read().split('\n')[:-1]

# Calculate set of all alive node coords
initial_alive_nodes = populateInitialNodes(data)
# Run calculations based upon rules
alive_nodes = runCycles(initial_alive_nodes, 6)

answer = len(alive_nodes)
print(answer)   # 1884 

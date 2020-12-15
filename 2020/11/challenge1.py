# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:28:12 2020

@author: Josh Stow
"""

class floorPlan():
    def __init__(self, plan):
        """Constructor method.
        """
        self.plan = plan
        self.prev_plan = None
        self.x = len(plan[0])
        self.y = len(plan)
        
    def simulateMovement(self):
        """Updates plan attribute based on rules set by challenge.
        """
        self.prev_plan = [x[:] for x in self.plan]   # Assign current plan to previous plan
        new_plan = [x[:] for x in self.plan]    # Assign current plan to new plan
        # Iterate through each position in plan
        for y in range(self.y):
            for x in range(self.x):
                # Test for occupied seats, try/except on conditions which may cause index out of range error
                occupied = 0
                # Top left
                if self.plan[y-1][x-1] == '#' and y-1 >= 0 and x-1 >= 0:
                    occupied += 1
                # Top mid
                if self.plan[y-1][x] == '#' and y-1 >= 0:
                    occupied += 1
                # Top right
                try:
                    if self.plan[y-1][x+1] == '#' and y-1 >= 0:
                        occupied += 1
                except:
                    pass
                # Mid left
                if self.plan[y][x-1] == '#' and x-1 >= 0:
                    occupied += 1
                # Mid right
                try:
                    if self.plan[y][x+1] == '#':
                        occupied += 1
                except:
                    pass
                # Bottom left
                try:
                    if self.plan[y+1][x-1] == '#' and x-1 >= 0:
                        occupied += 1
                except:
                    pass
                # Bottom mid
                try:
                    if self.plan[y+1][x] == '#':
                        occupied += 1
                except:
                    pass
                # Bottom right
                try:
                    if self.plan[y+1][x+1] == '#':
                        occupied += 1
                except:
                    pass
                # If seat empty and no occupied seats adjacent to it, seat becomes occupied
                if self.plan[y][x] == 'L' and occupied == 0:
                    new_plan[y][x] = '#'
                # If seat occupied and four or more seats adjacent to it occupied, seat becomes empty
                if self.plan[y][x] == '#' and occupied >= 4:
                    new_plan[y][x] = 'L'
        self.plan = new_plan

    def isSame(self):
        """Returns boolean based on whether current plan is same as previous
        plan or not.
        """
        if self.plan == self.prev_plan:
            return True
        return False
    
    def getOccupied(self):
        """Returns number of occupied seats in plan.
        """
        occupied = 0
        for line in self.plan:
            occupied += line.count('#')
        return occupied

with open('inputs.txt', 'r') as f:   # Open file of puzzle inputs
    # Read text from file into variable, split on new line, cast each string to list
    inputs = [list(line) for line in f.read().split('\n')]

fp = floorPlan(inputs)  # Instantiate floor plan object

# Simulate each stage of movement until nothing changes
while True:
    fp.simulateMovement()
    # End loop if current plan same is previous plan
    if fp.isSame():
        answer = fp.getOccupied()   # Get number of occupied seats in plan
        break

print(answer)   # 2270
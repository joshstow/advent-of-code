# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:58:28 2020

@author: joshstow
"""

# Generator function for frame
def create_frame(data):
    for i in range(25,len(data[25:])):  # 25 previous elements for each element
        yield data[i-25:i]

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.readlines()   # Read text from file into variable
    
data = [int(elem) for elem in inputs]   # Convert strings in list to integers

frame = create_frame(data)  # Initialise generator for frame
head = (num for num in data[25:])   # Create generator for head
        
while True:
    # Set variables for current frame and head
    f = next(frame)
    h = next(head)
    found = False
    # Loop through frame
    for i in range(25):
        if h-f[i] in f and h/2 != f[i]: # Check if other number in frame and numbers arent identical
            found = True
            break
    if found == False:
        answer = h
        break

print(answer)   # 105950735
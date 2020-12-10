# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:29:02 2020

@author: joshstow
"""

TARGET = 105950735  # From previous part

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.readlines()   # Read text from file into variable
    
data = [int(elem) for elem in inputs]   # Convert strings in list to integers

start = 0   # Declare iterator variable
while True:
    nums = []
    index = 0   # Declare iterator variable for nested loop
    while True:
        nums.append(data[start+index])  # Append each number to list
        index += 1
        if sum(nums) >= TARGET: # Add elements from list
            start += 1
            break
    if sum(nums) == TARGET:
        print(True)
        break
    
answer = min(nums) + max(nums)  # Add smallest and largest numbers in list as required
print(answer)   # 13826915
        
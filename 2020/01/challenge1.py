# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:35:42 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    numbers = file.read()   # Read text from file into variable
    
numbers = numbers.split('\n')   # Split string on each new line char
numbers = [int(num) for num in numbers] # Cast string values to list of integers
    
for num in numbers:
    if (2020-num) in numbers:   # Search list for number which results in 2020 when added to first number
        num1 = num
        num2 = 2020-num
        break

answer = num1*num2 # Multiply complimentary numbers as per instructions
print(answer)   # 468051
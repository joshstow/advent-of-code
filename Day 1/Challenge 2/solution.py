# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:04:46 2020

@author: joshstow
"""

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    numbers = file.read()   # Read text from file into variable
    
numbers = numbers.split('\n')   # Split string on each new line char
numbers = [int(num) for num in numbers] # Cast string values to list of integers

end = False     # Condition for breaking loop

for i in numbers:
    for j in numbers:
        if (2020-(i+j)) in numbers:   # Search list for number which results in 2020 when added to first number
            num1 = i
            num2 = j
            num3 = 2020-(i+j)
            end = True
            break
    if end == True:
        break
        
answer = num1*num2*num3     # Multiply complimentary numbers as per instructions
print(answer)   # 272611658
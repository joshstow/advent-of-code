# -*- coding: utf8 -*-
"""
Created on Tue Feb 23 15:19:28 2021

@author: Josh Stow
"""

# Import dependencies
import re

with open('inputs.txt', 'r') as f:  # Open file of puzzle inputs
    # Read lines into list
    expressions = [str(item.strip().replace(' ', '')) for item in f.readlines()]

def calculateExpression(expression):
    # Create stacks for operators and operands
    operators = list(reversed([item for item in expression if item in ('+', '*')]))
    operands = list(reversed(re.findall(r'\d+', expression))) 
    result = operands.pop()
    # Sequentially calculate result of stacks
    for n in list(reversed(operands)):
        result = eval(str(result) + operators.pop() + n)
        
    return result

def compileExpression(expression):
    while '(' in expression:
        # Find all inner brackets
        inners = [item for item in re.findall(r'\([^()]+\)', ''.join(expression))]
        for n in inners:
            # Replace inner brackets with evaluation
            result = calculateExpression(n[1:-1])
            expression = expression.replace(n, str(result), 1)

    return calculateExpression(expression)

answer = sum(compileExpression(expression) for expression in expressions) # Total of all expressions as required
print(answer)   # 2743012121210

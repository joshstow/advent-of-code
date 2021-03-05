# -*- coding: utf8 -*-
"""
Created on Mon Mar  1 12:03:43 2021

@author: Josh Stow
"""

# Import dependencies
import re

with open('inputs.txt', 'r') as f:  # Open file of puzzle inputs
    # Read lines into list
    expressions = [str(item.strip().replace(' ', '')) for item in f.readlines()]

def calculateExpression(expression):
    while '+' in expression:
        # Find first addition
        addition = re.findall(r'\d+\+\d+', expression)[0]
        # Replace first addition in string with result
        result = eval(addition)
        expression = expression.replace(addition, str(result), 1)

    return eval(expression)

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
print(answer)   # 65658760783597 

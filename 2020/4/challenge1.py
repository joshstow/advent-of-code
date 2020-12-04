# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:58:54 2020

@author: joshstow
"""

import re

# Create Passport class
class Passport():
    def __init__(self, fields):
        self.fields = fields    # Dictionary showing fields found in each passport
    
    # Returns True if no fields have False as value
    def isValid(self):
        for item in self.fields.values():
            if not item:
                return False
        return True

with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n\n')     # Split string on each new line char

# Iterate over items
passports = []
for item in inputs:
    # Search for fields using RegEx and construct dictionary
    fields = {'byr': bool(re.search(r'byr:',item)),
              'iyr': bool(re.search(r'iyr:',item)),
              'eyr': bool(re.search(r'eyr:',item)),
              'hgt': bool(re.search(r'hgt:',item)),
              'hcl': bool(re.search(r'hcl:',item)),
              'ecl': bool(re.search(r'ecl:',item)),
              'pid': bool(re.search(r'pid:',item))
              }
    passports.append(Passport(fields))  # Instantiate new passport object and append to list

answer = 0
for passport in passports:
    if passport.isValid():  # Increment answer if function returns True
        answer += 1

print(answer)   # 245
    
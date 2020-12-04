# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:18:44 2020

@author: joshstow
"""

import re

# Create Passport class
class Passport():
    def __init__(self, fields):
        self.fields = fields    # Dictionary showing fields found in each passport
    
    # Returns True if no fields have False as value
    def isValid(self):
        # Evaluate validity of each field value
        if not(self.fields['byr'] != '' and (int(self.fields['byr']) >= 1920 and int(self.fields['byr']) <= 2002)):
            return False
        if not(self.fields['iyr'] != '' and (int(self.fields['iyr']) >= 2010 and int(self.fields['iyr']) <= 2020)):
            return False
        if not(self.fields['eyr'] != '' and (int(self.fields['eyr']) >= 2020 and int(self.fields['eyr']) <= 2030)):
            return False
        if self.fields['hgt'] != '':
            if not((self.fields['hgt'][-2:] == 'cm' and (int(self.fields['hgt'][:-2]) >= 150 and int(self.fields['hgt'][:-2]) <= 193)) or (self.fields['hgt'][-2:] == 'in' and (int(self.fields['hgt'][:-2]) >= 59 and int(self.fields['hgt'][:-2]) <= 76))):
                return False
        else:
            return False
        if self.fields['hcl'] == '' or self.fields['ecl'] == '':
            return False
        if len(self.fields['pid']) != 9:
            return False
        return True


with open('inputs.txt', 'r') as file:   # Open file of puzzle inputs
    inputs = file.read()   # Read text from file into variable
    
inputs = inputs.split('\n\n')     # Split string on each new line char

# Create RegEx patterns
byr_pattern = re.compile(r'byr:\d{4}')
iyr_pattern = re.compile(r'iyr:\d{4}')
eyr_pattern = re.compile(r'eyr:\d{4}')
hgt_pattern = re.compile(r'hgt:\d+[cmin]+')
hcl_pattern = re.compile(r'hcl:#[0-9a-f]{6}')
ecl_pattern = re.compile(r'(ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth)')
pid_pattern = re.compile(r'pid:\d+')

# Iterate over items
passports = []
for item in inputs:
    # Search for fields using RegEx and construct dictionary
    fields = {'byr': ''.join(re.findall(byr_pattern, item))[4:],
              'iyr': ''.join(re.findall(iyr_pattern, item))[4:],
              'eyr': ''.join(re.findall(eyr_pattern, item))[4:],
              'hgt': ''.join(re.findall(hgt_pattern, item))[4:],
              'hcl': ''.join(re.findall(hcl_pattern, item))[4:],
              'ecl': ''.join(re.findall(ecl_pattern, item))[4:],
              'pid': ''.join(re.findall(pid_pattern, item))[4:]
              }
    passports.append(Passport(fields))  # Instantiate new passport object and append to list

answer = 0
for passport in passports:
    if passport.isValid():  # Increment answer if function returns True
        answer += 1

print(answer)   # 133
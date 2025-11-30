# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:20:15 2024

@author: joshstow
"""

with open("input.txt", "r") as f:   # Open file of puzzle inputs
    puzzle_input = f.read().split("\n")   # Read text from file into list

def part1(puzzle_input):
    total = 0

    for item in puzzle_input:
        digits_only = "".join(filter(str.isdigit, item))
        calibration_value = int(f"{digits_only[0]}{digits_only[-1]}")

        total += calibration_value

    return total

def part2(puzzle_input):
    NUMERIC_LITERALS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    total = 0

    for item in puzzle_input:
        digits_only = item
        print(item)
        for key in NUMERIC_LITERALS:
            digits_only = digits_only.replace(key, str(NUMERIC_LITERALS[key]))
        print(digits_only)

        digits_only = "".join(filter(str.isdigit, digits_only))
        print(digits_only)
        calibration_value = int(f"{digits_only[0]}{digits_only[-1]}")
        print(calibration_value)

        total += calibration_value
        print(total)

    return total


answer1 = part1(puzzle_input)
print(f"Answer 1: {answer1}")

answer2 = part2(puzzle_input)
print(f"Answer 2: {answer2}")

"""
@author: github.com/joshstow
"""

with open("puzzle_input.txt", "r") as f:  # Open puzzle input file
    puzzle_input = f.read().split("\n")   # Split file contents into list by new lines
    rotations = [(rotation[0], int(rotation[1:])) for rotation in puzzle_input] # Seperate directional component from distance component 


def part1():
    pos = 50    # Starting position
    zero_count = 0  # Number of times we land on zero
    
    for direction, distance in rotations:   # Iterate through all rotation instructions
        if direction == 'L':
            pos = (pos - distance) % 100

        if direction == 'R':
            pos = (pos + distance) % 100

        if pos == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")
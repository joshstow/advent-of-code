"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    lines = f.read().split('\n')
    lines = [line.split() for line in lines]

def part1():
    total = 0

    for i in range(len(lines[0])):
        equation = lines[0][i]
        operator = lines[4][i]

        for j in range(1, len(lines)-1):
            equation += operator + lines[j][i]

        total += eval(equation)

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")
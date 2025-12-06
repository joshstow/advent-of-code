"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    lines = f.read().split('\n')

    start_col = 0
    col_ranges = []

    for col_idx in range(len(lines[0])):
        is_empty = not any(lines[row][col_idx] != ' ' for row in range(len(lines)))

        if start_col == None:
            start_col = col_idx

        if is_empty:
            col_ranges.append((start_col, col_idx - 1))
            start_col = None

    # Remember to include last column
    col_ranges.append((start_col, len(lines[0]) - 1))

def part1():
    total = 0

    for start, end in col_ranges:
        # Get first operand
        equation = lines[0][start:end+1].strip()
        # Get operator
        operator = lines[4][start:end+1].strip()

        for j in range(1, len(lines)-1):
            equation += operator + lines[j][start:end+1].strip()

        total += eval(equation)

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")
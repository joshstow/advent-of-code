"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    grid = f.read().split('\n')

def part1():
    wavefront = [0] * len(grid[0])
    beam_idx = grid[0].index('S')
    wavefront[beam_idx] = 1

    total = 0

    for row in grid[1:]:
        for col_idx in range(len(row)):
            if row[col_idx] == '^' and wavefront[col_idx] == 1:
                total += 1
                wavefront[col_idx] = 0
                wavefront[col_idx-1] = 1
                wavefront[col_idx+1] = 1

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")
"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    # Split file contents by double newline to seperate ranges from the ids
    ranges, ids = f.read().split('\n\n')
    ranges = [tuple(map(int, line.split('-'))) for line in ranges.split('\n')]
    ids = [int(id) for id in ids.split('\n')]

def part1():
    total_fresh = 0

    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                total_fresh += 1
                break

    return total_fresh

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

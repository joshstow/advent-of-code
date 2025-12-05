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
    total = 0

    for id in ids:
        for lower, upper in ranges:
            if lower <= id <= upper:
                total += 1
                break

    return total

def part2():
    sorted_ranges = sorted(ranges)

    total = 0
    current_lower, current_upper = sorted_ranges[0]

    for lower, upper in sorted_ranges[1:]:
        if lower > current_upper + 1:
            total += current_upper - current_lower + 1
            current_lower, current_upper = lower, upper
        else:
            current_upper = max(current_upper, upper)

    total += current_upper - current_lower + 1

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
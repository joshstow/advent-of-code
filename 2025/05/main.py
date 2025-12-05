"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    # Split file contents by double newline to seperate ranges from the ids
    ranges, ids = f.read().split('\n\n')
    # Parse ranges into list of (lower, upper) tuples
    ranges = [tuple(map(int, line.split('-'))) for line in ranges.split('\n')]
    # Parse ids into list of integers
    ids = [int(id) for id in ids.split('\n')]

def part1():
    total = 0

    # Check id against all ranges
    for id in ids:
        for lower, upper in ranges:
            # If id is within range, increment total
            if lower <= id <= upper:
                total += 1
                break

    return total

def part2():
    # Sort ranges by lower bound
    sorted_ranges = sorted(ranges)

    total = 0
    # Start with first range as current merged range
    current_lower, current_upper = sorted_ranges[0]

    for lower, upper in sorted_ranges[1:]:
        # If a gap is found
        if lower > current_upper + 1:
            # Add current merged range to total and start new range
            total += current_upper - current_lower + 1
            current_lower, current_upper = lower, upper
        # If ranges touch or overlap
        else:
            # Extend current range
            current_upper = max(current_upper, upper)

    # Add final merged range to total
    total += current_upper - current_lower + 1

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", "r") as f:
    # Split file contents into list by commas
    puzzle_input = f.read().split(',')
    # Convert each "start-end" string into tuple of integers
    ranges = [tuple(map(int, item.split('-'))) for item in puzzle_input]

def part1():
    invalid_total = 0

    for start, end in ranges:
        for i in range(start, end+1):
            str_i = str(i)
            # Only check numbers with even digit length
            if not(len(str_i) % 2):
                # Split the number into two equal halves
                string1, string2 = str_i[:len(str_i)//2], str_i[len(str_i)//2:]
                # Add to total if both halves are identical
                if string1 == string2:
                    invalid_total += i

    return invalid_total

def part2():
    invalid_total = 0

    for start, end in ranges:
        for i in range(start, end+1):
            str_i = str(i)
            # Check if str_i has repeating pattern by searching for it in (str_i + str_i)
            # Starting at index 1 avoids matching the original string
            # If found before midpoint, indicates repeating structure
            if (str_i + str_i).index(str_i, 1) < len(str_i):
                invalid_total += i

    return invalid_total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")

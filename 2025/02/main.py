"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", "r") as f:
    puzzle_input = f.read().split(',')
    ranges = [tuple(map(int, item.split('-'))) for item in puzzle_input]


def part1():
    invalid_total = 0

    for start, end in ranges:
        for i in range(start, end+1):
            str_i = str(i)
            if not(len(str_i) % 2):
                string1, string2 = str_i[:len(str_i)//2], str_i[len(str_i)//2:]
                if string1 == string2:
                    invalid_total += i

    return invalid_total



if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    lines = f.read().split('\n')
    tiles = [tuple(map(int, line.split(','))) for line in lines]

def part1():
    largest_area = 0

    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            width = abs(tiles[i][0] - tiles[j][0]) + 1
            height = abs(tiles[i][1] - tiles[j][1]) + 1
            largest_area = max(largest_area, width * height)

    return largest_area

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")
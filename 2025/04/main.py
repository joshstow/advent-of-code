"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", "r") as f:
    # Split file contents by newlines into list
    grid = f.read().split('\n')

def paper_at_position(grid, y, x):
    if (y < 0) or (x < 0) or (y > len(grid)-1) or (x > len(grid[0])-1):
        return False

    if grid[y][x] == '@':
        return True
    
    else:
        return False

def part1():
    total_accessible = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            adjacent_total = 0

            # If there is a roll of paper at this grid position
            if grid[y][x] == '@':
                for cy in range(-1, 2):
                    for cx in range(-1, 2):
                        if not(cy == 0 and cx == 0):
                            if paper_at_position(grid, y+cy, x+cx):
                                adjacent_total += 1

                if adjacent_total < 4:
                    total_accessible += 1

    return total_accessible

def part2():
    total_removed = 0
    has_removals = True

    mutable_grid = [list(row) for row in grid]

    while has_removals == True:
        removed_this_iteration = 0

        for y in range(len(mutable_grid)):
            for x in range(len(mutable_grid[y])):
                adjacent_total = 0

                # If there is a roll of paper at this grid position
                if mutable_grid[y][x] == '@':
                    for cy in range(-1, 2):
                        for cx in range(-1, 2):
                            if not(cy == 0 and cx == 0):
                                if paper_at_position(mutable_grid, y+cy, x+cx):
                                    adjacent_total += 1

                    if adjacent_total < 4:
                        removed_this_iteration += 1
                        mutable_grid[y][x] = '.'

        total_removed += removed_this_iteration

        if removed_this_iteration == 0:
            has_removals = False

    return total_removed

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    grid = f.read().split('\n')

def part1():
    # Create wavefront, tracks beam presence at each column position
    wavefront = [0] * len(grid[0])
    # Find starting position of beam
    beam_idx = grid[0].index('S')
    wavefront[beam_idx] = 1

    total = 0

    # Process each row after first row
    for row in grid[1:]:
        for col_idx in range(len(row)):
            # Check if beam encounters a splitter
            if row[col_idx] == '^' and wavefront[col_idx] == 1:
                # Count the split
                total += 1
                # Remove original beam
                wavefront[col_idx] = 0
                # Create beams going left and right
                wavefront[col_idx-1] = 1
                wavefront[col_idx+1] = 1

    return total

def part2():
    # Create wavefront, tracks number of beams at each column position
    wavefront = [0] * len(grid[0])
    # Find starting position of beam
    beam_idx = grid[0].index('S')
    wavefront[beam_idx] = 1

    # Process each row after first row
    for row in grid[1:]:
        for col_idx in range(len(row)):
            current_beams = wavefront[col_idx]

            # Check if beams encounter a splitter
            if row[col_idx] == '^' and current_beams != 0:
                # Remove original beams
                wavefront[col_idx] = 0
                # Add beams going left and right
                wavefront[col_idx-1] += current_beams
                wavefront[col_idx+1] += current_beams

    return sum(wavefront)

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
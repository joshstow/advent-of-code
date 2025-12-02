"""
@author: github.com/joshstow
"""

with open("puzzle_input.txt", "r") as f:  # Open puzzle input file
    puzzle_input = f.read().split("\n")   # Split file contents into list by new lines
    rotations = [(rotation[0], int(rotation[1:])) for rotation in puzzle_input] # Seperate directional component from distance component 


def part1():
    pos = 50    # Starting position
    zero_count = 0  # Number of times we land on zero
    
    for direction, distance in rotations:   # Iterate through all rotation instructions
        if direction == 'L':
            pos = (pos - distance) % 100

        if direction == 'R':
            pos = (pos + distance) % 100

        if pos == 0:
            zero_count += 1

    return zero_count


def part2():
    pos = 50    # Starting position
    zero_count = 0  # Number of times we land on zero
    
    for direction, distance in rotations:   # Iterate through all rotation instructions    
        start_pos = pos % 100   # Normalise position to within 0-99

        # Calculate distance from zero position
        # Moving right: From start_pos up to 100 (wraps to zero)
        # Moving left: From start_pos down to zero
        # When either left or right case evaluate to zero, distance to zero is 100
        distance_to_zero = ((100 - start_pos) if direction == "R" else start_pos) or 100
        
        # If distance is enough to reach zero at least once, count first crossing plus any additional full laps
        if distance >= distance_to_zero:
            zero_count += 1 + (distance - distance_to_zero) // 100

        # Update position using modular arithmetic so value can "wrap around"
        if direction == 'L':
            pos = (pos - distance) % 100
        if direction == 'R':
            pos = (pos + distance) % 100

    return zero_count



if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
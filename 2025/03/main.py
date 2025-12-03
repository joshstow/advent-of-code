"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", "r") as f:
    # Split file contents by newlines into list
    blocks = f.read().split('\n')

def part1():
    total = 0

    for block in blocks:
        largest_joltage = 0

        # Try all pairs of indices
        for i in range(len(block)):
            for j in range(i+1, len(block)):
                # Concatenate characters at i and j to form number
                current_joltage = int(block[i] + block[j])
                
                if current_joltage > largest_joltage:
                    largest_joltage = current_joltage

        total += largest_joltage

    return total

def part2():
    NUM_DIGITS = 12
    total = 0

    for block in blocks:
        last_position = 0   # Keep track of where we last picked a digit
        largest_joltage = ""

        for digit_index in range(NUM_DIGITS):
            max_digit = '0'
            # Calculate furthest position we can search while still leaving enough characters for remaining digits
            remaining_digits = NUM_DIGITS - digit_index - 1
            search_end = len(block) - remaining_digits

            # Find the maximum digit in the valid range
            for i in range(last_position, search_end):
                if block[i] > max_digit:
                    max_digit = block[i]
                    # Store last position
                    last_position = i

            # Move past selected character for next iteration
            last_position += 1
            largest_joltage += max_digit

        total += int(largest_joltage)

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
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

        for i in range(len(block)):
            for j in range(i+1, len(block)):
                current_joltage = int(block[i] + block[j])
                
                if current_joltage > largest_joltage:
                    largest_joltage = current_joltage

        total += largest_joltage

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

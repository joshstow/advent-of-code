"""
@author: github.com/joshstow
"""

from collections import deque

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    lines = f.read().split('\n')
    
    machines = []
    for line in lines:
        machine = []

        # Split line into components
        line = line.split()

        # Parse light diagram
        light_diagram = line.pop(0)[1:-1]

        # Build integer bitmask
        goal = 0
        for i, light in enumerate(light_diagram):
            if light == '#':
                # Set bit at position i
                goal |= (1 << i)

        machine.append(goal)

        # Parse joltage requirements
        machine.append(tuple(map(int, line.pop(-1)[1:-1].split(','))))

        # Parse wiring schematic
        wiring_schematic = [tuple(map(int, item[1:-1].split(','))) for item in line]
        machine.append(wiring_schematic)

        machines.append(machine)

def bfs(goal, buttons):
    start = 0

    if start == goal:
        return 0
    
    # Create deque for BFS
    queue = deque([(start, 0)])
    # Create set for visited states
    visited = {start}

    while queue:
        # Dequeue state
        state, presses = queue.popleft()

        for button in buttons:
            new_state = state

            for idx in button:
                # Toggle the bit at position idx
                new_state ^= (1 << idx)

            # Check if we have reached the goal
            if new_state == goal:
                return presses + 1
            
            # If new state not visited, enqueue it
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

def part1():
    total = 0

    for machine in machines:
        goal = machine[0]
        buttons = machine[2]

        presses = bfs(goal, buttons)
        total += presses

    return total

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")
"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    lines = f.read().split('\n')
    # Parse tile coordinates
    tiles = [tuple(map(int, line.split(','))) for line in lines]

def get_boundary_segments(tiles):
    segments = []

    for i in range(len(tiles)):
        current = tiles[i]
        # Wrap around to first tile after last
        next_tile = tiles[(i + 1) % len(tiles)]

        segments.append((current, next_tile))

    return segments

def segment_intersects_rectangle(seg, x1, y1, x2, y2):
    # Extract segment endpoints
    (s_x1, s_y1), (s_x2, s_y2) = seg
    
    # Normalise rectangle coordinates
    r_x1, r_x2 = min(x1, x2), max(x1, x2)
    r_y1, r_y2 = min(y1, y2), max(y1, y2)
    
    # Vertical segment
    if s_x1 == s_x2:
        # Must be strictly inside x-range
        if r_x1 < s_x1 < r_x2:
            seg_min_y, seg_max_y = min(s_y1, s_y2), max(s_y1, s_y2)
            # Check if segment overlaps rectangle's y-range
            if seg_min_y < r_y2 and seg_max_y > r_y1:
                return True
    
    # Horizontal segment
    else:
        # Must be strictly inside y-range
        if  r_y1 < s_y1 < r_y2:
            seg_min_x, seg_max_x = min(s_x1, s_x2), max(s_x1, s_x2)

            # Check if segment overlaps rectangle's x-range
            if seg_min_x < r_x2 and seg_max_x > r_x1:
                return True
    
    return False

def is_valid_rectangle(segments, x1, y1, x2, y2):
    for seg in segments:
        # Rectangle is invalid if a boundary segment crosses through it
        if segment_intersects_rectangle(seg, x1, y1, x2, y2):
            return False

    return True

def part1():
    largest_area = 0

    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            width = abs(tiles[i][0] - tiles[j][0]) + 1
            height = abs(tiles[i][1] - tiles[j][1]) + 1
            largest_area = max(largest_area, width * height)

    return largest_area

def part2():
    # Get boundary segments for the shape formed by tiles
    segments = get_boundary_segments(tiles)

    rectangles = []

    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            # Get coordinates of opposite corners
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            rectangles.append((area, x1, y1, x2, y2))

    # Sort rectangles by area in descending order
    rectangles.sort(reverse=True)

    for area, x1, y1, x2, y2 in rectangles:
        if is_valid_rectangle(segments, x1, y1, x2, y2):
            return area

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
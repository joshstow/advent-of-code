"""
@author: github.com/joshstow
"""

# Open puzzle input file
with open("puzzle_input.txt", 'r') as f:
    lines = f.read().split('\n')
    # Parse input coordinates
    coords = [tuple(map(int, line.split(','))) for line in lines]
    # Sort coordinates
    coords.sort()

def calculate_3d_distance_sq(p, q):
    # Return squared Euclidean distance between 3D points p and q, omit sqrt for efficiency
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # If x itself is its own parent, its the root
        if self.parent[x] == x:
            return x
            
        # Otherwise recursively find the root of x's parent
        return self.find(self.parent[x])

    def union(self, a, b):
        # Find root representatives of a and b
        ra, rb = self.find(a), self.find(b)

        # If already in the same set, do nothing
        if ra == rb:
            return
        
        # Union by size (attach smaller tree under larger tree)
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        # Point root of smaller tree to root of larger tree
        self.parent[rb] = ra
        # Update size of the merged tree
        self.size[ra] += self.size[rb]

    def component_sizes(self):
        # Return sizes of all components (only for root nodes)
        return [self.size[i] for i in range(len(self.parent)) if i == self.parent[i]]

def part1():
    n = len(coords)
    distance_edges = [] # (distance_sq, idx_a, idx_b)

    # Build all edges with squared distances
    for i in range(n-1):
        for j in range(i+1, n):
            distance_edges.append((calculate_3d_distance_sq(coords[i], coords[j]), i, j))

    # Sort edges by distance
    distance_edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)
    # Union the first n edges
    for _, a, b in distance_edges[:n]:
        uf.union(a, b)

    # Get sizes of all components, largest to smallest
    sizes = sorted(uf.component_sizes(), reverse=True)

    # Find product of three largest components
    return sizes[0] * sizes[1] * sizes[2]

def part2():
    n = len(coords)
    distance_edges = [] # (distance_sq, idx_a, idx_b)

    # Build all edges with squared distances
    for i in range(n-1):
        for j in range(i+1, n):
            distance_edges.append((calculate_3d_distance_sq(coords[i], coords[j]), i, j))

    # Sort edges by distance
    distance_edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)
    # Union edges until all connected
    for _, a, b in distance_edges:
        # if uf.find(a) != uf.find(b):
            uf.union(a,b)

            # Check if all connected
            if len(uf.component_sizes()) == 1:
                # All connected
                return coords[a][0] * coords[b][0]

if __name__ == "__main__":
    answer1 = part1()
    print(f"Answer 1: {answer1}")

    answer2 = part2()
    print(f"Answer 2: {answer2}")
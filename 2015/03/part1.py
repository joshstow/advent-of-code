with open("input.txt", "r") as f:
  instructions = f.read()

visited = {"0,0": 1}
x = 0
y = 0
for instruction in instructions:
  if instruction == "^":
    y += 1
  if instruction == "v":
    y -= 1
  if instruction == ">":
    x += 1
  if instruction == "<":
    x -= 1

  visited[f"{x},{y}"] = visited.get(f"{x},{y}", 1) + 1 

print(len(visited))
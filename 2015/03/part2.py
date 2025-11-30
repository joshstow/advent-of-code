with open("input.txt", "r") as f:
  instructions = f.read()

visited = {"0,0": 2}
santa_pos = [0,0] # [x,y]
robo_pos = [0,0]  # [x,y]

for idx, instruction in enumerate(instructions):
  if idx % 2 == 0:  # santa
    if instruction == "^":
      santa_pos[1] += 1
    if instruction == "v":
      santa_pos[1] -= 1
    if instruction == ">":
      santa_pos[0] += 1
    if instruction == "<":
      santa_pos[0] -= 1

    visited[f"{santa_pos[0]},{santa_pos[1]}"] = visited.get(f"{santa_pos[0]},{santa_pos[1]}", 1) + 1 

  else: # robo-santa
    if instruction == "^":
      robo_pos[1] += 1
    if instruction == "v":
      robo_pos[1] -= 1
    if instruction == ">":
      robo_pos[0] += 1
    if instruction == "<":
      robo_pos[0] -= 1

    visited[f"{robo_pos[0]},{robo_pos[1]}"] = visited.get(f"{robo_pos[0]},{robo_pos[1]}", 1) + 1 


print(len(visited))
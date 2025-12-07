with open("inputs/input_07.txt") as file:
    grid = [[x for x in a] for a in file.read().strip("\n").split("\n")]

for y in range(len(grid)):
    if 'S' in grid[y]:
        beams = [(grid[y].index('S'),y),]
        break

splits = 0

while beams[0][1] < len(grid)-1:
    new_beams = []
    while len(beams):
        beam = beams.pop()
        if grid[beam[1]+1][beam[0]] == '.':
            new_beams += [(beam[0],beam[1]+1)]
        elif grid[beam[1]+1][beam[0]] == '^':
            splits += 1
            new_beams += [(beam[0]-1,beam[1]+1)]
            new_beams += [(beam[0]+1,beam[1]+1)]
    beams = list(set(new_beams))

print(splits)
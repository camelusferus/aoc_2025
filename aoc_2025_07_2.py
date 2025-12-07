with open("inputs/input_07.txt") as file:
    grid = [[x for x in a] for a in file.read().strip("\n").split("\n")]

for y in range(len(grid)):
    if 'S' in grid[y]:
        beams = {(grid[y].index('S'), y): 1}
        break

for i in range(y,len(grid)-1):
    new_beams = {}
    for beam in beams.keys():
        if grid[beam[1]+1][beam[0]] == '.':
            new_beams[(beam[0], beam[1] + 1)] = beams[(beam[0], beam[1])] + new_beams.get((beam[0], beam[1] + 1), 0)
        elif grid[beam[1]+1][beam[0]] == '^':
            new_beams[(beam[0] - 1, beam[1] + 1)] = beams[(beam[0], beam[1])] + new_beams.get((beam[0] - 1, beam[1] + 1), 0)
            new_beams[(beam[0] + 1, beam[1] + 1)] = beams[(beam[0], beam[1])] + new_beams.get((beam[0] + 1, beam[1] + 1), 0)
    beams = new_beams

print(sum(beams.values()))
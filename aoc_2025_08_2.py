with open("inputs/input_08.txt") as file:
    coords = [[int(x) for x in a.split(',')] for a in file.read().strip("\n").split("\n")]

circuits = []
dists = {}
notfinished = True

for y in range(len(coords)):
    for x in range(len(coords)):
        if y<x:
            dists[(y,x)] = sum([(a-b)**2 for a,b in zip(coords[y],coords[x])])

while notfinished:
    con_pair = min(dists, key=dists.get)
    del(dists[con_pair])
    left_cir = next((x for x in circuits if con_pair[0] in x), [con_pair[0],])
    right_cir = next((x for x in circuits if con_pair[1] in x), [con_pair[1],])
    if left_cir in circuits:
        circuits.remove(left_cir)
    if right_cir in circuits:
        circuits.remove(right_cir)
    circuits.append(list(set(left_cir + right_cir)))
    if len(circuits) == 1 and len(circuits[0]) == 1000:
        notfinished = False

print(eval(f'{coords[con_pair[0]][0]}*{coords[con_pair[1]][0]}'))
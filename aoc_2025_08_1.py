with open("inputs/input_08.txt") as file:
    coords = [[int(x) for x in a.split(',')] for a in file.read().strip("\n").split("\n")]

circuits = []
dists = {}
range_size = 10 if 'demo' in file.name else 1000

for y in range(len(coords)):
    for x in range(len(coords)):
        if y<x:
            dists[(y,x)] = sum([(a-b)**2 for a,b in zip(coords[y],coords[x])])

for i in range(range_size):
    con_pair = min(dists, key=dists.get)
    del(dists[con_pair])
    left_cir = next((x for x in circuits if con_pair[0] in x), [con_pair[0],])
    right_cir = next((x for x in circuits if con_pair[1] in x), [con_pair[1],])
    if left_cir in circuits:
        circuits.remove(left_cir)
    if right_cir in circuits:
        circuits.remove(right_cir)
    circuits.append(list(set(left_cir + right_cir)))

lengths = sorted([len(cir) for cir in circuits],reverse=True)[:3]

print(eval(f'{lengths[0]}*{lengths[1]}*{lengths[2]}'))
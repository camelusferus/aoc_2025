with open("inputs/input_05.txt") as file:
    input = file.read()
    ranges = [(int(a.split('-')[0]),int(a.split('-')[1])) for a in input.split("\n\n")[0].strip("\n").split("\n")]
    available = [int(a) for a in input.split("\n\n")[1].strip("\n").split("\n")]

fresh = 0
for ingredient in available:
    for r in ranges:
        if ingredient in range(r[0],r[1]+1):
            fresh +=1
            break

print(fresh)
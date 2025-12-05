with open("inputs/input_05.txt") as file:
    ranges = [[int(a.split('-')[0]),int(a.split('-')[1])] for a in file.read().split("\n\n")[0].strip("\n").split("\n")]

old_fresh = []
fresh = ranges

while len(fresh) != len(old_fresh):
    old_fresh = fresh
    new_fresh = []
    for r in fresh:
        for fr in new_fresh:
            if r[0] in range(fr[0],fr[1]+1):
                if r[1] in range(fr[0],fr[1]+1):
                    break
                fr[1] = r[1]
                break
            elif r[1] in range(fr[0],fr[1]+1):
                fr[0] = r[0]
                break
        else:
            new_fresh.append(r)
    old_fresh = fresh
    fresh = new_fresh

print(sum([len(range(a[0],a[1]+1)) for a in new_fresh]))
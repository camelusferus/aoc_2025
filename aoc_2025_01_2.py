with open("inputs/input_01.txt") as f:
    input = [(a[0], int(a[1:])) for a in f.read().strip('\n').split("\n")]

state = 50
times_0 = 0

for element in input:
    if element[0] == 'L':
        for i in range(element[1]):
            state -= 1
            if state % 100 == 0:
                times_0 += 1
    else:
        for i in range(element[1]):
            state += 1
            if state % 100 == 0:
                times_0 += 1

print(times_0)
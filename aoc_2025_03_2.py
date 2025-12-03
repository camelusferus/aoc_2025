with open("inputs/input_03.txt") as f:
    inputs = [[int(i) for i in a] for a in f.read().strip('\n').split("\n")]

jolts = 0

for line in inputs:
    length = len(line)
    max_jolt = 0
    last_digit = -1
    for i in range(11,-1,-1):
        for digit in [9,8,7,6,5,4,3,2,1]:
            if digit in line[last_digit+1:length-i]:
                last_digit = line.index(digit,last_digit+1)
                max_jolt = max_jolt * 10 + digit
                break
    jolts += max_jolt

print(jolts)
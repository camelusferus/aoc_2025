with open("inputs/input_03.txt") as f:
    inputs = [[int(i) for i in a] for a in f.read().strip('\n').split("\n")]

jolts = 0

for line in inputs:
    max_line = 0
    max_first = max_line // 10
    max_second = max_line % 10
    for index_first in range(len(line)-1):
        if line[index_first] > max_first:
            max_first = line[index_first]
            max_second = 0
            for index_second in range(index_first + 1, len(line)):
                if line[index_second] > max_second:
                    max_second = line[index_second]
        elif line[index_first] == max_first:
            for index_second in range(index_first + 1, len(line)):
                if line[index_second] > max_second:
                    max_second = line[index_second]
        max_line = max_first * 10 + max_second
    jolts += max_line

print(jolts)
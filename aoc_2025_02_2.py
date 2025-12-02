with open("inputs/input_02.txt") as f:
    input = [(int(a.split('-')[0]),int(a.split('-')[1])) for a in f.read().strip(',').split(",")]

invalids = 0

for id_range in input:
    for num in range(id_range[0],id_range[1]+1):
        str_num = str(num)
        length = len(str_num)
        for i in range(1,length//2+1):
            if length % i:
                continue
            repetitions = length // i
            if str_num == ''.join(str_num[:i]*repetitions):
                invalids += num
                break

print(invalids)
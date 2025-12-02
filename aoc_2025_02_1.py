with open("inputs/input_02.txt") as f:
    input = [(int(a.split('-')[0]),int(a.split('-')[1])) for a in f.read().strip(',').split(",")]

invalids = 0

for id_range in input:
    for num in range(id_range[0],id_range[1]+1):
        str_num = str(num)
        if str_num[:len(str_num)//2] == str_num[len(str_num)//2:]:
            invalids += num

print(invalids)
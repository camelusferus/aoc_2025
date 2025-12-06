with open("inputs/input_06.txt") as f:
    inputs = list(zip(*[[i for i in a.split(' ') if i != ''] for a in f.read().strip('\n').split("\n")]))

results = [eval(a[-1].join(str(item) for item in a[:-1])) for a in inputs]

print(sum(results))
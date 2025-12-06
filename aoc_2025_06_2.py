with open("inputs/input_06.txt") as f:
    inputs = list(zip(*[a for a in f.read().strip('\n').split("\n")]))
    blocks = [i for i,v in enumerate(inputs) if v == (' ',) * len(inputs[0])]
    numbers = [inputs[i:j] for i,j in zip([0] + [b + 1 for b in blocks], blocks + [len(inputs)])]

results = [eval(n[0][-1].join([''.join(item[:-1]) for item in n])) for n in numbers]

print(sum(results))
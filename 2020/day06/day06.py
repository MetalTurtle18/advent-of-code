n = open("../day06/day06.txt", "r").read().split("\n\n")
n = [i.split("\n") for i in n]
output = 0
for i in n:
    ints = {}
    for j in range(len(i)):
        if j == 0:
            ints = set(i[j])
        else:
            ints = ints.intersection(i[j])
    output += len(ints)
print(output)

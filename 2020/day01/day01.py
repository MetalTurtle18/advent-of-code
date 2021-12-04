n = open("../day01/day01.txt", "r").read().split("\n")
o = 0
for i in range(len(n)):
    for j in range(len(n)):
        for k in range(len(n)):
            if int(n[i]) + int(n[j]) + int(n[k]) == 2020 and i != j and j != k and i != k:
                o = int(n[i]) * int(n[j]) * int(n[k])
print(str(o))
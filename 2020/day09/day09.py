n = open("../day09/day09.txt", "r").read().split("\n")
preamble = n[:25]
other_numbers = n[25:]
found = False
found_two_electric_boolgaloo = False
for i in other_numbers:
    for j in range(25):
        for k in range(25):
            if j != k and int(preamble[j]) + int(preamble[k]) == int(i):
                preamble = preamble[1:]
                preamble.append(i)
                found = True
                break
        if found:
            found = False
            break
        if j == 24:
            print("Puzzle 1: " + str(i))
            found_two_electric_boolgaloo = True
            break
    if found_two_electric_boolgaloo:
        break

for i in range(len(n)):
    n[i] = int(n[i])

for i in range(len(n)):
    for j in range(int(i) + 2, len(n)):
        if sum(n[i:j]) == 26796446:
            print("Puzzle 2: " + str(max(n[i:j]) + min(n[i:j])))

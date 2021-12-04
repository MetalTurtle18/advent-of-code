n = open("../day03/day03.txt", "r").read().split("\n")
output = 0
column = 0
for i in range(0, len(n), 2):
    if n[i][column] == "#":
        output += 1
    column += 1
    column %= len(n[i])
print(output)
#print(228*84*89*100*40)
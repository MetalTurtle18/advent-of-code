output = [18, 11, 9, 0, 5, 1]
seen = {output[i]: i for i in range(len(output))}
val = 0
for i in range(len(output), 30000000):
    output.append(val)
    last = {val: i}
    val = i - seen.get(val, i)
    seen.update(last)
print("Puzzle 1: ", output[2019])
print("Puzzle 2: ", output[29999999])

from copy import deepcopy as dc
n = open("../day14/day14test.txt", "r").read().split("\n")
current_mask = ""
memory = {}
for i in n:
    if i[:4] == "mask":
        current_mask = i[7:]
        continue
    value = bin(int(i.split(" = ")[1])).replace("0b", "")
    memory_address = i.split("] = ")[0][4:]
    writing_value = ""
    for j in range(37 - len(value)):
        value = "0" + value
    for j in range(36):
        if current_mask[j] != "X":
            writing_value += current_mask[j]
        else:
            writing_value += value[j + 1]
    memory[memory_address] = int(writing_value, 2)
memory_sum = 0
for i in memory:
    memory_sum += memory[i]
print("Puzzle 1: " + str(memory_sum))
# Part 2:
memory = {}
for i in n:
    if i[:4] == "mask":
        current_mask = i[7:]
        continue
    value = int(i.split(" = ")[1])
    memory_address = bin(int(i.split("] = ")[0][4:])).replace("0b", "")
    for j in range(37 - len(memory_address)):
        memory_address = "0" + memory_address
    writing_address = ""
    for j in range(36):
        if current_mask[j] == "X":
            writing_address += "X"
        elif current_mask[j] == "1":
            writing_address += "1"
        elif current_mask[j] == "0":
            writing_address += memory_address[j + 1]
    for j in range(2**writing_address.count("X")):
        floatings_bits = bin(j).replace("0b", "").zfill(writing_address.count("X"))
        floating_add_index = 0
        address_with_floating_bits = dc(writing_address)
        this_address = ""
        for k in range(36):
            if address_with_floating_bits[k] == "X":
                this_address += floatings_bits[floating_add_index]
                floating_add_index += 1
            else:
                this_address += address_with_floating_bits[k]
        memory[int(this_address, 2)] = value
memory_sum = 0
for i in memory:
    memory_sum += memory[i]
print("Puzzle 2: " + str(memory_sum))

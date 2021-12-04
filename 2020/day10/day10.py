n = open("../day10/day10.txt", "r").read().split("\n")
ready_input = [int(i) for i in n]
ready_input.append(0)
ready_input.append(max(ready_input) + 3)
ready_input = sorted(ready_input)
one_jolt_total = 0
three_jolt_total = 0
for i in range(len(ready_input) - 1):
    if ready_input[i + 1] - ready_input[i] == 1:
        one_jolt_total += 1
    elif ready_input[i + 1] - ready_input[i] == 3:
        three_jolt_total += 1
print("Puzzle 1: " + str(one_jolt_total * three_jolt_total))

# Part 2
ready_input_two = sorted([int(i) for i in n])
ready_input_two.append(max(ready_input_two) + 3)
combinations = {0: 1}
for i in range(len(ready_input_two)):
    value = 0
    if ready_input_two[i] - 3 in combinations.keys():
        value += combinations[ready_input_two[i] - 3]
    if ready_input_two[i] - 2 in combinations.keys():
        value += combinations[ready_input_two[i] - 2]
    if ready_input_two[i] - 1 in combinations.keys():
        value += combinations[ready_input_two[i] - 1]
    combinations[ready_input_two[i]] = value
print("Puzzle 2: " + str(combinations[max(ready_input_two)]))

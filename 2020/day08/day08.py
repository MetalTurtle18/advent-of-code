from copy import deepcopy as dc


def run_kid_handheld_game_console(instructions_set):
    instruction_index = 0
    executed_instructions = []
    accumulator = 0
    errored = False
    while True:
        if instruction_index == len(instructions_set):
            break
        if instruction_index in executed_instructions:
            errored = True
            break
        if instructions_set[instruction_index][0] == "acc":
            executed_instructions.append(instruction_index)
            accumulator += instructions_set[instruction_index][1]
            instruction_index += 1
        elif instructions_set[instruction_index][0] == "jmp":
            executed_instructions.append(instruction_index)
            instruction_index += instructions_set[instruction_index][1]
        elif instructions_set[instruction_index][0] == "nop":
            executed_instructions.append(instruction_index)
            instruction_index += 1
    if errored:
        return True, accumulator
    else:
        return False, accumulator


n = open("../day08/day08.txt", "r").read().split("\n")
instructions = []
for i in n:
    ins = i.split()[0]
    val = i.split()[1]
    if val[0] == "+":
        val = int(val[1:])
    else:
        val = int(val)
    instructions.append([ins, val])

iter_instructions = dc(instructions)
for i in range(len(instructions)):
    iter_instructions = dc(instructions)
    if instructions[i][0] == "jmp":
        iter_instructions[i][0] = "nop"
    elif instructions[i][0] == "nop":
        iter_instructions[i][0] = "jmp"
    else:
        continue
    running_output = run_kid_handheld_game_console(iter_instructions)
    if running_output[0]:
        continue
    else:
        print(running_output[1])
        break

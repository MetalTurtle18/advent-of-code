def part1(data):
    instructions = data[0]
    nodes = {i.split()[0]: (i.split()[2][1:-1], i.split()[3][:-1]) for i in data[2:]}
    node = 'AAA'
    i = 0
    while node != 'ZZZ':
        current_instruction = instructions[i % len(instructions)]
        if current_instruction == 'L':
            node = nodes[node][0]
        elif current_instruction == 'R':
            node = nodes[node][1]
        i += 1
    return i


def part2(data):
    instructions = data[0]
    nodes = {i.split()[0]: (i.split()[2][1:-1], i.split()[3][:-1]) for i in data[2:]}
    current_nodes = [i for i in nodes.keys() if i[2] == 'A']
    ij = 0
    while any([i[2] != 'Z' for i in current_nodes]):
        print(ij, current_nodes)
        current_instruction = instructions[ij % len(instructions)]
        if current_instruction == 'L':
            current_nodes = [nodes[i][0] for i in current_nodes]
        elif current_instruction == 'R':
            current_nodes = [nodes[i][1] for i in current_nodes]
        ij += 1
    return ij


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    # print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

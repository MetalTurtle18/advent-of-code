import re

def part1(data):
    _crates, _moves = data.split('\n\n')

    num_stacks = int(_crates[len(_crates) - 1])
    tallest_stack = _crates.count('\n') - 1
    crates_raw = _crates.split('\n')[:-1]

    crate_stacks = [[] for _ in range(num_stacks)]
    for y in range(tallest_stack, -1, -1):
        for stack in range(num_stacks):
            if len(crates_raw[y]) > stack * 4 + 1:
                crate = crates_raw[y][stack * 4 + 1]
                if crate.isalpha():
                    crate_stacks[stack].append(crate)

    moves = _moves.split('\n')

    for move in moves:
        n, s, t = list(map(int, re.findall(r'\d+', move)))
        for i in range(n):
            crate_stacks[t - 1].append(crate_stacks[s - 1].pop())

    output = ''

    for stack in crate_stacks:
        output += stack.pop()

    return output


def part2(data):
    _crates, _moves = data.split('\n\n')

    num_stacks = int(_crates[len(_crates) - 1])
    tallest_stack = _crates.count('\n') - 1
    crates_raw = _crates.split('\n')[:-1]

    crate_stacks = [[] for _ in range(num_stacks)]
    for y in range(tallest_stack, -1, -1):
        for stack in range(num_stacks):
            if len(crates_raw[y]) > stack * 4 + 1:
                crate = crates_raw[y][stack * 4 + 1]
                if crate.isalpha():
                    crate_stacks[stack].append(crate)

    moves = _moves.split('\n')

    for move in moves:
        n, s, t = list(map(int, re.findall(r'\d+', move)))
        temp = []
        for i in range(n):
            temp.append(crate_stacks[s - 1].pop())
        for i in range(n):
            crate_stacks[t - 1].append(temp.pop())

    output = ''

    for stack in crate_stacks:
        output += stack.pop()

    return output


puzzle_input = open("input.txt", "r").read()
test_input = open("test.txt", "r").read()

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

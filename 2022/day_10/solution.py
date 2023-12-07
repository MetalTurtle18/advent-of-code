def check_cycle(cycle, register):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(cycle, register)
        return register * cycle
    return 0


def part1(data):
    opp = -1
    register = 1
    strength = 0
    skip_opp = False
    next_v = 0
    for cycle in range(1, 221):
        strength += check_cycle(cycle, register)
        if not skip_opp:
            opp += 1
            if data[opp].startswith("addx"):
                next_v = int(data[opp].split(" ")[1])
                skip_opp = True
        else:
            register += next_v
            skip_opp = False
    return strength


def check_sprite(cycle, register):
    if cycle % 40 == 0:
        print()
    if cycle % 40 in range(register - 1, register + 2):
        print('#', end='')
    else:
        print('.', end='')


def part2(data):
    cycle = 0
    register = 1
    for opp in data:
        if opp.startswith('addx'):
            for _ in range(2):
                check_sprite(cycle, register)
                cycle += 1
            register += int(opp.split(' ')[1])
        else:
            check_sprite(cycle, register)
            cycle += 1
    return ''


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

from copy import deepcopy as dc

def part1(data):
    s = 0
    for report in data:
        levels = list(map(int, report.split()))
        safe = True
        for i in range(1, len(levels)):
            if 4 > abs(levels[i] - levels[i - 1]) > 0:
                continue
            else:
                safe = False
                break
        if levels[0] < levels[1]:
            for i in range(1, len(levels)):
                if levels[i] < levels[i - 1]:
                    safe = False
                    break
        elif levels[0] > levels[1]:
            for i in range(1, len(levels)):
                if levels[i] > levels[i - 1]:
                    safe = False
                    break
        s += 1 if safe else 0
    return s


def safety_check(levels_in, exclude):
    if exclude >= len(levels_in):
        return False
    elif exclude == -1:
        levels = levels_in
    else:
        levels = dc(levels_in)
        levels.pop(exclude)

    safe = True
    for i in range(1, len(levels)):
        if 4 > abs(levels[i] - levels[i - 1]) > 0:
            continue
        else:
            safe = False
            break
    if levels[0] < levels[1]:
        for i in range(1, len(levels)):
            if levels[i] < levels[i - 1]:
                safe = False
                break
    elif levels[0] > levels[1]:
        for i in range(1, len(levels)):
            if levels[i] > levels[i - 1]:
                safe = False
                break
    return safe or safety_check(levels_in, exclude + 1)

def part2(data):
    s = 0
    for report in data:
        levels = list(map(int, report.split()))
        safe = safety_check(levels, -1)
        s += 1 if safe else 0
    return s


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

import re

def part1(data):
    inst = re.findall('(?<=mul\()\d+,\d+(?=\))', data)
    s = 0
    for i in inst:
        a, b = i.split(',')
        s += int(a) * int(b)
    return s


def part2(data):
    inst = re.findall('((?<=mul\()\d+,\d+(?=\)))|(do\(\))|(don\'t\(\))', data)
    s = 0
    en = True
    for i, do, dont in inst:
        if do == 'do()':
            en = True
            continue
        elif dont == 'don\'t()':
            en = False
            continue
        elif en:
            a, b = i.split(',')
            s += int(a) * int(b)
    return s


puzzle_input = open("input.txt", "r").read().replace("\n", "")
test_input = open("test.txt", "r").read().replace("\n", "")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

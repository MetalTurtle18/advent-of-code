from util import *


def part1(data):
    total = 0
    for r in data:
        low, high = map(int, r.split('-'))
        for n in range(low, high + 1):
            sn = str(n)
            if len(sn) % 2 == 0:
                if sn[:len(sn) // 2] == sn[-len(sn) // 2:]:
                    total += n
    return total


def part2(data):
    total = 0
    for r in data:
        low, high = map(int, r.split('-'))
        for n in range(low, high + 1):
            valid = False
            sn = str(n)
            for i in range(2, len(sn) + 1):
                if len(sn) % i == 0 and not valid:
                    if sn == sn[:len(sn) // i] * i:
                        # print(sn, i, sn[:len(sn) // i], sn[:len(sn) // i] * i)
                        valid = True
                        total += n
    return total


if __name__ == "__main__":
    aoc = AOC(2, CSV)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))

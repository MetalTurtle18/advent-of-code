from util import *

def part1(data):
    tot = 0
    pos = 50
    for step in data:
        if step[0] == 'L':
            pos -= int(step[1:])
        elif step[0] == 'R':
            pos += int(step[1:])
        pos %= 100
        if pos == 0:
            tot += 1
    return tot


def part2(data):
    tot = 0
    pos = 50
    for step in data:
        for i in range(int(step[1:])):
            if step[0] == 'L':
                pos -= 1
                if pos == -1:
                    pos = 99
            if step[0] == 'R':
                pos += 1
                if pos == 100:
                    pos = 0
            if pos == 0:
                tot += 1
    return tot


if __name__ == "__main__":
    aoc = AOC(1)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
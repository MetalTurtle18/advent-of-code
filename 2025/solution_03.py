from util import *

def part1(data):
    total = 0
    for bank in data:
        jolts = [int(i) for i in bank]
        first = max(jolts[:-1])
        last = max(jolts[jolts.index(first) + 1:])
        joltage = int(f'{first}{last}')
        total += joltage
    return total


def part2(data):
    total = 0
    for bank in data:
        jolts = [int(i) for i in bank]
        joltage = ''
        last_i = -1
        for i in range(12):
            m = 0
            m_i = 0
            for j in range(last_i + 1, len(jolts) - (11 - i)):
                if jolts[j] > m:
                    m = jolts[j]
                    m_i = j
                if m == 9:
                    break
            last_i = m_i
            joltage += str(m)
        total += int(joltage)
    return total


if __name__ == "__main__":
    aoc = AOC(3)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
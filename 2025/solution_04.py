from util import *
from copy import deepcopy

def part1(data):
    total = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '.':
                continue
            adj = -1
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    if (0 <= x < len(data[row]) and 0 <= y < len(data)) and data[x][y] == '@':
                        adj += 1
            if adj < 4:
                total += 1
    return total


def part2(data_in):
    acc = -1
    removed = 0
    next_data = deepcopy(data_in)
    while acc != 0:
        data = deepcopy(next_data)
        tot = 0
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == '.':
                    continue
                adj = -1
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        if (0 <= x < len(data[row]) and 0 <= y < len(data)) and data[x][y] == '@':
                            adj += 1
                if adj < 4:
                    removed += 1
                    tot += 1
                    next_data[row] = next_data[row][:col] + '.' + next_data[row][col + 1:]
        acc = tot
    return removed


if __name__ == "__main__":
    aoc = AOC(4)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
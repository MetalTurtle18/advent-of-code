from util import *

def part1(data):
    splits = 0
    beams = set()
    beams.add(data[0].index('S'))
    for row in data[1:]:
        for i, pos in enumerate(row):
            if i in beams and pos == '^':
                splits += 1
                beams.add(i - 1)
                beams.add(i + 1)
                beams.remove(i)
    return splits


def part2(data):
    beams = [(data[0].index('S'), 1)]  # tuple: the second element is the number of ways to get there
    for row in data[1:]:
        new_beams = []
        for beam in beams:
            if row[beam[0]] == '^':
                new_beams.append((beam[0] + 1, beam[1]))
                new_beams.append((beam[0] - 1, beam[1]))
            elif row[beam[0]] == '.':
                new_beams.append(beam)
        beams = []
        for beam in set(b[0] for b in new_beams):
            total = sum(b[1] for b in new_beams if b[0] == beam)
            beams.append((beam, total))

    return sum(b[1] for b in beams)


if __name__ == "__main__":
    aoc = AOC(7)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
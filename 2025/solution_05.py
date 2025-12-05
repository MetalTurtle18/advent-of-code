from util import *

def part1(data):
    ranges = data[0].split("\n")
    items = map(int, data[1].split("\n"))
    fresh = 0
    for item in items:
        for r in ranges:
            low, high = map(int, r.split("-"))
            if low <= item <= high:
                fresh += 1
                break
    return fresh


def part2(data):
    ranges = data[0].split("\n")
    points = []
    fresh = 0
    for r in ranges:
        low, high = map(int, r.split("-"))
        points.append(('[', low))
        points.append((']', high))
    points.sort(key=lambda p: p[0] == ']')  # Prevent duplicates by sorting same-number points
    points.sort(key=lambda p: p[1])
    in_range = 0
    bottom = -1
    for i in range(len(points)):
        end = points[i][0]
        point = points[i][1]
        if end == '[':
            in_range += 1
            if in_range == 1:  # We just entered a range
                bottom = point
        elif end == ']':
            in_range -= 1
            if in_range == 0:  # We just left a range
                fresh += point - bottom + 1
    return fresh


if __name__ == "__main__":
    aoc = AOC(5, SECTIONS)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
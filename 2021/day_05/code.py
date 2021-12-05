from collections import defaultdict


def part1(data):
    coords = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = map(int, line.replace(' -> ', ',').split(','))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                coords[(int(x1), y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                coords[(x, int(y1))] += 1
    return sum(1 for i in coords if coords[i] > 1)


def part2(data):
    coords = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = map(int, line.replace(' -> ', ',').split(','))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                coords[(int(x1), y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                coords[(x, int(y1))] += 1
        else:  # Diagonal
            # Order matters since they aren't lines, so I can't just use min and max
            range_x = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            range_y = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
            for x, y in zip(range_x, range_y):
                coords[(x, y)] += 1
    return sum(1 for i in coords if coords[i] > 1)


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

from collections import defaultdict
from itertools import combinations

def print_map(grid, antinodes):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) in antinodes:
                print('#', end = '')
            else:
                print(grid[row][col], end = '')
            print(' ', end = '')
        print()


def part1(data):
    frequencies: defaultdict[str: list[tuple[int]]] = defaultdict(list)
    for row in range(len(data)):
        for col in range(len(data[row])):
            if (a := data[row][col]) != '.':
                frequencies[a].append((row, col))

    antinodes: set[tuple[int]] = set()
    for freq in frequencies.values():
        pairings = list(combinations(freq, 2))
        for antenna_a, antenna_b in pairings:
            row1 = antenna_a[0] - (antenna_b[0] - antenna_a[0])
            row2 = antenna_b[0] + (antenna_b[0] - antenna_a[0])
            col1 = antenna_a[1] - (antenna_b[1] - antenna_a[1])
            col2 = antenna_b[1] + (antenna_b[1] - antenna_a[1])
            if 0 <= row1 < len(data) and 0 <= col1 < len(data[0]):
                antinodes.add((row1, col1))
            if 0 <= row2 < len(data) and 0 <= col2 < len(data[0]):
                antinodes.add((row2, col2))

    print_map(data, antinodes)

    return len(antinodes)


def part2(data):
    frequencies: defaultdict[str: list[tuple[int]]] = defaultdict(list)
    for row in range(len(data)):
        for col in range(len(data[row])):
            if (a := data[row][col]) != '.':
                frequencies[a].append((row, col))

    antinodes: set[tuple[int]] = set()
    for freq in frequencies.values():
        pairings = list(combinations(freq, 2))
        for antenna_a, antenna_b in pairings:
            row_diff = antenna_b[0] - antenna_a[0]
            col_diff = antenna_b[1] - antenna_a[1]
            r, c = antenna_a
            while 0 <= r < len(data) and 0<= c < len(data[0]):
                antinodes.add((r, c))
                r += row_diff
                c += col_diff
            r, c = antenna_b
            while 0 <= r < len(data) and 0<= c < len(data[0]):
                antinodes.add((r, c))
                r -= row_diff
                c -= col_diff

    print_map(data, antinodes)

    return len(antinodes)


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

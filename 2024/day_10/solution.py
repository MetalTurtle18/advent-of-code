def dfs(topo_map, start):
    peaks = []

    def recurse(r, c):
        value = topo_map[r][c]
        if value == 9:
            peaks.append((r, c))
        else:
            if r + 1 < len(topo_map)    and topo_map[r + 1][c] == value + 1:
                recurse(r + 1, c)
            if r - 1 >= 0               and topo_map[r - 1][c] == value + 1:
                recurse(r - 1, c)
            if c + 1 < len(topo_map[0]) and topo_map[r][c + 1] == value + 1:
                recurse(r, c + 1)
            if c - 1 >= 0               and topo_map[r][c - 1] == value + 1:
                recurse(r, c - 1)

    recurse(start[0], start[1])
    return peaks


def trails(data):
    data = [list(map(int, list(i))) for i in data]
    trailheads = []
    reachable_peaks = []
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if not col:
                trailheads.append((r, c))

    for trailhead in trailheads:
        reachable_peaks += [dfs(data, trailhead)]

    return reachable_peaks


def part1(data):
    return sum(len(set(i)) for i in trails(data))


def part2(data):
    return sum(len(i) for i in trails(data))


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

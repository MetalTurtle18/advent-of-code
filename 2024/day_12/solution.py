from itertools import combinations


def search(farm, start):
    crop = farm[start]
    edges = []
    plots = []
    perimeter = 0

    def recurse(r, c):
        nonlocal perimeter
        if (r, c) in plots:
            return 0
        if farm[(r, c)] == crop:
            plots.append((r, c))
        if farm[r + 1, c] != crop:
            perimeter += 1
            edges.append((r, c, 'b'))
        else:
            recurse(r + 1, c)
        if farm[r - 1, c] != crop:
            perimeter += 1
            edges.append((r, c, 't'))
        else:
            recurse(r - 1, c)
        if farm[r, c + 1] != crop:
            perimeter += 1
            edges.append((r, c, 'r'))
        else:
            recurse(r, c + 1)
        if farm[r, c - 1] != crop:
            perimeter += 1
            edges.append((r, c, 'l'))
        else:
            recurse(r, c - 1)

    recurse(start[0], start[1])

    return plots, perimeter, edges


def sides(edges):
    tot = len(edges)
    for i, j in combinations(edges, 2):
        if i[2] == j[2]:
            if ((i[0] == j[0] + 1 or i[0] == j[0] - 1) and i[1] == j[1]) or (i[1] == j[1] + 1 or i[1] == j[1] - 1) and i[0] == j[0]:
                tot -= 1
    return tot


def quote_fences(data, cost_function):
    data = ['-' * (len(data[0]) + 2)] + ['-' + i + '-' for i in data] + ['-' * (len(data[0]) + 2)]
    data = {(r, c): t for r, s in enumerate(data) for c, t in enumerate(s)}
    cost = 0
    plotted = []
    for (r, c), plot in data.items():
        if plot != '-' and (r, c) not in plotted:
            plots, perimeter, edges = search(data, (r, c))
            plotted += plots
            crop_cost = cost_function(plots, perimeter, edges)
            cost += crop_cost
    return cost


def part1(data):
    return quote_fences(data, lambda pl, pe, _: len(pl) * pe)


def part2(data):
    return quote_fences(data, lambda p, _, e: len(p) * sides(e))


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

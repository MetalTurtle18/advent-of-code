def part1(data):
    grid = [[int(tree) for tree in row] for row in data]
    visible = set()
    for y in range(len(grid)):
        tallest = -1
        tallest_x = -1
        for x in range(len(grid[y])):
            if (tree:= grid[y][x]) > tallest:
                tallest = tree
                tallest_x = x
                visible.add((x, y))
        tallest =-1
        for x in range(len(grid[y]) - 1, tallest_x, -1):
            if (tree:= grid[y][x]) > tallest:
                tallest = tree
                visible.add((x, y))
    for x in range(1, len(grid) - 1):
        tallest = -1
        tallest_y = -1
        for y in range(len(grid)):
            if (tree:= grid[y][x]) > tallest:
                tallest = tree
                tallest_y = y
                visible.add((x, y))
        tallest =-1
        for y in range(len(grid) - 1, tallest_y, -1):
            if (tree:= grid[y][x]) > tallest:
                tallest = tree
                visible.add((x, y))

    return len(visible)


def calc_score(grid, x, y):
    u, d, l, r = 0, 0, 0, 0

    # up
    for iter_y in range(y - 1, -1, -1):
        u += 1
        if grid[iter_y][x] >= grid[y][x]:
            break

    # down
    for iter_y in range(y + 1, len(grid)):
        d += 1
        if grid[iter_y][x] >= grid[y][x]:
            break

    # left
    for iter_x in range(x - 1, -1, -1):
        l += 1
        if grid[y][iter_x] >= grid[y][x]:
            break

    # right
    for iter_x in range(x + 1, len(grid[y])):
        r += 1
        if grid[y][iter_x] >= grid[y][x]:
            break

    return u * d * l * r


def part2(data):
    grid = [[int(tree) for tree in row] for row in data]
    best = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            best = max(best, calc_score(grid, x, y))
    return best



puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

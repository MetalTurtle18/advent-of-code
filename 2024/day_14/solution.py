import re

def part1(data, width, height):
    grid = [[[] for _ in range(width)] for _ in range(height)]
    for robot in data:
        x, y, vx, vy = map(int, re.match(r"p=(\d+),(\d+)\sv=(-?\d+),(-?\d+)", robot).groups())
        grid[y][x].append((vx, vy))

    for _ in range(100):
        new_grid = [[[] for _ in range(width)] for _ in range(height)]
        for row in range(height):
            for col in range(width):
                for robot in grid[row][col]:
                    x = (col + robot[0]) % width
                    y = (row + robot[1]) % height
                    new_grid[y][x].append(robot)
        grid = new_grid

    quads = [0, 0, 0, 0]
    for row in range(0, height // 2):
        for col in range(0, width // 2):
            quads[0] += len(grid[row][col])
        for col in range(width // 2 + 1, width):
            quads[1] += len(grid[row][col])
    for row in range(height // 2 + 1, height):
        for col in range(0, width // 2):
            quads[2] += len(grid[row][col])
        for col in range(width // 2 + 1, width):
            quads[3] += len(grid[row][col])

    return quads[0] * quads[1] * quads[2] * quads[3]


def part2(data, width, height):
    grid = [[[] for _ in range(width)] for _ in range(height)]
    for robot in data:
        x, y, vx, vy = map(int, re.match(r"p=(\d+),(\d+)\sv=(-?\d+),(-?\d+)", robot).groups())
        grid[y][x].append((vx, vy))

    i = 0
    while True:
        i += 1
        print(i)
        unique = True
        new_grid = [[[] for _ in range(width)] for _ in range(height)]
        for row in range(height):
            for col in range(width):
                for robot in grid[row][col]:
                    x = (col + robot[0]) % width
                    y = (row + robot[1]) % height
                    if len(new_grid[y][x]) > 0:
                        unique = False
                    new_grid[y][x].append(robot)
        grid = new_grid
        if unique:
            break

    return i


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input, 11, 7)}")
    # print(f"Part 2: {part2(test_input, 11, 7)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input, 101, 103)}")
    print(f"Part 2: {part2(puzzle_input, 101, 103)}")

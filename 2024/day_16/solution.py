def part1(data):
    start = (0, 0)
    finish = (0, 0)
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == 'S':
                start = (r, c)
            if data[r][c] == 'E':
                finish = (r, c)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # E, W, S, N
    visited = {}
    paths = []
    for _ in range(1000):
        None

    return data[0]


def part2(data):
    return data[0]


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    # print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    # print(f"Part 1: {part1(puzzle_input)}")
    # print(f"Part 2: {part2(puzzle_input)}")

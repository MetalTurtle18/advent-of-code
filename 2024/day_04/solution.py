def part1(data):
    tot = 0
    # horizontal
    for row in data:
        for i in range(len(row) - 3):
            if row[i:i+4] in ['XMAS', 'SAMX']:
                tot += 1
    # vertical
    for col in range(len(data[0])):
        for i in range(len(data) - 3):
            if data[i][col] + data[i + 1][col] + data[i + 2][col] + data[i + 3][col] in ['XMAS', 'SAMX']:
                tot += 1
    # northwest - southeast
    for row in range(len(data) - 3):
        for col in range(len(data[0]) - 3):
            if data[row][col] + data[row + 1][col + 1] + data[row + 2][col + 2] + data[row + 3][col + 3] in ['XMAS', 'SAMX']:
                tot += 1
    # northeast - southwest
    for row in range(len(data) - 3):
        for col in range(3, len(data[0])):
            if data[row][col] + data[row + 1][col - 1] + data[row + 2][col - 2] + data[row + 3][col - 3] in ['XMAS', 'SAMX']:
                tot += 1
    return tot


def part2(data):
    tot = 0
    for row in range(len(data) - 2):
        for col in range(len(data[0]) - 2):
            if (data[row][col] + data[row][col + 2] + data[row + 1][col + 1] + data[row + 2][col] + data[row + 2][col + 2]
                    in ['MMASS', 'MSAMS', 'SSAMM', 'SMASM']):
                tot += 1
    return tot


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

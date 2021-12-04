def part1(data):
    count = 0
    for i in range(1, len(data)):
        if int(data[i]) > int(data[i - 1]):
            count += 1
    return count


def part2(data):
    int_data = list(map(int, data))
    count = 0
    for i in range(0, len(int_data) - 3):
        if int_data[i] + int_data[i + 1] + int_data[i + 2] < int_data[i + 1] + int_data[i + 2] + int_data[i + 3]:
            count += 1
    return count


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

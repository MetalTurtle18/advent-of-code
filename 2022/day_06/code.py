def detect_unique_run(length, data):
    for i in range(length - 1, len(data)):
        if len(set(j for j in data[i - length + 1: i + 1])) == length:
            return i + 1


def part1(data):
    return detect_unique_run(4, data)


def part2(data):
    return detect_unique_run(14, data)


puzzle_input = open("input.txt", "r").read()
test_input = open("test.txt", "r").read()

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

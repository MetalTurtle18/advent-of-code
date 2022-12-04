def part1(data):
    total = 0
    for pair in data:
        one, two = map(lambda x: (int(x.split('-')[0]), int(x.split('-')[1])), pair.split(','))
        if (one[0] <= two[0] and one[1] >= two[1]) or (two[0] <= one[0] and two[1] >= one[1]):
            total += 1
    return total


def part2(data):
    total = 0
    for pair in data:
        one, two = map(lambda x: (int(x.split('-')[0]), int(x.split('-')[1])), pair.split(','))
        for i in range(one[0], one[1] + 1):
            if i in range(two[0], two[1] + 1):
                total += 1
                break
    return total


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

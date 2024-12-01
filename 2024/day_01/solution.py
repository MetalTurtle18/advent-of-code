def part1(data):
    a = [int(x.split()[0]) for x in data]
    b = [int(x.split()[1]) for x in data]
    a = sorted(a)
    b = sorted(b)

    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def part2(data):
    a = [int(x.split()[0]) for x in data]
    b = [int(x.split()[1]) for x in data]
    score = 0
    for i in a:
        score += i * b.count(i)

    return score

puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

def find_next(sequence, differences=None):
    if differences is None:
        differences = []
    if len(differences) != 0 and all(d == 0 for d in differences[-1]):
        new_diffs = [0]
        for i in range(len(differences) - 1, -1, -1):
            diff = differences[i][-1]
            new_diffs.append(new_diffs[-1] + diff)
        return sequence[-1] + new_diffs[-1]
    new_differences = []
    if len(differences) == 0:
        for i in range(len(sequence) - 1):
            new_differences.append(sequence[i + 1] - sequence[i])
    else:
        for i in range(len(differences[-1]) - 1):
            new_differences.append(differences[-1][i + 1] - differences[-1][i])
    return find_next(sequence, [*differences, new_differences])


def part1(data):
    total = 0
    for sequence in data:
        total += find_next(list(map(int, sequence.split())))
    return total


def part2(data):
    total = 0
    for sequence in data:
        total += find_next(list(reversed(list(map(int, sequence.split())))))
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

def part1(data):
    elves = [0]
    j = 0
    for i in data:
        if i == '':
            j += 1
            elves.append(0)
        else:
            elves[j] += int(i)
    return max(elves)


def part2(data):
    elves = [0]
    j = 0
    for i in data:
        if i == '':
            j += 1
            elves.append(0)
        else:
            elves[j] += int(i)
    elves = sorted(elves)
    return elves[len(elves) - 1] + elves[len(elves) - 2] + elves[len(elves) - 3]


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

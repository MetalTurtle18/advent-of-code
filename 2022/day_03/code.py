def part1(data):
    total = 0

    for sack in data:
        one, two = sack[:len(sack)//2], sack[len(sack)//2:]
        for item in two:
            if item in one:
                total += ord(item) - (96 if item.islower() else 38)
                break
    return total


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        one, two, three = data[i], data[i+1], data[i+2]
        for item in three:
            if item in two and item in one:
                total += ord(item) - (96 if item.islower() else 38)
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

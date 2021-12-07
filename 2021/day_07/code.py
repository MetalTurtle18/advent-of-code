def part1(data):
    positions = list(map(int, data[0].split(',')))
    fuel = sum(abs(max(positions) - i) for i in positions)
    for i in range(min(positions), max(positions)):
        fuel = min(fuel, sum(abs(i - j) for j in positions))
    return fuel


def part2(data):
    positions = list(map(int, data[0].split(',')))
    fuel = sum((abs(max(positions) - i) * (abs(max(positions) - i) + 1) // 2) for i in positions)
    for i in range(min(positions), max(positions)):
        fuel = min(fuel, sum((abs(i - j) * (abs(i - j) + 1) // 2) for j in positions))
    return fuel


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

from collections import defaultdict


def tick_fish(fish):
    new_fish = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + new_fish
    fish[7] = fish[8]
    fish[8] = new_fish


def puzzle(data, times):
    fish = defaultdict(int)
    for i in map(int, data[0].split(',')):
        fish[i] += 1
    for i in range(times):
        tick_fish(fish)
    return sum(fish.values())


def part1(data):
    return puzzle(data, 80)


def part2(data):
    return puzzle(data, 256)


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

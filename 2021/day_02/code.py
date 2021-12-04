def part1(data):
    horizontal = 0
    depth = 0
    for instruction in data:
        direction = instruction.split(" ")[0]
        num = int(instruction.split(" ")[1])
        if direction == "forward":
            horizontal += num
        elif direction == "down":
            depth += num
        elif direction == "up":
            depth -= num
    return horizontal * depth



def part2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in data:
        direction = instruction.split(" ")[0]
        num = int(instruction.split(" ")[1])
        if direction == "forward":
            horizontal += num
            depth += num * aim
        elif direction == "down":
            aim += num
        elif direction == "up":
            aim -= num
    return horizontal * depth


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

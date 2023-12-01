def part1(data):
    s = 0
    for line in data:
        num = ''
        for char in line:
            if char.isnumeric():
                num += char
                break
        for char in reversed(line):
            if char.isnumeric():
                num += char
                break
        s += int(num)
    return s


def part2(data):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    s = 0
    for line in data:
        num = '0'
        for i in range(len(line)):
            if line[i].isnumeric():
                num += line[i]
                break
            else:
                t = True
                for n in nums:
                    if t and line[i:].startswith(n):
                        num += str(nums.index(n))
                        t = False
                if not t:
                    break
        line = line[::-1]
        for i in range(len(line)):
            if line[i].isnumeric():
                num += line[i]
                break
            else:
                t = True
                for n in nums:
                    if t and line[i:].startswith(n[::-1]):
                        num += str(nums.index(n))
                        t = False
                if not t:
                    break
        s += int(num)
    return s


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    # print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

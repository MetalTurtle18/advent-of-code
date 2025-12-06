from util import *

def part1(data):
    total = 0
    problems = list(map(lambda p: p.split(), data[:-1]))
    operations = data[len(data) - 1].split()
    for problem in range(len(problems[0])):
        mult = operations[problem] == "*"
        ans = 1 if mult else 0
        for item in problems:
            if mult:
                ans *= int(item[problem])
            else:
                ans += int(item[problem])
        total += ans
    return total


def part2(data):
    total = 0
    longest_row = max(map(len, data))
    nums = []
    for i in range(longest_row - 1, -1, -1):
        col = [d[i] if len(d) > i else ' ' for d in data]
        num = ''.join(col[:-1]).strip()
        if num:
            nums.append(num)
        if col[-1] != ' ':
            total += eval(col[-1].join(nums))
            nums = []
    return total


if __name__ == "__main__":
    aoc = AOC(6)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
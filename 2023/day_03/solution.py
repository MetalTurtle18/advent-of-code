from collections import defaultdict

def part1(data):
    total = 0
    for i in range(len(data)):
        in_num = False
        num = ''
        digit_indices = []
        for c in range(len(data[i])):
            if data[i][c].isnumeric():
                if not in_num:
                    in_num = True
                    num = data[i][c]
                else:
                    num += data[i][c]
                digit_indices.append(c)
            if (not data[i][c].isnumeric() and in_num) or c == len(data[i]) - 1:
                in_num = False
                part = False
                for digit in digit_indices:
                    if digit != 0:
                        if data[i][digit - 1] not in '.1234567890':
                            part = True
                            break
                        if i != 0 and data[i - 1][digit - 1] not in '.1234567890':
                            part = True
                            break
                        if i != len(data) - 1 and data[i + 1][digit - 1] not in '.1234567890':
                            part = True
                            break
                    if digit != len(data[i]) - 1:
                        if data[i][digit + 1] not in '.1234567890':
                            part = True
                            break
                        if i != 0 and data[i - 1][digit + 1] not in '.1234567890':
                            part = True
                            break
                        if i != len(data) - 1 and data[i + 1][digit + 1] not in '.1234567890':
                            part = True
                            break
                    if i != 0 and data[i - 1][digit] not in '.1234567890':
                        part = True
                        break
                    if i != len(data) - 1 and data[i + 1][digit] not in '.1234567890':
                        part = True
                        break
                if part:
                    total += int(num)
                num = ''
                digit_indices = []

    return total


def part2(data):
    parts = defaultdict(lambda: 1)
    counts = defaultdict(lambda: 0)
    for i in range(len(data)):
        in_num = False
        num = ''
        digit_indices = []
        for c in range(len(data[i])):
            if data[i][c].isnumeric():
                if not in_num:
                    in_num = True
                    num = data[i][c]
                else:
                    num += data[i][c]
                digit_indices.append(c)
            if (not data[i][c].isnumeric() and in_num) or c == len(data[i]) - 1:
                in_num = False
                part = (-1, -1)
                for digit in digit_indices:
                    if digit != 0:
                        if data[i][digit - 1] == '*':
                            part = (i, digit - 1)
                            break
                        if i != 0 and data[i - 1][digit - 1] == '*':
                            part = (i - 1, digit - 1)
                            break
                        if i != len(data) - 1 and data[i + 1][digit - 1] == '*':
                            part = (i + 1, digit - 1)
                            break
                    if digit != len(data[i]) - 1:
                        if data[i][digit + 1] == '*':
                            part = (i, digit + 1)
                            break
                        if i != 0 and data[i - 1][digit + 1] == '*':
                            part = (i - 1, digit + 1)
                            break
                        if i != len(data) - 1 and data[i + 1][digit + 1] == '*':
                            part = (i + 1, digit + 1)
                            break
                    if i != 0 and data[i - 1][digit] == '*':
                        part = (i - 1, digit)
                        break
                    if i != len(data) - 1 and data[i + 1][digit] == '*':
                        part = (i + 1, digit)
                        break
                if part != (-1, -1):
                    parts[part] *= int(num)
                    counts[part] += 1
                num = ''
                digit_indices = []
    total = 0
    for part in parts:
        if counts[part] == 2:
            total += parts[part]
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

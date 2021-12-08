def list_intersection(a, b):
    if len(a) == 0:
        return b
    output = []
    for i in a:
        if i in b:
            output.append(i)
    return output


def part1(data):
    outputs = []
    for i in data:
        for j in i.split(' | ')[1].split(' '):
            outputs.append(j)
    return sum(1 for i in outputs if len(i) in [2, 3, 4, 7])


# does not work
def part2(data):
    digits_by_segments = [
        [0, 1, 2, 4, 5, 6],
        [2, 5],
        [0, 2, 3, 4, 6],
        [0, 2, 3, 5, 6],
        [1, 2, 3, 5],
        [0, 1, 3, 5, 6],
        [0, 1, 3, 4, 5, 6],
        [0, 2, 5],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6]
    ]

    total = 0
    for line in data:
        input_digits = [''.join(sorted(i)) for i in line.replace(' | ', ' ').split(' ')]
        numbers = [[] for _ in range(10)]
        for digit in input_digits:
            for num in range(10):
                if len(digits_by_segments[num]) == len(digit):  # right # of segments
                    numbers[num] = list_intersection(numbers[num], [digit])
        # now I have the code
        output_digits = [''.join(sorted(i)) for i in line.split(' | ')[1].split(' ')]
        output = ''
        for digit in output_digits:
            for possible_code in numbers:
                if digit in possible_code:
                    output += str(possible_code.index(digit))
        total += int(output)
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

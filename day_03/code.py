from statistics import mode
from copy import deepcopy


def reversible_mode(data, reverse=False):
    if data.count('1') == data.count('0'):
        return '0' if reverse else '1'
    else:
        return ('0' if mode(data) == '1' else '1') if reverse else mode(data)


def part1(data):
    gamma = ''.join([mode(k) for k in [[j[i] for j in data] for i in range(len(data[0]))]])
    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    data_o2 = deepcopy(data)
    data_co2 = deepcopy(data)

    for i in range(len(data[0])):
        if len(data_o2) > 1:
            data_o2 = [j for j in data_o2 if j[i] == reversible_mode([k[i] for k in data_o2])]
        if len(data_co2) > 1:
            data_co2 = [j for j in data_co2 if j[i] == reversible_mode([k[i] for k in data_co2], reverse=True)]
    return int(data_o2[0], 2) * int(data_co2[0], 2)


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

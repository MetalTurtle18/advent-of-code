from logging import exception
from copy import deepcopy as dc


def next_obs(grid, facing, r, c):
    match facing:
        case 'U':
            return grid[r - 1][c]
        case 'D':
            return grid[r + 1][c]
        case 'R':
            return grid[r][c + 1]
        case 'L':
            return grid[r][c - 1]
        case _:
            raise exception('Invalid direction')


def move(facing, r, c):
    match facing:
        case 'U':
            return r - 1, c
        case 'D':
            return r + 1, c
        case 'R':
            return r, c + 1
        case 'L':
            return r, c - 1
        case _:
            raise exception('Invalid direction')


def turn(facing):
    match facing:
        case 'U':
            return 'R'
        case 'D':
            return 'L'
        case 'R':
            return 'D'
        case 'L':
            return 'U'
        case _:
            raise exception('Invalid direction')


def part1(data):
    data = ['0' * len(data[0])] + ['0' + i + '0' for i in data] + ['0' * len(data[0])]

    facing = 'U' # U, D, L, R
    r, c = 0, 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '^':
                r, c = row, col
                break
        else:
            continue
        break

    visited = 1
    moves = 0

    while n := next_obs(data, facing, r, c):
        # print(n, facing, moves)
        match n:
            case '0':
                return visited
            case '.':
                r, c = move(facing, r, c)
                data[r] = data[r][:c] + 'X' + data[r][c + 1:]
                visited += 1
                moves += 1
            case 'X' | '^':
                r, c = move(facing, r, c)
                moves += 1
            case '#':
                facing = turn(facing)
        if moves >= len(data) * len(data[0]): # dumb approximation for loop checking
            break

    return -1


def part2(data):
    positions = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            print(f'row = {row}/{len(data)}, col = {col}/{len(data[row])}', end = '') # log to keep up with brute force that takes a long time
            if data[row][col] == '.':
                print(', testing position')
                test_data = dc(data)
                test_data[row] = test_data[row][:col] + '#' + ('' if col == len(test_data[row]) - 1 else test_data[row][col + 1:])
                if part1(test_data) == -1:
                    positions += 1
            else:
                print()

    return positions


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

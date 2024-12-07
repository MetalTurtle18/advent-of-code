from itertools import product

def part1(data):
    tot = 0
    for test in data:
        result, numbers = test.split(': ')
        result = int(result)
        numbers = numbers.split()
        operator_sets = list(map(
            lambda i: str(bin(i))[2:].rjust(len(numbers) - 1, '0')
            .replace('0', '+')
            .replace('1', '*'),
            range(0, int('1' * (len(numbers) - 1), 2) + 1)
        ))
        for operators in operator_sets:
            eqn = [''] * (len(numbers) * 3 - 1)
            eqn[::3] = numbers
            eqn[2::3] = operators
            eqn[1::3] = [')'] * len(numbers)
            eqn = '(' * len(numbers) + ''.join(eqn)
            if eval(eqn) == result:
                tot += result
                break
    return tot


def elephant_eval(eqn: list[str]):
    res = int(eqn[0])
    op = ''
    for token in eqn[1:]:
        if token in ['+', '*', '||']:
            op = token
        elif op == '+':
            res += int(token)
        elif op == '*':
            res *= int(token)
        elif op == '||':
            res = int(str(res) + token)
    return res


def part2(data):
    tot = 0
    for i, test in enumerate(data):
        print(f'Test {i}/{len(data)}')
        result, numbers = test.split(': ')
        result = int(result)
        numbers = numbers.split()
        operator_sets = list(product(['+', '*', '||'], repeat=len(numbers) - 1))
        for operators in operator_sets:
            eqn = [''] * (len(numbers) * 2 - 1)
            eqn[::2] = numbers
            eqn[1::2] = operators
            if elephant_eval(eqn) == result:
                tot += result
                break
    return tot


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

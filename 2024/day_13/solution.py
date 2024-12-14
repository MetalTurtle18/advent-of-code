from numpy import *

def run(data, p2):
    total = 0
    for machine in data:
        a_button, b_button, prize = machine.split('\n')
        ax, ay = map(lambda x: int(x[2:]), a_button.split(': ')[1].split(', '))
        bx, by = map(lambda x: int(x[2:]), b_button.split(': ')[1].split(', '))
        px, py = map(lambda x: int(x[2:]),    prize.split(': ')[1].split(', '))
        if p2:
            px += 10000000000000
            py += 10000000000000

        machine_matrix = array([[ax, bx], [ay, by]])
        prize_vector = array([[px], [py]])

        presses = linalg.lstsq(machine_matrix, prize_vector)[0]
        a = presses[0][0]
        b = presses[1][0]

        rounded_solution_vector = [[round(a)], [round(b)]]

        if (p2 or (a < 101 and b < 101)) and array_equal(matmul(machine_matrix, rounded_solution_vector), prize_vector):
            total += round(a) * 3 + round(b)

    return int(total)

def part1(data):
    return run(data, False)


def part2(data):
    return run(data, True)


puzzle_input = open("input.txt", "r").read().split("\n\n")
test_input = open("test.txt", "r").read().split("\n\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

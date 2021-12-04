def check_for_winner(board):
    for row in board:
        if all(j.count("*") == 1 for j in row):
            return True
    for column in [[board[i][j] for i in range(5)] for j in range(5)]:
        if all(j.count("*") == 1 for j in column):
            return True
    return False


def calculate_score(board, winner):
    total = 0
    for row in board:
        for column in row:
            if column.count("*") == 0:
                total += int(column)
    return total * winner


def part1(data):
    inputs = data.split("\n")[0].split(",")
    boards = []
    boards_data = data.split("\n\n")[1:]
    for i in range(0, len(boards_data)):
        boards.append([j for j in [[m for m in k.split(" ") if m != ''] for k in boards_data[i].split("\n")]])
    for i in [int(j) for j in inputs]:
        for board in range(len(boards)):
            for row in range(5):
                for column in range(5):
                    if boards[board][row][column].count("*") == 0 and int(boards[board][row][column]) == i:
                        boards[board][row][column] += "*"
        for board in boards:
            if check_for_winner(board):
                return calculate_score(board, int(i))


def part2(data):
    inputs = data.split("\n")[0].split(",")
    boards = []
    boards_data = data.split("\n\n")[1:]
    for i in range(0, len(boards_data)):
        boards.append([j for j in [[m for m in k.split(" ") if m != ''] for k in boards_data[i].split("\n")]])
    for i in [int(j) for j in inputs]:
        for board in range(len(boards)):
            for row in range(5):
                for column in range(5):
                    if boards[board][row][column].count("*") == 0 and int(boards[board][row][column]) == i:
                        boards[board][row][column] += "*"
        winners = []
        for board in boards:
            if check_for_winner(board):
                if len(boards) - len(winners) == 1:
                    return calculate_score(board, int(i))
                else:
                    winners.append(board)
        for board in winners:
            boards.remove(board)


puzzle_input = open("input.txt", "r").read()
test_input = open("test.txt", "r").read()

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

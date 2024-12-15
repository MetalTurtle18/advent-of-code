def add_tuples(a, b):
    return a[0] + b[0], a[1] + b[1]


def attempt_move(grid, start, move):
    offset = (0, 0)
    match move:
        case '^':
            offset = (-1, 0)
        case 'v':
            offset = (1, 0)
        case '<':
            offset = (0, -1)
        case '>':
            offset = (0, 1)
    next_location = add_tuples(start, offset)
    next_iter = next_location
    while grid[next_iter] == 'O':
        next_iter = add_tuples(next_iter, offset)
    if grid[next_location] == 'O' and grid[next_iter] == '.':
        grid[next_iter] = 'O'
        grid[start] = '.'
        grid[next_location] = '@'
        start = next_location
    if grid[next_location] == '.':
        grid[start] = '.'
        grid[next_location] = '@'
        start = next_location
    return grid, start


def attempt_move_wide(grid, start, move):
    def recurse(coords, direction):
        if grid[add_tuples(coords, (direction, 0))] == '.':
            return True, {coords}
        elif grid[add_tuples(coords, (direction, 0))] == '#':
            return False, set()
        elif grid[add_tuples(coords, (direction, 0))] == '[':
            left_box, set_l = recurse(add_tuples(coords, (direction, 0)), direction)
            right_box, set_r = recurse(add_tuples(coords, (direction, 1)), direction)
            full_set = set_l | set_r | {coords}
            return left_box and right_box, full_set
        elif grid[add_tuples(coords, (direction, 0))] == ']':
            left_box, set_l = recurse(add_tuples(coords, (direction, -1)), direction)
            right_box, set_r = recurse(add_tuples(coords, (direction, 0)), direction)
            full_set = set_l | set_r | {coords}
            return left_box and right_box, full_set
        return False, coords

    offset = (0, 0)
    match move:
        case '^':
            offset = (-1, 0)
        case 'v':
            offset = (1, 0)
        case '<':
            offset = (0, -1)
        case '>':
            offset = (0, 1)
    next_location = add_tuples(start, offset)
    next_iter = next_location
    while grid[next_iter] in ['[', ']']:
        next_iter = add_tuples(next_iter, offset)
    if grid[next_location] in ['[', ']'] and grid[next_iter] == '.':
        if move == '<': # simple case (no recursive searching required)
            for i in range(next_iter[1], start[1]):
                grid[(next_iter[0], i)] = grid[(next_iter[0], i + 1)]
            grid[start] = '.'
            start = next_location
        elif move == '>': # simple case (no recursive searching required)
            for i in range(next_iter[1], start[1], -1):
                grid[(next_iter[0], i)] = grid[(next_iter[0], i - 1)]
            grid[start] = '.'
            start = next_location
        elif move in ['^', 'v']:
            direction_move = -1 if move == '^' else 1
            movable_l, movable_r = False, False
            boxes_set_l, boxes_set_r = set(), set()
            if grid[next_location] == '[':
                movable_l, boxes_set_l = recurse(next_location, direction_move)
                movable_r, boxes_set_r = recurse(add_tuples(next_location, (0, 1)), direction_move)
            elif grid[next_location] == ']':
                movable_l, boxes_set_l = recurse(add_tuples(next_location, (0, -1)), direction_move)
                movable_r, boxes_set_r = recurse(next_location, direction_move)
            if movable_l and movable_r:
                boxes_to_move = boxes_set_l | boxes_set_r
                for box in sorted(boxes_to_move, key = lambda t: t[0], reverse = move == 'v'):
                    grid[add_tuples(box, (direction_move, 0))] = grid[box]
                    grid[box] = '.'

    if grid[next_location] == '.':
        grid[start] = '.'
        grid[next_location] = '@'
        start = next_location
    return grid, start


def part1(data):
    grid = {(r, c): t for r, s in enumerate(data[0].split('\n')) for c, t in enumerate(s)}
    moves = data[1].replace('\n', '')
    robot = (0, 0)
    for pos, token in grid.items():
        if token == '@':
            robot = pos
            break
    for move in moves:
        grid, robot = attempt_move(grid, robot, move)

    tot_gps = 0
    for pos, token in grid.items():
        if token == 'O':
            tot_gps += pos[0] * 100 + pos[1]

    # for i in range(10):
    #     for j in range(10):
    #         print(grid[(i, j)], end = ' ')
    #     print()

    return tot_gps


def part2(data):
    half_grid = data[0].split('\n')
    grid = [[] for _ in range(len(half_grid))]
    for r in range(len(half_grid)):
        for c in range(len(half_grid[0])):
            match half_grid[r][c]:
                case '#':
                    grid[r] += ['#', '#']
                case '.':
                    grid[r] += ['.', '.']
                case 'O':
                    grid[r] += ['[', ']']
                case '@':
                    grid[r] += ['@', '.']
    grid = {(r, c): t for r, s in enumerate(grid) for c, t in enumerate(s)}
    moves = data[1].replace('\n', '')
    robot = (0, 0)
    for pos, token in grid.items():
        if token == '@':
            robot = pos
            break
    # for move in moves:
    for move in moves:
        # if move == 'v':
        #     pass
        grid, robot = attempt_move_wide(grid, robot, move)

        # for i in range(10):
        #     for j in range(20):
        #         print(grid[(i, j)], end = ' ')
        #     print()
        # print(move)

    tot_gps = 0
    for pos, token in grid.items():
        if token == '[':
            tot_gps += pos[0] * 100 + pos[1]

    for i in range(10):
        for j in range(20):
            print(grid[(i, j)], end = ' ')
        print()

    return tot_gps


puzzle_input = open("input.txt", "r").read().split("\n\n")
test_input = open("test.txt", "r").read().split("\n\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

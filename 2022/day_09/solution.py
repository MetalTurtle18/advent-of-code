def simulate_move(_head, knots, tail_visits, direction, distance):
    if direction == 'U':
        for i in range(distance):
            for k in range(len(knots) - 1, -1, -1):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] + x, head[1] + 1) for x in
                            range(-1, 2)]:  # Check if the tail needs to move; only if below head
                    tail = head
                head = (head[0], head[1] - 1)
                if k == 0:
                    tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    elif direction == 'D':
        for i in range(distance):
            for k in range(len(knots) - 1, -1, -1):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] + x, head[1] - 1) for x in
                            range(-1, 2)]:  # Check if the tail needs to move; only if above head
                    tail = head
                head = (head[0], head[1] + 1)
                if k == len(knots) - 1:
                    tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    elif direction == 'L':
        for i in range(distance):
            for k in range(len(knots) - 1, -1, -1):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] + 1, head[1] + y) for y in
                            range(-1, 2)]:  # Check if the tail needs to move; only if right of head
                    tail = head
                head = (head[0] - 1, head[1])
                if k == 0:
                    tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    else:  # Right
        for i in range(distance):
            for k in range(len(knots) - 1, -1, -1):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] - 1, head[1] + y) for y in
                            range(-1, 2)]:  # Check if the tail needs to move; only if left of head
                    tail = head
                head = (head[0] + 1, head[1])
                if k == 0:
                    tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    return _head, knots, tail_visits


def part1(data):
    head = (0, 0)  # (x, y)
    tail = (0, 0)  # (x, y)
    tail_visits = {(0, 0)}  # Set of locations visited by tail
    for motion in data:
        direction, _distance = motion.split()
        distance = int(_distance)
        head, _knots, tail_visits = simulate_move(head, [tail], tail_visits, direction, distance)
        tail = _knots[0]
    return len(tail_visits)


def print_knots(knots):
    x_dim = max([k[0] for k in knots]) - min([k[0] for k in knots]) + 1
    y_dim = max([k[1] for k in knots]) - min([k[1] for k in knots]) + 1
    grid = [['.' for _ in range(x_dim)] for _ in range(y_dim)]
    for i, k in enumerate(knots):
        grid[k[1] - min([k[1] for k in knots])][k[0] - min([k[0] for k in knots])] = str(i)
    for row in grid:
        print(''.join(row))
    print()


def part2(data):
    steps = []
    for line in data:
        direction, distance = line.split()
        for _ in range(int(distance)):
            steps.append(direction)
    knots = [(0, 0) for _ in range(10)]  # 0 is the head, 9 is the tail
    tail_visits = {(0, 0)}  # Set of locations visited by tail

    for step in steps:
        if step == 'U':
            knots[0] = (knots[0][0], knots[0][1] + 1)  # Move head up
        elif step == 'D':
            knots[0] = (knots[0][0], knots[0][1] - 1)  # Move head down
        elif step == 'L':
            knots[0] = (knots[0][0] - 1, knots[0][1])  # Move head left
        else:  # step == 'R'
            knots[0] = (knots[0][0] + 1, knots[0][1])  # Move head right
        # print("Step:", step, "(after head move)")
        # print_knots(knots)
        for k in range(1, len(knots)):  # In order, starting from knot behind the head
            if knots[k][1] < knots[k - 1][1] - 1:  # If the knot is more than one space below the previous knot
                knots[k] = (knots[k][0], knots[k][1] + 1)
                if knots[k][0] < knots[k - 1][0]:  # If the knot is to the left of the next knot
                    knots[k] = (knots[k][0] + 1, knots[k][1])
                elif knots[k][0] > knots[k - 1][0]:  # If the knot is to the right of the next knot
                    knots[k] = (knots[k][0] - 1, knots[k][1])
            elif knots[k][1] > knots[k - 1][1] + 1:  # If the knot is more than one space above the previous knot
                knots[k] = (knots[k][0], knots[k][1] - 1)
                if knots[k][0] < knots[k - 1][0]:
                    knots[k] = (knots[k][0] + 1, knots[k][1])
                elif knots[k][0] > knots[k - 1][0]:
                    knots[k] = (knots[k][0] - 1, knots[k][1])
            elif knots[k][0] < knots[k - 1][0] - 1:  # If the knot is more than one space left of the previous knot
                knots[k] = (knots[k][0] + 1, knots[k][1])
                if knots[k][1] < knots[k - 1][1]:
                    knots[k] = (knots[k][0], knots[k][1] + 1)
                elif knots[k][1] > knots[k - 1][1]:
                    knots[k] = (knots[k][0], knots[k][1] - 1)
            elif knots[k][0] > knots[k - 1][0] + 1:  # If the knot is more than one space right of the previous knot
                knots[k] = (knots[k][0] - 1, knots[k][1])
                if knots[k][1] < knots[k - 1][1]:
                    knots[k] = (knots[k][0], knots[k][1] + 1)
                elif knots[k][1] > knots[k - 1][1]:
                    knots[k] = (knots[k][0], knots[k][1] - 1)
        tail_visits.add(knots[-1])
        # print("Step:", step, "(after knot moves)")
        # print_knots(knots)
    return len(tail_visits)


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

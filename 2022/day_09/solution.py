def simulate_move(_head, knots, tail_visits, direction, distance):
    if direction == 'U':
        for i in range(distance):
            for k in range(len(knots)):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] + x, head[1] + 1) for x in range(-1, 2)]:  # Check if the tail needs to move; only if below head
                    tail = head
                head = (head[0], head[1] - 1)
                tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    elif direction == 'D':
        for i in range(distance):
            for k in range(len(knots)):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] + x, head[1] - 1) for x in range(-1, 2)]:  # Check if the tail needs to move; only if above head
                    tail = head
                head = (head[0], head[1] + 1)
                tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    elif direction == 'L':
        for i in range(distance):
            for k in range(len(knots)):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] + 1, head[1] + y) for y in range(-1, 2)]:  # Check if the tail needs to move; only if right of head
                    tail = head
                head = (head[0] - 1, head[1])
                tail_visits.add(tail)
                knots[k] = tail
                if k == 0:
                    _head = head
                else:
                    knots[k - 1] = head
    else:  # Right
        for i in range(distance):
            for k in range(len(knots)):
                tail = knots[k]
                head = _head if k == 0 else knots[k - 1]
                if tail in [(head[0] - 1, head[1] + y) for y in range(-1, 2)]:  # Check if the tail needs to move; only if left of head
                    tail = head
                head = (head[0] + 1, head[1])
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


def part2(data):
    head = (0, 0)  # (x, y)
    knots = [(0, 0) for i in range(9)]
    tail_visits = {(0, 0)}  # Set of locations visited by tail
    for motion in data:
        direction, _distance = motion.split()
        distance = int(_distance)
        head, knots, tail_visits = simulate_move(head, knots, tail_visits, direction, distance)
    return len(tail_visits)


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    # print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

def part1(data):
    rules, updates = data.split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

    correct = [True for _ in range(len(updates))]

    for update in range(len(updates)):
        for a in range(0, len(updates[update]) - 1):
            for b in range(a + 1, len(updates[update])):
                for c, d in rules:
                    if updates[update][a] == d and updates[update][b] == c:
                        correct[update] = False

    tot = 0
    for update in range(len(correct)):
        if correct[update]:
            tot += updates[update][len(updates[update]) // 2]

    return tot

def wrong(update, rules):
    for a in range(0, len(update) - 1):
        for b in range(a + 1, len(update)):
            for c, d in rules:
                if update[a] == d and update[b] == c:
                    return True
    return False


def swap(update, rules):
    for a in range(0, len(update) - 1):
        for b in range(a + 1, len(update)):
            for c, d in rules:
                if update[a] == d and update[b] == c:
                    update[a], update[b] = update[b], update[a]


def part2(data):
    rules, updates = data.split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

    correct = [True for _ in range(len(updates))]

    for update in range(len(updates)):
        correct[update] = not wrong(updates[update], rules)

    tot = 0
    for update in range(len(correct)):
        if not correct[update]:
            while wrong(updates[update], rules):
                swap(updates[update], rules)
            tot += updates[update][len(updates[update]) // 2]

    return tot


puzzle_input = open("input.txt", "r").read()
test_input = open("test.txt", "r").read()

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

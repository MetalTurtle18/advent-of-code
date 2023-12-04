def part1(data):
    total = 0
    for card in data:
        points = 0.5
        _winning, _yours = card.split(': ')[1].split(' | ')
        winning = [int(_winning[i:i+2]) for i in range(0, len(_winning), 3)]
        yours = [int(_yours[i:i+2]) for i in range(0, len(_yours), 3)]

        for num in yours:
            if num in winning:
                points *= 2
        if points != 0.5:
            total += points
    return int(total)


def check_card(cards: dict, card: int) -> int:  # yay recursion; type hints will be helpful
    print(card)
    winners = 0
    for num in cards[card][1]:
        if num in cards[card][0]:
            winners += 1
    if winners == 0:
        return 1
    else:
        return 1 + sum(check_card(cards, i) if i in cards.keys() else 0 for i in range(card + 1, card + 1 + winners))


def part2(data):
    cards = {}
    for card in data:
        card, numbers = card.split(': ')
        _winning, _yours = numbers.split(' | ')
        winning = [int(_winning[i:i+2]) for i in range(0, len(_winning), 3)]
        yours = [int(_yours[i:i+2]) for i in range(0, len(_yours), 3)]
        cards[int(card.split()[1])] = (winning, yours)
    return sum(check_card(cards, i) for i in range(1, len(cards) + 1))


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

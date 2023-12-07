import functools

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def five_of_a_kind(cards):
    return all(card == cards[0] for card in cards)


def four_of_a_kind(cards):
    cards = sorted(cards, key=lambda x: card_values[x])
    return (all(card == cards[0] for card in cards[:4])
            or all(card == cards[1] for card in cards[1:]))


def full_house(cards):
    cards = sorted(cards, key=lambda x: card_values[x])
    return cards[0] == cards[1] and cards[3] == cards[4] and (cards[2] == cards[1] or cards[2] == cards[3])


def three_of_a_kind(cards):
    cards = sorted(cards, key=lambda x: card_values[x])
    return (cards[0] == cards[1] and cards[1] == cards[2]
            or cards[1] == cards[2] and cards[2] == cards[3]
            or cards[2] == cards[3] and cards[3] == cards[4])


def two_pair(cards):
    cards = sorted(cards, key=lambda x: card_values[x])
    return (cards[0] == cards[1] and cards[2] == cards[3]
            or cards[0] == cards[1] and cards[3] == cards[4]
            or cards[1] == cards[2] and cards[3] == cards[4])


def one_pair(cards):
    cards = sorted(cards, key=lambda x: card_values[x])
    return (cards[0] == cards[1]
            or cards[1] == cards[2]
            or cards[2] == cards[3]
            or cards[3] == cards[4])


def compare_high_card_hands(hand1, hand2):
    for i in range(5):
        if card_values[hand1[i]] > card_values[hand2[i]]:
            return 1
        elif card_values[hand1[i]] < card_values[hand2[i]]:
            return -1
    return 0


def compare_hands(hand1, hand2):
    """
    :param hand1: the first hand
    :param hand2: the second hand
    :return: 1 if hand1 wins, 0 if hands tie, -1 if hand2 wins
    """
    hand1 = hand1[0]
    hand2 = hand2[0]
    if five_of_a_kind(hand1):
        if five_of_a_kind(hand2):
            return compare_high_card_hands(hand1, hand2)
        return 1
    elif five_of_a_kind(hand2):
        return -1
    if four_of_a_kind(hand1):
        if four_of_a_kind(hand2):
            return compare_high_card_hands(hand1, hand2)
        return 1
    elif four_of_a_kind(hand2):
        return -1
    if full_house(hand1):
        if full_house(hand2):
            return compare_high_card_hands(hand1, hand2)
        return 1
    elif full_house(hand2):
        return -1
    if three_of_a_kind(hand1):
        if three_of_a_kind(hand2):
            return compare_high_card_hands(hand1, hand2)
        return 1
    elif three_of_a_kind(hand2):
        return -1
    if two_pair(hand1):
        if two_pair(hand2):
            return compare_high_card_hands(hand1, hand2)
        return 1
    elif two_pair(hand2):
        return -1
    if one_pair(hand1):
        if one_pair(hand2):
            return compare_high_card_hands(hand1, hand2)
        return 1
    elif one_pair(hand2):
        return -1
    return compare_high_card_hands(hand1, hand2)


def part1(data):
    hands = [([i for i in line[:5]], line[6:]) for line in data]
    sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands))

    return sum(int(hand[1]) * (i + 1) for i, hand in enumerate(sorted_hands))


def part2(data):
    return data[0]


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

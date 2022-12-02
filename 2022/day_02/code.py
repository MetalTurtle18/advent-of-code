def part1(data):
    opp_plays = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
    }
    you_plays = {
        'X': 'R',
        'Y': 'P',
        'Z': 'S'
    }
    points = {
        'R': 1,
        'P': 2,
        'S': 3,
    }

    score = 0
    for r in data:
        opp, you = r.split()
        opp_play = opp_plays[opp]
        you_play = you_plays[you]
        if opp_play == you_play:
            score += 3 + points[you_play]
        elif (opp_play == 'R' and you_play == 'S') or (opp_play == 'P' and you_play == 'R') or (opp_play == 'S' and you_play == 'P'):
            score += points[you_play]
        else:
            score += 6 + points[you_play]
    return score



def part2(data):
    opp_plays = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
    }
    points = {
        'R': 1,
        'P': 2,
        'S': 3,
    }

    win = {
        'R': 'P',
        'P': 'S',
        'S': 'R',
    }
    lose = {
        'R': 'S',
        'P': 'R',
        'S': 'P',
    }

    score = 0
    for r in data:
        opp, end = r.split()
        opp_play = opp_plays[opp]
        if end == 'X':
            score += points[lose[opp_play]]
        elif end == 'Y':
            score += 3 + points[opp_play]
        else:
            score += 6 + points[win[opp_play]]
    return score




puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

def part1(data):
    total = 0
    for game in data:
        game_id, colors = game[5:].split(': ')
        valid = True
        for pull in colors.split('; '):
            for color in pull.split(', '):
                if color.endswith(' red') and int(color[:-4]) > 12:
                    valid = False
                elif color.endswith(' blue') and int(color[:-5]) > 14:
                    valid = False
                elif color.endswith(' green') and int(color[:-6]) > 13:
                    valid = False
        if valid:
            total += int(game_id)

    return total


def part2(data):
    total = 0
    for game in data:
        pulls = game.split(': ')[1].split('; ')
        red = 0
        blue = 0
        green = 0
        for pull in pulls:
            for color in pull.split(', '):
                if color.endswith(' red'):
                    red = max(red, int(color[:-4]))
                elif color.endswith(' blue'):
                    blue = max(blue, int(color[:-5]))
                elif color.endswith(' green'):
                    green = max(green, int(color[:-6]))
        power = red * blue * green
        total += power

    return total


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

from collections import defaultdict


def blink(stones):
    out = []
    for stone in stones:
        if int(stone) == 0:
            out.append('1')
        elif len(stone) % 2 == 0:
            out.append(str(int(stone[:len(stone) // 2])))
            out.append(str(int(stone[len(stone) // 2:])))
        else:
            out.append(str(int(stone) * 2024))
    return out


def part1(data):
    for i in range(25):
        data = blink(data)
        # print(f'round {i}, {data}')
    return len(data)


def part2(data):
    def blink2(tiles):
        new_tiles = defaultdict(int)
        new_tiles['1'] += tiles['0']
        for key in tiles.keys():
            if len(key) % 2 == 0:
                new_tiles[str(int(key[:len(key) // 2]))] += tiles[key]
                new_tiles[str(int(key[len(key) // 2:]))] += tiles[key]
            elif key != '0':
                new_tiles[str(int(key) * 2024)] += tiles[key]
        return new_tiles

    start = defaultdict(int)
    for stone in data:
        start[stone] += 1
    for i in range(75):
        start = blink2(start)
        # print(f'round {i}, {start.items()}')

    return sum(start.values())


puzzle_input = open("input.txt", "r").read().split(" ")
test_input = open("test.txt", "r").read().split(" ")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

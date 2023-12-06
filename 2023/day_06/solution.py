from re import split

def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

def part1(data):
    _times, _distances = data
    times = list(map(int, split("\s+", _times.split(":")[1])[1:]))
    distances = list(map(int, split("\s+", _distances.split(":")[1])[1:]))
    ways = [0 for _ in range(len(times))]
    for i in range(len(times)):
        time = times[i]
        best_distance = distances[i]
        for s in range(1, time):
            moving_time = time - s
            speed = s
            distance = speed * moving_time
            if distance > best_distance:
                ways[i] += 1
    return product(ways)



def part2(data):
    _times, _distances = data
    time = int(_times.split(":")[1].replace(" ", ""))
    best_distance = int(_distances.split(":")[1].replace(" ", ""))
    ways = 0
    for s in range(1, time):
        moving_time = time - s
        speed = s
        distance = speed * moving_time
        if distance > best_distance:
            ways += 1

    return ways


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

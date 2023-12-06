# Thank you derailed-dash for helping me understand how to solve part 2
# https://github.com/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb

def part1(data):
    seeds = list(map(int, data[0].split()[1:]))
    for map_set in data[1:]:
        lines = map_set.split('\n')[1:]
        for i in range(len(seeds)):  # For each seed
            for mapping in lines:
                destination, source, length = map(int, mapping.split())
                if seeds[i] in range(source, source + length):
                    seeds[i] = destination + seeds[i] - source
                    break
    return min(seeds)


def map_intervals(intervals, mapping):
    new_intervals = []
    src_ranges = [(mapping[1], mapping[2]) for mapping in mapping]
    dest_ranges = [(mapping[0], mapping[2]) for mapping in mapping]
    for i, current_range in enumerate(src_ranges):
        src_start = current_range[0]
        src_end = current_range[0] + current_range[1]
        dest_start = dest_ranges[i][0]
        temp_intervals = []
        while intervals:
            (int_start, int_end) = intervals.pop(0)
            left = (int_start, min(int_end, src_start))
            mid = (max(int_start, src_start), min(src_end, int_end))
            right = (max(src_end, int_start), int_end)

            if left[1] > left[0]:  # if left has +ve length, then scenario 1, else scenario 2
                temp_intervals.append(left)  # pass on the interval unchanged
            if mid[1] > mid[0]:  # if mid has +ve length, then we need to apply the shift to this interval
                # furthermore, once mapped, we know this interval won't appear in another range
                new_intervals.append((mid[0] - src_start + dest_start, mid[1] - src_start + dest_start))
            if right[1] > right[0]:  # if right has +ve length
                temp_intervals.append(right)  # pass on the interval unchanged

        intervals = temp_intervals
    return new_intervals + intervals


def part2(data):
    seeds = list(map(int, data[0].split()[1:]))
    seed_intervals = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    current_intervals = seed_intervals

    for current_map in data[1:]:
        mapping = [(int(m.split()[0]), int(m.split()[1]), int(m.split()[2])) for m in current_map.split('\n')[1:]]
        current_intervals = map_intervals(current_intervals, mapping)

    return min(start for start, _ in current_intervals)


puzzle_input = open("input.txt", "r").read().split("\n\n")
test_input = open("test.txt", "r").read().split("\n\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

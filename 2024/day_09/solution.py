import re

def part1(data):
    data = list(data)
    file_id = 0
    spaces = 0
    disk = []

    # make disk layout
    for i, block in enumerate(data):
        if i % 2:
            disk += ['.'] * int(block)
            spaces += int(block)
        else:
            disk += [str(file_id)] * int(block)
            file_id += 1
    print(disk)

    # move blocks
    first_index = 0
    last_index = len(disk)
    while first_index < last_index:
        first_index = disk.index('.')
        for i in range(len(disk) - 1, -1, -1):
            if disk[i] != '.':
                last_index = i
                break
        if first_index < last_index:
            print(f'moving {last_index} to {first_index} (diff = {last_index - first_index})')
            id_cur = disk[last_index]
            disk[last_index] = '.'
            disk[first_index] = id_cur
            # print(disk)

    # checksum
    checksum = 0
    for i, id_cur in enumerate(disk):
        if id_cur == '.':
            break
        checksum += i * int(id_cur)

    return checksum


def sublist_search(outer, inner):
    for i in range(len(outer) - len(inner) + 1):
        if outer[i:i + len(inner)] == inner:
            return i
    return -1


def part2(data):
    data = list(data)
    file_id = 0
    block_sizes = []
    disk = []

    # make disk layout
    for i, block in enumerate(data):
        if i % 2 == 0:
            disk.append([str(file_id)] * int(block))
            block_sizes.append(int(block))
            file_id += 1
        elif block != '0':
            disk += ['.'] * int(block)
    print(disk)

    # move blocks
    for id_cur in range(file_id - 1, 0, -1):
        block_size = block_sizes[id_cur]
        first_index = sublist_search(disk, ['.'] * block_size)
        block_index = disk.index([str(id_cur)] * block_size)
        if 0 <= first_index < block_index:
            print(f'moving {block_index} to {first_index} (diff = {block_index - first_index})')
            del disk[block_index]
            del disk[first_index:first_index + block_size]
            disk.insert(first_index, [str(id_cur)] * block_size)
            for i in range(block_size): disk.insert(block_index - block_size + 1, '.')
        # print(disk)

    # checksum
    checksum = 0
    k = 0
    for i, block in enumerate(disk):
        if block == '.':
            k += 1
            continue
        for j in block:
            checksum += k * int(j)
            k += 1

    return checksum


puzzle_input = open("input.txt", "r").read()
test_input = open("test.txt", "r").read()

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")

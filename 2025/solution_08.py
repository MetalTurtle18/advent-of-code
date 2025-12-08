# This is not a good or optimized solution. Part 2 took nearly ten minutes to run. Maybe I'll revisit this when I have time

from math import sqrt

from util import *

PAIRS = 1000


def part1(data):
    boxes = list(map(lambda d: tuple(map(int, d.split(','))), data))
    nodes = []
    edges = {}
    for box in boxes:
        nodes.append(box)
        for node in nodes[:-1]:
            edges[(node, box)] = sqrt((box[0] - node[0]) ** 2 + (box[1] - node[1]) ** 2 + (box[2] - node[2]) ** 2)
    circuits = []
    flat_circuits = set()
    for _ in range(PAIRS):
        closest = min(edges, key=edges.get)
        if closest[0] in flat_circuits or closest[1] in flat_circuits:  # This is connected to an existing circuit
            l0 = list(filter(lambda l: closest[0] in l, circuits))
            l1 = list(filter(lambda l: closest[1] in l, circuits))
            i0 = circuits.index(l0[0]) if l0 else -1
            i1 = circuits.index(l1[0]) if l1 else -1
            if i1 == -1 and i0 != -1:
                circuits[i0].add(closest[1])
            elif i0 == -1 and i1 != -1:
                circuits[i1].add(closest[0])
            elif i1 != i0:
                circuits[i0] = circuits[i0].union(circuits[i1])
                circuits.pop(i1)
            flat_circuits.add(closest[0])
            flat_circuits.add(closest[1])
        else:  # This is a brand-new circuit
            circuits.append({closest[0], closest[1]})
            flat_circuits.add(closest[0])
            flat_circuits.add(closest[1])
        edges.pop(closest)
        print(_)
        # print(*circuits, sep='\n', end='\n\n')
    lengths = [len(c) for c in circuits]
    lengths.sort(reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def part2(data):
    boxes = list(map(lambda d: tuple(map(int, d.split(','))), data))
    nodes = []
    edges = {}
    for box in boxes:
        nodes.append(box)
        for node in nodes[:-1]:
            edges[(node, box)] = sqrt((box[0] - node[0]) ** 2 + (box[1] - node[1]) ** 2 + (box[2] - node[2]) ** 2)
    circuits = [{b} for b in boxes]
    flat_circuits = set()
    last_connection = -1
    while len(circuits) > 1:
        print(len(circuits))
        closest = min(edges, key=edges.get)
        last_connection = closest
        l0 = list(filter(lambda l: closest[0] in l, circuits))
        l1 = list(filter(lambda l: closest[1] in l, circuits))
        i0 = circuits.index(l0[0]) if l0 else -1
        i1 = circuits.index(l1[0]) if l1 else -1
        if i1 == -1 and i0 != -1:
            circuits[i0].add(closest[1])
        elif i0 == -1 and i1 != -1:
            circuits[i1].add(closest[0])
        elif i1 != i0:
            circuits[i0] = circuits[i0].union(circuits[i1])
            circuits.pop(i1)
        flat_circuits.add(closest[0])
        flat_circuits.add(closest[1])
        edges.pop(closest)

    return last_connection[0][0] * last_connection[1][0]


if __name__ == "__main__":
    aoc = AOC(8)
    # print(aoc.test(part1, part2))
    print(aoc.test(p2=part2))
    # print(aoc.run(part1, part2))
    print(aoc.run(p2=part2))

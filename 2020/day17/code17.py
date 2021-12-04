import numpy as np
from copy import deepcopy as dc
relative_coords = [(1, -1, 1),
            (1, 0, 1),
            (1, 1, 1),
            (0, -1, 1),
            (0, 0, 1),
            (0, 1, 1),
            (-1, -1, 1),
            (-1, 0, 1),
            (-1, 1, 1),  # End of top layer
            (1, -1, 0),
            (1, 0, 0),
            (1, 1, 0),
            (0, -1, 0),
            (0, 1, 0),
            (-1, -1, 0),
            (-1, 0, 0),
            (-1, 1, 0),  # End of middle layer
            (1, -1, -1),
            (1, 0, -1),
            (1, 1, -1),
            (0, -1, -1),
            (1, 0, -1),
            (1, 1, -1),
            (-1, -1, -1),
            (-1, 0, -1),
            (-1, 1, -1)]


def simulate(hyperplane):
    expanded_hyperplane = np.pad(hyperplane, pad_width=1, mode='constant', constant_values='.')
    output = dc(expanded_hyperplane)
    for x in range(len(expanded_hyperplane)):
        for y in range(len(expanded_hyperplane)):
            for z in range(len(expanded_hyperplane)):
                if get_surrounding_cube_count(expanded_hyperplane, x, y, z) not in [2, 3] and (expanded_hyperplane[x][y][z] == "#"):
                    output[x][y][z] = "."
                elif (get_surrounding_cube_count(expanded_hyperplane, x, y, z) == 3) and (expanded_hyperplane[x][y][z] == "."):
                    output[x][y][z] = "#"
    return output


def get_surrounding_cube_count(hyperplane, x, y, z):
    count = 0
    expanded_hyperplane = np.pad(hyperplane, pad_width=1, mode='constant', constant_values='.')
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx == dy == dz == 0:
                    continue
                if expanded_hyperplane[(x + dx, y + dy, z + dz)] == "#":
                    count += 1
    return count


p_in = open("../day17/test17.txt", "r").read().split("\n")
world = np.array([[list(i) for i in p_in]])
print("Original\n", world)
world = simulate(dc(world))
print("Gen 1\n", world)
world = simulate(dc(world))
print("Gen 2\n", world)
world = simulate(dc(world))
print("Gen 3\n", world)
world = simulate(dc(world))
print("Gen 4\n", world)
world = simulate(dc(world))
print("Gen 5\n", world)
world = simulate(dc(world))
print("Gen 6\n", world)
count_active = 0
for x in range(len(world)):
    for y in range(len(world[x])):
        for z in range(len(world[x][y])):
            if world[x][y][z] == "#":
                count_active += 1
print(count_active)

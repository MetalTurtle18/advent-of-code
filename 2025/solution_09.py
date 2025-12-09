# Wow part 1 was super easy (sub 6 minutes) and part 2 was insanely hard
# would have been impossible without this https://www.xjavascript.com/blog/check-if-polygon-is-inside-a-polygon/
# And I peaked at this sol'n from Reddit: https://github.com/seligman/aoc/blob/master/2025/Helpers/day_09.py
# That one had a similar approach to me so I could compare some things
# Added matplotlib just to visualize wtf was happening
# Even though part 2 works, it still takes like 2 minutes to run. Oh well. I never come back to optimize AOC solutions

from util import *
import matplotlib.pyplot as plt


def corner_area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(data):
    data = list(map(lambda d: tuple(map(int, d.split(','))), data))
    max_area = 0
    for i, c1 in enumerate(data[:-1]):
        for j, c2 in enumerate(data[i + 1:]):
            max_area = max(max_area, corner_area(c1, c2))
    return max_area


def point_on_segment(p, a, b):
    x, y = p
    x1, y1 = a
    x2, y2 = b

    if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
        cross_product = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        return cross_product == 0
    return False


def point_inside_polygon(p, vertices):
    inside = False
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        xi, yi = vertices[i]
        xj, yj = vertices[j]

        if point_on_segment(p, (xi, yi), (xj, yj)):
            return True

        if (yi > p[1]) != (yj > p[1]):
            x_int = ((p[1] - yi) * (xj - xi)) / (yj - yi) + xi
            if p[0] < x_int:
                inside = not inside
    return inside


def segments_intersect(a, b, c, d):
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    return o1 * o2 < 0 and o3 * o4 < 0  # That would indicate: both have one 1 and one -1
    # o1 and o2 are how c and d arranged. If one cw and one ccw, then that should mean they are perpendicular
    # ok I guess that makes sense


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def on_segment(p, q, r):
    return max(p[0], r[0]) >= q[0] >= min(p[0], r[0]) and max(p[1], r[1]) >= q[1] >= min(p[1], r[1])


def rect_in_polygon(c1, c2, vertices):
    corners = [c1, c2, (c1[0], c2[1]), (c2[0], c1[1])]
    for corner in corners:
        inside = point_inside_polygon(corner, vertices)
        if not inside:
            return False
    for i_e in range(4):
        for j_e in range(len(vertices)):
            intersect = segments_intersect(corners[i_e], corners[(i_e + 1) % 4], vertices[j_e], vertices[(j_e + 1) % len(vertices)])
            if intersect:
                return False
    return True

def part2(data):
    data = list(map(lambda d: tuple(map(int, d.split(','))), data))
    max_area = 0
    max_shape = ((0, 0), (0, 0))
    plt.close('all')
    plt.plot([d[0] for d in data], [d[1] for d in data])
    for i, c1 in enumerate(data[:-1]):
        for j, c2 in enumerate(data[i + 1:]):
            print(f'rect: {i}, {j}')
            if rect_in_polygon(c1, c2, data):
                area = corner_area(c1, c2)
                if area > max_area:
                    max_area = area
                    max_shape = (c1, c2)
    plt.plot([max_shape[0][0], max_shape[0][0], max_shape[1][0], max_shape[1][0]],
             [max_shape[0][1], max_shape[1][1], max_shape[1][1], max_shape[0][1]])
    plt.show()
    print(max_shape)
    return max_area


if __name__ == "__main__":
    aoc = AOC(9)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))

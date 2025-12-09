from util import *

def corner_area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(data):
    data = list(map(lambda d: tuple(map(int, d.split(','))), data))
    max_area = 0
    for i, c1 in enumerate(data[:-1]):
        for j, c2 in enumerate(data[i+1:]):
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



def point_inside_polygon(p, vertices, memo):
    if p in memo:
        return True, memo
    inside = False
    if p not in memo:
        for i in range(len(vertices)):
            j = (i + 1) % len(vertices)
            xi, yi = vertices[i]
            xj, yj = vertices[j]

            if point_on_segment(p, (xi, yi), (xj, yj)):
                memo.add(p)
                return True, memo

            if (yi > p[1]) != (yj > p[1]):
                x_int = ((p[1] - yi) * (xj - xi)) / (yj - yi) + xi
                if p[0] < x_int:
                    inside = not inside
    if inside:
        memo.add(p)
    return inside, memo


def segments_intersect(a, b, c, d):
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if o1 != o2 and o3 != o4:
        return True

    # if o1 == 0 and on_segment(a, c, b):
    #     return True
    # if o2 == 0 and on_segment(a, d, b):
    #     return True
    # if o3 == 0 and on_segment(c, a, d):
    #     return True
    # if o4 == 0 and on_segment(c, b, d):
    #     return True

    return False


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def on_segment(p, q, r):
    return max(p[0], r[0]) >= q[0] >= min(p[0], r[0]) and max(p[1], r[1]) >= q[1] >= min(p[1], r[1])


def part2(data):  # doesn't work
    data = list(map(lambda d: tuple(map(int, d.split(','))), data))
    max_area = 0
    max_shape = (0, 0)
    memo = set()
    for i, c1 in enumerate(data[:-1]):
        for j, c2 in enumerate(data[i+1:]):
            corners = [c1, c2, (c1[0], c2[1]), (c2[0], c1[1])]
            rect_inside = True
            print(f'rect: {i}, {j}')
            for corner in corners:
                inside, memo = point_inside_polygon(corner, data, memo)
                rect_inside = rect_inside and inside
            # for i_e in range(4):
            #     for j_e in range(len(data)):
            #         inside = not segments_intersect(corners[i_e], corners[(i_e + 1) % 4], data[j_e], data[(j_e + 1) % len(data)])
            #         rect_inside = rect_inside and inside
            if rect_inside:
                area = corner_area(c1, c2)
                if area > max_area:
                    max_area = area
                    max_shape = (c1, c2)
    print(max_shape)
    return max_area


if __name__ == "__main__":
    aoc = AOC(9)
    print(aoc.test(part1, part2))
    print(aoc.run(part1, part2))
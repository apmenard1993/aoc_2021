from input import get_input


test_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''


def parse_points_from_line(line, no_diag=False):
    points = []
    s, e = line.split(' -> ')
    s = [int(x) for x in s.split(',')]
    e = [int(x) for x in e.split(',')]

    if no_diag and (s[0] != e[0]) and (s[1] != e[1]):
        return points

    d0 = 1 if s[0] < e[0] else 0 if s[0] == e[0] else -1
    d1 = 1 if s[1] < e[1] else 0 if s[1] == e[1] else -1

    cx, cy = s[0], s[1]
    points.append((cx, cy))
    while cx != e[0] or cy != e[1]:
        cx += d0
        cy += d1
        points.append((cx, cy))

    return points


def print_all_lines(point_counts):
    min_x = min([point[0] for point in point_counts.keys()])
    min_y = min([point[1] for point in point_counts.keys()])
    max_x = max([point[0] for point in point_counts.keys()])
    max_y = max([point[1] for point in point_counts.keys()])
    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            line += str(point_counts[(x, y)]) if (x, y) in point_counts else '.'
        print(line)


def find_intersection_points(input, no_diag=False):
    lines = input.splitlines()
    point_counts = {}
    for line in lines:
        points = parse_points_from_line(line, no_diag)
        for point in points:
            if point in point_counts:
                point_counts[point] += 1
            else:
                point_counts[point] = 1
    # print_all_lines(point_counts)

    agg = 0
    for key, val in point_counts.items():
        if val >= 2:
            agg += 1
    print(agg)


if __name__ == '__main__':
    find_intersection_points(get_input(5), True)
    find_intersection_points(get_input(5))
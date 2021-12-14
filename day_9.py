import math
import statistics

from input import get_input

test_input = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''


def parse_input(raw_str):
    return [[int(n) for n in list(line)] for line in raw_str.splitlines()]


def low_points_horiz(line):
    return [(i, n) for i, n in enumerate(line) if
            (i == 0 or line[i - 1] > n) and ((i + 1) == len(line) or line[i + 1] > n)]


def is_all_low(i, j, v, all):
    higher = False
    for x in [i - 1, i + 1]:
        if x >= len(all) or x < 0:
            continue
        for y in [j - 1, j + 1]:
            if y >= len(all[x]) or y < 0:
                continue
            higher = v > all[x][y]
            if higher:
                return not higher
    return not higher


def is_vert_low(i, j, v, all):
    higher = False
    for x in [i - 1, i + 1]:
        if x >= len(all) or x < 0:
            continue
        higher = v > all[x][j]
        if higher:
            return not higher
    return not higher


def part_one(input):
    lph = [(index, low_points_horiz(line)) for index, line in enumerate(input)]
    out = []
    for first_index, lprow in lph:
        for second_index, lp in lprow:
            if is_vert_low(first_index, second_index, lp, input):
                out.append(lp)
    print(sum([x + 1 for x in out]))
    return sum([x + 1 for x in out])


def print_basin(basin, input):
    print(f'basin of length {len(basin)}')
    arr = []
    for x, line in enumerate(input):
        arr.append([])
        for y, v in enumerate(line):
            arr[x].append(str(input[x][y]) if (x, y) in basin else '*')
        print(arr[x])


def part_two(input):
    basins = []
    # start at low points
    lph = [(index, low_points_horiz(line)) for index, line in enumerate(input)]
    out = []
    for first_index, lprow in lph:
        for second_index, lp in lprow:
            if is_vert_low(first_index, second_index, lp, input):
                out.append((first_index, second_index, lp))

    for i, j, v in out:
        already = False
        for basin in basins:
            if (i, j) in basin:
                already = True
                break
        if already:
            continue
        b = fill_basin(i, j, input)
        basins.append(b)
    for basin in basins:
        print_basin(basin, input)
    basins = sorted(basins, key=lambda x: len(x))
    top_three = [len(x) for x in basins][-3:]
    print(math.prod(top_three))


def fill_basin(i, j, input):
    return recursive_fill_basin(i, j, input, [])


def recursive_fill_basin(x, y, input, current_basin):
    if x >= len(input) or x < 0 or y >= len(input[x]) or y < 0 or input[x][y] == 9:
        return current_basin

    for i, j in current_basin:
        if (x, y) == (i, j):
            return current_basin

    current_basin.append((x, y))
    up = recursive_fill_basin(x - 1, y, input, current_basin)
    down = recursive_fill_basin(x + 1, y, input, current_basin)
    left = recursive_fill_basin(x, y - 1, input, current_basin)
    right = recursive_fill_basin(x, y + 1, input, current_basin)
    return set(up).union(set(down)).union(set(left)).union(set(right))


if __name__ == '__main__':
    input = parse_input(test_input)
    part_one(input)
    part_two(input)
    input = parse_input(get_input(9))
    part_one(input)
    part_two(input)

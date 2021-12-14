import math
import statistics

from input import get_input

test_input = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''


def parse_input(raw_str):
    return [[int(x) for x in list(line)] for line in raw_str.splitlines()]


def get_surrounding(x, y, input_lines):
    surrounding = []
    xwid = len(input_lines)
    ywid = len(input_lines[0])
    positions = []
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            if (a, b) == (x, y):
                continue
            positions.append((a, b))

    for i, j in positions:
        if i < 0 or i >= xwid or j < 0 or j >= ywid:
            continue
        surrounding.append((i, j, input_lines[i][j]))
    return surrounding


def print_octomap(input, flashing):
    lines = ''
    for x, line in enumerate(input):
        for y, octo in enumerate(line):
            lines += ' '
            if (x, y) in flashing:
                lines += '\033[1m' + str(octo) + '\033[0m'
            else:
                lines += str(octo)
            lines += ' '
        lines += '\n'
    print(lines)


def part_one(input_lines, n_steps):
    flashes = 0
    print('Before Step 1')
    print_octomap(input_lines, [])
    for step in range(1, n_steps + 1):
        stack = []
        for x, line in enumerate(input_lines):
            stack.extend([(x, y, o) for y, o in enumerate(line)])
        already_flashed = []
        while stack:
            x, y, o = stack.pop()
            if (x, y) in already_flashed:
                continue
            if (o + 1) > 9:
                # add flash
                already_flashed.append((x, y))
                flashes += 1
                # add all surrounding to top of stack
                surrounding = get_surrounding(x, y, input_lines)
                stack.extend(surrounding)
                # set to 0
                input_lines[x][y] = 0
                for si, sx in enumerate(stack):
                    a, b, o = sx
                    if (a, b) == (x, y):
                        stack[si] = (a, b, 0)
            else:
                # increase o by one
                input_lines[x][y] += 1
                for si, sx in enumerate(stack):
                    a, b, o = sx
                    if (a, b) == (x, y):
                        stack[si] = (a, b, o + 1)
        print(f'After step {step}')
        print_octomap(input_lines, already_flashed)
        print('\n')
    print(flashes)



def part_two(input_lines):
    flashes = 0
    print('Before Step 1')
    print_octomap(input_lines, [])
    step = 0
    while True:
        stack = []
        for x, line in enumerate(input_lines):
            stack.extend([(x, y, o) for y, o in enumerate(line)])
        already_flashed = []
        while stack:
            x, y, o = stack.pop(0)
            if (x, y) in already_flashed:
                continue
            if (o + 1) > 9:
                # add flash
                already_flashed.append((x, y))
                flashes += 1
                # add all surrounding to top of stack
                surrounding = get_surrounding(x, y, input_lines)
                surrounding.extend(stack)
                stack = surrounding
                # set to 0
                input_lines[x][y] = 0
                for si, sx in enumerate(stack):
                    a, b, o = sx
                    if (a, b) == (x, y):
                        stack[si] = (a, b, 0)
            else:
                # increase o by one
                input_lines[x][y] += 1
                for si, sx in enumerate(stack):
                    a, b, o = sx
                    if (a, b) == (x, y):
                        stack[si] = (a, b, o + 1)
        print(f'After step {step}')
        print_octomap(input_lines, already_flashed)
        print('\n')
        step += 1
        if len(already_flashed) == (len(input_lines) * len(input_lines[0])):
            return step


if __name__ == '__main__':
    part_one(parse_input(test_input), 100)
    fstep = part_two(parse_input(test_input))
    print(fstep)
    part_one(parse_input(get_input(11)), 100)
    fstep = part_two(parse_input(get_input(11)))
    print(fstep)

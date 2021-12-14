import itertools

from input import get_input

test_input = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along x=5
fold along y=7
'''


def zip_longest(a, b):
    offset = abs(len(a) - len(b))
    zipped = []
    if len(a) > len(b):
        for i in range(len(a) - 1, -1, -1):
            zipped.append((a[i], b[i - offset]))
        zipped.reverse()
    elif len(b) > len(a):
        for i in range(len(b) - 1, -1, -1):
            zipped.append((a[i - offset], b[i]))
        zipped.reverse()
    else:
        for i in range(0, len(a)):
            zipped.append((a[i], b[i]))
    return zipped


def parse_input(raw_str):
    lines = raw_str.splitlines()
    fold_queue = []
    dots = []
    dots_raw = []
    for line in lines:
        if line:
            if line.startswith('fold'):
                l = line.split()
                dir, val = l[2].split('=')
                fold_queue.append((dir, int(val)))
            else:
                y,x = line.split(',')
                dots_raw.append((int(x), int(y)))

    mkey = max(dots_raw, key=lambda x: x[0])[0]
    mvalue = max(dots_raw, key=lambda x: x[1])[1]
    for i in range(0, mkey + 1):
        dots.append([False for _ in range(0, mvalue+1)])
    for key, value in dots_raw:
        dots[key][value] = True

    return dots, fold_queue


def print_dots_map(dots):
    strdots = ''
    for line in dots:
        for item in line:
            strdots += ' . ' if not item else ' # '
        strdots += '\n'
    print(strdots)


def perform_fold(dots, fold):
    dir, val = fold
    if dir == 'x':
        for i, line in enumerate(dots):
            lhs = line[0:val]
            rhs = line[val+1:]
            rhs.reverse()
            zipped = zip_longest(lhs, rhs)
            fin = [x or y for x, y in zipped]
            dots[i] = fin
    else:
        top = dots[0:val]
        bot = dots[val+1:]
        bot.reverse()
        zipped = zip_longest(top, bot)
        fin = []
        for i, j in zipped:
            if i is None:
                fin.append(j)
            elif j is None:
                fin.append(i)
            else:
                zl = list(zip_longest(i, j))
                fin.append([x or y for x, y in zl])
        dots.clear()
        dots.extend(fin)


def part_one(dots, fold_queue):
    for fold_count, fold in enumerate(fold_queue):
        print(f'Folding {fold[0]} on line {fold[1]}')
        perform_fold(dots, fold)
        # print_dots_map(dots)
        total = 0
        for line in dots:
            for i in line:
                total += 1 if i else 0
        print(f'Total dots left after folding {fold_count+1} is {total}')


if __name__ == '__main__':
    # dots, fold_queue = parse_input(test_input)
    # print_dots_map(dots)
    # print(fold_queue)
    # part_one(dots, fold_queue)

    dots, fold_queue = parse_input(get_input(13))
    s = 0
    for line in dots:
        s += sum([1 if i else 0 for i in line])
    print(s, len(dots), len(dots[0]))
    part_one(dots, fold_queue)
    print_dots_map(dots)
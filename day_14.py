import collections
import itertools

from input import get_input

test_input = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''

def parse_input(raw_string):
    lines = raw_string.splitlines()
    start = lines[0]
    insertion_map = {i.split(' -> ')[0] : i.split(' -> ')[1] for i in lines[2:]}
    return start, insertion_map


def part_one(start, insertion_map):
    l = [start[i] + start[i + 1] for i in range(0, len(start) - 1)]
    c = collections.Counter(l)

    for step in range(0,40):
        current = collections.Counter()
        for m, v in c.items():
            new = insertion_map[m]
            current[m[0] + new] += v
            current[new + m[1]] += v
        c = dict(current)

    totals = collections.Counter()

    for k, v in c.items():
        lhs = k[0]
        totals[lhs] += v
    totals[start[-1]] += 1
    print(start)
    print(c)
    mc = totals.most_common()
    print(mc)
    print(mc[0][1] - mc[-1][1])


if __name__ == '__main__':
    start, insertion_map = parse_input(test_input)
    part_one(start, insertion_map)
    start, insertion_map = parse_input(get_input(14))
    part_one(start, insertion_map)
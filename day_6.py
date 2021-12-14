import collections

from input import get_input

test_input = '3,4,3,1,2'


reset_to = 6
new_spawn = 8


def parse_input(raw_str):
    fish_map = {}
    for si in raw_str.split(','):
        i = int(si)
        if i not in fish_map:
            fish_map[i] = 1
        else:
            fish_map[i] += 1
    return fish_map


def sim(in_map, n_days):
    if n_days == 0:
        return in_map
    for _ in range(n_days,0, -1):
        in_map = collections.OrderedDict(sorted(in_map.items(), reverse=True))
        tmp_map = {}
        for k, v in in_map.items():
            if k == 0:
                if new_spawn not in tmp_map:
                    tmp_map[new_spawn] = v
                else:
                    tmp_map[new_spawn] += v
                if reset_to not in tmp_map:
                    tmp_map[reset_to] = v
                else:
                    tmp_map[reset_to] += v
            else:
                if k - 1 not in tmp_map:
                    tmp_map[k - 1] = v
                else:
                    tmp_map[k - 1] += v
        in_map = tmp_map.copy()
    return in_map


if __name__ == '__main__':
    input = parse_input(test_input)
    fish = sim(input, 256)
    print(sum([f for f in fish.values()]))

    input = parse_input(get_input(6))
    fish = sim(input, 256)
    print(sum([f for f in fish.values()]))
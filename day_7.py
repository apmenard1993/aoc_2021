import math
import statistics

from input import get_input

test_input = '16,1,2,0,4,2,7,1,2,14'

reset_to = 6
new_spawn = 8


def parse_input(raw_str):
    return [int(k) for k in raw_str.split(',')]


# part 1 -> median, part 2 -> mean with 1 to n sum


if __name__ == '__main__':
    input = parse_input(test_input)
    mean = math.ceil(statistics.mean(input))
    print(math.ceil(mean))
    print(sum([sum([j for j in range(0, abs(k - mean) + 1)]) for k in input]))
    input = parse_input(get_input(7))
    mean = math.floor(statistics.mean(input))
    print(math.floor(mean))
    print(sum([(abs(k - mean) * (abs(k - mean) + 1)) / 2 for k in input]))

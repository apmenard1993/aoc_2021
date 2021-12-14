import math
import statistics

from input import get_input

test_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

left_to_right = {'[': ']', '{': '}', '(': ')', '<': '>'}
part_one_points_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
part_two_points_map = {')': 1, ']': 2, '}': 3, '>': 4}

def parse_input(raw_str):
    return [line for line in raw_str.splitlines()]


def part_one(input_lines):
    curr_input = []
    corrupted_values = []
    for input in input_lines:
        for char in list(input):
            if not curr_input:
                curr_input.append(char)
                continue
            curr_char = curr_input.pop()
            if char in left_to_right.values():
                # right side
                if left_to_right[curr_char] == char:
                    # match, discard both and continue
                    pass
                else:
                    # no match, corrupt - save corrupted value and break
                    corrupted_values.append(char)
            else:
                # left side, keep current and save next
                curr_input.append(curr_char)
                curr_input.append(char)
    print(sum([part_one_points_map[i] for i in corrupted_values]))


def part_two(input_lines):
    curr_input = []
    corrupted_values = []
    corrupt_inputs = []
    for input in input_lines:
        for char in list(input):
            if not curr_input:
                curr_input.append(char)
                continue
            curr_char = curr_input.pop()
            if char in left_to_right.values():
                # right side
                if left_to_right[curr_char] == char:
                    # match, discard both and continue
                    pass
                else:
                    # no match, corrupt - save corrupted value and break
                    corrupt_inputs.append(input)
            else:
                # left side, keep current and save next
                curr_input.append(curr_char)
                curr_input.append(char)

    total_scores = []
    for input in input_lines:
        if input not in corrupt_inputs:
            unfinished_chars = []
            finishing_chars = []
            for char in list(input):
                if char in left_to_right.values():
                    unfinished_chars.pop()
                else:
                    unfinished_chars.append(char)
            while unfinished_chars:
                u = unfinished_chars.pop()
                finishing_chars.append(left_to_right[u])
            print(finishing_chars)
            total = 0
            for c in finishing_chars:
                total = total * 5
                total += part_two_points_map[c]
            print(total)
            total_scores.append(total)

    print(sorted(total_scores)[math.floor(len(total_scores)/2)])


if __name__ == '__main__':
    input = parse_input(test_input)
    # part_one(input)
    part_two(input)
    input = parse_input(get_input(10))
    # part_one(input)
    part_two(input)

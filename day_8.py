import math
import statistics

from input import get_input


tiny_input = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

test_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''


class DigitDisplay:
    def __init__(self, encoding, output):
        self.encoding = [list(n) for n in encoding.split(' ')]
        self.output = [list(n) for n in output.split(' ')]
        self.encoding_map = {}

    def __repr__(self):
        return f"{self.encoding} | {self.output}"

    def output_as_int(self):
        if not self.encoding_map:
            return None
        out_str = ''
        for num in self.output:
            num = list(num)
            num.sort()
            for k, v in self.encoding_map.items():
                if num == v:
                    out_str += k
                    break
        return int(out_str)


    def build_encoding_map(self):
        one = ''
        seven = ''
        four = ''
        eight = ''
        for d in self.encoding:
            d.sort()
            if len(d) == 2:
                one = d
            if len(d) == 3:
                seven = d
            if len(d) == 4:
                four = d
            if len(d) == 7:
                eight = d
        top = [n for n in seven if n not in one]
        left_and_middle = [n for n in four if n not in one]
        three = [n for n in self.encoding if len([x for x in n if x not in seven]) == 2 and n != four][0]
        top_left = [n for n in left_and_middle if n not in three]
        middle = [n for n in left_and_middle if n not in top_left]
        bottom = [n for n in three if n not in top and n not in middle and n not in one]
        six = ''
        five = ''
        two = ''
        for n in self.encoding:
            if len(n) == 5:
                if top_left[0] in n:
                    five = n
                elif bottom[0] in n and n != three:
                    two = n

        bottom_left = [n for n in eight if n not in five and n not in three]
        nine = [n for n in eight if n not in bottom_left]
        zero = [n for n in eight if n not in middle]
        for n in self.encoding:
            if len(n) == 6:
                if n != nine and n != zero:
                    six = n
            if len(n) == 5:
                if top_left[0] in n:
                    five = n
                elif bottom[0] in n and n != three:
                    two = n

        self.encoding_map = {
            '1': sorted(one),
            '2': sorted(two),
            '3': sorted(three),
            '4': sorted(four),
            '5': sorted(five),
            '6': sorted(six),
            '7': sorted(seven),
            '8': sorted(eight),
            '9': sorted(nine),
            '0': sorted(zero)
        }


def parse_input(raw_str):
    return [DigitDisplay(line.split(' | ')[0], line.split(' | ')[1]) for line in raw_str.splitlines()]


# part 1 -> median, part 2 -> mean with 1 to n sum


def unique_digits(input):
    total_unique = 0
    for digit in input:
        print(digit)
        for o in digit.output:
            if len(o) in [2, 3, 4, 7]:
                total_unique += 1
    print(total_unique)


if __name__ == '__main__':
    input = parse_input(tiny_input)
    for digit in input:
        digit.build_encoding_map()
        i = digit.output_as_int()
        print(i)

    input = parse_input(test_input)
    total = 0
    for digit in input:
        digit.build_encoding_map()
        i = digit.output_as_int()
        total += i
    print(total)

    input = parse_input(get_input(8))
    total = 0
    for digit in input:
        digit.build_encoding_map()
        i = digit.output_as_int()
        total += i
    print(total)
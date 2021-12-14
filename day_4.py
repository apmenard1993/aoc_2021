from input import get_input

test_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

'''



def split_and_clean_input(input):
    return input.splitlines(False)


class Board:
    def __init__(self, input_str_list=None):
        if input_str_list is None:
            self.rows = [[Node() for _ in range(0, 5)] for _ in range(0, 5)]
        else:
            self.rows = [[Node(v) for v in in_line.strip().split()] for in_line in input_str_list]

    def __repr__(self):
        return f"{self.rows}".replace('],', '],\n')

    def try_mark(self, value):
        for row in self.rows:
            for node in row:
                if node.value == value:
                    node.marked = True
                    return self.check_complete()
        return False

    def check_complete(self):
        for row in self.rows:
            if all(node.marked for node in row):
                return True

        for i in range(0, len(self.rows[0])):
            if all((row[i].marked for row in self.rows)):
                return True
        return False

    def sum_unmarked(self):
        sum = 0
        for row in self.rows:
            for node in row:
                if not node.marked:
                    sum += int(node.value)
        return sum


class Node:
    def __init__(self, value=None):
        self.value = value
        self.marked = False

    def __repr__(self):
        bold = '|'
        end = '|'
        return f"{bold if self.marked else ''}{self.value}{bold if self.marked else ''}"


def parse_boards(split_input):
    boards = []
    current_board = []
    for line in split_input[2:]:
        line = line.strip()
        if line == '' and current_board != []:
            boards.append(Board(current_board))
            current_board = []
            continue
        current_board.append(line)
    return boards


def sim_bingo(nums, in_boards, find_last=False):
    if not find_last:
        return sim_win_bingo(nums, in_boards)
    return simulate_loser_bingo(nums, in_boards)


def simulate_loser_bingo(nums, in_boards):
    survivor = None
    final_num = None
    winners = []
    for n in nums.split(','):
        for board in in_boards:
            if board in winners:
                continue
            done = board.try_mark(n)
            if done:
                winners.append(board)
                survivor = board
                final_num = n

    return survivor, final_num


def sim_win_bingo(nums, in_boards):
    winner = None
    final_num = None
    for n in nums.split(','):
        for board in in_boards:
            done = board.try_mark(n)
            if done:
                winner = board
                final_num = n
                return winner, final_num
    return winner, final_num


def run(split_input):
    numbers = split_input[0]

    boards = parse_boards(split_input)

    winning_board, final_number = sim_bingo(numbers, boards, True)
    win_sum = winning_board.sum_unmarked()

    print(winning_board)
    print(final_number)
    print(win_sum)
    print(win_sum * int(final_number))


if __name__ == '__main__':
    split_input_test = split_and_clean_input(test_input)
    run(split_input_test)
    input = get_input(4)
    run(split_and_clean_input(input))

import math
import statistics

from input import get_input

test_input = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''


def parse_input(raw_str):
    graph = {}
    for line in raw_str.splitlines():
        lhs, rhs = line.split('-')
        if lhs in graph:
            graph[lhs].append(rhs)
        else:
            graph[lhs] = [rhs]
        if rhs in graph and lhs not in graph[rhs]:
            graph[rhs].append(lhs)
        else:
            graph[rhs] = [lhs]
    return graph


def find_paths(graph, start, end, visited_small=False, path=None):
    if path is None:
        path = []
    if not visited_small and start == start.lower() and start != 'start' and start != 'end' and start in path:
        visited_small = True
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []

    for node in graph[start]:
        if node not in path or node == node.upper() or (
                node == node.lower() and not visited_small and node != 'start' and node != 'end'):
            newpaths = find_paths(graph, node, end, visited_small, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == '__main__':
    input = parse_input(test_input)
    print(input)
    paths = find_paths(input, 'start', 'end')
    print(len(paths))

    input = parse_input(get_input(12))
    print(len(find_paths(input, 'start', 'end')))
    # part_one(parse_input(test_input), 100)
    # fstep = part_two(parse_input(test_input))
    # print(fstep)
    # part_one(parse_input(get_input(11)), 100)
    # fstep = part_two(parse_input(get_input(11)))
    # print(fstep)

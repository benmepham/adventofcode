from argparse import ArgumentParser
from collections import defaultdict
from itertools import permutations

from aocd import data, submit


def part_a(data):
    grid = [list(row) for row in data.splitlines()]
    antennas = defaultdict(list)
    for pos_row, row in enumerate(grid):
        for pos_col, char in enumerate(row):
            if char.isalnum():
                antennas[char].append([pos_row, pos_col])

    locations = set()
    for antenna in antennas:
        combos = list(permutations(antennas[antenna], 2))
        for combo in combos:
            diff = [combo[0][0] - combo[1][0], combo[0][1] - combo[1][1]]
            loc = [combo[0][0] + diff[0], combo[0][1] + diff[1]]
            if (loc[0] >= 0 and loc[0] < len(grid) and loc[1] >=0 and loc[1] < len(grid[0])):
                locations.add(''.join(str(x) for x in loc))
    return len(locations)



def part_b(data):
    # more code here..
    return result


test_data = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('part', choices=['1', '2'])
    args = parser.parse_args()

    if args.part == '1':
        ans = part_a(test_data)
        print('test_data ans:', ans)
        assert ans == 14
        ans = part_a(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='a')

    elif args.part == '2':  
        ans = part_b(test_data)
        print('test_data ans:', ans)
        assert ans == 1
        ans = part_b(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='b')
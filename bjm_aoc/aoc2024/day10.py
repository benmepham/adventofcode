from argparse import ArgumentParser

from aocd import data, submit


def find_neighbour(cur, value, grid):
    neighbours = []
    next = str(int(value) + 1)
    row = cur[0]
    col = cur[1]
    if row + 1 < len(grid) and grid[row+1][col] == next:
        neighbours.append([row+1, col])
    if row - 1 >= 0 and grid[row-1][col] == next:
        neighbours.append([row-1, col])
    if col + 1 < len(grid[0]) and grid[row][col+1] == next:
        neighbours.append([row, col+1])
    if col - 1 >= 0 and grid[row][col-1] == next:
        neighbours.append([row, col-1])
    return neighbours


def find_path(loc, value, grid, ignore_visited):
    score = 0
    visited = set()
    queue = []
    queue.append(loc)
    while queue:
        cur = queue.pop()
        rep = ','.join(str(x) for x in cur)
        if rep in visited and not ignore_visited:
            continue
        visited.add(rep)
        value = grid[cur[0]][cur[1]]
        if value == '9':
            score +=1
            continue
        queue.extend(find_neighbour(cur, value, grid))
    return score


def part_a(data):
    grid = [list(row) for row in data.splitlines()]
    trail_heads = []
    for pos_row, row in enumerate(grid):
        for pos_col, col in enumerate(row):
            if col == '0':
                trail_heads.append([pos_row, pos_col])
    total = 0
    for trail_head in trail_heads:
        total += find_path(trail_head, '0', grid)
    return total


def part_b(data):
    grid = [list(row) for row in data.splitlines()]
    trail_heads = []
    for pos_row, row in enumerate(grid):
        for pos_col, col in enumerate(row):
            if col == '0':
                trail_heads.append([pos_row, pos_col])
    total = 0
    for trail_head in trail_heads:
        total += find_path(trail_head, '0', grid, True)
    return total


test_data = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('part', choices=['1', '2'])
    args = parser.parse_args()

    if args.part == '1':
        ans = part_a(test_data)
        print('test_data ans:', ans)
        assert ans == 36
        ans = part_a(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='a')

    elif args.part == '2':  
        ans = part_b(test_data)
        print('test_data ans:', ans)
        assert ans == 81
        ans = part_b(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='b')
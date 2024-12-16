from aocd import data, submit

def get_next(pos, pos_row, pos_col):
    if pos == '^':
        return [pos_row - 1, pos_col]
    if pos == '>':
        return [pos_row, pos_col + 1]   
    if pos == 'v':
        return [pos_row + 1, pos_col] 
    if pos == '<':
        return [pos_row, pos_col - 1]
    raise Exception('unknown direction')

def validate_pos(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    return True

next_rotate = {'>': 'v', 'v': '<', '<': '^', '^': '>'}

def part_a(data):
    grid = [list(row) for row in data.splitlines()]
    pos_row = 0
    pos_col = 0
    visited_set = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^' or grid[i][j] == '>' or grid[i][j] == 'v' or grid[i][j] == '<':
                pos_row = i
                pos_col = j   
    while True:
        visited_set.add(''.join(str(x) + ',' for x in [pos_row, pos_col]))
        pos = grid[pos_row][pos_col]
        next_row, next_col = get_next(pos, pos_row, pos_col)
        if not validate_pos(grid, next_row, next_col):
            return len(visited_set)
        if grid[next_row][next_col] == '#':
            grid[pos_row][pos_col] = next_rotate[pos]
            continue
        grid[next_row][next_col] = str(pos)
        pos_row = next_row
        pos_col = next_col


def part_b(data):
    # more code here..
    return result


test_data = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 41
    # part_a_ans = part_a(data)
    # print(part_a_ans)
    # input("Submit?")
    # submit(part_a_ans, part='a')  
  
    assert part_b(test_data) == 2
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part='b')
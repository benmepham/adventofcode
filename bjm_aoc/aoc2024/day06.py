from aocd import data, submit


def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (
                grid[i][j] == "^"
                or grid[i][j] == ">"
                or grid[i][j] == "v"
                or grid[i][j] == "<"
            ):
                return i, j


def get_next(pos, pos_row, pos_col):
    if pos == "^":
        return [pos_row - 1, pos_col]
    if pos == ">":
        return [pos_row, pos_col + 1]
    if pos == "v":
        return [pos_row + 1, pos_col]
    if pos == "<":
        return [pos_row, pos_col - 1]
    raise Exception("unknown direction")


def validate_pos(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    return True


def take_step(grid, pos_row, pos_col):
    next_row, next_col = get_next(grid[pos_row][pos_col], pos_row, pos_col)
    if not validate_pos(grid, next_row, next_col):
        return None, None
    while grid[next_row][next_col] == "#":
        grid[pos_row][pos_col] = next_rotate[grid[pos_row][pos_col]]
        next_row, next_col = get_next(grid[pos_row][pos_col], pos_row, pos_col)
    grid[next_row][next_col] = str(grid[pos_row][pos_col])
    return next_row, next_col


next_rotate = {">": "v", "v": "<", "<": "^", "^": ">"}


def part_a(data):
    grid = [list(row) for row in data.splitlines()]
    visited_set = set()
    pos_row, pos_col = find_guard(grid)
    while pos_row:
        visited_set.add("".join(str(x) + "," for x in [pos_row, pos_col]))
        pos_row, pos_col = take_step(grid, pos_row, pos_col)
    return len(visited_set)


def part_b(data):
    grid = [list(row) for row in data.splitlines()]
    visited_set = set()
    pos_row, pos_col = find_guard(grid)
    guard_row, guard_col = pos_row, pos_col
    while pos_row:
        visited_set.add("".join(str(x) + "," for x in [pos_row, pos_col]))
        pos_row, pos_col = take_step(grid, pos_row, pos_col)

    loops = 0
    for visited in visited_set:
        block_row, block_col = [int(x) for x in visited.split(",")[:-1]]
        if block_row == guard_row and block_col == guard_col:
            continue
        new_grid = [list(row) for row in data.splitlines()]
        new_grid[block_row][block_col] = "#"
        pos_row, pos_col = guard_row, guard_col
        steps, limit = 0, 10000
        while pos_row and steps < limit:
            pos_row, pos_col = take_step(new_grid, pos_row, pos_col)
            steps += 1
        if steps == limit:
            loops += 1
    return loops


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

    assert part_b(test_data) == 6
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part="b")

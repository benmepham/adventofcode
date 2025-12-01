from aocd import data, submit


def part_a(data):
    data = data.splitlines()
    grid = [list(row) for row in data]
    total = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "X":
                # north
                if (
                    i >= 3
                    and grid[i - 1][j] == "M"
                    and grid[i - 2][j] == "A"
                    and grid[i - 3][j] == "S"
                ):
                    total += 1
                # north east
                if (
                    i >= 3
                    and j < len(grid[i]) - 3
                    and grid[i - 1][j + 1] == "M"
                    and grid[i - 2][j + 2] == "A"
                    and grid[i - 3][j + 3] == "S"
                ):
                    total += 1
                # east
                if (
                    j < len(grid[i]) - 3
                    and grid[i][j + 1] == "M"
                    and grid[i][j + 2] == "A"
                    and grid[i][j + 3] == "S"
                ):
                    total += 1
                # s e
                if (
                    i < len(grid[i]) - 3
                    and j < len(grid[i]) - 3
                    and grid[i + 1][j + 1] == "M"
                    and grid[i + 2][j + 2] == "A"
                    and grid[i + 3][j + 3] == "S"
                ):
                    total += 1
                # south
                if (
                    i < len(grid[i]) - 3
                    and grid[i + 1][j] == "M"
                    and grid[i + 2][j] == "A"
                    and grid[i + 3][j] == "S"
                ):
                    total += 1
                # s w
                if (
                    i < len(grid[i]) - 3
                    and j >= 3
                    and grid[i + 1][j - 1] == "M"
                    and grid[i + 2][j - 2] == "A"
                    and grid[i + 3][j - 3] == "S"
                ):
                    total += 1
                # west
                if (
                    j >= 3
                    and grid[i][j - 1] == "M"
                    and grid[i][j - 2] == "A"
                    and grid[i][j - 3] == "S"
                ):
                    total += 1
                # n w
                if (
                    i >= 3
                    and j >= 3
                    and grid[i - 1][j - 1] == "M"
                    and grid[i - 2][j - 2] == "A"
                    and grid[i - 3][j - 3] == "S"
                ):
                    total += 1
    return total


def part_b(data):
    data = data.splitlines()
    grid = [list(row) for row in data]
    total = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "A":
                if (
                    i > 0
                    and i < len(grid) - 1
                    and j > 0
                    and j < len(grid[i]) - 1
                    and grid[i - 1][j - 1] == "M"
                    and grid[i - 1][j + 1] == "M"
                    and grid[i + 1][j - 1] == "S"
                    and grid[i + 1][j + 1] == "S"
                ):
                    total += 1
                if (
                    i > 0
                    and i < len(grid) - 1
                    and j > 0
                    and j < len(grid[i]) - 1
                    and grid[i - 1][j - 1] == "M"
                    and grid[i - 1][j + 1] == "S"
                    and grid[i + 1][j - 1] == "M"
                    and grid[i + 1][j + 1] == "S"
                ):
                    total += 1
                if (
                    i > 0
                    and i < len(grid) - 1
                    and j > 0
                    and j < len(grid[i]) - 1
                    and grid[i - 1][j - 1] == "S"
                    and grid[i - 1][j + 1] == "S"
                    and grid[i + 1][j - 1] == "M"
                    and grid[i + 1][j + 1] == "M"
                ):
                    total += 1
                if (
                    i > 0
                    and i < len(grid) - 1
                    and j > 0
                    and j < len(grid[i]) - 1
                    and grid[i - 1][j - 1] == "S"
                    and grid[i - 1][j + 1] == "M"
                    and grid[i + 1][j - 1] == "S"
                    and grid[i + 1][j + 1] == "M"
                ):
                    total += 1
    return total


test_data = """\
some example test data
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 1
    # part_a_ans = part_a(data)
    # print(part_a_ans)
    # input("Submit?")
    # submit(part_a_ans, part='a')

    # assert part_b(test_data) == 2
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part="b")

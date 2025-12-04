from aocd import data, submit
from argparse import ArgumentParser


def check_accessible(grid: list[list[str]], i: int, j: int):
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue
            if grid[x][y] == "@":
                count += 1
    return count


def part_a(data):
    rows = data.split("\n")
    grid = [list(row) for row in rows]
    accessible = 0
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            if col == "@" and check_accessible(grid, i, j) < 4:
                accessible += 1
    return accessible


def update_accessible(grid: list[list[str]], i: int, j: int, accessible_dict):
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                continue
            key = f"{x},{y}"
            if key in accessible_dict:
                accessible_dict[key] = accessible_dict[key] - 1


def part_b(data):
    rows = data.split("\n")
    grid = [list(row) for row in rows]
    accessible_dict = {}

    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            if col == "@":
                count = check_accessible(grid, i, j)
                accessible_dict[f"{i},{j}"] = count
    initial_size = len(accessible_dict)

    while True:
        no_updates = True
        for k in list(accessible_dict):
            if accessible_dict[k] >= 4:
                continue
            no_updates = False
            pos = [int(x) for x in k.split(",")]
            update_accessible(grid, pos[0], pos[1], accessible_dict)
            del accessible_dict[k]
        if no_updates:
            print(accessible_dict)
            break
    return initial_size - len(accessible_dict)


test_data = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 13
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 43
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

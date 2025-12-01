from argparse import ArgumentParser

from aocd import data, submit


def part_a(data):
    locks = []
    keys = []
    for item in data.split("\n\n"):
        pin_heights = [0, 0, 0, 0, 0]
        item_grid = [list(row) for row in item.splitlines()]
        for i in range(1, 6):
            for j in range(5):
                if item_grid[i][j] == "#":
                    pin_heights[j] += 1

        if item[0] == "#":
            locks.append(pin_heights)
        else:
            keys.append(pin_heights)

    total = 0
    for lock in locks:
        for key in keys:
            count = 0
            for i in range(5):
                if lock[i] + key[i] <= 5:
                    count += 1
            if count == 5:
                total += 1
    return total


test_data = """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 3
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

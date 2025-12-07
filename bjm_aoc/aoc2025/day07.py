from argparse import ArgumentParser

from aocd import data, submit


def part_a(data):
    data = data.split("\n")
    row_is_beam = [False if x == "." else True for x in data[0]]
    splits = 0
    for row in data:
        for x in range(1, len(row_is_beam)):
            if row[x] == "^" and row_is_beam[x]:
                splits += 1
                row_is_beam[x - 1] = True
                row_is_beam[x + 1] = True
                row_is_beam[x] = False
    return splits


def part_b(data):
    data = data.split("\n")
    row_beam_count = [0 if x == "." else 1 for x in data[0]]
    for row in data:
        for x in range(1, len(row_beam_count)):
            if row[x] == "^":
                row_beam_count[x - 1] += row_beam_count[x]
                row_beam_count[x + 1] += row_beam_count[x]
                row_beam_count[x] = 0
    return sum(row_beam_count)


test_data = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 21
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 40
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

import re
from argparse import ArgumentParser

from aocd import data, submit


def part_a(data):
    data = data.split("\n\n")
    fresh_ranges = data[0].split("\n")
    ids = data[1].split("\n")
    fresh = 0
    for id in ids:
        for range in fresh_ranges:
            range = range.split("-")
            if int(id) >= int(range[0]) and int(id) <= int(range[1]):
                fresh += 1
                break
    return fresh


def part_b(data):
    fresh_ranges = list(list(map(int, line.split('-'))) for line in data.split('\n\n')[0].split('\n'))
    total = 0
    last_upper = 0
    print(sorted(fresh_ranges))
    for lower, upper in sorted(fresh_ranges):
        if upper <= last_upper:
            continue
        total += upper - max(lower, last_upper + 1) + 1
        last_upper = max(upper, last_upper)
    return total


test_data = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


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

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 14
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

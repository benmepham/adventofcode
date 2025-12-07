import math
from argparse import ArgumentParser

from aocd import data, submit


def part_a(data):
    total = 0
    data = data.split("\n")
    data = [list(filter(lambda x: x != "", line.split(" "))) for line in data]
    data = [list(x) for x in zip(*data[::-1])]
    for col in data:
        op = col.pop(0)
        col = [int(x) for x in col]
        if op == "+":
            total += sum(col)
        else:
            total += math.prod(col)
    return total


# todo: optimise this
def part_b(data):
    total = 0
    data = data.split("\n")
    grid = []
    prev = 0
    for x in range(0, len(data[0])):
        if all(row[x] == " " for row in data):
            grid.append([row[prev:x] for row in data])
            prev = x + 1
    grid.append([row[prev:] for row in data])

    for col in grid:
        op = col.pop().strip()
        numbers = []
        for x in range(0, len(col[0])):
            numbers.append(int("".join([num[x] for num in col if num[x] != " "])))
        if op == "+":
            total += sum(numbers)
        else:
            total += math.prod(numbers)
    return total


test_data = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +   """


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 4277556
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 3263827
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

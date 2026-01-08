from aocd import data, submit
from argparse import ArgumentParser


def part_a(data):
    data = [[int(x) for x in row.split(",")] for row in data.split("\n")]
    largest_area = 0
    for first_point in data:
        for second_point in data:
            area = (abs(first_point[0] - second_point[0]) + 1) * (abs(first_point[1] - second_point[1]) + 1)
            if area > largest_area:
                largest_area = area
    return largest_area


def part_b(data):
    # more code here..
    return result


test_data = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 50
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 1
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

from aocd import data, submit
from argparse import ArgumentParser
import re


def part_a(data):
    position = 50
    zero_count = 0
    for row in data.split("\n"):
        [direction, number] = re.findall("([RL])(\d+)", row)[0]
        if direction == "L":
            position -= int(number)
        else:
            position += int(number)
        if position % 100 == 0:
            zero_count += 1
    return zero_count


# todo: revisit to get rid of nested for loop
def part_b(data):
    position = 50
    zero_count = 0
    for row in data.split("\n"):
        [direction, number] = re.findall("([RL])(\d+)", row)[0]
        for _ in range(1, int(number) + 1):
            if direction == "L":
                position -= 1
            else:
                position += 1
            if position % 100 == 0:
                zero_count += 1
    return zero_count


test_data = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


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
        assert ans == 6
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

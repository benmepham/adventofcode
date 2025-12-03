from aocd import data, submit
from argparse import ArgumentParser
from itertools import combinations


def part_a(data):
    total = 0
    for battery_bank in data.split("\n"):
        battery_bank = list(battery_bank)
        high_num = 0
        for x in range(0, len(battery_bank) - 1):
            for y in range(x + 1, len(battery_bank)):
                num = int(battery_bank[x] + battery_bank[y])
                if num > high_num:
                    high_num = num
        total += high_num
    return total


def find_max(array: list[str], start: int, end: int):
    max = 0
    max_pos = 0
    for x in range(start, end):
        if int(array[x]) > max:
            max = int(array[x])
            max_pos = x
    return max, max_pos


def part_b(data):
    total = 0
    for battery_bank in data.split("\n"):
        start_pos = 0
        batteries = ""
        for _ in range(0, 12):
            max, max_pos = find_max(
                battery_bank, start_pos, len(battery_bank) - 12 + 1 + len(batteries)
            )
            batteries += str(max)
            start_pos = max_pos + 1
        total += int(batteries)
    return total


test_data = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 357
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 3121910778619
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

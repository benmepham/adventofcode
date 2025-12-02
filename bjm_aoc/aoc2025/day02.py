from aocd import data, submit
from argparse import ArgumentParser


def part_a(data):
    incorrect = 0
    for pair in data.split(","):
        ids = pair.split("-")
        for id in range(int(ids[0]), int(ids[1]) + 1):
            first, second = (
                str(id)[: len(str(id)) // 2 + len(str(id)) % 2],
                str(id)[len(str(id)) // 2 + len(str(id)) % 2 :],
            )
            if first == second:
                incorrect += id
    return incorrect


# todo: revisit to get rid of nested for loop
def part_b(data):
    incorrect = 0
    for pair in data.split(","):
        ids = pair.split("-")
        for id in range(int(ids[0]), int(ids[1]) + 1):
            id_str = str(id)
            for part_size in range(len(str(id)) // 2, 0, -1):
                first_part = id_str[0:part_size]
                matching = True
                for i in range(part_size, len(id_str), part_size):
                    if id_str[i : i + part_size] != first_part:
                        matching = False
                        break
                if matching:
                    incorrect += id
                    break
    return incorrect


test_data = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        assert ans == 1227775554
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 4174379265
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

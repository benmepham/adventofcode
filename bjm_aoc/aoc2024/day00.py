from aocd import data, submit
from argparse import ArgumentParser

def part_a(data):
    # your code here..
    return result


def part_b(data):
    # more code here..
    return result


test_data = """\
some example test data
"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('part', choices=['1', '2'])
    args = parser.parse_args()

    if args.part == '1':
        ans = part_a(test_data)
        print('test_data ans:', ans)
        assert ans == 1
        ans = part_a(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='a')

    elif args.part == '2':  
        ans = part_b(test_data)
        print('test_data ans:', ans)
        assert ans == 1
        ans = part_b(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='b')
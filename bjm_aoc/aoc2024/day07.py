from aocd import data, submit
from itertools import product
from argparse import ArgumentParser

def part_a(data):
    data = data.splitlines()
    total = [int(x.split(':')[0]) for x in data]
    num_groups = [x.split(' ')[1:] for x in data]
    ans = 0
    for i, nums in enumerate(num_groups):
        op_groups = list(product(['*', '+'], repeat=len(nums)-1))
        for ops in op_groups:
            ops = list(ops)
            ops.append(' ')
            new = [x for z in zip(nums, ops) for x in z]
            new.pop()
            result = new.pop(0)
            while len(new) != 0:
                result = eval(f"{result} {new.pop(0)} {new.pop(0)}")
            if result == total[i]:
                ans+=result
                break
    return ans


# todo: this takes multiple minutes, look at a recursive solution
def part_b(data):
    data = data.splitlines()
    total = [int(x.split(':')[0]) for x in data]
    num_groups = [x.split(' ')[1:] for x in data]
    ans = 0
    for i, nums in enumerate(num_groups):
        op_groups = list(product(['*', '+', '|'], repeat=len(nums)-1))
        for ops in op_groups:
            ops = list(ops)
            ops.append(' ')
            new = [x for z in zip(nums, ops) for x in z]
            new.pop()
            result = new.pop(0)
            while len(new) != 0:
                op = new.pop(0)
                next = new.pop(0)
                if op == '|':
                    result = int(str(result) + str(next))
                else:   
                    result = eval(f"{result} {op} {next}")
            if result == total[i]:
                ans+=result
                break
    return ans


test_data = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('part', choices=['1', '2'])
    args = parser.parse_args()

    if args.part == '1':
        ans = part_a(test_data)
        print('test_data ans:', ans)
        assert ans == 3749
        ans = part_a(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER)")
        if resp == 'y':
            submit(ans, part='a')

    elif args.part == '2':  
        ans = part_b(test_data)
        print('test_data ans:', ans)
        assert ans == 11387
        ans = part_b(data)
        print('ans:', ans)
        resp = input("Submit? (y/ENTER): ")
        if resp == 'y':
            submit(ans, part='b')
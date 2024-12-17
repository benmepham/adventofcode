from aocd import data, submit
from itertools import product


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


def part_b(data):
    # more code here..
    return result


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
    assert part_a(test_data) == 3749
    part_a_ans = part_a(data)
    print(part_a_ans)
    input("Submit?")
    submit(part_a_ans, part='a')  
  
    # assert part_b(test_data) == 2
    # part_b_ans = part_b(data)
    # print(part_b_ans)
    # input("Submit?")
    # submit(part_b_ans, part='b')
from aocd import data, submit


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
    assert part_a(test_data) == 1
    part_a_ans = part_a(data)
    print(part_a_ans)
    input("Submit?")
    submit(part_a_ans, part='a')  
  
    # assert part_b(test_data) == 2
    # part_b_ans = part_b(data)
    # print(part_b_ans)
    # input("Submit?")
    # submit(part_b_ans, part='b')
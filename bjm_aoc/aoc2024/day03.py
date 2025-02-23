from aocd import data, submit
import re


def part_a(data):
    result = re.findall(r"mul\((\d+),(\d+)\)", data)
    total = 0
    for operation in result:
        total += int(operation[0])*int(operation[1])
    return total


def part_b(data):
    data += "do()"
    data = re.sub(r"don't\(\)[\s\S]*?do\(\)", '', data)
    result = re.findall(r"mul\((\d+),(\d+)\)", data)
    total = 0
    for operation in result:
        total += int(operation[0])*int(operation[1])
    return total


test_data_a = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


test_data_b = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


if __name__ == "__main__":
    # assert part_a(test_data_a) == 1
    part_a_ans = part_a(data)
    print(part_a_ans)
    input("Submit?")
    submit(part_a_ans, part='a')  
  
    # assert part_b(test_data_b) == 2
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part='b')
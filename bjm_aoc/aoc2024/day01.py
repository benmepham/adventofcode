from aocd import data, submit


def part_a(data):
    arr1 = []
    arr2 = []
    total = 0

    for line in data.splitlines():
        if not line:
            continue
        nums = [int(x) for x in line.split("   ")]
        arr1.append(nums[0])
        arr2.append(nums[1])

    arr1.sort()
    arr2.sort()

    for a, b in zip(arr1, arr2):
        total+=abs(a-b)
    return total


def part_b(data):
    arr1 = []
    arr2 = []
    total = 0

    for line in data.splitlines():
        if not line:
            continue
        nums = [int(x) for x in line.split("   ")]
        arr1.append(nums[0])
        arr2.append(nums[1])

    arr1.sort()
    arr2.sort()

    total_pt2 = 0
    for a in arr1:
        total_pt2 += a * arr2.count(a)

    return total_pt2


test_data = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 1
    part_a_ans = part_a(data)
    print(part_a_ans)
    input("Submit?")
    submit(part_a_ans, part='a')  
  
    # assert part_b(test_data) == 2
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part='b')
from aocd import data, submit
import functools


def part_a(data):
    arr = [int(n) for n in data.split()]
    for i in range(25):
        j = 0
        while j < len(arr):
            if arr[j] == 0:
                arr[j] = 1
            elif len(str(arr[j])) % 2 == 0:
                temp = str(arr[j])
                arr[j] = int(temp[: int(len(temp) / 2)])
                arr.insert(j + 1, int(temp[int(len(temp) / 2) :]))
                j = j + 1
            else:
                arr[j] = arr[j] * 2024
            j = j + 1
    return len(arr)


@functools.cache
def solve_item(item, iters):
    if iters == 0:
        return 1
    elif item == "0":
        return solve_item("1", iters - 1)
    elif len(item) % 2 == 0:
        middle = int(len(item) / 2)
        return solve_item(item[:middle], iters - 1) + solve_item(
            str(int(item[middle:])), iters - 1
        )
    return solve_item(str(int(item) * 2024), iters - 1)


def part_b(data):
    return sum(solve_item(item, 75) for item in data.split())


test_data = """\
125 17
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 55312
    # part_a_ans = part_a(data)
    # print(part_a_ans)
    # input("Submit?")
    # submit(part_a_ans, part='a')

    # assert part_b(test_data) == 1
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part="b")

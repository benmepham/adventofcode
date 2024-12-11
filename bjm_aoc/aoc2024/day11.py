from aocd import data, submit


def part_a(data):
    arr = [int(n) for n in data.split()]
    for i in range(25):
        j = 0
        while j < len(arr):
            if arr[j] == 0:
                arr[j] = 1
            elif len(str(arr[j])) % 2 ==0:
                temp = str(arr[j])
                arr[j] = int(temp[:int(len(temp)/2)])
                arr.insert(j+1, int(temp[int(len(temp)/2):]))
                j = j + 1
            else:
                arr[j] = arr[j] * 2024
            j = j+1
    return len(arr)


def part_b(data):
    # more code here..
    return result


test_data = """\
125 17
"""


if __name__ == "__main__":
    assert part_a(test_data) == 55312
    part_a_ans = part_a(data)
    print(part_a_ans)
    input("Submit?")
    submit(part_a_ans, part='a')  
  
    # assert part_b(test_data) == 1
    # part_b_ans = part_b(data)
    # print(part_b_ans)
    # input("Submit?")
    # submit(part_b_ans, part='b')
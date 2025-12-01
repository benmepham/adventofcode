from aocd import data, submit


def check_list(items):
    for i in range(len(items) - 1):
        if not (items[i + 1] - items[i] >= 1 and items[i + 1] - items[i] <= 3):
            return False
    return True


def part_a(data):
    reports = data.splitlines()
    result = 0
    for report in reports:
        if not report:
            continue
        report_items = [int(i) for i in report.split(" ")]
        if report_items[1] < report_items[0]:
            report_items.reverse()
        if check_list(report_items):
            result += 1
    return result


def check_all_list(items):
    for i in range(2):
        if check_list(items):
            return True
        for i in range(0, len(items)):
            if check_list(items[:i] + items[i + 1 :]):
                return True
        items.reverse()
    return False


def part_b(data):
    reports = data.splitlines()
    result = 0
    for report in reports:
        if not report:
            continue
        report_items = [int(i) for i in report.split(" ")]
        if check_all_list(report_items):
            result += 1
    return result


test_data = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 1
    # part_a_ans = part_a(data)
    # print(part_a_ans)
    # input("Submit?")
    # submit(part_a_ans, part='a')

    # assert part_b(test_data) == 2
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part="b")

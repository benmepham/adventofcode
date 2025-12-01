from aocd import data, submit


def parse_data(data):
    data = data.split("\n\n")
    page_groups = [pages.split(",") for pages in data[1].splitlines()]
    rules = {}
    for rule in data[0].splitlines():
        split = rule.split("|")
        if not split[0] in rules:
            rules[split[0]] = []
        rules[split[0]].append(split[1])
    return page_groups, rules


def part_a(data):
    page_groups, rules = parse_data(data)

    result = 0
    for pages in page_groups:
        valid = True
        for i, page in enumerate(pages):
            if not page in rules.keys():
                continue
            for post in rules[page]:
                if post in pages[:i]:
                    valid = False
        if valid:
            result += int(pages[len(pages) // 2])
    return result


def create_new(pages, rules):
    new = []
    new.append(pages[0])
    for item in pages[1:]:
        min_index = 1000000
        if item in rules.keys():
            for post in rules[item]:
                if post in new:
                    if new.index(post) < min_index:
                        min_index = new.index(post)
        if min_index != 1000000:
            new.insert(min_index, item)
        else:
            new.append(item)
    return new


def part_b(data):
    page_groups, rules = parse_data(data)

    result = 0
    for pages in page_groups:
        valid = True
        for i, page in enumerate(pages):
            if not page in rules.keys():
                continue
            for post in rules[page]:
                if post in pages[:i]:
                    valid = False
        if not valid:
            pages_new = create_new(pages, rules)
            result += int(pages_new[len(pages_new) // 2])
    return result


test_data = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 143
    # part_a_ans = part_a(data)
    # print(part_a_ans)
    # input("Submit?")
    # submit(part_a_ans, part='a')

    assert part_b(test_data) == 123
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part="b")

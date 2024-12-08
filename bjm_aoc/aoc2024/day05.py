from aocd import data


def part_a(data):
    data = data.split('\n\n')
    rules = data[0].splitlines()
    pagesets = data[1].splitlines()
    rulesdict = {}
    for rule in rules:
        split = rule.split('|')
        if not split[0] in rulesdict:
            rulesdict[split[0]] = []
        rulesdict[split[0]].append(split[1])
    print(rulesdict)
    pagesetsf = [pages.split(',') for pages in pagesets]
    print(pagesetsf)
    result = []
    for pages in pagesetsf:
        valid = 1
        for page in pages:
            if page in rulesdict:
                valid = 0
        if valid == 1:
            result.append(pages[(len(pages) -1 )/2])

    print(result)
    return result


def part_b(data):
    # more code here..
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
    assert part_a(test_data) == "expected test result a"
    assert part_b(test_data) == "expected test result b"
    print(part_a(data))
    print(part_b(data))

from argparse import ArgumentParser
from itertools import combinations
from math import dist, prod

from aocd import data, submit

# I got a little stuck on this one. Found this link helpful: https://aoc.winslowjosiah.com/solutions/2025/day/8/


class DisjointSet:
    def __init__(self, items):
        self.parent = {str(item): str(item) for item in items}
        self.size = {str(item): 1 for item in items}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1, item2):
        root1, root2 = self.find(item1), self.find(item2)
        if root1 == root2:
            return
        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        del self.size[root2]

    @property
    def sizes(self) -> list[int]:
        return list(self.size.values())


def part_a(data):
    boxes = [[int(x) for x in row.split(",")] for row in data.split("\n")]
    edges = sorted(combinations(boxes, 2), key=lambda pair: dist(*pair))

    disjoint_set = DisjointSet(boxes)
    num_initial_pairs = 1000  # 10 for test
    for item1, item2 in edges[:num_initial_pairs]:
        disjoint_set.union(str(item1), str(item2))

    return prod(sorted(disjoint_set.sizes, reverse=True)[:3])


def part_b(data):
    boxes = [[int(x) for x in row.split(",")] for row in data.split("\n")]
    edges = sorted(combinations(boxes, 2), key=lambda pair: dist(*pair))

    disjoint_set = DisjointSet(boxes)
    for item1, item2 in edges:
        disjoint_set.union(str(item1), str(item2))
        if len(disjoint_set.sizes) == 1:
            return item1[0] * item2[0]


test_data = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    args = parser.parse_args()

    if args.part == "1":
        ans = part_a(test_data)
        print("test_data ans:", ans)
        # assert ans == 1
        ans = part_a(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="a")

    elif args.part == "2":
        ans = part_b(test_data)
        print("test_data ans:", ans)
        assert ans == 25272
        ans = part_b(data)
        print("ans:", ans)
        resp = input("Submit? (y/ENTER)")
        if resp == "y":
            submit(ans, part="b")

"""A plausible formula that counts some cases twice, caught by building the collection.
"""
from itertools import combinations

from dmkit.counting import enumerate_check, report_count

people = list("abcde")


def committees_with_a_chair(group, size):
    """Every committee of the given size, paired with one of its members as chair."""
    return [(tuple(c), chair) for c in combinations(group, size) for chair in c]


def by_choosing_the_chair_first(n, size):
    """Pick the chair, then fill the rest: n times the ways to choose the others."""
    from math import comb
    return n * comb(n - 1, size - 1)


def by_choosing_twice(n, size):
    """A plausible route: pick the chair, then pick the whole committee around them."""
    from math import comb
    return n * comb(n, size - 1)


print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
for size in (2, 3, 4):
    print(report_count(enumerate_check(
        by_choosing_the_chair_first(len(people), size),
        lambda s=size: committees_with_a_chair(people, s),
        f"committee of {size} with a chair")))
for size in (2, 3, 4):
    print(report_count(enumerate_check(
        by_choosing_twice(len(people), size),
        lambda s=size: committees_with_a_chair(people, s),
        f"the same by the second route, {size}")))

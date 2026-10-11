"""One collection, counted by every rule of the day and checked against itself."""
from itertools import combinations, combinations_with_replacement, permutations, product

from dmkit.combin import (binomial, combinations_count, combinations_with_repetition,
                          distinct_arrangements, multiset_permutations,
                          permutations_count)
from dmkit.counting import enumerate_check, report_count

items = list("abcde")
k = 3

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    len(items) ** k, lambda: list(product(items, repeat=k)),
    "ordered, repeats allowed")))
print(report_count(enumerate_check(
    permutations_count(len(items), k), lambda: list(permutations(items, k)),
    "ordered, no repeats")))
print(report_count(enumerate_check(
    combinations_count(len(items), k), lambda: list(combinations(items, k)),
    "unordered, no repeats")))
print(report_count(enumerate_check(
    combinations_with_repetition(len(items), k),
    lambda: list(combinations_with_replacement(items, k)),
    "unordered, repeats allowed")))
print(report_count(enumerate_check(
    multiset_permutations([2, 2, 1]), lambda: distinct_arrangements("aabbc"),
    "arrangements of aabbc")))
print(report_count(enumerate_check(
    sum(binomial(len(items), j) for j in range(len(items) + 1)),
    lambda: [c for j in range(len(items) + 1) for c in combinations(items, j)],
    "subsets of all sizes")))
print()
big = permutations_count(52, 5)
print(f"ordered hands of 5 from 52: {big}")
print(f"unordered hands of 5 from 52: {combinations_count(52, 5)}")
print(f"and the ratio is {big // combinations_count(52, 5)}, which is 5!.")

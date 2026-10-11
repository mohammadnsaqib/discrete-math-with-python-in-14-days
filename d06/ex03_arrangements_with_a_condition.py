"""Counting arrangements that satisfy a condition, by splitting rather than by listing.
"""
from itertools import permutations

from dmkit.combin import factorial_of, permutations_count
from dmkit.counting import enumerate_check, report_count

people = list("abcde")

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    permutations_count(len(people)),
    lambda: list(permutations(people)),
    "all arrangements of five")))
print(report_count(enumerate_check(
    factorial_of(len(people) - 1),
    lambda: [p for p in permutations(people) if p[0] == "a"],
    "those starting with a")))
print(report_count(enumerate_check(
    2 * factorial_of(len(people) - 1),
    lambda: [p for p in permutations(people) if abs(p.index("a") - p.index("b")) == 1],
    "those with a next to b")))
print(report_count(enumerate_check(
    factorial_of(len(people)) - 2 * factorial_of(len(people) - 1),
    lambda: [p for p in permutations(people) if abs(p.index("a") - p.index("b")) > 1],
    "those with a NOT next to b")))

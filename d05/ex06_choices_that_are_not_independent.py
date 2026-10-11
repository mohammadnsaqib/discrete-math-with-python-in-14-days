"""The product rule stops applying the moment one choice restricts the next."""
from itertools import permutations, product

from dmkit.counting import enumerate_check, product_rule, report_count

people = ["Ada", "Ben", "Cleo", "Dan"]

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    product_rule(len(people), len(people)),
    lambda: list(product(people, repeat=2)),
    "two seats, repeats allowed")))
print(report_count(enumerate_check(
    product_rule(len(people), len(people)),
    lambda: list(permutations(people, 2)),
    "two seats, no repeats")))
print(report_count(enumerate_check(
    product_rule(len(people), len(people) - 1),
    lambda: list(permutations(people, 2)),
    "the same, with the rule corrected")))
print()
print(f"the pairs with a repeat: "
      f"{[p for p in product(people, repeat=2) if p[0] == p[1]]}")

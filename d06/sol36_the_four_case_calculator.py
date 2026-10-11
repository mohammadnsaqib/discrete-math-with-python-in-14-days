"""Problem 6.25: one routine that answers all four cases and names each one."""
from itertools import combinations, combinations_with_replacement, permutations, product

from dmkit.combin import (combinations_count, combinations_with_repetition,
                          permutations_count)


def count(n, k, ordered, repeats):
    """The count for one of the four cases, chosen by two yes-or-no answers."""
    if ordered and repeats:
        return n ** k
    if ordered:
        return permutations_count(n, k)
    if repeats:
        return combinations_with_repetition(n, k)
    return combinations_count(n, k)


def build(items, k, ordered, repeats):
    """The collection that count() claims to size, built with itertools."""
    if ordered and repeats:
        return list(product(items, repeat=k))
    if ordered:
        return list(permutations(items, k))
    if repeats:
        return list(combinations_with_replacement(items, k))
    return list(combinations(items, k))


names = {(True, True): "ordered, repeats", (True, False): "ordered, no repeats",
         (False, False): "unordered, no repeats", (False, True): "unordered, repeats"}
print(f"{'n':>4} {'k':>4} {'case':>24} {'by the rule':>13} {'by building':>13} "
      f"{'agree':>7}")
faults = 0
for n in (3, 5):
    for k in (2, 3):
        for ordered in (True, False):
            for repeats in (True, False):
                items = list("abcde"[:n])
                counted = count(n, k, ordered, repeats)
                built = len(build(items, k, ordered, repeats))
                faults += counted != built
                print(f"{n:>4} {k:>4} {names[(ordered, repeats)]:>24} {counted:>13} "
                      f"{built:>13} {str(counted == built):>7}")
print()
print(f"rows where the rule disagreed with its collection: {faults}")

"""Problem 6.28: what each wrong case costs, measured at every size."""
from itertools import combinations, combinations_with_replacement, permutations, product

from dmkit.combin import (combinations_count, combinations_with_repetition,
                          permutations_count)

CASES = {
    "ordered, repeats": (lambda n, k: n ** k,
                         lambda items, k: product(items, repeat=k)),
    "ordered, no repeats": (permutations_count,
                            lambda items, k: permutations(items, k)),
    "unordered, no repeats": (combinations_count,
                              lambda items, k: combinations(items, k)),
    "unordered, repeats": (combinations_with_repetition,
                           lambda items, k: combinations_with_replacement(items, k)),
}
n = 5
items = list("abcde")
print(f"{'k':>3} " + " ".join(f"{name:>22}" for name in CASES))
for k in range(0, 6):
    row = [str(formula(n, k)) for formula, _ in CASES.values()]
    print(f"{k:>3} " + " ".join(f"{v:>22}" for v in row))
print()
print(f"{'k':>3} " + " ".join(f"{name:>22}" for name in CASES))
for k in range(0, 6):
    row = [str(len(list(build(items, k)))) for _, build in CASES.values()]
    print(f"{k:>3} " + " ".join(f"{v:>22}" for v in row))
print()
faults = 0
for k in range(0, 6):
    for formula, build in CASES.values():
        faults += formula(n, k) != len(list(build(items, k)))
print(f"places where a formula and its collection differed: {faults}")
print()
target = "unordered, no repeats"
print(f"{'k':>3} {'correct':>10} {'largest wrong answer':>22} {'times too large':>17}")
for k in range(1, 6):
    correct = CASES[target][0](n, k)
    worst = max(formula(n, k) for name, (formula, _) in CASES.items() if name != target)
    ratio = "-" if correct == 0 else f"{worst / correct:.1f}"
    print(f"{k:>3} {correct:>10} {worst:>22} {ratio:>17}")

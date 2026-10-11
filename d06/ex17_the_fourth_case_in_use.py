"""The fourth case against the other three, on questions that sound almost identical."""
from itertools import combinations, combinations_with_replacement, permutations, product

from dmkit.combin import (combinations_count, combinations_with_repetition,
                          permutations_count)

print(f"{'from':>6} {'choose':>8} {'ordered,':>10} {'ordered,':>10} {'unordered,':>12} "
      f"{'unordered,':>12}")
print(f"{'':>6} {'':>8} {'repeats':>10} {'no repeats':>10} {'no repeats':>12} "
      f"{'repeats':>12}")
for n in (3, 5, 8):
    for k in (2, 3, 4):
        print(f"{n:>6} {k:>8} {n ** k:>10} {permutations_count(n, k):>10} "
              f"{combinations_count(n, k):>12} "
              f"{combinations_with_repetition(n, k):>12}")
print()
faults = 0
for n in range(1, 6):
    for k in range(0, 5):
        items = list("abcde"[:n])
        rows = [(n ** k, len(list(product(items, repeat=k)))),
                (permutations_count(n, k), len(list(permutations(items, k)))),
                (combinations_count(n, k), len(list(combinations(items, k)))),
                (combinations_with_repetition(n, k),
                 len(list(combinations_with_replacement(items, k))))]
        faults += sum(1 for a, b in rows if a != b)
print(f"formula and collection compared at {5 * 5 * 4} places; disagreements: {faults}")

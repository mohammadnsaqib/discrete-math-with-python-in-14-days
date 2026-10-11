"""Arrangements of some of the items, where the product stops early."""
from itertools import permutations
from math import perm

from dmkit.combin import permutations_count

print(f"{'from':>6} {'choose':>8} {'by the rule':>14} {'by building':>14} "
      f"{'library':>10} {'agree':>7}")
for n in range(0, 6):
    for k in range(0, n + 1):
        counted = permutations_count(n, k)
        built = len(list(permutations(range(n), k)))
        print(f"{n:>6} {k:>8} {counted:>14} {built:>14} {perm(n, k):>10} "
              f"{str(counted == built == perm(n, k)):>7}")
print()
print(f"choosing 2 from 4 in order: {[''.join(p) for p in permutations('abcd', 2)]}")

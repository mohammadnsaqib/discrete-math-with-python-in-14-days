"""Selections where the order is ignored, counted, built and checked twice."""
from itertools import combinations
from math import comb

from dmkit.combin import combinations_count

print(f"{'from':>6} {'choose':>8} {'by the rule':>13} {'by building':>13} "
      f"{'library':>9} {'agree':>7}")
for n in range(0, 7):
    for k in range(0, n + 1):
        counted = combinations_count(n, k)
        built = len(list(combinations(range(n), k)))
        print(f"{n:>6} {k:>8} {counted:>13} {built:>13} {comb(n, k):>9} "
              f"{str(counted == built == comb(n, k)):>7}")
print()
print(f"the ten ways to choose 3 from 5: "
      f"{[''.join(c) for c in combinations('abcde', 3)]}")

"""Three claims proved by counting holes, and each one checked by search."""
from itertools import combinations

numbers = list(range(1, 21))

pairs_summing = [(a, b) for a, b in combinations(range(1, 11), 2) if a + b == 11]
print(f"pairs from 1..10 that sum to 11: {pairs_summing}")
print(f"there are {len(pairs_summing)} such pairs, so any 6 numbers from 1..10 include "
      f"one.")
chosen = list(range(1, 7))
found = [p for p in pairs_summing if p[0] in chosen and p[1] in chosen]
print(f"choosing {chosen} gives the pair {found}")
print()
worst = [1, 2, 3, 4, 5]
missing = [p for p in pairs_summing if p[0] in worst and p[1] in worst]
print(f"five numbers can avoid it: {worst} contains {len(missing)} of the pairs.")
print()
groups = {}
for n in numbers:
    groups.setdefault(n % 6, []).append(n)
print("1 to 20 by remainder on division by 6:")
for r in sorted(groups):
    print(f"   remainder {r}: {groups[r]}")
biggest = max(len(g) for g in groups.values())
print()
print(f"twenty numbers into six remainders, so some remainder holds at least 4.")
print(f"the fullest here holds {biggest}. The claim gives a floor, never the exact "
      f"count,")
print("and reading it as the exact count is the usual mistake.")

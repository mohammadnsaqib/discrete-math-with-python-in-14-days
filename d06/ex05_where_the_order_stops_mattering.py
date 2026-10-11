"""The same choices, counted once with the order kept and once with it dropped."""
from itertools import combinations, permutations

from dmkit.combin import combinations_count, permutations_count

letters = list("abcd")
k = 2
ordered = list(permutations(letters, k))
unordered = list(combinations(letters, k))

print(f"choosing {k} from {letters}")
print(f"   with the order kept    : {[''.join(p) for p in ordered]}")
print(f"   with the order dropped : {[''.join(c) for c in unordered]}")
print()
print(f"{'from':>6} {'choose':>8} {'ordered':>10} {'unordered':>11} {'ratio':>8} "
      f"{'k!':>6}")
for n in range(1, 7):
    for k in range(1, n + 1):
        o = permutations_count(n, k)
        u = combinations_count(n, k)
        print(f"{n:>6} {k:>8} {o:>10} {u:>11} {o // u:>8} "
              f"{__import__('math').factorial(k):>6}")

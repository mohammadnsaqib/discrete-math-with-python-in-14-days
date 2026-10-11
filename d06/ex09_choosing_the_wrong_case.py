"""What a wrong case costs, measured against the collection the question describes."""
from itertools import combinations, combinations_with_replacement, permutations, product

from dmkit.combin import (combinations_count, combinations_with_repetition,
                          permutations_count)

n, k = 6, 3
right = list(combinations(range(n), k))

answers = [
    ("order ignored, no repeats (correct)", combinations_count(n, k)),
    ("order matters, no repeats", permutations_count(n, k)),
    ("order matters, repeats allowed", n ** k),
    ("order ignored, repeats allowed", combinations_with_repetition(n, k)),
]
print(f"{'case used':>38} {'says':>8} {'the collection holds':>22} {'off by':>9}")
for text, counted in answers:
    print(f"{text:>38} {counted:>8} {len(right):>22} {counted - len(right):>9}")
print()
print(f"{'k':>4} {'correct':>10} {'ordered':>10} {'with repeats':>14} "
      f"{'ordered/correct':>17}")
for k in range(1, 7):
    correct = combinations_count(n, k)
    ordered = permutations_count(n, k)
    print(f"{k:>4} {correct:>10} {ordered:>10} "
          f"{combinations_with_repetition(n, k):>14} {ordered // correct:>17}")

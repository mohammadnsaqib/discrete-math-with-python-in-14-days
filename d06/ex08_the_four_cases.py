"""Two questions, four answers, and the collection each answer claims to size."""
from itertools import combinations, combinations_with_replacement, permutations, product

from dmkit.combin import (combinations_count, combinations_with_repetition,
                          permutations_count)

n, k = 4, 2
items = list("abcd")
cases = [
    ("order matters, repeats allowed", n ** k,
     lambda: ["".join(t) for t in product(items, repeat=k)]),
    ("order matters, no repeats", permutations_count(n, k),
     lambda: ["".join(t) for t in permutations(items, k)]),
    ("order ignored, no repeats", combinations_count(n, k),
     lambda: ["".join(t) for t in combinations(items, k)]),
    ("order ignored, repeats allowed", combinations_with_repetition(n, k),
     lambda: ["".join(t) for t in combinations_with_replacement(items, k)]),
]
print(f"{'case':>32} {'by the rule':>12} {'by building':>12} {'agree':>7}")
for text, counted, build in cases:
    built = build()
    print(f"{text:>32} {counted:>12} {len(built):>12} {str(counted == len(built)):>7}")
print()
for text, _, build in cases:
    print(f"{text}:")
    print(f"   {build()}")

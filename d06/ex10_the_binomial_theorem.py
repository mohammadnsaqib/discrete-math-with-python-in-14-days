"""Where the coefficients of an expansion come from, counted rather than multiplied."""
from itertools import product

from dmkit.combin import binomial, expand_binomial

n = 4
picks = list(product("ab", repeat=n))
by_count = {}
for pick in picks:
    by_count.setdefault(pick.count("b"), []).append("".join(pick))

print(f"every way to take a or b from each of {n} brackets: {len(picks)}")
print(f"{'copies of b':>13} {'ways':>6} {'binomial(4, k)':>16} {'agree':>7}")
for k in sorted(by_count):
    ways = len(by_count[k])
    print(f"{k:>13} {ways:>6} {binomial(n, k):>16} {str(ways == binomial(n, k)):>7}")
print()
print(f"the {len(by_count[2])} ways to take b from exactly two brackets:")
print(f"   {by_count[2]}")
print()
print(f"the coefficients of (a + b)**{n}: {expand_binomial(n)}")

"""Problem 9.27: how far apart consecutive primes get, measured rather than described.
"""
from math import log

from dmkit.number import sieve

primes = sieve(1000000)
gaps = [(primes[i + 1] - primes[i], primes[i]) for i in range(len(primes) - 1)]

print(f"{'limit':>10} {'primes':>9} {'largest gap':>13} {'after':>10} "
      f"{'mean gap':>10} {'ln(limit)':>11}")
for limit in (100, 1000, 10000, 100000, 1000000):
    inside = [(g, p) for g, p in gaps if p < limit]
    biggest = max(inside)
    mean = sum(g for g, _ in inside) / len(inside)
    print(f"{limit:>10} {len(inside) + 1:>9} {biggest[0]:>13} {biggest[1]:>10} "
          f"{mean:>10.4f} {log(limit):>11.4f}")
print()
print(f"{'gap':>6} {'how often below a million':>27} {'first pair':>22}")
for size in (2, 4, 6, 8, 14, 34):
    matching = [(g, p) for g, p in gaps if g == size]
    first = matching[0] if matching else None
    shown = f"({first[1]}, {first[1] + size})" if first else "-"
    print(f"{size:>6} {len(matching):>27} {shown:>22}")
print()
twins = [(p, p + 2) for g, p in gaps if g == 2]
print(f"pairs two apart below a million: {len(twins)}")
print(f"the largest of them: {twins[-1]}")
print()
first_big = next((g, p) for g, p in gaps if g >= 100)
print(f"the first gap of 100 or more starts after {first_big[1]}, and is "
      f"{first_big[0]}")

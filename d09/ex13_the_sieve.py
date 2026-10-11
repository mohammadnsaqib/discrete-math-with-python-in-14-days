"""Finding every prime up to a limit by crossing out multiples."""
from math import isqrt

from sympy import isprime

from dmkit.number import sieve

limit = 50
flags = [True] * (limit + 1)
flags[0] = flags[1] = False
print(f"crossing out up to {limit}:")
for p in range(2, isqrt(limit) + 1):
    if flags[p]:
        crossed = [m for m in range(p * p, limit + 1, p) if flags[m]]
        for m in crossed:
            flags[m] = False
        print(f"   from {p:>2}: {crossed}")
print(f"   what is left: {[n for n, ok in enumerate(flags) if ok]}")
print()
print(f"{'limit':>10} {'primes found':>14} {'largest':>10} {'all prime':>11}")
for limit in (10, 100, 1000, 10000):
    primes = sieve(limit)
    print(f"{limit:>10} {len(primes):>14} {primes[-1]:>10} "
          f"{str(all(isprime(p) for p in primes)):>11}")
print()
missed = [n for n in range(2, 10000) if isprime(n) and n not in set(sieve(10000))]
print(f"primes below 10000 the sieve missed: {missed}")

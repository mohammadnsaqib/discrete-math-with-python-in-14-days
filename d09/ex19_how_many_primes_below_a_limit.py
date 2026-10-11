"""Counting the primes, and comparing the count with two estimates."""
from math import log

from dmkit.number import prime_count

print(f"{'limit':>12} {'primes':>10} {'limit / ln(limit)':>19} {'ratio':>8} "
      f"{'limit / (ln - 1)':>18} {'ratio':>8}")
for limit in (100, 1000, 10000, 100000, 1000000):
    count = prime_count(limit)
    rough = limit / log(limit)
    better = limit / (log(limit) - 1)
    print(f"{limit:>12} {count:>10} {rough:>19.1f} {count / rough:>8.4f} "
          f"{better:>18.1f} {count / better:>8.4f}")
print()
print(f"{'limit':>12} {'primes':>10} {'share':>10} {'1 / ln(limit)':>15}")
for limit in (100, 1000, 10000, 100000, 1000000):
    count = prime_count(limit)
    print(f"{limit:>12} {count:>10} {count / limit:>10.5f} {1 / log(limit):>15.5f}")

"""The other side of the gcd, found without searching for it."""
from math import gcd as library_gcd
from math import lcm as library_lcm

from dmkit.number import gcd, lcm

print(f"{'a':>8} {'b':>8} {'gcd':>7} {'lcm':>10} {'gcd * lcm':>12} {'a * b':>10} "
      f"{'agree':>7}")
for a, b in ((4, 6), (48, 18), (12, 35), (100, 75), (17, 5), (9, 0)):
    g, l = gcd(a, b), lcm(a, b)
    print(f"{a:>8} {b:>8} {g:>7} {l:>10} {g * l:>12} {a * b:>10} "
          f"{str(g * l == a * b):>7}")
print()
a, b = 4, 6
multiples_a = [a * k for k in range(1, 8)]
multiples_b = [b * k for k in range(1, 8)]
shared = sorted(set(multiples_a) & set(multiples_b))
print(f"multiples of {a}: {multiples_a}")
print(f"multiples of {b}: {multiples_b}")
print(f"in both        : {shared}, and the smallest is {shared[0]}")
print()
bad = [(a, b) for a in range(1, 60) for b in range(1, 60)
       if lcm(a, b) != library_lcm(a, b) or gcd(a, b) != library_gcd(a, b)]
print(f"pairs from 1 to 59 where either routine disagrees with the library: {len(bad)}")

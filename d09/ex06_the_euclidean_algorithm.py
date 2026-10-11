"""The remainder form of the algorithm, with every pair it passes through."""
from math import gcd as library_gcd

from dmkit.number import gcd, gcd_steps

print(f"{'a':>10} {'b':>8} {'gcd':>8} {'steps':>7} {'library':>9} {'agree':>7}")
for a, b in ((48, 18), (270, 192), (1071, 462), (1000000, 2), (17, 5),
             (123456789, 987654321)):
    answer, trail = gcd_steps(a, b)
    print(f"{a:>10} {b:>8} {answer:>8} {len(trail):>7} {library_gcd(a, b):>9} "
          f"{str(answer == library_gcd(a, b)):>7}")
print()
a, b = 1071, 462
answer, trail = gcd_steps(a, b)
print(f"the algorithm on ({a}, {b}):")
for x, y, q, r in trail:
    print(f"   {x:>5} = {q:>2} * {y:>4} + {r:>4}")
print(f"   the last non-zero remainder is {answer}")
print()
bad = [(a, b) for a in range(1, 60) for b in range(1, 60) if gcd(a, b) != library_gcd(a,
       b)]
print(f"pairs from 1 to 59 where the routine and the library disagree: {len(bad)}")

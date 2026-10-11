"""The gcd written as a combination of the two numbers."""
from math import gcd as library_gcd

from dmkit.number import extended_gcd

print(f"{'a':>8} {'b':>8} {'gcd':>6} {'x':>8} {'y':>8} {'a*x + b*y':>11} {'agree':>7}")
for a, b in ((48, 18), (270, 192), (1071, 462), (17, 5), (35, 64), (-48, 18)):
    g, x, y = extended_gcd(a, b)
    print(f"{a:>8} {b:>8} {g:>6} {x:>8} {y:>8} {a * x + b * y:>11} "
          f"{str(a * x + b * y == g and g == library_gcd(a, b)):>7}")
print()
a, b = 48, 18
g, x, y = extended_gcd(a, b)
print(f"{a} * {x} + {b} * {y} = {a * x + b * y}")
print()
values = sorted({a * i + b * j for i in range(-6, 7) for j in range(-6, 7)})
positive = [v for v in values if v > 0]
print(f"the positive values of {a}*i + {b}*j for small i and j: {positive[:10]}")
print(f"the smallest of them is {min(positive)}, and the gcd is {g}")
print()
bad = [(a, b) for a in range(1, 40) for b in range(1, 40)
       if extended_gcd(a, b)[0] != library_gcd(a, b)
       or a * extended_gcd(a, b)[1] + b * extended_gcd(a, b)[2] != library_gcd(a, b)]
print(f"pairs from 1 to 39 where the identity fails: {len(bad)}")

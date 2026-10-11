"""The inverse is a Bezout coefficient, and a search finds it too, only slower."""
from dmkit.crypto import mod_inverse
from dmkit.number import extended_gcd

print(f"{'a':>6} {'m':>6} {'gcd':>5} {'x':>7} {'y':>7} {'a*x + m*y':>11} "
      f"{'x mod m':>9} {'a * that mod m':>16}")
for a, m in ((3, 7), (5, 12), (11, 26), (17, 3120), (4, 12)):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        print(f"{a:>6} {m:>6} {g:>5} {x:>7} {y:>7} {a * x + m * y:>11} "
              f"{'-':>9} {'no inverse':>16}")
        continue
    print(f"{a:>6} {m:>6} {g:>5} {x:>7} {y:>7} {a * x + m * y:>11} "
          f"{x % m:>9} {a * (x % m) % m:>16}")
print()
a, m = 17, 3120
g, x, y = extended_gcd(a, m)
print(f"{a} * {x} + {m} * {y} = {a * x + m * y}")
print(f"so {a} * {x % m} is 1 more than a multiple of {m}: "
      f"{a * (x % m)} = {a * (x % m) // m} * {m} + {a * (x % m) % m}")
print(f"and mod_inverse agrees: {mod_inverse(a, m)}")

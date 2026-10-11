"""The oldest form of the algorithm, where every step is visible."""
from math import gcd as library_gcd

from dmkit.number import gcd_by_subtraction

print(f"{'a':>8} {'b':>8} {'gcd':>6} {'steps':>8} {'library gcd':>13} {'agree':>7}")
for a, b in ((48, 18), (270, 192), (17, 5), (100, 100), (1071, 462), (1000000, 2)):
    answer, steps = gcd_by_subtraction(a, b)
    print(f"{a:>8} {b:>8} {answer:>6} {steps:>8} {library_gcd(a, b):>13} "
          f"{str(answer == library_gcd(a, b)):>7}")
print()
a, b = 48, 18
print(f"every pair the subtraction form passes through, from ({a}, {b}):")
while a and b:
    print(f"   ({a:>3}, {b:>3})")
    if a > b:
        a -= b
    else:
        b -= a
print(f"   ({a:>3}, {b:>3})  and the answer is {a or b}")

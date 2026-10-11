"""Assuming the opposite, and finding the assumption impossible."""
from fractions import Fraction

from dmkit.proof import exists

# CLAIM. The square root of two is not a fraction. PROOF. Suppose it were, in lowest
# terms a/b. Then a^2 = 2b^2, so a^2 is even, so a is even (Example 2.14), so a = 2c and
# 4c^2 = 2b^2, so b^2 = 2c^2 and b is even too. Both even contradicts lowest terms. The
# assumption is therefore impossible.
#
# A search cannot establish this, and the point of the program is to show what it CAN
# do.
print("searching fractions a/b with b up to 2000 for one whose square is exactly 2")
found = exists(lambda ab: Fraction(ab[0], ab[1]) ** 2 == 2,
               [(a, b) for b in range(1, 2001) for a in range(1, 2 * b + 1)])
print(f"   found: {found}")
print()
best, gap = None, None
for b in range(1, 2001):
    a = round((2 ** 0.5) * b)
    d = abs(Fraction(a, b) ** 2 - 2)
    if gap is None or d < gap:
        best, gap = Fraction(a, b), d
print(f"the closest such fraction is {best}, and its square misses 2 by "
      f"{float(gap):.3e}")

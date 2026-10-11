"""Problem 9.26: the two forms of the algorithm counted across many pairs."""
from math import gcd as library_gcd

from dmkit.number import gcd_by_subtraction, gcd_steps

pairs = [(a, b) for a in range(1, 61) for b in range(1, 61)]
subtractions = []
remainders = []
faults = 0
for a, b in pairs:
    answer, steps = gcd_by_subtraction(a, b)
    other, trail = gcd_steps(a, b)
    if not (answer == other == library_gcd(a, b)):
        faults += 1
    subtractions.append(steps)
    remainders.append(len(trail))
print(f"pairs tested: {len(pairs)}")
print(f"pairs where any of the three answers differed: {faults}")
print()
print(f"{'form':>20} {'worst':>8} {'mean':>9} {'total':>10}")
print(f"{'subtraction':>20} {max(subtractions):>8} "
      f"{sum(subtractions) / len(subtractions):>9.2f} {sum(subtractions):>10}")
print(f"{'remainder':>20} {max(remainders):>8} "
      f"{sum(remainders) / len(remainders):>9.2f} {sum(remainders):>10}")
print()
worst = max(range(len(pairs)), key=lambda i: subtractions[i])
a, b = pairs[worst]
print(f"the worst pair for subtraction is ({a}, {b}), at {subtractions[worst]} steps")
print(f"   the remainder form takes {remainders[worst]}")
print()
worst = max(range(len(pairs)), key=lambda i: remainders[i])
a, b = pairs[worst]
print(f"the worst pair for the remainder form is ({a}, {b}), at {remainders[worst]} "
      f"steps")
print(f"   its gcd is {library_gcd(a, b)}")

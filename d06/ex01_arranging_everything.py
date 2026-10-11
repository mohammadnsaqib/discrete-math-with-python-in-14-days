"""Arrangements of a whole collection, counted and then built."""
from itertools import permutations
from math import factorial, perm

from dmkit.combin import factorial_of, permutations_count
from dmkit.counting import enumerate_check, report_count

print(f"{'items':>8} {'by the rule':>14} {'by building':>14} {'library':>12} "
      f"{'agree':>7}")
for n in range(0, 8):
    counted = permutations_count(n)
    result = enumerate_check(counted, lambda n=n: list(permutations(range(n))), "")
    print(f"{n:>8} {counted:>14} {result['built']:>14} {perm(n, n):>12} "
          f"{str(counted == result['built'] == perm(n, n)):>7}")
print()
print("the six arrangements of three items:")
for arrangement in permutations("abc"):
    print(f"   {''.join(arrangement)}")
print()
print(f"factorial_of(20) is {factorial_of(20)} and math.factorial agrees: "
      f"{factorial_of(20) == factorial(20)}")

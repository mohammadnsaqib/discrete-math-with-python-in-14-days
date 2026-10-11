"""Counting divisors from the factorisation rather than by searching for them."""
from dmkit.number import divisors, factorise

print(f"{'n':>8} {'factorisation':>22} {'divisors found':>16} {'from the powers':>17} "
      f"{'agree':>7}")
for n in (12, 36, 60, 97, 128, 720, 1024):
    factors = factorise(n)
    counted = 1
    for _, power in factors:
        counted *= power + 1
    found = len(divisors(n))
    shown = " * ".join(f"{p}**{k}" for p, k in factors)
    print(f"{n:>8} {shown:>22} {found:>16} {counted:>17} {str(found == counted):>7}")
print()
print("a divisor chooses, for each prime, how "
      "many copies of it to take: none, one, up to")
print("the power present. So the count of divisors "
      "is the product of one more than each")
print("power, which is Day 5's product rule applied to the factorisation.")
print()
print(f"{'n':>8} {'divisors':>10} {'the largest proper one':>24}")
for n in (12, 97, 100, 1024):
    d = divisors(n)
    print(f"{n:>8} {len(d):>10} {d[-2] if len(d) > 1 else 0:>24}")

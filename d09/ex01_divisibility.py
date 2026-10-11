"""What it means for one integer to divide another, including the cases people skip."""
from dmkit.number import divides, divisors

print(f"{'a':>6} {'b':>8} {'a divides b':>13} {'why':>34}")
cases = [(3, 12, "12 is 3 times 4"), (5, 12, "12 is not a whole number of 5s"),
         (1, 12, "every integer divides by "
                 "1"), (12, 12, "every integer divides itself"),
         (12, 0, "0 is 12 times 0"), (0, 0, "0 is 0 times anything"),
         (0, 5, "no multiple of 0 is 5"), (-3, 12, "12 is -3 times -4")]
for a, b, why in cases:
    print(f"{a:>6} {b:>8} {str(divides(a, b)):>13} {why:>34}")
print()
for n in (12, 36, 97, 100):
    print(f"the divisors of {n:>4}: {divisors(n)}")
print()
print(f"{'n':>6} {'divisors':>10} {'sum of them':>13}")
for n in (6, 12, 28, 30, 496):
    d = divisors(n)
    print(f"{n:>6} {len(d):>10} {sum(d):>13}")

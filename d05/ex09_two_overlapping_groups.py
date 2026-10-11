"""Inclusion and exclusion for two groups, checked against the union itself."""
from dmkit.counting import enumerate_check, inclusion_exclusion, report_count, sum_rule

upto = list(range(1, 101))
by_2 = [n for n in upto if n % 2 == 0]
by_3 = [n for n in upto if n % 3 == 0]
by_6 = [n for n in upto if n % 6 == 0]

print(f"{'divisible by 2':>18} {len(by_2):>6}")
print(f"{'divisible by 3':>18} {len(by_3):>6}")
print(f"{'divisible by 6':>18} {len(by_6):>6}")
print()
print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    sum_rule(len(by_2), len(by_3)),
    lambda: sorted(set(by_2) | set(by_3)),
    "by 2 or by 3, added naively")))
print(report_count(enumerate_check(
    inclusion_exclusion(by_2, by_3),
    lambda: sorted(set(by_2) | set(by_3)),
    "by 2 or by 3, with the overlap out")))
print()
print(f"the overlap is exactly the multiples of 6, and there are {len(by_6)} of them.")
print(f"50 plus 33 minus 16 is {50 + 33 - 16}, which the enumeration confirms.")

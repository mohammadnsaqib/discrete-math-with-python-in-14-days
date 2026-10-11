"""The commonest counting error, and the one enumeration catches instantly."""
from dmkit.counting import enumerate_check, report_count

print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
cases = [("integers 3 to 9", 3, 9)]
for name, lo, hi in cases:
    print(report_count(enumerate_check(hi - lo, lambda: list(range(lo, hi + 1)),
                                       f"{name}, by subtracting")))
    print(report_count(enumerate_check(hi - lo + 1, lambda: list(range(lo, hi + 1)),
                                       f"{name}, plus one")))
print()
print(f"{'from':>8} {'to':>8} {'hi - lo':>10} {'built':>8} {'agree':>8}")
for lo, hi in ((3, 9), (0, 0), (1, 100), (-5, 5), (7, 7)):
    built = len(range(lo, hi + 1))
    print(f"{lo:>8} {hi:>8} {hi - lo:>10} {built:>8} {str(hi - lo == built):>8}")

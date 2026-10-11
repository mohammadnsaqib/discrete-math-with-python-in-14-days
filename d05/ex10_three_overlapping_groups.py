"""Why three groups need a third term, and what happens without it."""
from dmkit.counting import enumerate_check, inclusion_exclusion, report_count

upto = list(range(1, 101))
by_2 = [n for n in upto if n % 2 == 0]
by_3 = [n for n in upto if n % 3 == 0]
by_5 = [n for n in upto if n % 5 == 0]
union = sorted(set(by_2) | set(by_3) | set(by_5))

pairs = (len(set(by_2) & set(by_3)) + len(set(by_2) & set(by_5))
         + len(set(by_3) & set(by_5)))
triple = len(set(by_2) & set(by_3) & set(by_5))
singles = len(by_2) + len(by_3) + len(by_5)

print(f"{'sizes added':>26} {singles:>6}")
print(f"{'pairwise overlaps':>26} {pairs:>6}")
print(f"{'in all three':>26} {triple:>6}")
print()
print(f"{'collection':>34} {'by the rule':>12} {'by building':>12}  verdict")
print(report_count(enumerate_check(
    singles - pairs, lambda: union, "stopping after the pairs")))
print(report_count(enumerate_check(
    singles - pairs + triple, lambda: union, "adding the triple back")))
print(report_count(enumerate_check(
    inclusion_exclusion(by_2, by_3, by_5), lambda: union, "by the routine")))
print()
print(f"the {triple} numbers divisible by all three are counted three times by the "
      f"first")

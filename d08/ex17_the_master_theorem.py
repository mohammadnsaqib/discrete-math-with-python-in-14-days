"""Three cases, decided by comparing the splitting work with the work at the top."""
from dmkit.recur import divide_conquer, master_theorem

cases = [
    ("T(n) = T(n/2) + 1", 1, 2, 0),
    ("T(n) = 2*T(n/2) + n", 2, 2, 1),
    ("T(n) = 3*T(n/2) + n", 3, 2, 1),
    ("T(n) = 4*T(n/2) + n", 4, 2, 1),
    ("T(n) = 2*T(n/2) + n**2", 2, 2, 2),
    ("T(n) = 8*T(n/2) + n**2", 8, 2, 2),
    ("T(n) = 7*T(n/2) + n**2", 7, 2, 2),
]
print(f"{'recurrence':>26} {'subproblems':>12} {'split**power':>13} {'case':>6} "
      f"{'growth':>18}")
for text, subproblems, factor, power in cases:
    verdict = master_theorem(subproblems, factor, power)
    print(f"{text:>26} {subproblems:>12} {factor ** power:>13} "
          f"{verdict['case']:>6} {verdict['growth']:>18}")
print()
print("the comparison is between the number of "
      "subproblems and the factor raised to the")
print("power of the extra work. More subproblems "
      "than that and the leaves dominate; fewer")
print("and the top does; equal and every level costs the same, which produces the log.")
print()
print(f"{'recurrence':>26} {'T(1024)':>14} {'T(512)':>12} {'ratio':>8} "
      f"{'measured exponent':>18}")
from math import log2
for text, subproblems, factor, power in cases:
    extra = (lambda n: 1) if power == 0 else (lambda n, p=power: n ** p)
    costs = divide_conquer(subproblems, factor, extra, 1, 1024)
    ratio = costs[1024] / costs[512]
    print(f"{text:>26} {costs[1024]:>14} {costs[512]:>12} {ratio:>8.4f} "
          f"{log2(ratio):>18.4f}")

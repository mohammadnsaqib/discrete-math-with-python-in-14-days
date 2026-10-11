"""A claim whose step is airtight and whose base was never checked."""
from math import factorial

from dmkit.induct import induction_report, report_induction

claims = [
    ("sum 1..n = n(n+1)/2",
     lambda n: sum(range(1, n + 1)) == n * (n + 1) // 2),
    ("sum 1..n = n(n+1)/2 + 7",
     lambda n: sum(range(1, n + 1)) == n * (n + 1) // 2 + 7),
    ("n! is at least 2**n",
     lambda n: factorial(n) >= 2 ** n),
    ("n is at least 5",
     lambda n: n >= 5),
]
for text, claim in claims:
    print(f"{text}")
    print(f"   {report_induction(induction_report(claim, 1, 60))}")
print()
print(f"{'n':>4} {'sum 1..n':>10} {'n(n+1)/2 + 7':>14} {'gap':>5}")
for n in range(1, 7):
    left, right = sum(range(1, n + 1)), n * (n + 1) // 2 + 7
    print(f"{n:>4} {left:>10} {right:>14} {right - left:>5}")

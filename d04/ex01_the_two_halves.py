"""Induction is two claims, and both are needed."""
from dmkit.induct import induction_report, report_induction

claims = [
    ("n(n+1)/2 equals the sum to n",
     lambda n: n * (n + 1) // 2 == sum(range(1, n + 1)), 1, 300),
    ("2**n is greater than n", lambda n: 2 ** n > n, 0, 300),
    ("n is at least 5", lambda n: n >= 5, 1, 300),
    ("n squared is greater than 10", lambda n: n * n > 10, 1, 300),
]
for text, claim, start, limit in claims:
    print(f"{text}")
    print(f"   {report_induction(induction_report(claim, start, limit))}")

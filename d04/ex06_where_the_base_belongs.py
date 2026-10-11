"""Finding the smallest value from which a claim actually holds."""
from math import factorial

from dmkit.induct import induction_report

claims = [
    ("2**n >= n**2", lambda n: 2 ** n >= n * n),
    ("n! >= 2**n", lambda n: factorial(n) >= 2 ** n),
    ("n! >= n**2", lambda n: factorial(n) >= n * n),
    ("2**n > n**3", lambda n: 2 ** n > n ** 3),
]
print(f"{'claim':>16} {'fails at':>26} {'holds from':>12} {'step from there':>18}")
for text, claim in claims:
    fails = [n for n in range(1, 60) if not claim(n)]
    start = max(fails) + 1 if fails else 1
    r = induction_report(claim, start, 200)
    step = "holds" if not r["step_failures"] else f"fails at {r['first_step_failure']}"
    print(f"{text:>16} {str(fails):>26} {start:>12} {step:>18}")

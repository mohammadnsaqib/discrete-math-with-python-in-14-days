"""Problem 4.26: the smallest starting value from which a claim never fails again."""
from math import factorial

from dmkit.induct import induction_report


def smallest_base(claim, limit=200):
    """The first value from which the claim holds all the way to the limit.

    The search runs DOWNWARD from the limit rather than upward from 1, because a claim
    can hold at 1, fail at 3 and hold from 4 on -- and an upward search would stop at 1
    and report a base case that the step cannot carry.
    """
    start = limit
    for n in range(limit - 1, 0, -1):
        if claim(n):
            start = n
        else:
            break
    return start


claims = [("2**n >= n**2", lambda n: 2 ** n >= n * n),
          ("2**n > n**3", lambda n: 2 ** n > n ** 3),
          ("n! >= 2**n", lambda n: factorial(n) >= 2 ** n),
          ("n! >= n**3", lambda n: factorial(n) >= n ** 3),
          ("n**2 >= 2*n + 3", lambda n: n * n >= 2 * n + 3),
          ("2**n >= n + 1", lambda n: 2 ** n >= n + 1)]
print(f"{'claim':>18} {'fails at':>28} {'base belongs at':>16} {'step from there':>16}")
for text, claim in claims:
    limit = 60
    fails = [n for n in range(1, limit) if not claim(n)]
    base = smallest_base(claim, limit)
    r = induction_report(claim, base, 200)
    step = "holds" if not r["step_failures"] else f"cut at {r['first_step_failure']}"
    shown = str(fails) if len(fails) < 6 else f"{fails[:5]} and {len(fails) - 5} more"
    print(f"{text:>18} {shown:>28} {base:>16} {step:>16}")

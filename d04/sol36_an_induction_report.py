"""Problem 4.25: one report on any claim, naming the repair each failure needs."""
from math import factorial

from dmkit.induct import induction_report


def audit(text, claim, start, limit):
    """Both halves of the induction, and what a failure in each one means."""
    r = induction_report(claim, start, limit)
    if r["base"] and not r["step_failures"]:
        verdict = "both halves hold over the range"
    elif not r["base"] and not r["step_failures"]:
        verdict = "move the base, or the claim is false everywhere"
    elif r["base"] and r["step_failures"]:
        verdict = f"the chain is cut at {r['first_step_failure']}"
    else:
        verdict = "neither half holds; the claim is not repairable by moving the base"
    print(f"{text:>28} {str(r['base']):>6} "
          f"{str(not r['step_failures']):>6}  {verdict}")


print(f"{'claim':>28} {'base':>6} {'step':>6}  what it means")
audit("sum 1..n = n(n+1)/2", lambda n: sum(range(1, n + 1)) == n * (n + 1) // 2, 1, 60)
audit("sum 1..n = n(n+1)/2 + 7",
      lambda n: sum(range(1, n + 1)) == n * (n + 1) // 2 + 7, 1, 60)
audit("n! is at least 2**n", lambda n: factorial(n) >= 2 ** n, 1, 40)
audit("n! is at least 2**n from 4", lambda n: factorial(n) >= 2 ** n, 4, 40)
audit("n is not a multiple of 7", lambda n: n % 7 != 0, 1, 40)
audit("2**n is at least n**2", lambda n: 2 ** n >= n * n, 1, 40)
audit("n is at least 5", lambda n: n >= 5, 1, 40)

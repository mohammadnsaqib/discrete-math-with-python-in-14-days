"""A step that always holds, attached to a base that does not."""
from dmkit.induct import induction_report, report_induction


def bad(n):
    """The claim 'n is at least 100'."""
    return n >= 100


result = induction_report(bad, 1, 400)
print("claim: every positive integer is at least 100")
print(f"   {report_induction(result)}")
print()
print("the step holds at every one of the 399 values checked. If n is at least 100")
print("then n+1 is too, and there is no way for that to fail.")
print()
print(f"and the claim is false at n = 1: {bad(1)}")
print(f"   false at 1 through 99, true from 100 on. Values checked: "
      f"{sum(1 for n in range(1, 400) if not bad(n))} false, "
      f"{sum(1 for n in range(1, 400) if bad(n))} true.")

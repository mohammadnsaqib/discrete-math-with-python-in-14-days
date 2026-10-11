"""A base that holds, attached to a step that fails once."""
from dmkit.induct import induction_report, report_induction


def claim(n):
    """The claim 'n divides 24', which holds at 1, 2, 3, 4, 6, 8, 12 and 24."""
    return 24 % n == 0


result = induction_report(claim, 1, 30)
print("claim: every positive integer divides 24")
print(f"   {report_induction(result)}")
print()
holds = [n for n in range(1, 30) if claim(n)]
print(f"values where it holds  : {holds}")
print(f"first step failure     : {result['first_step_failure']}")
print(f"step failures in 1..29 : {result['step_failures']}")

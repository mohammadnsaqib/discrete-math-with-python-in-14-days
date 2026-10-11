"""One broken step, and everything past it left unsupported."""
from dmkit.induct import induction_report


def claim(n):
    """n is not a multiple of 7."""
    return n % 7 != 0


r = induction_report(claim, 1, 30)
print("claim: no positive integer is a multiple of 7")
print(f"   base at 1 holds       : {r['base']}")
print(f"   step failures in 1..29: {r['step_failures']}")
print()
print(f"{'n':>4} {'claim':>7} {'step to n+1':>13}")
for n in range(1, 16):
    ok = claim(n)
    step = "-" if not ok else ("holds" if claim(n + 1) else "BREAKS")
    print(f"{n:>4} {str(ok):>7} {step:>13}")

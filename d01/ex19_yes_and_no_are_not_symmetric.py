"""Answering yes needs one row. Answering no needs all of them."""
from dmkit.logic import assignments, evaluate

names = ["p", "q", "r", "s"]


def satisfiable_counting(statement):
    """Find a satisfying assignment, and report how many rows had to be looked at."""
    for k, a in enumerate(assignments(names), start=1):
        if evaluate(statement, a):
            return dict(a), k
    return None, 2 ** len(names)


cases = [
    ("not p and not q and not r and not s",
     lambda p, q, r, s: (not p) and (not q) and (not r) and (not s)),
    ("p and q and r and s", lambda p, q, r, s: p and q and r and s),
    ("p and not p and q", lambda p, q, r, s: p and (not p) and q),
]
print(f"{'statement':>38} {'answer':>8} {'rows looked at':>16} {'of':>5}")
for name, fn in cases:
    found, looked = satisfiable_counting(fn)
    print(f"{name:>38} {('yes' if found else 'no'):>8} {looked:>16} "
          f"{2 ** len(names):>5}")

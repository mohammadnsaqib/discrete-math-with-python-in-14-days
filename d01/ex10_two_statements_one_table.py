"""Two statements written differently, and the two columns that decide whether they
agree."""
from dmkit.logic import assignments, equivalent, evaluate


def left(p, q):
    """not (p and q)."""
    return not (p and q)


def right(p, q):
    """(not p) or (not q)."""
    return (not p) or (not q)


names = ["p", "q"]
print(f"{'p':>7} {'q':>7} {'not (p and q)':>16} {'(not p) or (not q)':>21} "
      f"{'agree':>7}")
for a in assignments(names):
    x, y = evaluate(left, a), evaluate(right, a)
    print(f"{str(a['p']):>7} {str(a['q']):>7} {str(x):>16} {str(y):>21} "
          f"{str(x == y):>7}")
print()
print(f"equivalent: {equivalent(left, right, names)}")
print("no rewriting rule was used and none is needed. Two columns matched, four times.")

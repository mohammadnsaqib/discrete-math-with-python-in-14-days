"""A table is read for the rows that make the statement true."""
from dmkit.logic import implies, models, truth_table


def statement(p, q, r):
    """(p or q) and (not r)."""
    return (p or q) and (not r)


names = ["p", "q", "r"]
print(f"{'p':>6} {'q':>6} {'r':>6} {'value':>7}")
for a, value in truth_table(statement, names):
    print(f"{str(a['p']):>6} {str(a['q']):>6} {str(a['r']):>6} {str(value):>7}")
print()
true_rows = models(statement, names)
print(f"rows where it holds: {len(true_rows)} of {2 ** len(names)}")
for a in true_rows:
    print("   " + ", ".join(f"{k}={str(v)}" for k, v in a.items()))

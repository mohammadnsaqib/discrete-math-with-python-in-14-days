"""A normal form read straight off the false rows, with no rewriting rules at all."""
from dmkit.logic import cnf_text, implies, to_cnf, truth_table


def statement(p, q, r):
    """(p implies q) and r."""
    return implies(p, q) and r


names = ["p", "q", "r"]
print(f"{'p':>6} {'q':>6} {'r':>6} {'value':>7}   {'forbids':<26}")
for a, v in truth_table(statement, names):
    if v:
        forbid = ""
    else:
        forbid = "(" + " or ".join(
            (n if not a[n] else "not " + n) for n in names) + ")"
    print(f"{str(a['p']):>6} {str(a['q']):>6} {str(a['r']):>6} {str(v):>7}   "
          f"{forbid:<26}")
clauses = to_cnf(statement, names)
print()
print(f"false rows: {len(clauses)}, so the form has {len(clauses)} clauses")
print(f"conjunctive normal form:")
print(f"  {cnf_text(clauses)}")

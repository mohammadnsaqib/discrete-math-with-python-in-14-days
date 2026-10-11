"""The first table, printed in full: two variables, four rows."""
from dmkit.logic import truth_table


def statement(p, q):
    """p and (not q)."""
    return p and (not q)


print(f"{'p':>7} {'q':>7} {'p and not q':>14}")
for assignment, value in truth_table(statement, ["p", "q"]):
    print(f"{str(assignment['p']):>7} {str(assignment['q']):>7} {str(value):>14}")

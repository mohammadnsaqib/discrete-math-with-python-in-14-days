"""The form read off the table, checked against one produced by rewriting."""
import sympy as sp
from sympy.abc import P, Q, R

from dmkit.logic import assignments, cnf_text, implies, to_cnf

SYMS = {"p": P, "q": Q, "r": R}


def same_table(fn, expr, names):
    """True when a Python statement and a SymPy expression agree on every assignment.

    The two forms need not be the same STRING, and usually are not. What has to hold is
    that they have the same column, so that is what is compared.
    """
    for a in assignments(names):
        substitution = {SYMS[n]: (sp.true if a[n] else sp.false) for n in names}
        if bool(expr.subs(substitution)) != fn(**a):
            return False
    return True


cases = [
    ("p implies q", lambda p, q: implies(p, q), sp.Implies(P, Q), ["p", "q"]),
    ("p iff q", lambda p, q: p == q, sp.Equivalent(P, Q), ["p", "q"]),
    ("(p or q) and not r", lambda p, q, r: (p or q) and (not r),
     (P | Q) & ~R, ["p", "q", "r"]),
]
for name, fn, expr, names in cases:
    clauses = to_cnf(fn, names)
    theirs = sp.to_cnf(expr, simplify=True)
    theirs_count = len(theirs.args) if isinstance(theirs, sp.And) else 1
    print(name)
    print(f"   from the table : {cnf_text(clauses)}")
    print(f"   from sympy     : {theirs}")
    print(f"   same table     : {same_table(fn, theirs, names)}, "
          f"clauses {len(clauses)} against {theirs_count}")

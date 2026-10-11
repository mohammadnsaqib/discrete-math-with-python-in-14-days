"""The table's verdict, checked against a library that reaches it by rewriting instead.
"""
import sympy as sp
from sympy.abc import P, Q, R

from dmkit.logic import equivalent, implies

# dmkit decides equivalence by comparing two truth tables. SymPy decides it by
# simplifying the biconditional to a normal form. The routes share nothing.
cases = [
    ("not (p and q)", lambda p, q: not (p and q), ~(P & Q),
     "(not p) or (not q)", lambda p, q: (not p) or (not q), ~P | ~Q),
    ("p implies q", lambda p, q: implies(p, q), sp.Implies(P, Q),
     "(not p) or q", lambda p, q: (not p) or q, ~P | Q),
    ("p implies q", lambda p, q: implies(p, q), sp.Implies(P, Q),
     "q implies p", lambda p, q: implies(q, p), sp.Implies(Q, P)),
    ("p iff q", lambda p, q: p == q, sp.Equivalent(P, Q),
     "(p and q) or (not p and not q)", lambda p, q: (p and q) or ((not p) and (not q)),
     (P & Q) | (~P & ~Q)),
]
print(f"{'first':>16} {'second':>32} {'by table':>10} {'by sympy':>10} {'agree':>7}")
for na, fa, sa, nb, fb, sb in cases:
    mine = equivalent(fa, fb, ["p", "q"])
    theirs = bool(sp.simplify_logic(sp.Equivalent(sa, sb)) == sp.true)
    print(f"{na:>16} {nb:>32} {str(mine):>10} {str(theirs):>10} "
          f"{str(mine == theirs):>7}")

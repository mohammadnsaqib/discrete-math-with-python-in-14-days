"""Every law of logic this book uses, each settled by its own table."""
from dmkit.logic import equivalent, implies

laws = [
    ("double negation", lambda p: not (not p), lambda p: p, ["p"]),
    ("idempotence of and", lambda p: p and p, lambda p: p, ["p"]),
    ("commutativity of and", lambda p, q: p and q, lambda p, q: q and p, ["p", "q"]),
    ("commutativity of or", lambda p, q: p or q, lambda p, q: q or p, ["p", "q"]),
    ("de Morgan, and", lambda p, q: not (p and q),
     lambda p, q: (not p) or (not q), ["p", "q"]),
    ("de Morgan, or", lambda p, q: not (p or q),
     lambda p, q: (not p) and (not q), ["p", "q"]),
    ("absorption", lambda p, q: p or (p and q), lambda p, q: p, ["p", "q"]),
    ("the conditional", lambda p, q: implies(p, q),
     lambda p, q: (not p) or q, ["p", "q"]),
    ("contraposition", lambda p, q: implies(p, q),
     lambda p, q: implies(not q, not p), ["p", "q"]),
    ("associativity of and", lambda p, q, r: (p and q) and r,
     lambda p, q, r: p and (q and r), ["p", "q", "r"]),
    ("distribution over or", lambda p, q, r: p and (q or r),
     lambda p, q, r: (p and q) or (p and r), ["p", "q", "r"]),
    ("distribution over and", lambda p, q, r: p or (q and r),
     lambda p, q, r: (p or q) and (p or r), ["p", "q", "r"]),
]
print(f"{'law':>24} {'variables':>11} {'rows':>6} {'holds':>7}")
held = 0
for name, a, b, names in laws:
    ok = equivalent(a, b, names)
    held += ok
    print(f"{name:>24} {len(names):>11} {2 ** len(names):>6} {str(ok):>7}")
print()
print(f"{held} of {len(laws)} hold, and each was settled by building both tables.")

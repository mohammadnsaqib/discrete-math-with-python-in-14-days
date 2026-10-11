"""Problem 1.27: how large the form read off a table gets, and when it is the wrong
route."""
from dmkit.logic import implies, models, to_cnf

cases = [
    ("p", lambda p, q, r: p, ["p", "q", "r"]),
    ("p and q and r", lambda p, q, r: p and q and r, ["p", "q", "r"]),
    ("p or q or r", lambda p, q, r: p or q or r, ["p", "q", "r"]),
    ("p implies q", lambda p, q, r: implies(p, q), ["p", "q", "r"]),
    ("exactly one of p, q, r",
     lambda p, q, r: (p + q + r) == 1, ["p", "q", "r"]),
    ("an even count of them true",
     lambda p, q, r: (p + q + r) % 2 == 0, ["p", "q", "r"]),
]
print(f"{'statement':>26} {'true rows':>10} {'false rows':>11} {'clauses':>8} "
      f"{'literals':>9}")
for name, fn, names in cases:
    clauses = to_cnf(fn, names)
    literals = sum(len(c) for c in clauses)
    print(f"{name:>26} {len(models(fn, names)):>10} {len(clauses):>11} "
          f"{len(clauses):>8} {literals:>9}")

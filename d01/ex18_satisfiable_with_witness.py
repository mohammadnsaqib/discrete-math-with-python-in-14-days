"""A claim that something is satisfiable is worth nothing without the thing."""
from dmkit.logic import implies, satisfiable

cases = [
    ("p and not q", lambda p, q: p and (not q), ["p", "q"]),
    ("(p or q) and (not p or not q)", lambda p, q: (p or q) and ((not p) or (not q)),
     ["p", "q"]),
    ("p and not p", lambda p: p and (not p), ["p"]),
    ("(p implies q) and p and not q",
     lambda p, q: implies(p, q) and p and (not q), ["p", "q"]),
    ("(p or q or r) and (not p) and (not q)",
     lambda p, q, r: (p or q or r) and (not p) and (not q), ["p", "q", "r"]),
]
print(f"{'statement':>40} {'satisfiable':>12}   {'witness':<34}")
for name, fn, names in cases:
    found = satisfiable(fn, names)
    shown = ", ".join(f"{k}={str(v)}" for k,
                      v in found.items()) if found else "none exists"
    print(f"{name:>40} {str(found is not None):>12}   {shown:<34}")

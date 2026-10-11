"""Most statements are neither: true on some rows and false on others."""
from dmkit.logic import implies, is_contradiction, is_tautology, models

cases = [
    ("p or not p", lambda p: p or (not p), ["p"]),
    ("p and not p", lambda p: p and (not p), ["p"]),
    ("p and q", lambda p, q: p and q, ["p", "q"]),
    ("p implies q", lambda p, q: implies(p, q), ["p", "q"]),
    ("p or q or r", lambda p, q, r: p or q or r, ["p", "q", "r"]),
]
print(f"{'statement':>16} {'rows':>6} {'true on':>9} {'tautology':>11} "
      f"{'contradiction':>15} {'kind':>13}")
for name, st, names in cases:
    n = 2 ** len(names)
    t = len(models(st, names))
    taut, contra = is_tautology(st, names), is_contradiction(st, names)
    kind = "tautology" if taut else ("contradiction" if contra else "contingent")
    print(f"{name:>16} {n:>6} {t:>9} {str(taut):>11} {str(contra):>15} {kind:>13}")

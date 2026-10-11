"""Symmetric and antisymmetric are not opposites, and four relations show it."""
from dmkit.sets import is_antisymmetric, is_symmetric

dom = {1, 2, 3}
relations = [
    ("equality", {(1, 1), (2, 2), (3, 3)}),
    ("everything", {(a, b) for a in dom for b in dom}),
    ("at most", {(a, b) for a in dom for b in dom if a <= b}),
    ("differs by one", {(a, b) for a in dom for b in dom if abs(a - b) == 1}),
    ("one pair only", {(1, 2)}),
]
print(f"{'relation':>16} {'symmetric':>11} {'antisymmetric':>15} {'which':>16}")
for name, rel in relations:
    s, a = is_symmetric(rel), is_antisymmetric(rel)
    which = ("both" if s and a else "symmetric" if s else
             "antisymmetric" if a else "neither")
    print(f"{name:>16} {str(s):>11} {str(a):>15} {which:>16}")
